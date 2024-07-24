
import flet as ft
from variable import *

class Sign_in(ft.UserControl):

    def build(self):

        def vsisteme(e):
            if self.flag_ch == 0:
                self.checkbox_vsisteme.current.value=True
                self.flag_ch = 1
            else:
                self.checkbox_vsisteme.current.value=False
                self.flag_ch = 0
            self.update()
        self.flag_ch=0
        self.checkbox_vsisteme = ft.Ref[ft.CupertinoCheckbox]()
        self.sign_in = ft.Container(
            ft.Column(
                controls=[
                    ft.TextField(label="Email",bgcolor=c_white,border_radius=0,border_color=c_white,height=30,color=c_blue,cursor_color=c_blue,cursor_height=22,text_align='center',content_padding= ft.padding.only(10),),
                    ft.TextField(label="Пароль",password=True, can_reveal_password=True,bgcolor=c_white,border_radius=0,border_color=c_white,height=30,color=c_blue,cursor_color=c_blue,cursor_height=22,text_align='center',content_padding= ft.padding.only(10)),
                    ft.TextField(label="Api-key",password=True, can_reveal_password=True,bgcolor=c_white,border_radius=0,border_color=c_white,height=30,color=c_blue,cursor_color=c_blue,cursor_height=22,text_align='center',content_padding= ft.padding.only(10)),
                    ft.Container(
                        ft.Row(
                            controls=[
                                ft.CupertinoCheckbox(value=False,check_color=c_blue,active_color=c_yelow,inactive_color=c_blue,ref=self.checkbox_vsisteme),
                                ft.Container(ft.Text('Оставаться в системе',color=c_blue,),margin = ft.margin.only(left=-15),on_click=vsisteme)
                                
                            ]
                        ),margin = ft.margin.only(left=28,top=-5,bottom=-5)
                        # alignment=ft.alignment.center,
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