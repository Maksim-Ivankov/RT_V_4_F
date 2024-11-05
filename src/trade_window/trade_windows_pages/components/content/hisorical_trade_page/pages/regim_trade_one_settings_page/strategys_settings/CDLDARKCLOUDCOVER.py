# CDLDARKCLOUDCOVER([input_arrays], [penetration=0.5])

# Dark Cloud Cover (Pattern Recognition)
# Inputs:
# prices: ['open', 'high', 'low', 'close']

# Parameters:
# penetration: 0.5

# Outputs:
# integer (values are -100, 0 or 100)

# компонент - настройки стратегии CDLDARKCLOUDCOVER
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config
from src.trade_window.trade_windows_pages.components.content.UI.input import Input

class CDLDARKCLOUDCOVER(ft.UserControl):
    def __init__(self):
        super().__init__()


    def input_strat_CDLDARKCLOUDCOVER_penetration(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLDARKCLOUDCOVER_penetration':str(e.control.value)})
    def input_CDLDARKCLOUDCOVER_long(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLDARKCLOUDCOVER_long':str(e.control.value)})
    def input_CDLDARKCLOUDCOVER_short(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLDARKCLOUDCOVER_short':str(e.control.value)})



    def print_component(self):
        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.strat_CDLDARKCLOUDCOVER_penetration = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLDARKCLOUDCOVER_penetration')
        self.strat_CDLDARKCLOUDCOVER_long = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLDARKCLOUDCOVER_long')
        self.strat_CDLDARKCLOUDCOVER_short = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLDARKCLOUDCOVER_short')

        self.MA = ft.Container(
            ft.Container(
                
                    ft.Column(
                        controls=[
                            ft.Container(
                                ft.Container(ft.Text('Темный облачный покров',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))
                            ),
                            ft.Container(
                                ft.Container(
                                        ft.Column(controls=[
                                        ft.Container(ft.Text('Процент проникновения одной свечи внутри другой свечи',size=12,color=c_white,text_align='center'),width=350),
                                        Input(self.input_strat_CDLDARKCLOUDCOVER_penetration,self.strat_CDLDARKCLOUDCOVER_penetration,350),
                                        ft.Container(ft.Text('Процент сигнала в лонг',size=12,color=c_white,text_align='center'),width=350),
                                        Input(self.input_CDLDARKCLOUDCOVER_long,self.strat_CDLDARKCLOUDCOVER_long,350),
                                        ft.Container(ft.Text('Процент сигнала в шорт',size=12,color=c_white,text_align='center'),width=350),
                                        Input(self.input_CDLDARKCLOUDCOVER_short,self.strat_CDLDARKCLOUDCOVER_short,350),
                                ])),
                                width=396,
                                border = ft.border.all(1, c_white),
                                padding=ft.padding.only(top=14,bottom=14,left=20), 
                            )
                        ]
                    ),     
                alignment=ft.alignment.center
            ),
            width=860,
        )
        
        return self.MA

    def build(self):
        return self.print_component()
        