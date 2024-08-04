
import flet as ft
from variable import *
from imports import *


from src.trade_window.trade_windows_pages.components.content.UI.input import Input
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.settings_robot_page.UI.component_tp import Component_tp
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.settings_robot_page.UI.component_sl import Component_sl
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.settings_robot_page.UI.component_volume_min import Component_volume_min
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.settings_robot_page.UI.component_volume_max import Component_volume_max

class Change_strategy_trade_page(ft.UserControl):
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page

    def input_name_bot(self,e):
        print(e.control.value)
    def input_komission_mayker(self,e):
        print(e.control.value)
    def input_komission_taker(self,e):
        print(e.control.value)
    def input_deposit(self,e):
        print(e.control.value)
    def input_leverage(self,e):
        print(e.control.value)
    def input_tp(self,e):
        print(e.control.value)
    def input_sl(self,e):
        print(e.control.value)
    def input_volume_min(self,e):
        print(e.control.value)
    def input_volume_max(self,e):
        print(e.control.value)

    def build(self):
        self.change_strategy_trade_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text('Выберите одну или несколько стратегий реальной тестовой торговли',
                                        size=12,color=c_white,text_align='center',),padding=ft.padding.only(left=120)),
                                ft.Container(
                                    ft.Container(
                                        ft.Column(controls=[
                                            ft.Column(
                                                controls=[
                                                    ft.Container(
                                                        ft.Container(ft.Text('Выбор стратегии',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                    ft.Container(
                                                        
                                                        width=560,
                                                        border = ft.border.all(1, c_white),
                                                        padding=14
                                            )]),
                                            
                                            
                                                
                                    ])),
                                    width=560,
                                    # height=80,
                                    # bgcolor='red'
                                ),
                                ft.Container(
                                                ft.Container(
                                                    ft.Row(controls=[
                                                    ft.Container(ft.ElevatedButton(content = ft.Text('Назад',size=12,),data='Свободный фрейм',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                                    ft.Container(ft.ElevatedButton(content = ft.Text('Выбрать режим торговли',size=12,),data='Выбрать режим торговли',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                                ]),padding=ft.padding.only(left=130,top=10)
                                                ),
                                                width=560,
                                                # height=100
                                            )
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.change_strategy_trade_page