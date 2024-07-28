
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.UI.dropdown import Dropdown

class Settings(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def on_change_tema(self,e):
        print(e.control.value)

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
                                ft.Row(controls=[
                                        ft.Text('Выбор темы'),
                                        Dropdown(self.on_change_tema,'Темная',["Темная","Светлая"],100)
                                ]),
                                ft.Row(controls=[
                                        ft.Text('Кол-во монет\nтепловой карты'),
                                        ft.TextField(
                                            width=100,
                                            border_radius=0,
                                            border_color=c_white,
                                            height=30,
                                            content_padding=ft.padding.only(left=5,right=5),
                                            text_align='center',
                                            text_size=12
                                        )
                                ]),
                                   
                            ]
                        ),
                        width=283,
                        height=162,
                        border = ft.border.all(1, c_white)
                    ),
                ]
            )
        )
        
        return self.settings