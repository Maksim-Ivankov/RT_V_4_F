
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.UI.input import Input

class Proksi(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def on_change_addres(self,e):
        pass
    def on_change_port(self,e):
        pass

    def build(self):

        
        
        self.proksi = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(
                            ft.Text('Прокси',color=c_blue,),
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
                                    ft.Text('Прокси',size=12,color=c_white),
                                    ft.Container(ft.Text('неактивен',size=12,color=c_red),margin=ft.margin.only(left=-5),)
                                ]),margin=ft.margin.only(left=80)
                                ),
                                ft.Container(
                                    ft.Row(controls=[
                                        ft.Text('Мой ip адрес - ',size=12,color=c_white),
                                        ft.Container(ft.Text('31.181.35.129',size=12,color=c_white),margin=ft.margin.only(left=-10),)
                                    ]),margin=ft.margin.only(left=40,top=-5)
                                ),
                                ft.Container(
                                    ft.Row(controls=[
                                        ft.Text('Адрес',size=12,text_align='center'),
                                        Input(self.on_change_addres,'',150)
                                ]),margin=ft.margin.only(left=30,top=-2)
                                ),
                                ft.Container(
                                    ft.Row(controls=[
                                        ft.Text('Порт',size=12,text_align='center'),
                                        Input(self.on_change_port,'',150)
                                ]),margin=ft.margin.only(left=36,top=-2)
                                ),
                                ft.Container(
                                    ft.Row(
                                    controls=[
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Выключить прокси',size=12,),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),padding=ft.padding.only(left=0,right=0))),alignment=ft.alignment.center,height=30),
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Включить прокси',size=12,),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),padding=ft.padding.only(left=0,right=0))),alignment=ft.alignment.center,height=30)
                                    ]
                                ),margin=ft.margin.only(top=0,left=3)
                                )
                            ]
                        ),
                        width=283,
                        height=180,
                        border = ft.border.all(1, c_white),
                        padding=ft.padding.only(top=10,left=10)
                    ),
                ]
            )
        )
        
        return self.proksi