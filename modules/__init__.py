# Divination Modules
from . import bazi_calculator as bazi
from . import ziwei_calculator as ziwei
from . import yijing_calculator as yijing

# Create wrapper instances and functions for backward compatibility
_bazi_calc = bazi_calculator.bazi
_ziwei_calc = ziwei_calculator.ziwei

# Wrapper class to provide calculate_bazi method
class bazi:
    @staticmethod
    def calculate_bazi(**kwargs):
        return _bazi_calc.calculate(**kwargs)

class ziwei:
    @staticmethod
    def calculate_ziwei(**kwargs):
        return _ziwei_calc.calculate(**kwargs)
