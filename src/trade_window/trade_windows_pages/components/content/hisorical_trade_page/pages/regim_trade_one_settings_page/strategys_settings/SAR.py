# SAR([input_arrays], [acceleration=0.02], [maximum=0.2])

# Parabolic SAR (Overlap Studies)
# Inputs:
# prices: ['high', 'low']

# Parameters:
# acceleration: 0.02 maximum: 0.2

# Outputs:
# real

# компонент - настройки стратегии SAR
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config
from src.trade_window.trade_windows_pages.components.content.UI.input import Input

class SAR(ft.UserControl):
    def __init__(self):
        super().__init__()

    def input_SAR_acceleration(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_SAR_acceleration':str(e.control.value)})
    def input__SAR_maximum(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_MSAR_maximum':str(e.control.value)})


    def print_component(self):
        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.strat_SAR_acceleration = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_SAR_acceleration')
        self.strat_MSAR_maximum = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_MSAR_maximum')
        

        self.MA = ft.Container(
            ft.Container(
                
                    ft.Column(
                        controls=[
                            ft.Container(
                                ft.Container(ft.Text('Параболический SAR',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))
                            ),
                            ft.Container(
                                ft.Container(
                                        ft.Column(controls=[
                                        ft.Container(ft.Text('Ускорение',size=12,color=c_white,text_align='center'),width=350),
                                        Input(self.input_SAR_acceleration,self.strat_SAR_acceleration,350),
                                        ft.Container(ft.Text('Максимум',size=12,color=c_white,text_align='center'),width=350),
                                        Input(self.input__SAR_maximum,self.strat_MSAR_maximum,350),
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
        