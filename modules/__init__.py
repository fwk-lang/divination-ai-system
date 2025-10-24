# Divination Modules
from . import bazi_calculator
from . import ziwei_calculator
from . import yijing_calculator

# Create wrapper objects to match app.py's expected API
class bazi:
    """Wrapper for bazi calculator"""
    @staticmethod
    def calculate_bazi(**kwargs):
        return bazi_calculator.bazi.calculate(**kwargs)

class ziwei:
    """Wrapper for ziwei calculator"""
    @staticmethod
    def calculate_ziwei(**kwargs):
        return ziwei_calculator.calculate_ziwei(**kwargs)
