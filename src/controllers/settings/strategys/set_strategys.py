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
    
#-------------------------------------------------------------------------------------------------------------
        
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
        
#-------------------------------------------------------------------------------------------------------------        
        
class BBANDS():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_BBANDS_timeperiod = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_BBANDS_timeperiod')) 
            self.strat_BBANDS_nbdevup = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_BBANDS_nbdevup')) 
            self.strat_BBANDS_nbdevdn = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_BBANDS_nbdevdn')) 
            self.strat_BBANDS_matype = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_BBANDS_matype')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_BBANDS_set)
            self.strat_BBANDS_timeperiod = float(config_set.get(f'{str(number_trade)}_section', 'timeperiod'))
            self.strat_BBANDS_nbdevup = float(config_set.get(f'{str(number_trade)}_section', 'nbdevup'))
            self.strat_BBANDS_nbdevdn = float(config_set.get(f'{str(number_trade)}_section', 'nbdevdn'))
            self.strat_BBANDS_matype = float(config_set.get(f'{str(number_trade)}_section', 'matype'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_BBANDS_timeperiod,self.strat_BBANDS_nbdevup,self.strat_BBANDS_nbdevdn,self.strat_BBANDS_matype] # параметры через запятую
    
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_BBANDS_set)
        return {
            'timeperiod': float(config_set.get(f'{str(number)}_section', 'timeperiod')),
            'nbdevup': float(config_set.get(f'{str(number)}_section', 'nbdevup')),
            'nbdevdn': float(config_set.get(f'{str(number)}_section', 'nbdevdn')),
            'matype': float(config_set.get(f'{str(number)}_section', 'matype')),
        }   

#-------------------------------------------------------------------------------------------------------------

class EMA():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_EMA_timeperiod = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_EMA_timeperiod')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_EMA_set)
            self.strat_EMA_timeperiod = float(config_set.get(f'{str(number_trade)}_section', 'timeperiod'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_EMA_timeperiod] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_EMA_set)
        return {
            'timeperiod': float(config_set.get(f'{str(number)}_section', 'timeperiod')),
        }   

#-------------------------------------------------------------------------------------------------------------

class DEMA():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_DEMA_timeperiod = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_DEMA_timeperiod')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_DEMA_set)
            self.strat_DEMA_timeperiod = float(config_set.get(f'{str(number_trade)}_section', 'timeperiod'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_DEMA_timeperiod] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_DEMA_set)
        return {
            'timeperiod': float(config_set.get(f'{str(number)}_section', 'timeperiod')),
        }   

#-------------------------------------------------------------------------------------------------------------

class KAMA():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_KAMA_timeperiod = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_KAMA_timeperiod')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_KAMA_set)
            self.strat_KAMA_timeperiod = float(config_set.get(f'{str(number_trade)}_section', 'timeperiod'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_KAMA_timeperiod] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_KAMA_set)
        return {
            'timeperiod': float(config_set.get(f'{str(number)}_section', 'timeperiod')),
        }   

#-------------------------------------------------------------------------------------------------------------

class MAVP():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_MAVP_minperiod = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_MAVP_minperiod')) 
            self.strat_MAVP_maxperiod = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_MAVP_maxperiod')) 
            self.strat_MAVP_matype = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_MAVP_matype')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_MAVP_set)
            self.strat_MAVP_minperiod = float(config_set.get(f'{str(number_trade)}_section', 'minperiod'))
            self.strat_MAVP_maxperiod = float(config_set.get(f'{str(number_trade)}_section', 'maxperiod'))
            self.strat_MAVP_matype = float(config_set.get(f'{str(number_trade)}_section', 'matype'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_MAVP_minperiod,self.strat_MAVP_maxperiod,self.strat_MAVP_matype] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_MAVP_set)
        return {
            'minperiod': float(config_set.get(f'{str(number)}_section', 'minperiod')),
            'maxperiod': float(config_set.get(f'{str(number)}_section', 'maxperiod')),
            'matype': float(config_set.get(f'{str(number)}_section', 'matype')),
        }   

#-------------------------------------------------------------------------------------------------------------

class SAR():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_SAR_acceleration = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_SAR_acceleration')) 
            self.strat_SAR_maximum = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_SAR_maximum')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_SAR_set)
            self.strat_SAR_acceleration = float(config_set.get(f'{str(number_trade)}_section', 'acceleration'))
            self.strat_SAR_maximum = float(config_set.get(f'{str(number_trade)}_section', 'maximum'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_SAR_acceleration,self.strat_SAR_maximum] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_SAR_set)
        return {
            'acceleration': float(config_set.get(f'{str(number)}_section', 'acceleration')),
            'maximum': float(config_set.get(f'{str(number)}_section', 'maximum')),
        }   

#-------------------------------------------------------------------------------------------------------------

class TEMA():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_TEMA_timeperiod = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_TEMA_timeperiod')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_TEMA_set)
            self.strat_TEMA_timeperiod = float(config_set.get(f'{str(number_trade)}_section', 'timeperiod'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_TEMA_timeperiod] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_TEMA_set)
        return {
            'timeperiod': float(config_set.get(f'{str(number)}_section', 'timeperiod')),
        }   

#-------------------------------------------------------------------------------------------------------------

class TRIMA():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_TRIMA_timeperiod = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_TRIMA_timeperiod')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_TRIMA_set)
            self.strat_TRIMA_timeperiod = float(config_set.get(f'{str(number_trade)}_section', 'timeperiod'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_TRIMA_timeperiod] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_TRIMA_set)
        return {
            'timeperiod': float(config_set.get(f'{str(number)}_section', 'timeperiod')),
        }   

#-------------------------------------------------------------------------------------------------------------

class WMA():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_WMA_timeperiod = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_WMA_timeperiod')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_WMA_set)
            self.strat_WMA_timeperiod = float(config_set.get(f'{str(number_trade)}_section', 'timeperiod'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_WMA_timeperiod] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_WMA_set)
        return {
            'timeperiod': float(config_set.get(f'{str(number)}_section', 'timeperiod')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDL2CROWS():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDL2CROWS_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL2CROWS_long')) 
            self.strat_CDL2CROWS_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL2CROWS_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDL2CROWS_set)
            self.strat_CDL2CROWS_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDL2CROWS_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDL2CROWS_long,self.strat_CDL2CROWS_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDL2CROWS_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDL3BLACKCROWS():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDL3BLACKCROWS_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3BLACKCROWS_long')) 
            self.strat_CDL3BLACKCROWS_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3BLACKCROWS_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDL3BLACKCROWS_set)
            self.strat_CDL3BLACKCROWS_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDL3BLACKCROWS_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDL3BLACKCROWS_long,self.strat_CDL3BLACKCROWS_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDL3BLACKCROWS_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDL3INSIDE():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDL3INSIDE_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3INSIDE_long')) 
            self.strat_CDL3INSIDE_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3INSIDE_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDL3INSIDE_set)
            self.strat_CDL3INSIDE_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDL3INSIDE_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDL3INSIDE_long,self.strat_CDL3INSIDE_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDL3INSIDE_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDL3LINESTRIKE():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDL3LINESTRIKE_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3LINESTRIKE_long')) 
            self.strat_CDL3LINESTRIKE_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3LINESTRIKE_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDL3LINESTRIKE_set)
            self.strat_CDL3LINESTRIKE_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDL3LINESTRIKE_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDL3LINESTRIKE_long,self.strat_CDL3LINESTRIKE_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDL3LINESTRIKE_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDL3OUTSIDE():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDL3OUTSIDE_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3OUTSIDE_long')) 
            self.strat_CDL3OUTSIDE_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3OUTSIDE_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDL3OUTSIDE_set)
            self.strat_CDL3OUTSIDE_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDL3OUTSIDE_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDL3OUTSIDE_long,self.strat_CDL3OUTSIDE_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDL3OUTSIDE_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDL3STARSINSOUTH():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDL3STARSINSOUTH_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3STARSINSOUTH_long')) 
            self.strat_CDL3STARSINSOUTH_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3STARSINSOUTH_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDL3STARSINSOUTH_set)
            self.strat_CDL3STARSINSOUTH_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDL3STARSINSOUTH_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDL3STARSINSOUTH_long,self.strat_CDL3STARSINSOUTH_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDL3STARSINSOUTH_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDL3WHITESOLDIERS():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDL3WHITESOLDIERS_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3WHITESOLDIERS_long')) 
            self.strat_CDL3WHITESOLDIERS_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3WHITESOLDIERS_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDL3WHITESOLDIERS_set)
            self.strat_CDL3WHITESOLDIERS_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDL3WHITESOLDIERS_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDL3WHITESOLDIERS_long,self.strat_CDL3WHITESOLDIERS_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDL3WHITESOLDIERS_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDLABANDONEDBABY():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDLABANDONEDBABY_penetration = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLABANDONEDBABY_penetration')) 
            self.strat_CDLABANDONEDBABY_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLABANDONEDBABY_long')) 
            self.strat_CDLABANDONEDBABY_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLABANDONEDBABY_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDLABANDONEDBABY_set)
            self.strat_CDLABANDONEDBABY_penetration = float(config_set.get(f'{str(number_trade)}_section', 'penetration'))
            self.strat_CDLABANDONEDBABY_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDLABANDONEDBABY_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDLABANDONEDBABY_penetration,self.strat_CDLABANDONEDBABY_long,self.strat_CDLABANDONEDBABY_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDLABANDONEDBABY_set)
        return {
            'penetration': float(config_set.get(f'{str(number)}_section', 'penetration')),
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDLADVANCEBLOCK():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDLADVANCEBLOCK_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLADVANCEBLOCK_long')) 
            self.strat_CDLADVANCEBLOCK_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLADVANCEBLOCK_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDLADVANCEBLOCK_set)
            self.strat_CDLADVANCEBLOCK_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDLADVANCEBLOCK_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDLADVANCEBLOCK_long,self.strat_CDLADVANCEBLOCK_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDLADVANCEBLOCK_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDLBELTHOLD():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDLBELTHOLD_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLBELTHOLD_long')) 
            self.strat_CDLBELTHOLD_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLBELTHOLD_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDLBELTHOLD_set)
            self.strat_CDLBELTHOLD_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDLBELTHOLD_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDLBELTHOLD_long,self.strat_CDLBELTHOLD_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDLBELTHOLD_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDLCLOSINGMARUBOZU():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDLCLOSINGMARUBOZU_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLCLOSINGMARUBOZU_long')) 
            self.strat_CDLCLOSINGMARUBOZU_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLCLOSINGMARUBOZU_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDLCLOSINGMARUBOZU_set)
            self.strat_CDLCLOSINGMARUBOZU_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDLCLOSINGMARUBOZU_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDLCLOSINGMARUBOZU_long,self.strat_CDLCLOSINGMARUBOZU_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDLCLOSINGMARUBOZU_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDLCOUNTERATTACK():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDLCOUNTERATTACK_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLCOUNTERATTACK_long')) 
            self.strat_CDLCOUNTERATTACK_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLCOUNTERATTACK_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDLCOUNTERATTACK_set)
            self.strat_CDLCOUNTERATTACK_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDLCOUNTERATTACK_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDLCOUNTERATTACK_long,self.strat_CDLCOUNTERATTACK_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDLCOUNTERATTACK_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDLDARKCLOUDCOVER():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDLDARKCLOUDCOVER_penetration = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLDARKCLOUDCOVER_penetration')) 
            self.strat_CDLDARKCLOUDCOVER_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLDARKCLOUDCOVER_long')) 
            self.strat_CDLDARKCLOUDCOVER_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLDARKCLOUDCOVER_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDLDARKCLOUDCOVER_set)
            self.strat_CDLDARKCLOUDCOVER_penetration = float(config_set.get(f'{str(number_trade)}_section', 'penetration'))
            self.strat_CDLDARKCLOUDCOVER_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDLDARKCLOUDCOVER_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDLDARKCLOUDCOVER_penetration,self.strat_CDLDARKCLOUDCOVER_long,self.strat_CDLDARKCLOUDCOVER_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDLDARKCLOUDCOVER_set)
        return {
            'penetration': float(config_set.get(f'{str(number)}_section', 'penetration')),
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDLENGULFING():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDLENGULFING_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLENGULFING_long')) 
            self.strat_CDLENGULFING_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLENGULFING_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDLENGULFING_set)
            self.strat_CDLENGULFING_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDLENGULFING_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDLENGULFING_long,self.strat_CDLENGULFING_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDLENGULFING_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDLEVENINGDOJISTAR():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDLEVENINGDOJISTAR_penetration = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLEVENINGDOJISTAR_penetration')) 
            self.strat_CDLEVENINGDOJISTAR_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLEVENINGDOJISTAR_long')) 
            self.strat_CDLEVENINGDOJISTAR_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLEVENINGDOJISTAR_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDLEVENINGDOJISTAR_set)
            self.strat_CDLEVENINGDOJISTAR_penetration = float(config_set.get(f'{str(number_trade)}_section', 'penetration'))
            self.strat_CDLEVENINGDOJISTAR_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDLEVENINGDOJISTAR_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDLEVENINGDOJISTAR_penetration,self.strat_CDLEVENINGDOJISTAR_long,self.strat_CDLEVENINGDOJISTAR_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDLEVENINGDOJISTAR_set)
        return {
            'penetration': float(config_set.get(f'{str(number)}_section', 'penetration')),
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDLGRAVESTONEDOJI():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDLGRAVESTONEDOJI_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLGRAVESTONEDOJI_long')) 
            self.strat_CDLGRAVESTONEDOJI_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLGRAVESTONEDOJI_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDLGRAVESTONEDOJI_set)
            self.strat_CDLGRAVESTONEDOJI_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDLGRAVESTONEDOJI_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDLGRAVESTONEDOJI_long,self.strat_CDLGRAVESTONEDOJI_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDLGRAVESTONEDOJI_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDLHAMMER():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDLHAMMER_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLHAMMER_long')) 
            self.strat_CDLHAMMER_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLHAMMER_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDLHAMMER_set)
            self.strat_CDLHAMMER_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDLHAMMER_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDLHAMMER_long,self.strat_CDLHAMMER_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDLHAMMER_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDLHANGINGMAN():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDLHANGINGMAN_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLHANGINGMAN_long')) 
            self.strat_CDLHANGINGMAN_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLHANGINGMAN_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDLHANGINGMAN_set)
            self.strat_CDLHANGINGMAN_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDLHANGINGMAN_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDLHANGINGMAN_long,self.strat_CDLHANGINGMAN_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDLHANGINGMAN_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDLHARAMI():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDLHARAMI_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLHARAMI_long')) 
            self.strat_CDLHARAMI_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLHARAMI_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDLHARAMI_set)
            self.strat_CDLHARAMI_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDLHARAMI_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDLHARAMI_long,self.strat_CDLHARAMI_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDLHARAMI_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDLHARAMICROSS():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDLHARAMICROSS_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLHARAMICROSS_long')) 
            self.strat_CDLHARAMICROSS_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLHARAMICROSS_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDLHARAMICROSS_set)
            self.strat_CDLHARAMICROSS_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDLHARAMICROSS_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDLHARAMICROSS_long,self.strat_CDLHARAMICROSS_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDLHARAMICROSS_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDLHOMINGPIGEON():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDLHOMINGPIGEON_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLHOMINGPIGEON_long')) 
            self.strat_CDLHOMINGPIGEON_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLHOMINGPIGEON_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDLHOMINGPIGEON_set)
            self.strat_CDLHOMINGPIGEON_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDLHOMINGPIGEON_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDLHOMINGPIGEON_long,self.strat_CDLHOMINGPIGEON_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDLHOMINGPIGEON_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDLINVERTEDHAMMER():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDLINVERTEDHAMMER_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLINVERTEDHAMMER_long')) 
            self.strat_CDLINVERTEDHAMMER_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLINVERTEDHAMMER_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDLINVERTEDHAMMER_set)
            self.strat_CDLINVERTEDHAMMER_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDLINVERTEDHAMMER_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDLINVERTEDHAMMER_long,self.strat_CDLINVERTEDHAMMER_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDLINVERTEDHAMMER_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDLLADDERBOTTOM():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDLLADDERBOTTOM_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLLADDERBOTTOM_long')) 
            self.strat_CDLLADDERBOTTOM_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLLADDERBOTTOM_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDLLADDERBOTTOM_set)
            self.strat_CDLLADDERBOTTOM_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDLLADDERBOTTOM_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDLLADDERBOTTOM_long,self.strat_CDLLADDERBOTTOM_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDLLADDERBOTTOM_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDLLONGLEGGEDDOJI():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDLLONGLEGGEDDOJI_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLLONGLEGGEDDOJI_long')) 
            self.strat_CDLLONGLEGGEDDOJI_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLLONGLEGGEDDOJI_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDLLONGLEGGEDDOJI_set)
            self.strat_CDLLONGLEGGEDDOJI_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDLLONGLEGGEDDOJI_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDLLONGLEGGEDDOJI_long,self.strat_CDLLONGLEGGEDDOJI_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDLLONGLEGGEDDOJI_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDLMATCHINGLOW():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDLMATCHINGLOW_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLMATCHINGLOW_long')) 
            self.strat_CDLMATCHINGLOW_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLMATCHINGLOW_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDLMATCHINGLOW_set)
            self.strat_CDLMATCHINGLOW_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDLMATCHINGLOW_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDLMATCHINGLOW_long,self.strat_CDLMATCHINGLOW_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDLMATCHINGLOW_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDLMORNINGSTAR():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDLMORNINGSTAR_penetration = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLMORNINGSTAR_penetration')) 
            self.strat_CDLMORNINGSTAR_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLMORNINGSTAR_long')) 
            self.strat_CDLMORNINGSTAR_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLMORNINGSTAR_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDLMORNINGSTAR_set)
            self.strat_CDLMORNINGSTAR_penetration = float(config_set.get(f'{str(number_trade)}_section', 'penetration'))
            self.strat_CDLMORNINGSTAR_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDLMORNINGSTAR_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDLMORNINGSTAR_penetration,self.strat_CDLMORNINGSTAR_long,self.strat_CDLMORNINGSTAR_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDLMORNINGSTAR_set)
        return {
            'penetration': float(config_set.get(f'{str(number)}_section', 'penetration')),
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDLRICKSHAWMAN():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDLRICKSHAWMAN_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLRICKSHAWMAN_long')) 
            self.strat_CDLRICKSHAWMAN_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLRICKSHAWMAN_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDLRICKSHAWMAN_set)
            self.strat_CDLRICKSHAWMAN_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDLRICKSHAWMAN_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDLRICKSHAWMAN_long,self.strat_CDLRICKSHAWMAN_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDLRICKSHAWMAN_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDLSPINNINGTOP():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDLSPINNINGTOP_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLSPINNINGTOP_long')) 
            self.strat_CDLSPINNINGTOP_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLSPINNINGTOP_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDLSPINNINGTOP_set)
            self.strat_CDLSPINNINGTOP_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDLSPINNINGTOP_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDLSPINNINGTOP_long,self.strat_CDLSPINNINGTOP_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDLSPINNINGTOP_set)
        return {
            'long': float(config_set.get(f'{str(number)}_section', 'long')),
            'short': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

class CDLTASUKIGAP():
    def __init__(self,regime='one_set',number_trade=0):
        super().__init__()
        if regime=='one_set':
        # Этап штука работает на одной настройке
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            self.strat_CDLTASUKIGAP_long = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLTASUKIGAP_long')) 
            self.strat_CDLTASUKIGAP_short = float(config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLTASUKIGAP_short')) 
        elif regime=='much_set':
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_CDLTASUKIGAP_set)
            self.strat_CDLTASUKIGAP_long = float(config_set.get(f'{str(number_trade)}_section', 'long'))
            self.strat_CDLTASUKIGAP_short = float(config_set.get(f'{str(number_trade)}_section', 'short'))
            
    # Получить настройки одним массивом в режиме одной настройки
    def get_settings(self):
        return [self.strat_CDLTASUKIGAP_long,self.strat_CDLTASUKIGAP_short] # параметры через запятую
        
    def get_set_settings(self,number):
        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_CDLTASUKIGAP_set)
        return {
            'koef_bistro': float(config_set.get(f'{str(number)}_section', 'long')),
            'koef_bistro': float(config_set.get(f'{str(number)}_section', 'short')),
        }   

#-------------------------------------------------------------------------------------------------------------

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        