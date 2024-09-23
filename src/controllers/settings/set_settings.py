import flet as ft
from variable import *
from imports import *

class HisTrade_Svoboda_OneSettings():
    def __init__(self):
        super().__init__()
        
        config = configparser.ConfigParser()  
        config.read(path_imports_config)
        
        sledim_sa_cenoy = {"1m":1,"5m":5} # соедим за ценой
        change_work_tf = {'1m':1,'5m':5,'15m':15,'30m':30,'1h':60,'4h':240} # рабочий таймфрейм в минутах
        change_how_mach_time = {'12h':720,'24h':1440,'48h':2880} # сколько времени торгуем в минутах
        
        self.TF = change_work_tf[config.get('param_trade_historical_trade_svobodniy_freym', 'work_tf')] # таймфрейм
        self.TF_slegenie = sledim_sa_cenoy[config.get('param_trade_historical_trade_svobodniy_freym', 'sledim_money')] # таймфрейм слежения
        self.regime_TP = config.get('param_trade_historical_trade_svobodniy_freym', 'regim_tp') # режим тейка
        self.regime_SL = config.get('param_trade_historical_trade_svobodniy_freym', 'regim_sl') # режим стопа
        self.TP = float(config.get('param_trade_historical_trade_svobodniy_freym', 'tp')) # Тейк профит, процент
        self.SL = float(config.get('param_trade_historical_trade_svobodniy_freym', 'sl')) # Стоп лосс, процент
        self.DEPOSIT = int(config.get('param_trade_historical_trade_svobodniy_freym', 'deposit')) # Депозит
        self.LEVERAGE = int(config.get('param_trade_historical_trade_svobodniy_freym', 'leverage')) # торговое плечо
        self.COMMISSION_MAKER = float(config.get('param_trade_historical_trade_svobodniy_freym', 'komission_mayker')) # комиссия а вход
        self.COMMISSION_TAKER = float(config.get('param_trade_historical_trade_svobodniy_freym', 'komission_taker')) # комиссия на выхд
        self.VOLUME = change_how_mach_time[config.get('param_trade_historical_trade_svobodniy_freym', 'dlitelnost')]/self.TF # сколько свечей получить при запросе к бирже
        self.VOLUME_5MIN = change_how_mach_time[config.get('param_trade_historical_trade_svobodniy_freym', 'dlitelnost')]/self.TF_slegenie # сколько свечей получить в режиме слежения за ценой
        self.regime_CANDLE_COIN_MIN = config.get('param_trade_historical_trade_svobodniy_freym', 'regim_volume_min') # режим объема
        self.regime_CANDLE_COIN_MAX = config.get('param_trade_historical_trade_svobodniy_freym', 'regim_volume_max') # режим объема
        self.CANDLE_COIN_MIN = int(config.get('param_trade_historical_trade_svobodniy_freym', 'volume_min')) # объем торгов за свечку
        self.CANDLE_COIN_MAX = int(config.get('param_trade_historical_trade_svobodniy_freym', 'volume_max')) # объем торгов за свечку
        self.COINS = config.get('param_trade_historical_trade_svobodniy_freym', 'coins_trade').split('|') # монеты для торговли
        
        























