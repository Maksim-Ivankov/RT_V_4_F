
import flet as ft
from variable import *
from imports import *


class Istoriya_treyd_page(ft.UserControl):
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page
        


    def build(self):
        self.ferst_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Text('История торговли - схораненные карточки и статистика по всем проведенным торговым сессиям во вкладке исторической торговли',
                                        size=12,color=c_white,text_align='center'),
                                ft.Container(#11
                                    # ft.Row(controls=[
                                    #     ft.Container(ft.ElevatedButton(content = ft.Text('\nСвободный\nфрейм',size=12,text_align='center',height=70),data='Свободный фрейм',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7),
                                    #     ft.Container(ft.ElevatedButton(content = ft.Text('\nТорговля\nсо смещением',size=12,text_align='center',height=70),data='Торговля со смещением',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7),
                                    #     ft.Container(ft.ElevatedButton(content = ft.Text('\nИсторическая\nторговля',size=12,text_align='center',height=70),data='Историческая торговля',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7),
                                    # ]),
                                    width=440,
                                    height=80,
                                    margin=ft.margin.only(left=90),
                                ),
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.ferst_page