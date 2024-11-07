from variable import *
from imports import *

from src.controllers.settings.strategys.set_strategys import CDL2CROWS as CDL2CROWS_strat

class CDL2CROWS():
    def __init__(self,df,regime='one_set',number_set = 0):
        super().__init__()
        self.df = df
        self.index_trade = len(self.df)
        self.data_mas = []
        if regime=='one_set':
            self.var = CDL2CROWS_strat()
        elif regime=='much_set':
            self.var = CDL2CROWS_strat(regime,number_set)
        
    def check_cignal(self):
        # print('CDL2CROWS')
        try:
            res = abstract.CDL2CROWS(self.df)
            # print(res[-1])
            # print(res[len(self.df)-1])
            if res[len(self.df)-1]==100: return 'long'
            elif res[len(self.df)-1]==(-100): return 'short'
            else: return 'no'
        except Exception as e:
            print('wefwefw')
            return 'no'
    