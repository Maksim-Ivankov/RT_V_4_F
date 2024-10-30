from variable import *
from imports import *

from src.controllers.trade.strategys.one import One
from src.controllers.trade.strategys.MA import MA

class Check_if_signal():
    def __init__(self,df,strategys,regime='one_set',number_set=0):
        # print(f'Стратгеия - {strategys}')
        super().__init__()
        self.df = df
        self.strategys = strategys
        self.regime = regime
        self.number_set = number_set
        # if regime=='one_set':
        #     self.strategys_start = {
        #         'one':One(self.df),
        #         'MA':MA(self.df)
        #     }
        # elif regime=='much_set':
            # self.strategys_start = {
            #     'one':One(self.df,regime,number_set),
            #     'MA':MA(self.df,regime,number_set)
            # }
            
        
        
    
    def work_strat_trade(self):
        result_strat = []
        for strat in self.strategys:
            if self.regime=='one_set':
                if strat == 'one': trade_obj = One(self.df)
                if strat == 'MA': trade_obj = MA(self.df)
            elif self.regime=='much_set':
                if strat == 'one': trade_obj = One(self.df,self.regime,self.number_set)
                if strat == 'MA': trade_obj = MA(self.df,self.regime,self.number_set)
            result_strat.append(trade_obj.check_cignal())
        return result_strat
        # result_strat = []
        # for strat in self.strategys:
        #     trade_obj = self.strategys_start[strat]
        #     result_strat.append(trade_obj.check_cignal())
        # return result_strat