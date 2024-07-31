
import flet as ft
from variable import *
from imports import *

class Header(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

#121212
    def build(self):
        
        self.header = ft.Container(
            # ft.Column(controls=[
            #     ft.Container(
            #         ft.Row(controls=[
            #           ft.Container(ft.ElevatedButton(content = ft.Text('Информация',size=12,),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7,height=30),
            #           ft.Container(ft.ElevatedButton(content = ft.Text('История торговли',size=12,),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7,height=30),
            #     ]),bgcolor='red',width=350,alignment=ft.alignment.center,
            #     ),
            # ]),
            # expand=2,
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(
                            ft.Container(
                                ft.Row(controls=[
                                    ft.Container(ft.ElevatedButton(content = ft.Text('Информация',size=12,),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7,height=30),
                                    ft.Container(ft.ElevatedButton(content = ft.Text('История торговли',size=12,),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7,height=30),
                                ]),width=320),alignment=ft.alignment.center),height=60,margin=ft.margin.only(top=-14,left=-10,right=-10,bottom=-14),      
                    ),
                    ft.Container(
                        ft.Container(alignment=ft.alignment.center),height=1,bgcolor=c_white,margin=ft.margin.only(top=2,left=-10,right=-10),      
                    ),
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
                    ),
                    
                ]
            ),expand=2
            
        )
        
        return self.header