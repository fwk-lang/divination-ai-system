"""易經卦象計算模組 - 結合六爻與梅花易數"""
import random
from datetime import datetime

# 六十四卦卦名與卦象
HEXAGRAMS = {
    1: {'name': '乾為天', 'symbol': '☰☰', 'element': '金', 'nature': '剛健'},
    2: {'name': '坤為地', 'symbol': '☷☷', 'element': '土', 'nature': '柔順'},
    3: {'name': '水雷屯', 'symbol': '☵☳', 'element': '水木', 'nature': '艱難'},
    4: {'name': '山水蒙', 'symbol': '☶☵', 'element': '土水', 'nature': '蒙昧'},
    11: {'name': '地天泰', 'symbol': '☷☰', 'element': '土金', 'nature': '通泰'},
    12: {'name': '天地否', 'symbol': '☰☷', 'element': '金土', 'nature': '閉塞'},
    63: {'name': '水火既濟', 'symbol': '☵☲', 'element': '水火', 'nature': '成功'},
    64: {'name': '火水未濟', 'symbol': '☲☵', 'element': '火水', 'nature': '未完'}
}

class YijingCalculator:
    def __init__(self):
        self.hexagram_data = HEXAGRAMS
    
    def cast_hexagram(self, method='coins'):
        """起卦 - 支援硬幣法與時間法"""
        if method == 'coins':
            return self._coin_method()
        elif method == 'time':
            return self._time_method()
        else:
            return self._random_method()
    
    def _coin_method(self):
        """三枚硬幣法起卦（模擬）"""
        lines = []
        for i in range(6):
            coins = [random.choice([2, 3]) for _ in range(3)]  # 2=背, 3=正
            total = sum(coins)
            if total == 6:  # 老陰
                lines.append({'value': 6, 'type': '老陰', 'changing': True})
            elif total == 7:  # 少陽
                lines.append({'value': 7, 'type': '少陽', 'changing': False})
            elif total == 8:  # 少陰
                lines.append({'value': 8, 'type': '少陰', 'changing': False})
            elif total == 9:  # 老陽
                lines.append({'value': 9, 'type': '老陽', 'changing': True})
        return lines
    
    def _time_method(self):
        """梅花易數時間起卦法"""
        now = datetime.now()
        upper = (now.year + now.month + now.day) % 8
        lower = (now.year + now.month + now.day + now.hour) % 8
        changing_line = (now.year + now.month + now.day + now.hour + now.minute) % 6
        
        return {
            'upper_trigram': upper,
            'lower_trigram': lower,
            'changing_line': changing_line,
            'method': 'time'
        }
    
    def _random_method(self):
        """隨機起卦"""
        hexagram_num = random.randint(1, 64)
        return hexagram_num
    
    def interpret_hexagram(self, hexagram_num):
        """解卦 - 返回卦象基本資訊"""
        if hexagram_num in self.hexagram_data:
            return self.hexagram_data[hexagram_num]
        else:
            return {'name': '未知卦', 'symbol': '??', 'element': '未知', 'nature': '待解'}
    
    def get_full_reading(self, question=None):
        """完整卦象解讀"""
        lines = self.cast_hexagram('coins')
        hexagram_num = self._lines_to_number(lines)
        interpretation = self.interpret_hexagram(hexagram_num)
        
        return {
            'question': question,
            'hexagram_number': hexagram_num,
            'hexagram_name': interpretation['name'],
            'lines': lines,
            'interpretation': interpretation,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def _lines_to_number(self, lines):
        """將六爻轉換為卦號"""
        # 簡化版：根據陰陽組合計算
        binary = ''.join(['1' if line['type'] in ['老陽', '少陽'] else '0' for line in lines])
        return int(binary, 2) % 64 + 1
