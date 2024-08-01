
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.UI.header import Header

class Ferst_page(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def build(self):
        self.ferst_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Text('Свободный фрейм - торговля на 1 стратегии по выбранному небольшому фрейму данных \nТорговля со смещением - торговля на заданном небольшом фрейме данных интервалами со смещением \nИсторическая торговля  - торговля на длинном фрейме данных',
                                        size=12,color=c_white,text_align='center'),
                                ft.Container(#11
                                    ft.Row(controls=[
                                        ft.Container(ft.ElevatedButton(content = ft.Text('\nСвободный\nфрейм',size=12,text_align='center',height=70),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7),
                                        ft.Container(ft.ElevatedButton(content = ft.Text('\nТорговля\nсо смещением',size=12,text_align='center',height=70),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7),
                                        ft.Container(ft.ElevatedButton(content = ft.Text('\nИсторическая\nторговля',size=12,text_align='center',height=70),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7),
                                    ]),
                                    width=440,
                                    height=80,
                                    margin=ft.margin.only(left=90)
                                ),
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.ferst_page