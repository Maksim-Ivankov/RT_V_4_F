

# компонент - настройки стратегии MA
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config
from src.trade_window.trade_windows_pages.components.content.UI.input import Input

class MA(ft.UserControl):
    def __init__(self):
        super().__init__()

    def input_koef_bistro(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_MA_koef_bistro':str(e.control.value)})
    def input_koef_medleno(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_MA_koef_medleno':str(e.control.value)})
    def input_sovpad_last(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_MA_sovpad_last':str(e.control.value)})
    def input_up_chanal(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_MA_up_chanal':str(e.control.value)})
    def input_down_chanal(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_MA_down_chanal':str(e.control.value)})


    def print_component(self):
        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.strat_ma_koef_bistro = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_koef_bistro')
        self.strat_ma_koef_medleno = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_koef_medleno')
        self.strat_ma_sovpad_last = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_sovpad_last')
        self.strat_ma_up_chanal = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_up_chanal')
        self.strat_ma_down_chanal = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_down_chanal')
        

        self.MA = ft.Container(
            ft.Container(
                
                    ft.Column(
                        controls=[
                            ft.Container(
                                ft.Container(ft.Text('Скользящие средние',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))
                            ),
                            ft.Container(
                                ft.Row(controls=[
                                    ft.Container(
                                        ft.Column(controls=[
                                        ft.Container(ft.Text('Коэф. быстрой скольз. средней',size=12,color=c_white,text_align='center'),width=170),
                                        Input(self.input_koef_bistro,self.strat_ma_koef_bistro,170),
                                        ft.Container(ft.Text('Коэф. медленной скольз. средней',size=12,color=c_white,text_align='center'),width=170),
                                        Input(self.input_koef_medleno,self.strat_ma_koef_medleno,170),
                                    ]),
                                    padding=ft.padding.only(bottom=50)
                                    ),
                                    ft.Column(controls=[
                                        ft.Container(ft.Text('Кол-во совпадений в прошлом',size=12,color=c_white,text_align='center'),width=170),
                                        Input(self.input_sovpad_last,self.strat_ma_sovpad_last,170),
                                        ft.Container(ft.Text('Прижатие к верху коридора',size=12,color=c_white,text_align='center'),width=170),
                                        Input(self.input_up_chanal,self.strat_ma_up_chanal,170),
                                        ft.Container(ft.Text('Прижатие к низу коридора',size=12,color=c_white,text_align='center'),width=170),
                                        Input(self.input_down_chanal,self.strat_ma_down_chanal,170),
                                    ])
                                ]),
                                width=396,
                                border = ft.border.all(1, c_white),
                                padding=ft.padding.only(top=14,bottom=14,left=20),
                                
                                # padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                
                            )
                        ]
                    ),     
                alignment=ft.alignment.center
            ),
            width=860,
            # bgcolor='red'
        )
        
        return self.MA

    def build(self):
        return self.print_component()
        