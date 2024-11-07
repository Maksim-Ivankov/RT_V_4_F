from variable import *
from imports import *

from src.controllers.settings.strategys.set_strategys import CDLSPINNINGTOP as CDLSPINNINGTOP_strat

class CDLSPINNINGTOP():
    def __init__(self,df,regime='one_set',number_set = 0):
        super().__init__()
        self.df = df
        self.index_trade = len(self.df)
        self.data_mas = []
        if regime=='one_set':
            self.var = CDLSPINNINGTOP_strat()
        elif regime=='much_set':
            self.var = CDLSPINNINGTOP_strat(regime,number_set)
        
    def check_cignal(self):
        try:
            res = abstract.CDLSPINNINGTOP(self.df)
            # print(res[-1])
            if res[len(self.df)-1]==100: return 'long'
            elif res[len(self.df)-1]==(-100): return 'short'
            else: return 'no'
        except Exception as e:
            return 'no'
    