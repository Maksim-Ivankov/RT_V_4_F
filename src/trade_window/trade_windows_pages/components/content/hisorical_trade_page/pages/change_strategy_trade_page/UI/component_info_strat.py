# компонент информации о стратегии, которая отображается справа от чекбоксов выбора стратегии
import flet as ft
from variable import *
from imports import *

class Component_info_strat(ft.UserControl):
    def __init__(self,delete_strat,open_strat_btn):
        super().__init__()
        self.delete_strat = delete_strat
        self.open_strat_btn = open_strat_btn
        self.changes_strat_mas = []
    
    def update_component(self):
        self.controls = []
        self.controls.append(self.print_component())
        self.update()

    def print_component(self):
        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.strategys = config.get('param_trade_historical_trade_svobodniy_freym', 'strategys')
        # self.component_info_strat = ft.Container(  
        #     ft.Text(self.strategys)
        # )
        
        self.changes_strat_mas[:] = []
        if len(literal_eval(self.strategys))==0:
            self.changes_strat_mas.append(ft.Container(ft.Text('Стратегии не выбраны')))
        else:
            for strat in literal_eval(self.strategys):
                width_count = ((len(strat)*10)+40)
                if strat=='MA': width_count = ((len(strat)*10)+40)
                if strat=='MIN': width_count = 68
                if strat=='MA': width_count = 60
                if strat=='BBANDS': width_count = 94
                if strat=='EMA': width_count = 68
                if strat=='DEMA': width_count = 80
                if strat=='KAMA': width_count = 78
                if strat=='AMA': width_count = 72
                if strat=='MAVP': width_count = 78
                if strat=='SAR': width_count = 68
                if strat=='TEMA': width_count = 76
                if strat=='TRIMA': width_count = 82
                if strat=='WMA': width_count = 76
                if strat=='CDL2CROWS': width_count = 124
                if strat=='CDL3BLACKCROWS': width_count = 164
                if strat=='CDL3INSIDE': width_count = 118
                if strat=='CDL3LINESTRIKE': width_count = 146
                if strat=='CDL3OUTSIDE': width_count = 132
                if strat=='CDL3STARSINSOUTH': width_count = 176
                if strat=='CDL3WHITESOLDIERS': width_count = 180
                if strat=='CDLABANDONEDBABY': width_count = 186
                if strat=='CDLADVANCEBLOCK': width_count = 172
                if strat=='CDLBELTHOLD': width_count = 132
                if strat=='CDLBREAKAWAY': width_count = 144
                if strat=='CDLCLOSINGMARUBOZU': width_count = 200
                if strat=='CDLCOUNTERATTACK': width_count = 178
                if strat=='CDLDARKCLOUDCOVER': width_count = 192
                if strat=='CDLDOJI': width_count = 96
                if strat=='CDLDOJISTAR': width_count = 128
                if strat=='CDLENGULFING': width_count = 144
                if strat=='CDLEVENINGDOJISTAR': width_count = 188
                if strat=='CDLEVENINGSTAR': width_count = 158
                if strat=='CDLGAPSIDESIDEWHITE': width_count = 194
                if strat=='CDLGRAVESTONEDOJI': width_count = 184
                if strat=='CDLHAMMER': width_count = 128
                if strat=='CDLHANGINGMAN': width_count = 164
                if strat=='CDLHARAMI': width_count = 120
                if strat=='CDLHARAMICROSS': width_count = 164
                if strat=='CDLHIGHWAVE': width_count = 136
                if strat=='CDLHOMINGPIGEON': width_count = 176
                if strat=='CDLINVERTEDHAMMER': width_count = 192
                if strat=='CDLKICKING': width_count = 122
                if strat=='CDLLADDERBOTTOM': width_count = 176
                if strat=='CDLLONGLEGGEDDOJI': width_count = 186
                if strat=='CDLLONGLINE': width_count = 132
                if strat=='CDLMATCHINGLOW': width_count = 168
                if strat=='CDLMORNINGSTAR': width_count = 168
                if strat=='CDLRICKSHAWMAN': width_count = 168
                if strat=='CDLSPINNINGTOP': width_count = 158
                if strat=='CDLSTALLEDPATTERN': width_count = 178
                if strat=='CDLTASUKIGAP': width_count = 140
                if strat=='CDLTHRUSTING': width_count = 142
                if strat=='CDLUPSIDEGAP2CROWS': width_count = 196

                self.changes_strat_mas.append(ft.Container(ft.Row(controls=[
                    ft.Container(ft.Text(strat,color=c_blue),data=strat,on_click=self.open_strat_btn),
                    ft.Container(ft.Text('X',color=c_yelow,text_align='CENTER'),bgcolor=c_blue,width=20,data=strat,on_click=self.delete_strat),
                ],expand=True),padding=5,bgcolor=c_yelow,height=30,width=width_count,data=strat))
    
        
        self.component_info_strat = ft.Row(
            controls=self.changes_strat_mas,
            wrap=True,
            spacing=10,
            run_spacing=10,
            # width=400,
        )
        
        return self.component_info_strat

    def build(self):
        return self.print_component()
        