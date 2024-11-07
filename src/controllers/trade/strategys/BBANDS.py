from variable import *
from imports import *

from src.controllers.settings.strategys.set_strategys import BBANDS as BBANDS_strat

class BBANDS():
    def __init__(self,df,regime='one_set',number_set = 0):
        super().__init__()
        self.df = df
        self.index_trade = len(self.df)
        self.data_mas = []
        if regime=='one_set':
            self.var = BBANDS_strat()
        elif regime=='much_set':
            self.var = BBANDS_strat(regime,number_set)
        
    def check_cignal(self):
        # try:
            
            close = self.df['close']
            upper, middle, lower = ta.BBANDS(close.values, self.var.strat_BBANDS_timeperiod, self.var.strat_BBANDS_nbdevup, self.var.strat_BBANDS_nbdevdn, self.var.strat_BBANDS_matype)
            # print((upper[-1] - lower[-1]) / middle[-1])
            # if ((upper[-1] - lower[-1]) / middle[-1])!=0: return 'long'
            if ((upper[-1] - lower[-1]) / middle[-1])>0.01: return 'long'
            else: return 'no'
            
        # except Exception as e:
        #     return 'no'
    
    