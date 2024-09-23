import flet as ft
from variable import *
from imports import *

class One():
    def __init__(self):
        super().__init__()
        
        config = configparser.ConfigParser()  
        config.read(path_imports_config)
        
        self.strat_one_up_chanal = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_up_chanal')) # верх канала
        self.strat_one_down_chanal = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_down_chanal')) # низ канала
        self.strat_one_corner_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_corner_long')) # угол лонг
        self.strat_one_corner_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_corner_short')) # угол шорт
        
    def get_settings(self):
        return [self.strat_one_up_chanal,self.strat_one_down_chanal,self.strat_one_corner_long,self.strat_one_corner_short]
    

        
class MA():
    def __init__(self):
        super().__init__()
        
        config = configparser.ConfigParser()  
        config.read(path_imports_config)
        
        self.strat_ma_koef_bistro = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_koef_bistro')) # коэфициент быстрой скользящей средней
        self.strat_ma_koef_medleno = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_koef_medleno')) # коэфициент медленной скользящей средней
        self.strat_ma_sovpad_last = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_sovpad_last')) # кол-во совпадений в прошлом
        self.strat_ma_up_chanal = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_up_chanal')) # верх канала
        self.strat_ma_down_chanal = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_down_chanal')) # низ канала
        
    def get_settings(self):
        return [self.strat_ma_koef_bistro,self.strat_ma_koef_medleno,self.strat_ma_sovpad_last,self.strat_ma_up_chanal,self.strat_ma_down_chanal]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        