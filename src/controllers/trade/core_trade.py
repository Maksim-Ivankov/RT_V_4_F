
import flet as ft
from variable import *
from imports import *

from src.controllers.settings.set_settings import HisTrade_Svoboda_OneSettings

class Core_trade():
    def __init__(self,regime,strategy):
        super().__init__()
        self.regime = regime
        self.strategy = strategy
        
        get_settings_our = {
            'Историческая торговля|Свободный фрейм|Ода настройка': HisTrade_Svoboda_OneSettings(),
        }
        self.var = get_settings_our[regime] # объект, хранящий все переменные общих настроек
        self.INDEX_START = 20 # начинаем не с нуля, а с 20 свечи
        self.path_save_log = f'{path_save_trade}\\{len(os.listdir(path_save_trade))}\\log_trade.txt' # путь сохранения логов в папке трейда
        
        self.trade_param = {
            'position':False, # стоим в позиции или нет
        }
        
        
    def print_file_log(self,msg,path):
        file = open(path,'a')
        file.write(msg)
        file.close()
            

    def start_trade(self):
        data_numbers = []
        for index in range(self.var.VOLUME):
            data_numbers.append(index) # добавляем в массив номера итераций - 0,1,2,3 - имитируем реальную торговлю
            if index>self.INDEX_START: # начинаем не с нуля, а с 20-ой свечи
                # self.print_file_log(f'{index}\n',self.path_save_log)
                if self.trade_param['position'] == False: # если не стоим в позиции
                    for coin in self.var.COINS:
                        df = pd.read_csv(f'{path_svoboda_freym}\\{self.var.number_trade}\\work\\{coin}.csv') # получили датафрейм по монете из файла
                        print(df)



































