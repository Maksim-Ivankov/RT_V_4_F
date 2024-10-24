# компонент - настройки стратегии One
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config
from src.trade_window.trade_windows_pages.components.content.UI.input import Input

class One(ft.UserControl):
    def __init__(self):
        super().__init__()

    def input_up_chanal(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_one_up_chanal':str(e.control.value)})
    def input_down_chanal(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_one_down_chanal':str(e.control.value)})
    def input_corner_long(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_one_corner_long':str(e.control.value)})
    def input_corner_short(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_one_corner_short':str(e.control.value)})


    def print_component(self):
        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.strat_one_up_chanal = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_up_chanal')
        self.strat_one_down_chanal = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_down_chanal')
        self.strat_one_corner_long = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_corner_long')
        self.strat_one_corner_short = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_corner_short')
        

        self.one = ft.Container(
            ft.Container(
                
                    ft.Column(
                        controls=[
                            ft.Container(
                                ft.Container(ft.Text('Канал, тренд, локаль, объём',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))
                            ),
                            ft.Container(
                                ft.Row(controls=[
                                    ft.Column(controls=[
                                        ft.Container(ft.Text('Верх канала, %',size=12,color=c_white,text_align='center'),width=170),
                                        Input(self.input_up_chanal,self.strat_one_up_chanal,170),
                                        ft.Container(ft.Text('Низ канала, %',size=12,color=c_white,text_align='center'),width=170),
                                        Input(self.input_down_chanal,self.strat_one_down_chanal,170),
                                    ]),
                                    ft.Column(controls=[
                                        ft.Container(ft.Text('Угол тренда лонг',size=12,color=c_white,text_align='center'),width=170),
                                        Input(self.input_corner_long,self.strat_one_corner_long,170),
                                        ft.Container(ft.Text('Угол тренда шорт',size=12,color=c_white,text_align='center'),width=170),
                                        Input(self.input_corner_short,self.strat_one_corner_short,170),
                                    ])
                                ]),
                                width=396,
                                border = ft.border.all(1, c_white),
                                padding=ft.padding.only(top=14,bottom=14,left=20),
                                
                                # padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                
                            ),
                            
                        ]
                    ),     
                alignment=ft.alignment.center
            ),
            width=860,
            # bgcolor='red'
        )
        
        return self.one

    def build(self):
        return self.print_component()
        