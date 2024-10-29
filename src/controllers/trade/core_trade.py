
import flet as ft
from variable import *
from imports import *

from src.controllers.settings.set_settings import HisTrade_Svoboda_OneSettings, HisTrade_Svoboda_SetSettings
from src.controllers.trade.check_if_signal import Check_if_signal

class Core_trade():
    def __init__(self,regime,strategy):
        super().__init__()
        self.regime = regime
        self.strategy = strategy
        
        get_settings_our = {
            'Историческая торговля|Свободный фрейм|Ода настройка': HisTrade_Svoboda_OneSettings(),
            'Историческая торговля|Свободный фрейм|Сет настроек': HisTrade_Svoboda_SetSettings(),
        }
        self.INDEX_START = 20 # начинаем не с нуля, а с 20 свечи
        if self.regime == 'Историческая торговля|Свободный фрейм|Ода настройка':
            self.var = get_settings_our[regime] # объект, хранящий все переменные общих настроек
            self.path_save_log = f'{path_save_trade}\\{len(os.listdir(path_save_trade))}\\log_trade.txt' # путь сохранения логов в папке трейда
            self.path_save_trade_log = f'{path_save_trade}\\{len(os.listdir(path_save_trade))}\\trade.txt' # путь сохранения логов в папке трейда
            self.DEPOSIT_GLOBAL = self.var.DEPOSIT
            self.trend_mas = []

            self.trade_param = {
                'position':False, # стоим в позиции или нет
                'coin':'', # монета, которую сейчас рассматриваем
                'trend':'', # записываем тренд - лонг, шорт или no
                'price_treyd':'', # цена входа в сделку
                'open_time_trade':'', # время входа в сделку
                'take_profit_price':'', # цена тейк профита
                'stop_loss_price':'', # цена стоп лосса
            }
        elif self.regime == 'Историческая торговля|Свободный фрейм|Сет настроек':
            self.var = get_settings_our[regime]
            # print(self.var.data_set)
            # print('-----------------')
            # print(self.var.strat_set)
            
        
    # пишем в файл результаты на каждом шаге
    def print_file_log(self,msg,path):
        file = open(path,'a')
        file.write(msg)
        file.close()
        
    def count_result_trade(self,res,index):
        self.count_none = 0
        self.coun_long =0
        self.count_short = 0
        for i in res:
            if i == 'no':self.count_none+=1
            if i == 'long':self.coun_long+=1
            if i == 'short':self.count_short+=1
        if len(res)==1:
            return res[0]
        else:
            if res.count(res[0]) == len(res): return res[0]
            else: return 'no'
            
    # считаем шаг совпадения времени датафрейма рабочего и слежения
    def search_step_see(self,index):
        return (self.trade_param['step_df'] + (self.var.VOLUME_5MIN/self.var.VOLUME)*index)
    
    # считаем шаг остатвания фреймов
    # проверено на сет
    def calculation_step_df(self,coin):
        df_work = pd.read_csv(f'{path_svoboda_freym}\\{self.var.number_trade}\\work\\{coin}.csv') # получили датафрейм из файла
        df_see = pd.read_csv(f'{path_svoboda_freym}\\{self.var.number_trade}\\see\\{coin}.csv') # получили датафрейм мини из файла
        for index, row in df_work.iterrows():
            self.close_time_work_now = row['close_time']
            break
        for index, row in df_see.iterrows():
            if row['close_time'] == self.close_time_work_now:
                self.trade_param['step_df'] = index
                self.trade_param['timeframe'] = self.var.VOLUME_5MIN/self.var.VOLUME
                break
            

    def start_trade(self,change_pb,add_logi_trade,add_trade_table,print_trade_end,number_trade=0):
        if self.regime == 'Историческая торговля|Свободный фрейм|Ода настройка':
            self.add_trade_table = add_trade_table
            data_numbers = []
            self.calculation_step_df(self.var.COINS[0])
            add_logi_trade('Начали торговлю')
            self.trade_param['index_entry'] = 0
            self.trade_param['index_exit'] = 0
            for index in range(self.var.VOLUME):
                change_pb(index/self.var.VOLUME)
                data_numbers.append(index) # добавляем в массив номера итераций - 0,1,2,3 - имитируем реальную торговлю
                if index>self.INDEX_START: # начинаем не с нуля, а с 20-ой свечи
                    self.trade_param['index_trade'] = index
                    if self.trade_param['position'] == False: # если не стоим в позиции
                        for coin in self.var.COINS:
                            df = pd.read_csv(f'{path_svoboda_freym}\\{self.var.number_trade}\\work\\{coin}.csv') # получили датафрейм по монете из файла
                            if len(df) != self.var.VOLUME : continue # если размер фрейма не совпадает с тем, который должен быть (фильтр от недавно залистенных монет)
                            self.trade_param['coin'] = coin # монета, которую сейча срассматриваем
                            self.trade_param['df_now_step'] = df.iloc[data_numbers] # фрейм по текущий шаг иетрации по текущей монете
                            # ниже - если входим в диапазон по объёму
                            if self.trade_param['df_now_step']['VOLUME'][index]*self.trade_param['df_now_step']['open'][index]>self.var.CANDLE_COIN_MIN and self.trade_param['df_now_step']['VOLUME'][index]*self.trade_param['df_now_step']['open'][index]<self.var.CANDLE_COIN_MAX:
                                self.check_signal = Check_if_signal(self.trade_param['df_now_step'],self.var.strategys)
                                self.trend_mas = self.check_signal.work_strat_trade()
                                self.trade_param['trend'] = self.count_result_trade(self.trend_mas,index) # получаем сигналы и тут же сортируем
                                if self.trade_param['trend'] != 'no': # если есть сигнал, выходим из цикла
                                    self.trade_param['index_entry'] = index
                                    self.trade_param['price_treyd'] = self.trade_param['df_now_step']['close'][index]
                                    self.trade_param['open_time_trade'] = self.trade_param['df_now_step']['open_time'][index]
                                    self.trade_param['path_df'] = f'{path_svoboda_freym}\\{self.var.number_trade}\\work\\{coin}.csv'
                                    self.open_position() # открываем позицию 
                                    self.df_see = pd.read_csv(f'{path_svoboda_freym}\\{self.var.number_trade}\\see\\{coin}.csv')
                                    add_logi_trade(f'{index}|Сигнал {self.trade_param['trend']}, монета {coin}, цена входа - {self.trade_param['price_treyd']}')
                                    break
                                # else: add_logi_trade(f'{index}|Монета {coin} - Нет сигнала')
                                # add_logi_trade(f'')
                        add_logi_trade(f'{index} Нет сигнала')
                    else:
                        try:
                            self.trade_param['df_see'] = self.df_see.iloc[int(self.search_step_see(self.trade_param['index_trade'])):int(self.search_step_see(self.trade_param['index_trade'])+self.trade_param['timeframe'])] # получили датафрейм мини из файла
                        except Exception as e:
                            add_logi_trade(f'{index}| Закончили торговлю')
                            print(f'Находимся в конце фрейма, не успеваем выйти из сделки - {e}')
                        for nonindex, row in self.trade_param['df_see'].iterrows():
                            self.trade_param['close_time_trade'] = int(row['open_time'])
                            if self.check_trade(row['close'],self.var.COMMISSION_MAKER,self.var.COMMISSION_TAKER,self.var.TP,self.var.SL,self.var.LEVERAGE):
                                if self.local_profit>0: add_logi_trade(f'{index}|Вышли из сделки, депозит - {self.DEPOSIT_GLOBAL}, профит {self.local_profit}')
                                else: add_logi_trade(f'{index}|Вышли из сделки, депозит - {self.DEPOSIT_GLOBAL}, убыток {self.local_profit}')
                                break # чекаем монету по шагам итерации между большим и мальеньким фреймомd
                            else: add_logi_trade(f'{index}|Стоим в сделке')
                self.print_file_log(f'{index}|{self.DEPOSIT_GLOBAL}|{self.trend_mas}|{self.trade_param['trend']}|{self.trade_param['coin']}|{self.trade_param['open_time_trade']}\n',self.path_save_log)
            add_logi_trade(f'Закончили торговлю')
            print_trade_end()
# ________________________________________________________ РЕЖИМ ТОРГОВЛИ ПО СЕТУ НАСТРОЕК ___________________________________________________________
# self.var.data_set
# self.var.data_set[str(self.number_trade_now)]['diapazon_tp']
# {'1': 
#       {
    #       'start_time': '10', 
    #       'stop_time': '19', 
    #       'depo': '100', 
    #       'leveradg': '20', 
    #       'diapazon_tp': '1.2', 
    #       'diapazon_sl': '0.3', 
    #       'diapazon_volume_min': '500000', 
    #       'diapazon_volume_max': '1500000'}, 
    # }}
# -----------------
# self.var.strat_set
# {1: 
#   {'MA': 
#       {
    #       'koef_bistro': 7.0, 
    #       'koef_medleno': 16.0, 
    #       'sovpad_last': 1.0, 
    #       'up_chanal': 0.6, 
    #       'down_chanal': 0.1}}, 
    # }
    
    # if self.regime == 'Историческая торговля|Свободный фрейм|Ода настройка':
    # elif self.regime == 'Историческая торговля|Свободный фрейм|Сет настроек':

        elif self.regime == 'Историческая торговля|Свободный фрейм|Сет настроек':
            self.logger_and_progress_bar = change_pb
            self.number_trade_now = number_trade
            self.path_save_log = f'{path_save_trade}\\{len(os.listdir(path_save_trade))}\\folder_trade\\{number_trade}\\log_trade.txt' # путь сохранения логов в папке трейда
            self.path_save_trade_log = f'{path_save_trade}\\{len(os.listdir(path_save_trade))}\\folder_trade\\{number_trade}\\trade.txt' # путь сохранения логов в папке трейда
            self.DEPOSIT_GLOBAL = self.var.data_set[str(number_trade)]['depo']
            self.trend_mas = []
            
            if not os.path.isdir(f'{path_save_trade}\\{len(os.listdir(path_save_trade))}\\folder_trade'):
                os.mkdir(f'{path_save_trade}\\{len(os.listdir(path_save_trade))}\\folder_trade')
            if not os.path.isdir(f'{path_save_trade}\\{len(os.listdir(path_save_trade))}\\folder_trade\\{number_trade}'):
                os.mkdir(f'{path_save_trade}\\{len(os.listdir(path_save_trade))}\\folder_trade\\{number_trade}')

            self.trade_param = {
                'position':False, # стоим в позиции или нет
                'coin':'', # монета, которую сейчас рассматриваем
                'trend':'', # записываем тренд - лонг, шорт или no
                'price_treyd':'', # цена входа в сделку
                'open_time_trade':'', # время входа в сделку
                'take_profit_price':'', # цена тейк профита
                'stop_loss_price':'', # цена стоп лосса
            }
            # self.add_trade_table = add_trade_table # добавление сделок в окно сделок
            data_numbers = [] # добавляем в массив номера итераций - 0,1,2,3 - имитируем реальную торговлю
            data_numbers[:] = [] # обнуляем массив
            self.calculation_step_df(self.var.COINS[0])
            # add_logi_trade('Начали торговлю') # добавление логов в окно логов
            self.trade_param['index_entry'] = 0
            self.trade_param['index_exit'] = 0
            
            for index in range(self.var.VOLUME):
                change_pb(index/self.var.VOLUME) # прогрессбар
                data_numbers.append(index) # добавляем в массив номера итераций - 0,1,2,3 - имитируем реальную торговлю
                if index>self.INDEX_START: # начинаем не с нуля, а с 20-ой свечи
                    self.trade_param['index_trade'] = index
                    if self.trade_param['position'] == False: # если не стоим в позиции
                        for coin in self.var.COINS:
                            df = pd.read_csv(f'{path_svoboda_freym}\\{self.var.number_trade}\\work\\{coin}.csv') # получили датафрейм по монете из файла
                            if len(df) != self.var.VOLUME : continue # если размер фрейма не совпадает с тем, который должен быть (фильтр от недавно залистенных монет)
                            self.trade_param['coin'] = coin # монета, которую сейча срассматриваем
                            self.trade_param['df_now_step'] = df.iloc[data_numbers] # фрейм по текущий шаг иетрации по текущей монете
                            # ниже - если входим в диапазон по объёму
                            if self.trade_param['df_now_step']['VOLUME'][index]*self.trade_param['df_now_step']['open'][index]>int(self.var.data_set[str(number_trade)]['diapazon_volume_min']) and self.trade_param['df_now_step']['VOLUME'][index]*self.trade_param['df_now_step']['open'][index]<int(self.var.data_set[str(number_trade)]['diapazon_volume_max']):
                                self.check_signal = Check_if_signal(self.trade_param['df_now_step'],self.var.strategys,'much_set',number_trade)
                                self.trend_mas = self.check_signal.work_strat_trade()
                                self.trade_param['trend'] = self.count_result_trade(self.trend_mas,index) # получаем сигналы и тут же сортируем
                                if self.trade_param['trend'] != 'no': # если есть сигнал, выходим из цикла
                                    self.trade_param['index_entry'] = index
                                    self.trade_param['price_treyd'] = self.trade_param['df_now_step']['close'][index]
                                    self.trade_param['open_time_trade'] = self.trade_param['df_now_step']['open_time'][index]
                                    self.trade_param['path_df'] = f'{path_svoboda_freym}\\{self.var.number_trade}\\work\\{coin}.csv'
                                    self.open_position() # открываем позицию 
                                    self.df_see = pd.read_csv(f'{path_svoboda_freym}\\{self.var.number_trade}\\see\\{coin}.csv')
                                    # add_logi_trade(f'{index}|Сигнал {self.trade_param['trend']}, монета {coin}, цена входа - {self.trade_param['price_treyd']}')
                                    # print(f'{self.number_trade_now}|{index} - СИГНАЛ!!!')
                                    break
                                # else: print(f'{self.number_trade_now}|{index} - Нет сигнала')
                        # add_logi_trade(f'{index} Нет сигнала')
                    else:
                        try:
                            self.trade_param['df_see'] = self.df_see.iloc[int(self.search_step_see(self.trade_param['index_trade'])):int(self.search_step_see(self.trade_param['index_trade'])+self.trade_param['timeframe'])] # получили датафрейм мини из файла
                        except Exception as e:
                            pass
            #                 add_logi_trade(f'{index}| Закончили торговлю')
            #                 print(f'Находимся в конце фрейма, не успеваем выйти из сделки - {e}')
                        # print(f'{self.number_trade_now}|{index} - В сделке')
                        for nonindex, row in self.trade_param['df_see'].iterrows():
                            self.trade_param['close_time_trade'] = int(row['open_time'])
                            # print(f'{self.number_trade_now} | {index} В сделке | вход={self.trade_param['price_treyd']} | сейчас={row['close']} | TP={self.trade_param['take_profit_price']} | SL={self.trade_param['stop_loss_price']} ')
                            if self.check_trade(row['close'],self.var.COMMISSION_MAKER,self.var.COMMISSION_TAKER,self.var.data_set[str(self.number_trade_now)]['diapazon_tp'],self.var.data_set[str(self.number_trade_now)]['diapazon_sl'],self.var.data_set[str(self.number_trade_now)]['leveradg']):
                                # if self.local_profit>0: add_logi_trade(f'{index}|Вышли из сделки, депозит - {self.DEPOSIT_GLOBAL}, профит {self.local_profit}')
            #                     else: add_logi_trade(f'{index}|Вышли из сделки, депозит - {self.DEPOSIT_GLOBAL}, убыток {self.local_profit}')
                                # print(f'{self.number_trade_now} Вышли из сделки - {self.trade_param['index_exit']}')
                                break # чекаем монету по шагам итерации между большим и мальеньким фреймомd
            #                 else: add_logi_trade(f'{index}|Стоим в сделке')
            #     self.print_file_log(f'{index}|{self.DEPOSIT_GLOBAL}|{self.trend_mas}|{self.trade_param['trend']}|{self.trade_param['coin']}|{self.trade_param['open_time_trade']}\n',self.path_save_log)
            # add_logi_trade(f'Закончили торговлю')
            # print_trade_end()


        
    # открывает лонг или шорт
    def open_position(self):
        self.trade_param['position'] = True
        if self.regime == 'Историческая торговля|Свободный фрейм|Ода настройка':
            self.trade_param['take_profit_price'] = self.get_take_profit(self.trade_param['trend'],self.trade_param['price_treyd'],self.var.TP) # получаем цену тэйк профита
            self.trade_param['stop_loss_price'] = self.get_stop_loss(self.trade_param['trend'],self.trade_param['price_treyd'],self.var.SL) # получаем цену стоп лосса
        elif self.regime == 'Историческая торговля|Свободный фрейм|Сет настроек':
            self.trade_param['take_profit_price'] = self.get_take_profit(self.trade_param['trend'],self.trade_param['price_treyd'],float(self.var.data_set[str(self.number_trade_now)]['diapazon_tp'])) # получаем цену тэйк профита
            self.trade_param['stop_loss_price'] = self.get_stop_loss(self.trade_param['trend'],self.trade_param['price_treyd'],float(self.var.data_set[str(self.number_trade_now)]['diapazon_sl'])) # получаем цену стоп лосса

    # получаем цену тейк профита в зависимости от направления
    def get_take_profit(self,trend,price_trade,TP): 
        if trend == 'long':
            return price_trade*(1+TP)
        if trend == 'short':
            return price_trade*(1-TP)

    # получаем цену стоп лосса в зависимости от направления
    def get_stop_loss(self,trend,price_trade,SL): 
        if trend == 'long':
            return price_trade*(1-SL)
        if trend == 'short':
            return price_trade*(1+SL)
        
     # когда в сделке - чекаем, словили тп или сл
    def check_trade(self,price,COMMISSION_MAKER,COMMISSION_TAKER,TP,SL,LEVERAGE):
        if self.trade_param['trend'] == 'long':
            if float(price)>float(self.trade_param['take_profit_price']):
                self.close_trade('+',TP,COMMISSION_MAKER,COMMISSION_TAKER,LEVERAGE)
                return 1
            if float(price)<float(self.trade_param['stop_loss_price']):
                self.close_trade('-',SL,COMMISSION_MAKER,COMMISSION_TAKER,LEVERAGE)
                return 1
        if self.trade_param['trend'] == 'short':
            if float(price)<float(self.trade_param['take_profit_price']):
                self.close_trade('+',TP,COMMISSION_MAKER,COMMISSION_TAKER,LEVERAGE)
                return 1
            if float(price)>float(self.trade_param['stop_loss_price']):
                self.close_trade('-',SL,COMMISSION_MAKER,COMMISSION_TAKER,LEVERAGE)
                return 1

    # Закрываем сделку
    def close_trade(self,status,procent,COMMISSION_MAKER,COMMISSION_TAKER,LEVERAGE):
        if status == '+': # если закрыли в плюс
            self.local_profit = LEVERAGE*self.DEPOSIT_GLOBAL*procent
            self.comission = LEVERAGE*self.DEPOSIT_GLOBAL*(COMMISSION_MAKER+COMMISSION_TAKER)
            self.profit = self.local_profit - self.comission
            self.DEPOSIT_GLOBAL = self.DEPOSIT_GLOBAL + LEVERAGE*self.DEPOSIT_GLOBAL*procent - LEVERAGE*self.DEPOSIT_GLOBAL*(COMMISSION_MAKER+COMMISSION_TAKER) # обновляем размер депо
            self.DEPOSIT_GLOBAL = round(self.DEPOSIT_GLOBAL,2)
            self.place_open_position_profit = round(LEVERAGE*self.DEPOSIT_GLOBAL*procent-LEVERAGE*self.DEPOSIT_GLOBAL*(COMMISSION_MAKER+COMMISSION_TAKER),2)
        if status == '-': # если закрыли в минус
            self.local_profit = -LEVERAGE*self.DEPOSIT_GLOBAL*procent
            self.comission = LEVERAGE*self.DEPOSIT_GLOBAL*(COMMISSION_MAKER+COMMISSION_TAKER)
            self.profit = self.local_profit - self.comission
            self.DEPOSIT_GLOBAL = self.DEPOSIT_GLOBAL - LEVERAGE*self.DEPOSIT_GLOBAL*procent - LEVERAGE*self.DEPOSIT_GLOBAL*(COMMISSION_MAKER+COMMISSION_TAKER) # обновляем размер депо
            self.DEPOSIT_GLOBAL = round(self.DEPOSIT_GLOBAL,2)
            self.place_open_position_profit = round(-LEVERAGE*self.DEPOSIT_GLOBAL*procent-LEVERAGE*self.DEPOSIT_GLOBAL*(COMMISSION_MAKER+COMMISSION_TAKER),2)
        
        self.trade_param['index_exit'] = self.trade_param['index_trade']
        self.trade_param['position'] = False
        if self.regime == 'Историческая торговля|Свободный фрейм|Ода настройка':
            self.print_file_log(f'{self.trade_param['trend']}|{self.var.DEPOSIT}|{self.DEPOSIT_GLOBAL}|{round(self.profit,2)}|{round(self.comission,2)}|{round(self.local_profit,2)}|{self.trade_param['coin']}|{self.trade_param['take_profit_price']}|{self.trade_param['stop_loss_price']}|{self.trade_param['price_treyd']}|{self.trade_param['open_time_trade']}|{self.trade_param['close_time_trade']}|{self.trade_param['path_df']}|{self.trade_param['index_entry']}|{self.trade_param['index_exit']}\n',self.path_save_trade_log)
            if self.profit>0: self.add_trade_table({'result':'+','data':f'{self.trade_param['coin']}| {self.trade_param['trend']} | Депозит: {round(self.DEPOSIT_GLOBAL,2)} | Профит: {round(self.local_profit,2)}'})
            else: self.add_trade_table({'result':'-','data':f'{self.trade_param['coin']}| {self.trade_param['trend']} | Депозит: {round(self.DEPOSIT_GLOBAL,2)} | Убыток: {round(self.local_profit,2)}'})
        elif self.regime == 'Историческая торговля|Свободный фрейм|Сет настроек':
            self.print_file_log(f'{self.trade_param['trend']}|{self.var.data_set[str(self.number_trade_now)]['depo']}|{self.DEPOSIT_GLOBAL}|{round(self.profit,2)}|{round(self.comission,2)}|{round(self.local_profit,2)}|{self.trade_param['coin']}|{self.trade_param['take_profit_price']}|{self.trade_param['stop_loss_price']}|{self.trade_param['price_treyd']}|{self.trade_param['open_time_trade']}|{self.trade_param['close_time_trade']}|{self.trade_param['path_df']}|{self.trade_param['index_entry']}|{self.trade_param['index_exit']}\n',self.path_save_trade_log)
            if self.profit>0: 
                # self.add_trade_table({'result':'+','data':f'{self.trade_param['coin']}| {self.trade_param['trend']} | Депозит: {round(self.DEPOSIT_GLOBAL,2)} | Профит: {round(self.local_profit,2)}'})
                self.logger_and_progress_bar(int(self.trade_param['index_trade'])/self.var.VOLUME,{
                    'result':'+',
                    'data':f'Депо {self.DEPOSIT_GLOBAL}| Рез: {round(self.local_profit,2)}'
                                    })
            else: 
                self.logger_and_progress_bar(int(self.trade_param['index_trade'])/self.var.VOLUME,{
                    'result':'-',
                    'data':f'Депо {self.DEPOSIT_GLOBAL}| Рез: {round(self.local_profit,2)}'
                                    })
                # self.add_trade_table({'result':'-','data':f'{self.trade_param['coin']}| {self.trade_param['trend']} | Депозит: {round(self.DEPOSIT_GLOBAL,2)} | Убыток: {round(self.local_profit,2)}'})
            
        





























