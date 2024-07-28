
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.UI.dropdown import Dropdown
from src.trade_window.trade_windows_pages.components.content.UI.input import Input

class Settings(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def on_change_tema(self,e):
        # print(e.control.value)
        pass

    def on_change_count_coin(self,e):
        # print(e.control.value)
        pass

    def build(self):
        
        self.settings = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(
                            ft.Text(
                            'Настройки программы',
                            color=c_blue,
                            ),
                            bgcolor=c_yelow,
                            padding=5,
                            margin=ft.margin.only(bottom=-10),
                            border=ft.border.all(1,c_white)
                        )
                    ),
                    ft.Container(
                        ft.Column(
                            controls=[
                                ft.Container(
                                    ft.Row(controls=[
                                        ft.Container(ft.Text('Выбор темы',size=12),margin=ft.margin.only(right=10)),
                                        Dropdown(self.on_change_tema,'Темная',["Темная","Светлая"],150)
                                ]),margin=ft.margin.only(left=10)
                                ),
                                ft.Container(
                                    ft.Row(controls=[
                                        ft.Text('Кол-во монет\nтепловой карты',size=12,text_align='center'),
                                        Input(self.on_change_count_coin,'10',150)
                                ])
                                ),
                                ft.Container(ft.ElevatedButton(content = ft.Text('Сохранить',size=12,),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7,height=30)
                     
                            ]
                        ),
                        width=283,
                        height=180,
                        border = ft.border.all(1, c_white),
                        padding=ft.padding.only(top=30,left=10)
                    ),
                ]
            )
        )
        
        return self.settings