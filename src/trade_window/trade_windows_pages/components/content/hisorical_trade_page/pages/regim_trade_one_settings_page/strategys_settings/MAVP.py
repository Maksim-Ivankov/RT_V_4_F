# MAVP([input_arrays], [minperiod=2], [maxperiod=30], [matype=0])

# Moving average with variable period (Overlap Studies)
# Inputs:1
# price: (any ndarray) periods: (any ndarray)

# Parameters:
# minperiod: 2 maxperiod: 30 matype: 0 (Simple Moving Average)

# Outputs:
# real

# компонент - настройки стратегии MAVP
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config
from src.trade_window.trade_windows_pages.components.content.UI.input import Input

class MAVP(ft.UserControl):
    def __init__(self):
        super().__init__()

    def input_MAVP_minperiod(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_MAVP_minperiod':str(e.control.value)})
    def input_kMAVP_maxperiod(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_MAVP_maxperiod':str(e.control.value)})
    def input_MAVP_matype(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_MAVP_matype':str(e.control.value)})

    def print_component(self):
        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.strat_MAVP_minperiod = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_MAVP_minperiod')
        self.strat_MAVP_maxperiod = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_MAVP_maxperiod')
        self.strat_MAVP_matype = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_MAVP_matype')
        

        self.MA = ft.Container(
            ft.Container(
                
                    ft.Column(
                        controls=[
                            ft.Container(
                                ft.Container(ft.Text('Сколь средняя с пер периодом',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))
                            ),
                            ft.Container(
                                ft.Container(
                                        ft.Column(controls=[
                                        ft.Container(ft.Text('Минимальный период',size=12,color=c_white,text_align='center'),width=350),
                                        Input(self.input_MAVP_minperiod,self.strat_MAVP_minperiod,350),
                                        ft.Container(ft.Text('Максимальный период',size=12,color=c_white,text_align='center'),width=350),
                                        Input(self.input_kMAVP_maxperiod,self.strat_MAVP_maxperiod,350),
                                        ft.Container(ft.Text('Тип скользящей средней',size=12,color=c_white,text_align='center'),width=350),
                                        Input(self.input_MAVP_matype,self.strat_MAVP_matype,350),
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
        