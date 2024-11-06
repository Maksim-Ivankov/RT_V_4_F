# EMA([input_arrays], [timeperiod=30])

# Exponential Moving Average (Overlap Studies)
# Inputs:1
# price: (any ndarray)

# Parameters:
# timeperiod: 30

# Outputs:
# real

# компонент - настройки стратегии EMA
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config
from src.trade_window.trade_windows_pages.components.content.UI.input import Input

class EMA(ft.UserControl):
    def __init__(self):
        super().__init__()

    def input_strat_EMA_timeperiod(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_EMA_timeperiod':str(e.control.value)})


    def print_component(self):
        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.strat_EMA_timeperiod = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_EMA_timeperiod')

        

        self.MA = ft.Container(
            ft.Container(
                
                    ft.Column(
                        controls=[
                            ft.Container(
                                ft.Container(ft.Text('Эксп скользящая средняя',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))
                            ),
                            ft.Container(
                                ft.Container(
                                        ft.Column(controls=[
                                        ft.Container(ft.Text('Временной промежуток',size=12,color=c_white,text_align='center'),width=350),
                                        Input(self.input_strat_EMA_timeperiod,self.strat_EMA_timeperiod,350),
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
        