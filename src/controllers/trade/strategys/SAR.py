from variable import *
from imports import *

from src.controllers.settings.strategys.set_strategys import SAR as SAR_strat

class SAR():
    def __init__(self,df,regime='one_set',number_set = 0):
        super().__init__()
        self.df = df
        self.index_trade = len(self.df)
        self.data_mas = []
        if regime=='one_set':
            self.var = SAR_strat()
        elif regime=='much_set':
            self.var = SAR_strat(regime,number_set)
        
    def check_cignal(self):
        try:
            return 'no'
        except Exception as e:
            return 'no'
    