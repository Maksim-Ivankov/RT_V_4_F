from variable import *
from imports import *

from src.controllers.settings.strategys.set_strategys import MA as MA_strat

class MA():
    def __init__(self,df,regime='one_set',number_set = 0):
        super().__init__()
        self.df = df
        self.index_trade = len(self.df)
        self.data_mas = []
        if regime=='one_set':
            self.var = MA_strat()
        elif regime=='much_set':
            self.var = MA_strat(regime,number_set)
        
    def check_cignal(self):
        sum_price = 0
        # вычисляем основную скользящую среднюю в текущей точкеf
        for i in range(self.index_trade-int(self.var.strat_ma_koef_bistro),self.index_trade):
            sum_price=sum_price+self.df['close'][i]*(1-(2/(self.index_trade-i+1))*0.01)
        save_middle_price_1 = sum_price/int(self.var.strat_ma_koef_bistro)
        sum_price = 0
        # вычесляем отстающую скользящую среднюю в текущей точке
        for i in range(self.index_trade-int(self.var.strat_ma_koef_medleno),self.index_trade):
            sum_price=sum_price+self.df['close'][i]*(1-(2/(self.index_trade-i+1))*0.01)
        save_middle_price_2 = sum_price/int(self.var.strat_ma_koef_medleno)
        data_once = save_middle_price_1<save_middle_price_2
        # закинуть в массив сравнение скользящих средних ха последние N точек
        for j in range(int(self.index_trade-self.var.strat_ma_sovpad_last),self.index_trade):
            sum_price = 0
            for l in range(j-int(self.var.strat_ma_koef_bistro),j):
                sum_price=sum_price+self.df['close'][l]*(1-(2/(j-l+1))*0.01)
            save_middle_price_11 = sum_price/int(self.var.strat_ma_koef_bistro)
            sum_price = 0
            for l in range(j-int(self.var.strat_ma_koef_medleno),j):
                sum_price=sum_price+self.df['close'][l]*(1-(2/(j-l+1))*0.01)
            save_middle_price_21 = sum_price/int(self.var.strat_ma_koef_medleno)
            self.data_mas.append(save_middle_price_11<save_middle_price_21) 

        prepared_df = self.PrepareDF(self.df)
        i=self.index_trade-2
        if self.all_the_same(self.data_mas)==True:
            # если в массиве все одинаковые
            if self.data_mas[0] == True and data_once==False:
                if prepared_df['position_in_channel'][i-1]<self.var.strat_ma_down_chanal: # проверяем, прижаты ли мы к верхней границе канала
                    self.data_mas[:] = []
                    return 'long'
                else:
                    self.data_mas[:] = []
                    return 'no'
            elif self.data_mas[0] == False and data_once==True:
                if prepared_df['position_in_channel'][i-1]>self.var.strat_ma_up_chanal: # проверяем, прижаты ли мы к нижней границе канала
                    self.data_mas[:] = []
                    return 'short'
                else:
                    self.data_mas[:] = []
                    return 'no'
            else:
                self.data_mas[:] = []
                return 'no'
        else:
            self.data_mas[:] = []
            return 'no'
    
    
    
    # проверяет, одинаковые ли данные в массиве
    def all_the_same(self,elements):
        return len(elements) == elements.count(elements[0])

    # сгенерируйте фрейм данных со всеми необходимыми данными
    def PrepareDF(self,DF):
        ohlc = DF.iloc[:,[0,1,2,3,4,5]]
        ohlc.columns = ["date","open","high","low","close","VOLUME"]
        ohlc=ohlc.set_index('date')
        df = self.indATR(ohlc,14).reset_index()
        df['channel_max'] = df['high'].rolling(10).max() # определяем верхний уровень канала
        df['channel_min'] = df['low'].rolling(10).min() # определяем нижний уровень канала
        df['position_in_channel'] = (df['close']-df['channel_min']) / (df['channel_max']-df['channel_min']) # сейчас находимся выше середины канала или ниже
        df = df.set_index('date')
        df = df.reset_index()
        return(df)

    # Индикатор истинного диапазона и среднего значения истинного диапазона
    def indATR(self,df,n):
        df['H-L']=abs(df['high']-df['low'])
        df['H-PC']=abs(df['high']-df['close'].shift(1))
        df['L-PC']=abs(df['low']-df['close'].shift(1))
        df['TR']=df[['H-L','H-PC','L-PC']].max(axis=1,skipna=False)
        df['ATR'] = df['TR'].rolling(n).mean()
        df_temp = df.drop(['H-L','H-PC','L-PC'],axis=1)
        return df_temp