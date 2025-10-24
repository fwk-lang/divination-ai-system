"""八字计算模块 - Bazi Calculator Module

基于china-testing/bazi库的简化封装
Simplified wrapper for china-testing/bazi library
"""

from datetime import datetime
import sys
import os

# 添加第三方库路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../vendor'))

class BaziCalculator:
    """八字计算器 - Bazi Calculator"""
    
    def __init__(self):
        """初始化计算器"""
        self.cached_results = {}
    
    def calculate(self, birth_year: int, birth_month: int, birth_day: int, 
                  birth_hour: int, gender: str = '男') -> dict:
        """计算八字
        
        Args:
            birth_year: 出生年份
            birth_month: 出生月份
            birth_day: 出生日期
            birth_hour: 出生时辰(0-23)
            gender: 性别 ('男' 或 '女')
        
        Returns:
            dict: 包含八字信息的字典
        """
        try:
            # 构建缓存key
            cache_key = f"{birth_year}-{birth_month}-{birth_day}-{birth_hour}-{gender}"
            
            # 检查缓存
            if cache_key in self.cached_results:
                return self.cached_results[cache_key]
            
            # TODO: 集成china-testing/bazi库
            # 当前返回模拟数据结构
            result = {
                'year_pillar': {'stem': '甲', 'branch': '子'},
                'month_pillar': {'stem': '丙', 'branch': '寅'},
                'day_pillar': {'stem': '戊', 'branch': '辰'},
                'hour_pillar': {'stem': '庚', 'branch': '午'},
                'five_elements': {'金': 1, '木': 2, '水': 1, '火': 2, '土': 2},
                'ten_gods': {
                    'year': '偏印',
                    'month': '食神',
                    'day': '日主',
                    'hour': '正财'
                },
                'day_master': '戊土',
                'strength': '中和',
                'favorable_elements': ['金', '水'],
                'unfavorable_elements': ['木'],
                'major_fortune': [],  # 大运
                'natal_stars': [],  # 神煞
                'nayin': '霹雳火',  # 纳音
                'void': ['戌', '亥']  # 空亡
            }
            
            # 缓存结果
            self.cached_results[cache_key] = result
            return result
            
        except Exception as e:
            return {
                'error': str(e),
                'status': 'failed'
            }
    
    def get_interpretation(self, bazi_data: dict) -> str:
        """获取八字解读
        
        Args:
            bazi_data: calculate()返回的八字数据
        
        Returns:
            str: 基础解读文本
        """
        if 'error' in bazi_data:
            return f"计算出错: {bazi_data['error']}"
        
        interpretation = []
        interpretation.append(f"日主: {bazi_data.get('day_master', '未知')}")
        interpretation.append(f"八字强弱: {bazi_data.get('strength', '未知')}")
        
        favorable = bazi_data.get('favorable_elements', [])
        if favorable:
            interpretation.append(f"喜用神: {', '.join(favorable)}")
        
        unfavorable = bazi_data.get('unfavorable_elements', [])
        if unfavorable:
            interpretation.append(f"忌神: {', '.join(unfavorable)}")
        
        return '\n'.join(interpretation)
    
    def format_pillars(self, bazi_data: dict) -> str:
        """格式化四柱输出
        
        Args:
            bazi_data: calculate()返回的八字数据
        
        Returns:
            str: 格式化的四柱文本
        """
        if 'error' in bazi_data:
            return f"错误: {bazi_data['error']}"
        
        pillars = []
        for pillar_name in ['year_pillar', 'month_pillar', 'day_pillar', 'hour_pillar']:
            pillar = bazi_data.get(pillar_name, {})
            stem = pillar.get('stem', '?')
            branch = pillar.get('branch', '?')
            pillars.append(f"{stem}{branch}")
        
        pillar_labels = ['年柱', '月柱', '日柱', '时柱']
        return '\n'.join([f"{label}: {pillar}" for label, pillar in zip(pillar_labels, pillars)])


def quick_calculate(year: int, month: int, day: int, hour: int, gender: str = '男') -> dict:
    """快速计算八字的便捷函数
    
    Args:
        year: 出生年份
        month: 出生月份
        day: 出生日期
        hour: 出生时辰(0-23)
        gender: 性别
    
    Returns:
        dict: 八字数据
    """
    calculator = BaziCalculator()
    return calculator.calculate(year, month, day, hour, gender)

# 為 app.py 提供的別名函數
calculate_bazi = quick_calculate
