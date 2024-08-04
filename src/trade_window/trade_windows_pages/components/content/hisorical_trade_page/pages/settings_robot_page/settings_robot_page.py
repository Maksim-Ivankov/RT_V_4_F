
import flet as ft
from variable import *
from imports import *


from src.trade_window.trade_windows_pages.components.content.UI.input import Input
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.settings_robot_page.UI.component_tp import Component_tp
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.settings_robot_page.UI.component_sl import Component_sl
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.settings_robot_page.UI.component_volume_min import Component_volume_min
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.settings_robot_page.UI.component_volume_max import Component_volume_max
from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config

class Settings_robot_page(ft.UserControl):
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page

    def input_name_bot(self,e):
        print(e.control.value)
        Save_config('param_trade_historical_trade_svobodniy_freym',{'name_bot':str(e.control.value)})
    def input_komission_mayker(self,e):
        print(e.control.value)
        Save_config('param_trade_historical_trade_svobodniy_freym',{'komission_mayker':str(e.control.value)})
    def input_komission_taker(self,e):
        print(e.control.value)
        Save_config('param_trade_historical_trade_svobodniy_freym',{'komission_taker':str(e.control.value)})
    def input_deposit(self,e):
        print(e.control.value)
        Save_config('param_trade_historical_trade_svobodniy_freym',{'deposit':str(e.control.value)})
    def input_leverage(self,e):
        print(e.control.value)
        Save_config('param_trade_historical_trade_svobodniy_freym',{'leverage':str(e.control.value)})
    def input_tp(self,e):
        print(e.control.value)
        Save_config('param_trade_historical_trade_svobodniy_freym',{'tp':str(e.control.value)})
    def input_sl(self,e):
        print(e.control.value)
        Save_config('param_trade_historical_trade_svobodniy_freym',{'sl':str(e.control.value)})
    def input_volume_min(self,e):
        print(e.control.value)
        Save_config('param_trade_historical_trade_svobodniy_freym',{'volume_min':str(e.control.value)})
    def input_volume_max(self,e):
        print(e.control.value)
        Save_config('param_trade_historical_trade_svobodniy_freym',{'volume_max':str(e.control.value)})

    def build(self):
        self.settings_robot = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text('Настройте робота для торговли на свободном фрейме',
                                        size=12,color=c_white,text_align='center',),padding=ft.padding.only(left=120)),
                                ft.Container(
                                    ft.Container(
                                        ft.Column(controls=[
                                            ft.Column(
                                                controls=[
                                                    ft.Container(
                                                        ft.Container(ft.Text('Настройки робота',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                    ft.Container(
                                                        ft.Row(
                                                            controls=[
                                                                ft.Column(controls=[
                                                                    ft.Container(ft.Text('Имя робота для логов',size=12,text_align='center'),width=170,padding=0),
                                                                    ft.Container(Input(self.input_name_bot,'Версия 22_07_24_1',170)),
                                                                    ft.Container(ft.Text('Комиссия мейкер, %',size=12,text_align='center'),width=170),
                                                                    Input(self.input_komission_mayker,'0.2',170)
                                                                ]),
                                                                ft.Column(controls=[
                                                                    ft.Container(ft.Text('Депозит,$',size=12,text_align='center'),width=170,padding=0),
                                                                    ft.Container(Input(self.input_deposit,'100',170)),
                                                                    ft.Container(ft.Text('Комиссия тейкер, %',size=12,text_align='center'),width=170),
                                                                    Input(self.input_komission_taker,'0.1',170)
                                                                ]),
                                                                ft.Container(ft.Column(controls=[
                                                                    ft.Container(ft.Text('Плечо',size=12,text_align='center'),width=170,padding=0),
                                                                    ft.Container(Input(self.input_leverage,'20',170)),
                                                                    
                                                                ]),margin=ft.margin.only(bottom=66)),
                                                            ]
                                                        ),
                                                        width=560,
                                                        border = ft.border.all(1, c_white),
                                                        padding=14
                                            )]),
                                            ft.Row(controls=[
                                                Component_tp(self.input_tp),
                                                Component_sl(self.input_sl)
                                            ]),
                                            ft.Row(controls=[
                                                Component_volume_min(self.input_volume_min),
                                                Component_volume_max(self.input_volume_max)
                                            ]),
                                                
                                    ])),
                                    width=560,
                                    # height=80,
                                    # bgcolor='red'
                                ),
                                ft.Container(
                                                ft.Container(
                                                    ft.Row(controls=[
                                                    ft.Container(ft.ElevatedButton(content = ft.Text('Назад',size=12,),data='Свободный фрейм',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                                    ft.Container(ft.ElevatedButton(content = ft.Text('Выбрать стратегию торговли',size=12,),data='Выбрать стратегию торговли',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                                ]),padding=ft.padding.only(left=130,top=10)
                                                ),
                                                width=560,
                                                # height=100
                                            )
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.settings_robot