from variable import *
from imports import *

from src.controllers.trade.strategys.one import One
from src.controllers.trade.strategys.MA import MA

class Check_if_signal():
    def __init__(self,df,strategys):
        super().__init__()
        self.df = df
        self.strategys = strategys
        
        self.strategys_start = {
            'one':One(self.df),
            'MA':MA(self.df)
        }
        
        
    
    def work_strat_trade(self):
        result_strat = []
        for strat in self.strategys:
            trade_obj = self.strategys_start[strat]
            result_strat.append(trade_obj.check_cignal())
        return result_strat