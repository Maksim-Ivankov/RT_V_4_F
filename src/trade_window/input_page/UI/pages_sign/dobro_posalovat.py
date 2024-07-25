
import flet as ft
from variable import *
from imports import *

class Dobro_posalovat(ft.UserControl):

    def build(self):
        
        self.dobro_posalovat = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Image(
                            src=f"src/img/logo_1.png",
                            width=254,
                            height=51,
                        ),
                        alignment=ft.alignment.center,
                        margin = ft.margin.only(bottom=-10,top=-10)
                    ),
                    ft.Text(
                        'Добро пожаловать в RoboTrade - место для тестирования стратегий на исторических данных, торговли роботом, индикаторами и нейронными сетями. Графическая торговля и торговля в стакане',
                        color=c_blue,
                        text_align='center',
                    ),
                    ft.Container(
                        ft.Dropdown(
                        options=[
                            ft.dropdown.Option("Русский"),
                            ft.dropdown.Option("Englesh"),
                            ft.dropdown.Option("Etalion"),
                        ]
                        ,width=110,height=30,bgcolor = c_blue,border_color = c_blue,border_radius=0,color=c_white,content_padding = 10,value='Русский',filled = True,text_size=12,
                    ),alignment=ft.alignment.center,
                    )
                ]
            ),
            bgcolor=c_yelow,
            width=301,
            height=230,
            padding=20,
            margin=0,
            border = ft.border.all(1, c_white)
        )
        
        return self.dobro_posalovat