from variable import *
from imports import *

from src.controllers.settings.strategys.set_strategys import One as One_strat

class One():
    def __init__(self,df):
        super().__init__()
        self.df = df
        self.var = One_strat()
        
    def check_cignal(self):
        self.prepared_df = self.PrepareDF(self.df)
        signal="no" # возвращаемый сигнал, лонг или шорт
        i=len(self.df)-2 # 99 - текущая свеча, которая не закрыта, 98 - последняя закрытая свеча, нам нужно 97, чтобы проверить, нижняя она или верхняяf
        if self.isHCC(self.prepared_df,i-1)>0: # если у нас локальный минимум
            if self.prepared_df['position_in_channel'][i-1]>self.var.strat_one_up_chanal: # проверяем, прижаты ли мы к нижней границе канала
                if self.prepared_df['slope'][i-1]>self.var.strat_one_corner_short: # смотрим, какой у нас наклон графика
                    signal='short'
        if self.isLCC(self.prepared_df,i-1)>0: # если у нас локальный максимум
            if self.prepared_df['position_in_channel'][i-1]<self.var.strat_one_down_chanal: # проверяем, прижаты ли мы к верхней границе канала
                if self.prepared_df['slope'][i-1]<self.var.strat_one_corner_long: # смотрим, какой наклон графика
                    signal='long'
        return signal
    
    
    
    
    # сгенерируйте фрейм данных со всеми необходимыми данными
    def PrepareDF(self,DF):
        ohlc = DF.iloc[:,[0,1,2,3,4,5]]
        ohlc.columns = ["date","open","high","low","close","VOLUME"]
        ohlc=ohlc.set_index('date')
        df = self.indATR(ohlc,14).reset_index()
        df['slope'] = self.indSlope(df['close'],5)
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

    # Определяем наклон ценовой линии
    def indSlope(self,series,n):
        array_sl = [j*0 for j in range(n-1)]
        for j in range(n,len(series)+1):
            y = series[j-n:j]
            x = np.array(range(n))
            x_sc = (x - x.min())/(x.max() - x.min())
            y_sc = (y - y.min())/(y.max() - y.min())
            x_sc = sm.add_constant(x_sc)
            model = sm.OLS(y_sc,x_sc)
            results = model.fit()
            array_sl.append(results.params[-1])
        slope_angle = (np.rad2deg(np.arctan(np.array(array_sl))))
        return np.array(slope_angle)

    # найти локальный максимум
    def isHCC(self,df,i):
        HCC=0
        if df['close'][i]>=df['close'][i+1] and df['close'][i]>=df['close'][i-1] and df['close'][i+1]<df['close'][i-1]:
            #найдена вершина
            HCC = i
        return HCC

    # найти локальный минимум
    def isLCC(self,df,i):
        LCC=0
        if df['close'][i]<=df['close'][i+1] and df['close'][i]<=df['close'][i-1] and df['close'][i+1]>df['close'][i-1]:
            #найдено Дно
            LCC = i-1
        return LCC