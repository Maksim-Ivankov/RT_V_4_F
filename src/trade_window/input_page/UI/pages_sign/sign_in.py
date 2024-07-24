
import flet as ft
from variable import *

class Sign_in(ft.UserControl):

    def build(self):
        
        self.sign_in = ft.Container(
            ft.Column(
                controls=[
                    ft.TextField(label="Email",bgcolor=c_white,border_radius=0,border_color=c_white,height=30,color=c_blue,cursor_color=c_blue,cursor_height=22,text_align='center',content_padding= ft.padding.only(10),),
                    ft.TextField(label="Пароль",password=True, can_reveal_password=True,bgcolor=c_white,border_radius=0,border_color=c_white,height=30,color=c_blue,cursor_color=c_blue,cursor_height=22,text_align='center',content_padding= ft.padding.only(10)),
                    ft.TextField(label="Api-key",password=True, can_reveal_password=True,bgcolor=c_white,border_radius=0,border_color=c_white,height=30,color=c_blue,cursor_color=c_blue,cursor_height=22,text_align='center',content_padding= ft.padding.only(10)),
                    ft.Container(
                        ft.Checkbox(label="Оставаться в системе",value=False,check_color=c_blue,active_color=c_yelow,
                                    
                                    )
                    ),
                    ft.Container(ft.ElevatedButton(text="Войти",bgcolor=c_blue,color=c_white,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),),data="reg",),alignment=ft.alignment.center,),
                    
                ],
                
            ),
            bgcolor=c_yelow,
            width=301,
            height=230,
            padding=20,
            margin=0,
            border = ft.border.all(1, c_white)
        )
        
        return self.sign_in