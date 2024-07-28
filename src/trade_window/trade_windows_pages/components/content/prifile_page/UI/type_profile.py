
import flet as ft
from variable import *
from imports import *

class Type_profile(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def build(self):
        
        self.type_profile = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(ft.Text('Тип профиля',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white),
                    )),
                    ft.Container(
                        ft.Row(controls=[
                            ft.Container(
                                ft.Column(controls=[
                                    ft.Container(ft.Text('Тип профиля',size=12,color=c_white),margin = ft.margin.only(left=35,top=30)),
                                    ft.Container(ft.Text('Бесплатный профиль',size=12,color=c_yelow),margin = ft.margin.only(left=12)),
                                ]),
                                width=150,
                                border = ft.border.only(right=ft.border.BorderSide(1, c_white)),
                            ),
                            ft.Column(controls=[
                                ft.Container(ft.ElevatedButton(content = ft.Text('Подписка',size=12,width=100,text_align='center'),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),padding=ft.padding.only(left=0,right=0))),alignment=ft.alignment.center,height=30,margin=ft.margin.only(top=15,left=5)),
                                ft.Container(ft.Text('Узнать подробнее\nо подписке и платном\nфункционале',size=12,text_align='center'))
                            ]),
                        ]),
                        width=295,
                        height=123,
                        border = ft.border.all(1, c_white),
                        padding=0,
                    ), 
                ]
            )
        )
        
        return self.type_profile