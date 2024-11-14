from variable import *
from imports import *

from src.controllers.settings.strategys.set_strategys import *

class HisTrade_Svoboda_OneSettings():
    def __init__(self):
        super().__init__()
        
        config = configparser.ConfigParser()  
        config.read(path_imports_config)
        
        settings_strat = {
            'one': One(),
            'MA': MA(),
            'BBANDS': BBANDS(),
            'EMA': EMA(),
            'DEMA': DEMA(),
            'KAMA': KAMA(),
            'MAVP': MAVP(),
            'SAR': SAR(),
            'TEMA': TEMA(),
            'TRIMA': TRIMA(),
            'WMA': WMA(),
            'CDL2CROWS': CDL2CROWS(),
            'CDL3BLACKCROWS': CDL3BLACKCROWS(),
            'CDL3INSIDE': CDL3INSIDE(),
            'CDL3LINESTRIKE': CDL3LINESTRIKE(),
            'CDL3OUTSIDE': CDL3OUTSIDE(),
            'CDL3STARSINSOUTH': CDL3STARSINSOUTH(),
            'CDL3WHITESOLDIERS': CDL3WHITESOLDIERS(),
            'CDLABANDONEDBABY': CDLABANDONEDBABY(),
            'CDLADVANCEBLOCK': CDLADVANCEBLOCK(),
            'CDLBELTHOLD': CDLBELTHOLD(),
            'CDLCLOSINGMARUBOZU': CDLCLOSINGMARUBOZU(),
            'CDLCOUNTERATTACK': CDLCOUNTERATTACK(),
            'CDLDARKCLOUDCOVER': CDLDARKCLOUDCOVER(),
            'CDLENGULFING': CDLENGULFING(),
            'CDLEVENINGDOJISTAR': CDLEVENINGDOJISTAR(),
            'CDLGRAVESTONEDOJI': CDLGRAVESTONEDOJI(),
            'CDLHAMMER': CDLHAMMER(),
            'CDLHANGINGMAN': CDLHANGINGMAN(),
            'CDLHARAMI': CDLHARAMI(),
            'CDLHARAMICROSS': CDLHARAMICROSS(),
            'CDLHOMINGPIGEON': CDLHOMINGPIGEON(),
            'CDLINVERTEDHAMMER': CDLINVERTEDHAMMER(),
            'CDLLADDERBOTTOM': CDLLADDERBOTTOM(),
            'CDLLONGLEGGEDDOJI': CDLLONGLEGGEDDOJI(),
            'CDLMATCHINGLOW': CDLMATCHINGLOW(),
            'CDLMORNINGSTAR': CDLMORNINGSTAR(),
            'CDLRICKSHAWMAN': CDLRICKSHAWMAN(),
            'CDLSPINNINGTOP': CDLSPINNINGTOP(),
            'CDLTASUKIGAP': CDLTASUKIGAP(),
        }
        
        sledim_sa_cenoy = {"1m":1,"5m":5} # соедим за ценой
        change_work_tf = {'1m':1,'5m':5,'15m':15,'30m':30,'1h':60,'4h':240} # рабочий таймфрейм в минутах
        change_how_mach_time = {'12h':720,'24h':1440,'48h':2880} # сколько времени торгуем в минутах
        
        self.TF = change_work_tf[config.get('param_trade_historical_trade_svobodniy_freym', 'work_tf')] # таймфрейм
        "рабочий таймфрейм в минутах"
        self.TF_slegenie = sledim_sa_cenoy[config.get('param_trade_historical_trade_svobodniy_freym', 'sledim_money')] # таймфрейм слежения
        "таймфрейм слежения в минутах"
        self.regime_TP = config.get('param_trade_historical_trade_svobodniy_freym', 'regim_tp') # режим тейка
        "режим тейка"
        self.regime_SL = config.get('param_trade_historical_trade_svobodniy_freym', 'regim_sl') # режим стопа
        "режим стопа"
        self.TP = float(config.get('param_trade_historical_trade_svobodniy_freym', 'tp'))/100 # Тейк профит, процент
        "Тейк профит, процент"
        self.SL = float(config.get('param_trade_historical_trade_svobodniy_freym', 'sl'))/100 # Стоп лосс, процент
        "Стоп лосс, процент"
        self.DEPOSIT = int(config.get('param_trade_historical_trade_svobodniy_freym', 'deposit')) # Депозит
        "Депозит"
        self.LEVERAGE = int(config.get('param_trade_historical_trade_svobodniy_freym', 'leverage')) # торговое плечо
        "торговое плечо"
        self.COMMISSION_MAKER = float(config.get('param_trade_historical_trade_svobodniy_freym', 'komission_mayker'))/100 # комиссия на вход
        "комиссия на вход"
        self.COMMISSION_TAKER = float(config.get('param_trade_historical_trade_svobodniy_freym', 'komission_taker'))/100 # комиссия на выхд
        "комиссия на выхд"
        self.VOLUME = int(change_how_mach_time[config.get('param_trade_historical_trade_svobodniy_freym', 'dlitelnost')]/self.TF) # сколько свечей получить при запросе к бирже
        "сколько свечей получить при запросе к бирже"
        self.VOLUME_5MIN = int(change_how_mach_time[config.get('param_trade_historical_trade_svobodniy_freym', 'dlitelnost')]/self.TF_slegenie) # сколько свечей получить в режиме слежения за ценой
        "сколько свечей получить в режиме слежения за ценой"
        self.regime_CANDLE_COIN_MIN = config.get('param_trade_historical_trade_svobodniy_freym', 'regim_volume_min') # режим объема
        "режим объема мин"
        self.regime_CANDLE_COIN_MAX = config.get('param_trade_historical_trade_svobodniy_freym', 'regim_volume_max') # режим объема
        "режим объема макс"
        if config.get('param_trade_historical_trade_svobodniy_freym', 'volume_min')[-2]=='.':
            self.CANDLE_COIN_MIN = int(config.get('param_trade_historical_trade_svobodniy_freym', 'volume_min')[:-2]) # объем торгов за свечку
            "объем торгов за свечку мин"
        else: 
            self.CANDLE_COIN_MIN = int(config.get('param_trade_historical_trade_svobodniy_freym', 'volume_min')) # объем торгов за свечку
            "объем торгов за свечку мин"
        if config.get('param_trade_historical_trade_svobodniy_freym', 'volume_min')[-2]=='.':
            self.CANDLE_COIN_MAX = int(config.get('param_trade_historical_trade_svobodniy_freym', 'volume_max')[:-2]) # объем торгов за свечку
            "объем торгов за свечку макс"
        else:
            self.CANDLE_COIN_MAX = int(config.get('param_trade_historical_trade_svobodniy_freym', 'volume_max')) # объем торгов за свечку
            "объем торгов за свечку макс"
        self.COINS = config.get('param_trade_historical_trade_svobodniy_freym', 'coins_trade').split('|') # монеты для торговли
        "монеты для торговли"
        self.change_time_settings = config.get('param_trade_historical_trade_svobodniy_freym', 'change_time_settings') # работает или нет функция торговли по времени
        "1 - работает функция торговли по времени | 0 - не работает функция торговли по времени"
        self.time_on_work = config.get('param_trade_historical_trade_svobodniy_freym', 'time_on_work') # Во сколько часов начать торговлю
        "Во сколько часов начать торговлю"
        self.time_off_work = config.get('param_trade_historical_trade_svobodniy_freym', 'time_off_work') # Во сколько часов выключить торговлю
        "Во сколько часов выключить торговлю"
        
        self.regime_trade_page = config.get('param_trade_historical_trade_svobodniy_freym', 'regime_trade_page')
        if self.regime_trade_page == 'svoboda':
            self.use_last_sost = config.get('param_trade_historical_trade_svobodniy_freym', 'use_last_sost')
            if config.get('param_trade_historical_trade_svobodniy_freym', 'use_last_sost') == 'True':
                self.number_trade = int(config.get('param_trade_historical_trade_svobodniy_freym', 'use_last_number')) # номер папки с датафеймами в хранилище
                self.use_last_number = int(config.get('param_trade_historical_trade_svobodniy_freym', 'use_last_number')) # номер папки с датафеймами в хранилище
                "номер папки с датафеймами в хранилище"
            else:
                self.number_trade = int(config.get('param_trade_historical_trade_svobodniy_freym', 'number_trade')) # номер папки с датафеймами в хранилище
                "номер папки с датафеймами в хранилище"
        elif self.regime_trade_page == 'historical':
            self.use_last_sost = config.get('param_trade_historical_trade_svobodniy_freym', 'use_last_sost_historical')
            if config.get('param_trade_historical_trade_svobodniy_freym', 'use_last_sost_historical') == 'True':
                self.number_trade = int(config.get('param_trade_historical_trade_svobodniy_freym', 'use_last_number_historical')) # номер папки с датафеймами в хранилище
                self.use_last_number = int(config.get('param_trade_historical_trade_svobodniy_freym', 'use_last_number_historical')) # номер папки с датафеймами в хранилище
                "номер папки с датафеймами в хранилище"
            else:
                self.number_trade = int(config.get('param_trade_historical_trade_svobodniy_freym', 'number_trade_historical')) # номер папки с датафеймами в хранилище
                "номер папки с датафеймами в хранилище"
        
        
            
        
        # Сохраняем общие настройки в папку с трейдом
        if len(os.listdir(path_save_trade)) == 0:
            self.path_folder_trade = f'{path_save_trade}\\1'
            os.mkdir(self.path_folder_trade)
        else:
            self.path_folder_trade = f'{path_save_trade}\\{len(os.listdir(path_save_trade))+1}'
            os.mkdir(self.path_folder_trade)
        file = open(f'{self.path_folder_trade}\\settings_our.txt', 'a')
        file.write(config.get('param_trade_historical_trade_svobodniy_freym', 'strategi_coin')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'sledim_money')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'work_tf')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'dlitelnost')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'how_mach_money')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'coins_trade')+'&'+
                   str(self.number_trade)+'&'+
                #    config.get('param_trade_historical_trade_svobodniy_freym', 'number_trade')+'&'+
                   str(self.use_last_number)+'&'+
                #    config.get('param_trade_historical_trade_svobodniy_freym', 'use_last_number')+'&'+
                   str(self.use_last_sost)+'&'+
                #    config.get('param_trade_historical_trade_svobodniy_freym', 'use_last_sost')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'regim_tp')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'regim_sl')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'regim_volume_min')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'regim_volume_max')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'name_bot')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'komission_mayker')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'deposit')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'leverage')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'komission_taker')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'tp')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'sl')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'volume_min')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'volume_max')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'strategys') +'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'change_time_settings') +'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'time_on_work') +'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'time_off_work')
        )
        file.close()
        self.strategys = literal_eval(config.get('param_trade_historical_trade_svobodniy_freym', 'strategys'))
        "Стратегии торговли в массиве"
        for strat in self.strategys:
            strat_obj = settings_strat[strat]
            str_set = ''
            
            for i,data in enumerate(strat_obj.get_settings()):
                if i<(len(strat_obj.get_settings())-1):str_set = str_set+str(data)+'&'
                else:str_set = str_set+str(data)
            file_strat = open(f'{self.path_folder_trade}\\{strat}.txt', 'a')
            file_strat.write(str_set)
            file_strat.close()
        
#1


class HisTrade_Svoboda_SetSettings():
    def __init__(self):
        super().__init__()
        self.strat_set = {}
        config = configparser.ConfigParser()  
        config.read(path_imports_config)
        
        settings_strat = {
            'one': One(),
            'MA': MA(),
            'BBANDS': BBANDS(),
            'EMA': EMA(),
            'DEMA': DEMA(),
            'KAMA': KAMA(),
            'MAVP': MAVP(),
            'SAR': SAR(),
            'TEMA': TEMA(),
            'TRIMA': TRIMA(),
            'WMA': WMA(),
            'CDL2CROWS': CDL2CROWS(),
            'CDL3BLACKCROWS': CDL3BLACKCROWS(),
            'CDL3INSIDE': CDL3INSIDE(),
            'CDL3LINESTRIKE': CDL3LINESTRIKE(),
            'CDL3OUTSIDE': CDL3OUTSIDE(),
            'CDL3STARSINSOUTH': CDL3STARSINSOUTH(),
            'CDL3WHITESOLDIERS': CDL3WHITESOLDIERS(),
            'CDLABANDONEDBABY': CDLABANDONEDBABY(),
            'CDLADVANCEBLOCK': CDLADVANCEBLOCK(),
            'CDLBELTHOLD': CDLBELTHOLD(),
            'CDLCLOSINGMARUBOZU': CDLCLOSINGMARUBOZU(),
            'CDLCOUNTERATTACK': CDLCOUNTERATTACK(),
            'CDLDARKCLOUDCOVER': CDLDARKCLOUDCOVER(),
            'CDLENGULFING': CDLENGULFING(),
            'CDLEVENINGDOJISTAR': CDLEVENINGDOJISTAR(),
            'CDLGRAVESTONEDOJI': CDLGRAVESTONEDOJI(),
            'CDLHAMMER': CDLHAMMER(),
            'CDLHANGINGMAN': CDLHANGINGMAN(),
            'CDLHARAMI': CDLHARAMI(),
            'CDLHARAMICROSS': CDLHARAMICROSS(),
            'CDLHOMINGPIGEON': CDLHOMINGPIGEON(),
            'CDLINVERTEDHAMMER': CDLINVERTEDHAMMER(),
            'CDLLADDERBOTTOM': CDLLADDERBOTTOM(),
            'CDLLONGLEGGEDDOJI': CDLLONGLEGGEDDOJI(),
            'CDLMATCHINGLOW': CDLMATCHINGLOW(),
            'CDLMORNINGSTAR': CDLMORNINGSTAR(),
            'CDLRICKSHAWMAN': CDLRICKSHAWMAN(),
            'CDLSPINNINGTOP': CDLSPINNINGTOP(),
            'CDLTASUKIGAP': CDLTASUKIGAP(),
        }
        
        sledim_sa_cenoy = {"1m":1,"5m":5} # соедим за ценой
        change_work_tf = {'1m':1,'5m':5,'15m':15,'30m':30,'1h':60,'4h':240} # рабочий таймфрейм в минутах
        change_how_mach_time = {'12h':720,'24h':1440,'48h':2880} # сколько времени торгуем в минутах
        
        self.TF = change_work_tf[config.get('param_trade_historical_trade_svobodniy_freym', 'work_tf')] # таймфрейм
        "рабочий таймфрейм в минутах"
        self.TF_slegenie = sledim_sa_cenoy[config.get('param_trade_historical_trade_svobodniy_freym', 'sledim_money')] # таймфрейм слежения
        "таймфрейм слежения в минутах"
        self.COMMISSION_MAKER = float(config.get('param_trade_historical_trade_svobodniy_freym', 'komission_mayker'))/100 # комиссия на вход
        "комиссия на вход"
        self.COMMISSION_TAKER = float(config.get('param_trade_historical_trade_svobodniy_freym', 'komission_taker'))/100 # комиссия на выхд
        "комиссия на выхд"
        self.VOLUME = int(change_how_mach_time[config.get('param_trade_historical_trade_svobodniy_freym', 'dlitelnost')]/self.TF) # сколько свечей получить при запросе к бирже
        "сколько свечей получить при запросе к бирже"
        self.VOLUME_5MIN = int(change_how_mach_time[config.get('param_trade_historical_trade_svobodniy_freym', 'dlitelnost')]/self.TF_slegenie) # сколько свечей получить в режиме слежения за ценой
        "сколько свечей получить в режиме слежения за ценой"
        self.COINS = config.get('param_trade_historical_trade_svobodniy_freym', 'coins_trade').split('|') # монеты для торговли
        "монеты для торговли"
        if config.get('param_trade_historical_trade_svobodniy_freym', 'use_last_sost') == 'True':
            self.number_trade = int(config.get('param_trade_historical_trade_svobodniy_freym', 'use_last_number')) # номер папки с датафеймами в хранилище
            "номер папки с датафеймами в хранилище"
        else:
            self.number_trade = int(config.get('param_trade_historical_trade_svobodniy_freym', 'number_trade')) # номер папки с датафеймами в хранилище
            "номер папки с датафеймами в хранилище"

#1

        config_set = configparser.ConfigParser()  
        config_set.read(path_ini_general_set)
        count_set_trade = len(config_set.sections()) # например, 3
        self.data_set = {}
        for i in range(1,count_set_trade+1):
            self.data_set[str(i)] = {
                'start_time': config_set.get(f'{str(i)}_section', 'start_time'),
                'stop_time': config_set.get(f'{str(i)}_section', 'stop_time'),
                'depo': int(config_set.get(f'{str(i)}_section', 'depo')),
                'leveradg': int(config_set.get(f'{str(i)}_section', 'leveradg')),
                'diapazon_tp': float(config_set.get(f'{str(i)}_section', 'diapazon_tp'))/100,
                'diapazon_sl': float(config_set.get(f'{str(i)}_section', 'diapazon_sl'))/100,
                'diapazon_volume_min': float(config_set.get(f'{str(i)}_section', 'diapazon_volume_min')),
                'diapazon_volume_max': float(config_set.get(f'{str(i)}_section', 'diapazon_volume_max')),
                'time_on_work': config_set.get(f'{str(i)}_section', 'start_time'),
                'time_off_work': config_set.get(f'{str(i)}_section', 'stop_time'),
            }
            
        # Сохраняем общие настройки в папку с трейдом
        if len(os.listdir(path_save_trade)) == 0:
            self.path_folder_trade = f'{path_save_trade}\\1'
            os.mkdir(self.path_folder_trade)
        else:
            self.path_folder_trade = f'{path_save_trade}\\{len(os.listdir(path_save_trade))+1}'
            os.mkdir(self.path_folder_trade)
        file = open(f'{self.path_folder_trade}\\settings_our.txt', 'a')
        file.write(config.get('param_trade_historical_trade_svobodniy_freym', 'strategi_coin')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'sledim_money')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'work_tf')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'dlitelnost')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'how_mach_money')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'coins_trade')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'number_trade')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'use_last_number')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'use_last_sost')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'regim_tp')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'regim_sl')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'regim_volume_min')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'regim_volume_max')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'name_bot')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'komission_mayker')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'deposit')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'leverage')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'komission_taker')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'tp')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'sl')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'volume_min')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'volume_max')+'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'strategys') +'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'change_time_settings') +'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'time_on_work') +'&'+
                   config.get('param_trade_historical_trade_svobodniy_freym', 'time_off_work')
        )
        file.close()
            
            
        self.strategys = literal_eval(config.get('param_trade_historical_trade_svobodniy_freym', 'strategys'))
        "Стратегии торговли в массиве"
        # print(f'Стратегии - {self.strategys}')
        for strat in self.strategys:
            strat_obj = settings_strat[strat]
            for i in range(1,count_set_trade+1): # тогда здесь идем по 1,2,3
                 self.strat_set[i] = {strat:strat_obj.get_set_settings(i) # strat_set[1] = {'one':one.get_set_settings(1)} - здесь формируется сет настроек для торговли
                 }
            














