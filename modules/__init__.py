# Divination Modules
from . import bazi_calculator
# Temporarily comment out ziwei to test if it's causing the hang
# from . import ziwei_calculator
from . import yijing_calculator

# Create wrapper objects to match app.py's expected API
class bazi:
    """Wrapper for bazi calculator"""
    @staticmethod
    def calculate_bazi(**kwargs):
        return bazi_calculator.bazi.calculate(**kwargs)

class ziwei:
    """Temporary stub for ziwei - will be implemented after fixing import issue"""
    @staticmethod
    def calculate_ziwei(**kwargs):
        return {
            'status': 'temporary_stub',
            'message': '紫微斗數模塊暫時禁用以調試部署問題',
            'palaces': {},
            'main_star_analysis': '功能開發中...'
        }
