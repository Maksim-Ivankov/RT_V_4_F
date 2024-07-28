
import flet as ft
from variable import *
from imports import *

class Data_profile(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def build(self):
        
        self.data_profile = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(ft.Text('Данные профиля',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white),)
                    ),
                    ft.Container(
                        ft.Column(controls=[
                            ft.Row(controls=[
                                ft.Text('Email',size=12,color=c_white),
                                ft.Container(ft.Text('MaksimIvankov26@yandex.ru',size=12,color=c_yelow),margin=ft.margin.only(left=130)),
                            ]),
                            ft.Row(controls=[
                                ft.Text('Ключ шифрования (Api-key)',size=12,color=c_white),
                                ft.Text('WEFI342HJKhh23kg5bJJBH23Kkhg3h',size=12,color=c_yelow),
                            ]),
                            ft.Row(controls=[
                                ft.Container(ft.ElevatedButton(content = ft.Text('Изменить пароль',size=12,width=140,text_align='center'),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),padding=ft.padding.only(left=0,right=0))),alignment=ft.alignment.center,height=30),
                                ft.Container(ft.ElevatedButton(content = ft.Text('Написать разработчикам',size=12,width=160,text_align='center'),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),padding=ft.padding.only(left=0,right=0))),alignment=ft.alignment.center,height=30),
                                ft.Container(ft.ElevatedButton(content = ft.Text('Удалить аккаунт',size=12,width=140,text_align='center'),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),padding=ft.padding.only(left=0,right=0))),alignment=ft.alignment.center,height=30),
                            ])
                        ]),
                        width=560,
                        height=123,
                        border = ft.border.all(1, c_white),
                        padding=ft.padding.only(left=25,top=15),
                    ), 
                ]
            )
        )
        
        return self.data_profile