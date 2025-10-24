# Divination Modules  
from . import bazi_calculator
from . import ziwei_calculator  
from . import yijing_calculator

# Create wrapper instances for the calculator modules
_bazi_instance = bazi_calculator.bazi
_ziwei_instance = ziwei_calculator.ziwei

# Create wrapper objects with the expected API
class bazi:
    @staticmethod
    def calculate_bazi(**kwargs):
        return _bazi_instance.calculate(**kwargs)

class ziwei:
    @staticmethod
    def calculate_ziwei(**kwargs):
        return _ziwei_instance.calculate(**kwargs)
