# Inputs:1
# prices: ['open', 'high', 'low', 'close']

# Outputs:
# integer (values are -100, 0 or 100)

# компонент - настройки стратегии CDL3STARSINSOUTH
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config
from src.trade_window.trade_windows_pages.components.content.UI.input import Input

class CDL3STARSINSOUTH(ft.UserControl):
    def __init__(self):
        super().__init__()

    def input_CDL3STARSINSOUTH_long(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDL3STARSINSOUTH_long':str(e.control.value)})
    def input_CDL3STARSINSOUTH_short(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDL3STARSINSOUTH_short':str(e.control.value)})

    def print_component(self):
        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.strat_CDL3STARSINSOUTH_long = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3STARSINSOUTH_long')
        self.strat_CDL3STARSINSOUTH_short = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3STARSINSOUTH_short')
        self.MA = ft.Container(
            ft.Container(
                
                    ft.Column(
                        controls=[
                            ft.Container(
                                ft.Container(ft.Text('Три звезды на юге',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))
                            ),
                            ft.Container(
                                ft.Container(
                                        ft.Column(controls=[
                                        ft.Container(ft.Text('Процент сигнала в лонг',size=12,color=c_white,text_align='center'),width=350),
                                        Input(self.input_CDL3STARSINSOUTH_long,self.strat_CDL3STARSINSOUTH_long,350),
                                        ft.Container(ft.Text('Процент сигнала в шорт',size=12,color=c_white,text_align='center'),width=350),
                                        Input(self.input_CDL3STARSINSOUTH_short,self.strat_CDL3STARSINSOUTH_short,350),
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
        