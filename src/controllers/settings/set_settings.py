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
        self.TP = float(config.get('param_trade_historical_trade_svobodniy_freym', 'tp')) # Тейк профит, процент
        "Тейк профит, процент"
        self.SL = float(config.get('param_trade_historical_trade_svobodniy_freym', 'sl')) # Стоп лосс, процент
        "Стоп лосс, процент"
        self.DEPOSIT = int(config.get('param_trade_historical_trade_svobodniy_freym', 'deposit')) # Депозит
        "Депозит"
        self.LEVERAGE = int(config.get('param_trade_historical_trade_svobodniy_freym', 'leverage')) # торговое плечо
        "торговое плечо"
        self.COMMISSION_MAKER = float(config.get('param_trade_historical_trade_svobodniy_freym', 'komission_mayker')) # комиссия на вход
        "комиссия на вход"
        self.COMMISSION_TAKER = float(config.get('param_trade_historical_trade_svobodniy_freym', 'komission_taker')) # комиссия на выхд
        "комиссия на выхд"
        self.VOLUME = int(change_how_mach_time[config.get('param_trade_historical_trade_svobodniy_freym', 'dlitelnost')]/self.TF) # сколько свечей получить при запросе к бирже
        "сколько свечей получить при запросе к бирже"
        self.VOLUME_5MIN = int(change_how_mach_time[config.get('param_trade_historical_trade_svobodniy_freym', 'dlitelnost')]/self.TF_slegenie) # сколько свечей получить в режиме слежения за ценой
        "сколько свечей получить в режиме слежения за ценой"
        self.regime_CANDLE_COIN_MIN = config.get('param_trade_historical_trade_svobodniy_freym', 'regim_volume_min') # режим объема
        "режим объема мин"
        self.regime_CANDLE_COIN_MAX = config.get('param_trade_historical_trade_svobodniy_freym', 'regim_volume_max') # режим объема
        "режим объема макс"
        self.CANDLE_COIN_MIN = int(config.get('param_trade_historical_trade_svobodniy_freym', 'volume_min')) # объем торгов за свечку
        "объем торгов за свечку мин"
        self.CANDLE_COIN_MAX = int(config.get('param_trade_historical_trade_svobodniy_freym', 'volume_max')) # объем торгов за свечку
        "объем торгов за свечку макс"
        self.COINS = config.get('param_trade_historical_trade_svobodniy_freym', 'coins_trade').split('|') # монеты для торговли
        "монеты для торговли"
        self.number_trade = int(config.get('param_trade_historical_trade_svobodniy_freym', 'number_trade')) # номер папки с датафеймами в хранилище
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
                   config.get('param_trade_historical_trade_svobodniy_freym', 'strategys') 
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
        























