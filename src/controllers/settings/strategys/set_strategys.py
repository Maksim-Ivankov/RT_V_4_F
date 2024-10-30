from variable import *
from imports import *

class One():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
            # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_one_up_chanal = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_up_chanal')) # верх канала
            self.strat_one_down_chanal = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_down_chanal')) # низ канала
            self.strat_one_corner_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_corner_long')) # угол лонг
            self.strat_one_corner_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_corner_short')) # угол шорт
        elif regime=='much_set':
            # print('Рабюотаем в ОНЕ')
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_one_set)
            self.strat_one_up_chanal = float(config_set.get(f'{str(number_trade)}_section', 'up_chanal')) # верх канала
            self.strat_one_down_chanal = float(config_set.get(f'{str(number_trade)}_section', 'down_chanal')) # низ канала
            self.strat_one_corner_long = float(config_set.get(f'{str(number_trade)}_section', 'corner_long')) # угол лонг
            self.strat_one_corner_short = float(config_set.get(f'{str(number_trade)}_section', 'corner_short')) # угол шорт
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_one_up_chanal,self.strat_one_down_chanal,self.strat_one_corner_long,self.strat_one_corner_short]
    
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_one_set)
        return {
            'up_chanal': float(config_set.get(f'{str(number)}_section', 'up_chanal')),
            'down_chanal': float(config_set.get(f'{str(number)}_section', 'down_chanal')),
            'corner_long': float(config_set.get(f'{str(number)}_section', 'corner_long')),
            'corner_short': float(config_set.get(f'{str(number)}_section', 'corner_short')),
        }
    

        
class MA():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_ma_koef_bistro = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_koef_bistro')) # коэфициент быстрой скользящей средней
            self.strat_ma_koef_medleno = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_koef_medleno')) # коэфициент медленной скользящей средней
            self.strat_ma_sovpad_last = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_sovpad_last')) # кол-во совпадений в прошлом
            self.strat_ma_up_chanal = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_up_chanal')) # верх канала
            self.strat_ma_down_chanal = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_down_chanal')) # низ канала
        elif regime=='much_set':
            # print('Рабюотаем в МА')
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_MA_set)
            self.strat_ma_koef_bistro = float(config_set.get(f'{str(number_trade)}_section', 'koef_bistro'))
            self.strat_ma_koef_medleno = float(config_set.get(f'{str(number_trade)}_section', 'koef_medleno'))
            self.strat_ma_sovpad_last = float(config_set.get(f'{str(number_trade)}_section', 'sovpad_last'))
            self.strat_ma_up_chanal = float(config_set.get(f'{str(number_trade)}_section', 'up_chanal'))
            self.strat_ma_down_chanal = float(config_set.get(f'{str(number_trade)}_section', 'down_chanal'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_ma_koef_bistro,self.strat_ma_koef_medleno,self.strat_ma_sovpad_last,self.strat_ma_up_chanal,self.strat_ma_down_chanal]
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_MA_set)
        return {
            'koef_bistro': float(config_set.get(f'{str(number)}_section', 'koef_bistro')),
            'koef_medleno': float(config_set.get(f'{str(number)}_section', 'koef_medleno')),
            'sovpad_last': float(config_set.get(f'{str(number)}_section', 'sovpad_last')),
            'up_chanal': float(config_set.get(f'{str(number)}_section', 'up_chanal')),
            'down_chanal': float(config_set.get(f'{str(number)}_section', 'down_chanal')),
        }
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        