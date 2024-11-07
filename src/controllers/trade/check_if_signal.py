from variable import *
from imports import *

from src.controllers.trade.strategys.one import One
from src.controllers.trade.strategys.MA import MA
from src.controllers.trade.strategys.BBANDS import BBANDS
from src.controllers.trade.strategys.EMA import EMA
from src.controllers.trade.strategys.DEMA import DEMA
from src.controllers.trade.strategys.KAMA import KAMA
from src.controllers.trade.strategys.MAVP import MAVP
from src.controllers.trade.strategys.SAR import SAR
from src.controllers.trade.strategys.TEMA import TEMA
from src.controllers.trade.strategys.TRIMA import TRIMA
from src.controllers.trade.strategys.WMA import WMA
from src.controllers.trade.strategys.CDL2CROWS import CDL2CROWS
from src.controllers.trade.strategys.CDL3BLACKCROWS import CDL3BLACKCROWS
from src.controllers.trade.strategys.CDL3INSIDE import CDL3INSIDE
from src.controllers.trade.strategys.CDL3LINESTRIKE import CDL3LINESTRIKE
from src.controllers.trade.strategys.CDL3OUTSIDE import CDL3OUTSIDE
from src.controllers.trade.strategys.CDL3STARSINSOUTH import CDL3STARSINSOUTH
from src.controllers.trade.strategys.CDL3WHITESOLDIERS import CDL3WHITESOLDIERS
from src.controllers.trade.strategys.CDLABANDONEDBABY import CDLABANDONEDBABY
from src.controllers.trade.strategys.CDLADVANCEBLOCK import CDLADVANCEBLOCK
from src.controllers.trade.strategys.CDLBELTHOLD import CDLBELTHOLD
from src.controllers.trade.strategys.CDLCLOSINGMARUBOZU import CDLCLOSINGMARUBOZU
from src.controllers.trade.strategys.CDLCOUNTERATTACK import CDLCOUNTERATTACK
from src.controllers.trade.strategys.CDLDARKCLOUDCOVER import CDLDARKCLOUDCOVER
from src.controllers.trade.strategys.CDLENGULFING import CDLENGULFING
from src.controllers.trade.strategys.CDLEVENINGDOJISTAR import CDLEVENINGDOJISTAR
from src.controllers.trade.strategys.CDLGRAVESTONEDOJI import CDLGRAVESTONEDOJI
from src.controllers.trade.strategys.CDLHAMMER import CDLHAMMER
from src.controllers.trade.strategys.CDLHANGINGMAN import CDLHANGINGMAN
from src.controllers.trade.strategys.CDLHARAMI import CDLHARAMI
from src.controllers.trade.strategys.CDLHARAMICROSS import CDLHARAMICROSS
from src.controllers.trade.strategys.CDLHOMINGPIGEON import CDLHOMINGPIGEON
from src.controllers.trade.strategys.CDLINVERTEDHAMMER import CDLINVERTEDHAMMER
from src.controllers.trade.strategys.CDLLADDERBOTTOM import CDLLADDERBOTTOM
from src.controllers.trade.strategys.CDLLONGLEGGEDDOJI import CDLLONGLEGGEDDOJI
from src.controllers.trade.strategys.CDLMATCHINGLOW import CDLMATCHINGLOW
from src.controllers.trade.strategys.CDLMORNINGSTAR import CDLMORNINGSTAR
from src.controllers.trade.strategys.CDLRICKSHAWMAN import CDLRICKSHAWMAN
from src.controllers.trade.strategys.CDLSPINNINGTOP import CDLSPINNINGTOP
from src.controllers.trade.strategys.CDLTASUKIGAP import CDLTASUKIGAP

class Check_if_signal():
    def __init__(self,df,strategys,regime='one_set',number_set=0):
        # print(f'Стратгеия - {strategys}')
        super().__init__()
        self.df = df
        self.strategys = strategys
        self.regime = regime
        self.number_set = number_set
            
        
    def work_strat_trade(self):
        result_strat = []
        for strat in self.strategys:
            if self.regime=='one_set':
                if strat == 'one': trade_obj = One(self.df)
                if strat == 'MA': trade_obj = MA(self.df)
                if strat == 'BBANDS': trade_obj = BBANDS(self.df)
                if strat == 'EMA': trade_obj = EMA(self.df)
                if strat == 'DEMA': trade_obj = DEMA(self.df)
                if strat == 'KAMA': trade_obj = KAMA(self.df)
                if strat == 'MAVP': trade_obj = MAVP(self.df)
                if strat == 'SAR': trade_obj = SAR(self.df)
                if strat == 'TEMA': trade_obj = TEMA(self.df)
                if strat == 'TRIMA': trade_obj = TRIMA(self.df)
                if strat == 'WMA': trade_obj = WMA(self.df)
                if strat == 'CDL2CROWS': trade_obj = CDL2CROWS(self.df)
                if strat == 'CDL3BLACKCROWS': trade_obj = CDL3BLACKCROWS(self.df)
                if strat == 'CDL3INSIDE': trade_obj = CDL3INSIDE(self.df)
                if strat == 'CDL3LINESTRIKE': trade_obj = CDL3LINESTRIKE(self.df)
                if strat == 'CDL3OUTSIDE': trade_obj = CDL3OUTSIDE(self.df)
                if strat == 'CDL3STARSINSOUTH': trade_obj = CDL3STARSINSOUTH(self.df)
                if strat == 'CDL3WHITESOLDIERS': trade_obj = CDL3WHITESOLDIERS(self.df)
                if strat == 'CDLABANDONEDBABY': trade_obj = CDLABANDONEDBABY(self.df)
                if strat == 'CDLADVANCEBLOCK': trade_obj = CDLADVANCEBLOCK(self.df)
                if strat == 'CDLBELTHOLD': trade_obj = CDLBELTHOLD(self.df)
                if strat == 'CDLCLOSINGMARUBOZU': trade_obj = CDLCLOSINGMARUBOZU(self.df)
                if strat == 'CDLCOUNTERATTACK': trade_obj = CDLCOUNTERATTACK(self.df)
                if strat == 'CDLDARKCLOUDCOVER': trade_obj = CDLDARKCLOUDCOVER(self.df)
                if strat == 'CDLENGULFING': trade_obj = CDLENGULFING(self.df)
                if strat == 'CDLEVENINGDOJISTAR': trade_obj = CDLEVENINGDOJISTAR(self.df)
                if strat == 'CDLGRAVESTONEDOJI': trade_obj = CDLGRAVESTONEDOJI(self.df)
                if strat == 'CDLHAMMER': trade_obj = CDLHAMMER(self.df)
                if strat == 'CDLHANGINGMAN': trade_obj = CDLHANGINGMAN(self.df)
                if strat == 'CDLHARAMI': trade_obj = CDLHARAMI(self.df)
                if strat == 'CDLHARAMICROSS': trade_obj = CDLHARAMICROSS(self.df)
                if strat == 'CDLHOMINGPIGEON': trade_obj = CDLHOMINGPIGEON(self.df)
                if strat == 'CDLINVERTEDHAMMER': trade_obj = CDLINVERTEDHAMMER(self.df)
                if strat == 'CDLLADDERBOTTOM': trade_obj = CDLLADDERBOTTOM(self.df)
                if strat == 'CDLLONGLEGGEDDOJI': trade_obj = CDLLONGLEGGEDDOJI(self.df)
                if strat == 'CDLMATCHINGLOW': trade_obj = CDLMATCHINGLOW(self.df)
                if strat == 'CDLMORNINGSTAR': trade_obj = CDLMORNINGSTAR(self.df)
                if strat == 'CDLRICKSHAWMAN': trade_obj = CDLRICKSHAWMAN(self.df)
                if strat == 'CDLSPINNINGTOP': trade_obj = CDLSPINNINGTOP(self.df)
                if strat == 'CDLTASUKIGAP': trade_obj = CDLTASUKIGAP(self.df)
            elif self.regime=='much_set':
                if strat == 'one': trade_obj = One(self.df,self.regime,self.number_set)
                if strat == 'MA': trade_obj = MA(self.df,self.regime,self.number_set)
                if strat == 'BBANDS': trade_obj = BBANDS(self.df,self.regime,self.number_set)
                if strat == 'EMA': trade_obj = EMA(self.df,self.regime,self.number_set)
                if strat == 'DEMA': trade_obj = DEMA(self.df,self.regime,self.number_set)
                if strat == 'KAMA': trade_obj = KAMA(self.df,self.regime,self.number_set)
                if strat == 'MAVP': trade_obj = MAVP(self.df,self.regime,self.number_set)
                if strat == 'SAR': trade_obj = SAR(self.df,self.regime,self.number_set)
                if strat == 'TEMA': trade_obj = TEMA(self.df,self.regime,self.number_set)
                if strat == 'TRIMA': trade_obj = TRIMA(self.df,self.regime,self.number_set)
                if strat == 'WMA': trade_obj = WMA(self.df,self.regime,self.number_set)
                if strat == 'CDL2CROWS': trade_obj = CDL2CROWS(self.df,self.regime,self.number_set)
                if strat == 'CDL3BLACKCROWS': trade_obj = CDL3BLACKCROWS(self.df,self.regime,self.number_set)
                if strat == 'CDL3INSIDE': trade_obj = CDL3INSIDE(self.df,self.regime,self.number_set)
                if strat == 'CDL3LINESTRIKE': trade_obj = CDL3LINESTRIKE(self.df,self.regime,self.number_set)
                if strat == 'CDL3OUTSIDE': trade_obj = CDL3OUTSIDE(self.df,self.regime,self.number_set)
                if strat == 'CDL3STARSINSOUTH': trade_obj = CDL3STARSINSOUTH(self.df,self.regime,self.number_set)
                if strat == 'CDL3WHITESOLDIERS': trade_obj = CDL3WHITESOLDIERS(self.df,self.regime,self.number_set)
                if strat == 'CDLABANDONEDBABY': trade_obj = CDLABANDONEDBABY(self.df,self.regime,self.number_set)
                if strat == 'CDLADVANCEBLOCK': trade_obj = CDLADVANCEBLOCK(self.df,self.regime,self.number_set)
                if strat == 'CDLBELTHOLD': trade_obj = CDLBELTHOLD(self.df,self.regime,self.number_set)
                if strat == 'CDLCLOSINGMARUBOZU': trade_obj = CDLCLOSINGMARUBOZU(self.df,self.regime,self.number_set)
                if strat == 'CDLCOUNTERATTACK': trade_obj = CDLCOUNTERATTACK(self.df,self.regime,self.number_set)
                if strat == 'CDLDARKCLOUDCOVER': trade_obj = CDLDARKCLOUDCOVER(self.df,self.regime,self.number_set)
                if strat == 'CDLENGULFING': trade_obj = CDLENGULFING(self.df,self.regime,self.number_set)
                if strat == 'CDLEVENINGDOJISTAR': trade_obj = CDLEVENINGDOJISTAR(self.df,self.regime,self.number_set)
                if strat == 'CDLGRAVESTONEDOJI': trade_obj = CDLGRAVESTONEDOJI(self.df,self.regime,self.number_set)
                if strat == 'CDLHAMMER': trade_obj = CDLHAMMER(self.df,self.regime,self.number_set)
                if strat == 'CDLHANGINGMAN': trade_obj = CDLHANGINGMAN(self.df,self.regime,self.number_set)
                if strat == 'CDLHARAMI': trade_obj = CDLHARAMI(self.df,self.regime,self.number_set)
                if strat == 'CDLHARAMICROSS': trade_obj = CDLHARAMICROSS(self.df,self.regime,self.number_set)
                if strat == 'CDLHOMINGPIGEON': trade_obj = CDLHOMINGPIGEON(self.df,self.regime,self.number_set)
                if strat == 'CDLINVERTEDHAMMER': trade_obj = CDLINVERTEDHAMMER(self.df,self.regime,self.number_set)
                if strat == 'CDLLADDERBOTTOM': trade_obj = CDLLADDERBOTTOM(self.df,self.regime,self.number_set)
                if strat == 'CDLLONGLEGGEDDOJI': trade_obj = CDLLONGLEGGEDDOJI(self.df,self.regime,self.number_set)
                if strat == 'CDLMATCHINGLOW': trade_obj = CDLMATCHINGLOW(self.df,self.regime,self.number_set)
                if strat == 'CDLMORNINGSTAR': trade_obj = CDLMORNINGSTAR(self.df,self.regime,self.number_set)
                if strat == 'CDLRICKSHAWMAN': trade_obj = CDLRICKSHAWMAN(self.df,self.regime,self.number_set)
                if strat == 'CDLSPINNINGTOP': trade_obj = CDLSPINNINGTOP(self.df,self.regime,self.number_set)
                if strat == 'CDLTASUKIGAP': trade_obj = CDLTASUKIGAP(self.df,self.regime,self.number_set)
            result_strat.append(trade_obj.check_cignal())
        return result_strat
