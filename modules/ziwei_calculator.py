"""紫微斗数计算模块 - Ziwei Doushu Calculator Module

基于iztro库的Python封装
Python wrapper for iztro library (JavaScript)

注：由于iztro是JavaScript/TypeScript库，需要通过Node.js或者PyExecJS调用
"""

from datetime import datetime
from typing import Dict, List, Optional
import json
import subprocess
import os

class ZiweiCalculator:
    """紫微斗数计算器 - Ziwei Doushu Calculator"""
    
    def __init__(self, use_nodejs: bool = True):
        """初始化计算器
        
        Args:
            use_nodejs: 是否使用Node.js执行（默认True）
        """
        self.use_nodejs = use_nodejs
        self.cached_results = {}
        self.palaces = [
            '命宫', '兄弟宫', '夫妻宫', '子女宫', '财帛宫', '疾厄宫',
            '迁移宫', '奴仆宫', '官禄宫', '田宅宫', '福德宫', '父母宫'
        ]
    
    def calculate(self, birth_year: int, birth_month: int, birth_day: int,
                  birth_hour: int, gender: str = '男', 
                  calendar_type: str = 'solar') -> dict:
        """计算紫微斗数命盘
        
        Args:
            birth_year: 出生年份
            birth_month: 出生月份
            birth_day: 出生日期
            birth_hour: 出生时辰(0-23)
            gender: 性别 ('男' 或 '女')
            calendar_type: 日历类型 ('solar'阳历 或 'lunar'阴历)
        
        Returns:
            dict: 包含紫微斗数命盘信息的字典
        """
        try:
            # 构建缓存key
            cache_key = f"{birth_year}-{birth_month}-{birth_day}-{birth_hour}-{gender}-{calendar_type}"
            
            # 检查缓存
            if cache_key in self.cached_results:
                return self.cached_results[cache_key]
            
            # TODO: 集成iztro库调用
            # 当前返回模拟数据结构
            result = {
                'birth_info': {
                    'year': birth_year,
                    'month': birth_month,
                    'day': birth_day,
                    'hour': birth_hour,
                    'gender': gender,
                    'calendar': calendar_type
                },
                'palaces': self._generate_palace_data(),
                'major_stars': {
                    '命宫': ['紫微', '天府'],
                    '兄弟宫': ['天机', '天梁'],
                    '夫妻宫': ['太阳'],
                    '子女宫': ['武曲', '天同'],
                    '财帛宫': ['太阴'],
                    '疾厄宫': ['贪狼'],
                    '迁移宫': ['巨门', '天相'],
                    '奴仆宫': ['天魁'],
                    '官禄宫': ['天府'],
                    '田宅宫': ['廉贞'],
                    '福德宫': ['七杀'],
                    '父母宫': ['破军']
                },
                'four_transformations': {
                    '化禄': '廉贞',
                    '化权': '破军',
                    '化科': '武曲',
                    '化忌': '太阳'
                },
                'life_palace': '寅宫',
                'body_palace': '午宫',
                'five_elements': '火六局',
                'decadal_fortune': []  # 大限
            }
            
            # 缓存结果
            self.cached_results[cache_key] = result
            return result
            
        except Exception as e:
            return {
                'error': str(e),
                'status': 'failed'
            }
    
    def _generate_palace_data(self) -> List[Dict]:
        """生成十二宫数据"""
        palace_data = []
        earthly_branches = ['寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥', '子', '丑']
        
        for i, palace_name in enumerate(self.palaces):
            palace_data.append({
                'name': palace_name,
                'earthly_branch': earthly_branches[i],
                'heavenly_stem': self._get_heavenly_stem(i),
                'major_stars': [],
                'minor_stars': [],
                'brightness': ''
            })
        
        return palace_data
    
    def _get_heavenly_stem(self, index: int) -> str:
        """获取天干"""
        stems = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
        return stems[index % 10]
    
    def get_interpretation(self, ziwei_data: dict) -> str:
        """获取紫微斗数解读
        
        Args:
            ziwei_data: calculate()返回的紫微数据
        
        Returns:
            str: 基础解读文本
        """
        if 'error' in ziwei_data:
            return f"计算出错: {ziwei_data['error']}"
        
        interpretation = []
        interpretation.append(f"命宫: {ziwei_data.get('life_palace', '未知')}")
        interpretation.append(f"身宫: {ziwei_data.get('body_palace', '未知')}")
        interpretation.append(f"五行局: {ziwei_data.get('five_elements', '未知')}")
        
        major_stars = ziwei_data.get('major_stars', {}).get('命宫', [])
        if major_stars:
            interpretation.append(f"命宫主星: {', '.join(major_stars)}")
        
        four_trans = ziwei_data.get('four_transformations', {})
        if four_trans:
            trans_text = ', '.join([f"{k}:{v}" for k, v in four_trans.items()])
            interpretation.append(f"四化: {trans_text}")
        
        return '\n'.join(interpretation)
    
    def format_palaces(self, ziwei_data: dict) -> str:
        """格式化十二宫输出
        
        Args:
            ziwei_data: calculate()返回的紫微数据
        
        Returns:
            str: 格式化的十二宫文本
        """
        if 'error' in ziwei_data:
            return f"错误: {ziwei_data['error']}"
        
        palace_texts = []
        major_stars = ziwei_data.get('major_stars', {})
        
        for palace_name in self.palaces:
            stars = major_stars.get(palace_name, [])
            star_text = ', '.join(stars) if stars else '无主星'
            palace_texts.append(f"{palace_name}: {star_text}")
        
        return '\n'.join(palace_texts)
    
    def get_palace_analysis(self, ziwei_data: dict, palace_name: str) -> dict:
        """获取特定宫位的详细分析
        
        Args:
            ziwei_data: 紫微数据
            palace_name: 宫位名称
        
        Returns:
            dict: 宫位分析数据
        """
        if palace_name not in self.palaces:
            return {'error': f'无效的宫位名称: {palace_name}'}
        
        palaces = ziwei_data.get('palaces', [])
        palace_index = self.palaces.index(palace_name)
        
        if palace_index < len(palaces):
            return palaces[palace_index]
        
        return {'error': '未找到宫位数据'}


def quick_calculate(year: int, month: int, day: int, hour: int, 
                   gender: str = '男', calendar: str = 'solar') -> dict:
    """快速计算紫微斗数的便捷函数
    
    Args:
        year: 出生年份
        month: 出生月份
        day: 出生日期
        hour: 出生时辰(0-23)
        gender: 性别
        calendar: 日历类型
    
    Returns:
        dict: 紫微数据
    """
    calculator = ZiweiCalculator()
    return calculator.calculate(year, month, day, hour, gender, calendar)

# 為 app.py 提供的別名函數
calculate_ziwei = quick_calculate
