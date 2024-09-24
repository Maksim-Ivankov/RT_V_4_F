
import flet as ft
from variable import *
from imports import *

from src.controllers.settings.set_settings import HisTrade_Svoboda_OneSettings
from src.controllers.trade.check_if_signal import Check_if_signal

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
                # print(f'Отстование - {self.trade_param['step_df']}')
                break
            

    def start_trade(self,change_pb):
        data_numbers = []
        self.calculation_step_df(self.var.COINS[0])
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
                                self.trade_param['price_treyd'] = self.trade_param['df_now_step']['close'][index]
                                self.trade_param['open_time_trade'] = self.trade_param['df_now_step']['open_time'][index]
                                self.open_position() # открываем позицию 
                                self.df_see = pd.read_csv(f'{path_svoboda_freym}\\{self.var.number_trade}\\see\\{coin}.csv')
                                break
                else:
                    try:
                        self.trade_param['df_see'] = self.df_see.iloc[int(self.search_step_see(self.trade_param['index_trade'])):int(self.search_step_see(self.trade_param['index_trade'])+self.trade_param['timeframe'])] # получили датафрейм мини из файла
                    except Exception as e:
                        print(f'Находимся в конце фрейма, не успеваем выйти из сделки - {e}')
                    for nonindex, row in self.trade_param['df_see'].iterrows():
                        if self.check_trade(row['close'],self.var.COMMISSION_MAKER,self.var.COMMISSION_TAKER,self.var.TP,self.var.SL,self.var.LEVERAGE):
                            break # чекаем монету по шагам итерации между большим и мальеньким фреймомd
            self.print_file_log(f'{index}|{self.DEPOSIT_GLOBAL}|{self.trend_mas}|{self.trade_param['trend']}|{self.trade_param['coin']}|{self.trade_param['open_time_trade']}\n',self.path_save_log)
        print('Готово')
        
    # открывает лонг или шорт
    def open_position(self):
        self.trade_param['position'] = True
        self.trade_param['take_profit_price'] = self.get_take_profit(self.trade_param['trend'],self.trade_param['price_treyd'],self.var.TP) # получаем цену тэйк профита
        self.trade_param['stop_loss_price'] = self.get_stop_loss(self.trade_param['trend'],self.trade_param['price_treyd'],self.var.SL) # получаем цену стоп лосса

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
        self.print_file_log(f'{self.trade_param['trend']}|{self.var.DEPOSIT}|{self.DEPOSIT_GLOBAL}|{round(self.profit,2)}|{round(self.comission,2)}|{round(self.local_profit,2)}\n',self.path_save_trade_log)
        self.trade_param['position'] = False































