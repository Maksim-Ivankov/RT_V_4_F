
import flet as ft
from variable import *
from imports import *

class Socsety(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu


    def build(self):
        
        self.socsety = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(ft.Text('Соцсети RoboTrade',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white),
                    )),
                    ft.Container(
                        ft.Row(controls=[
                            ft.Container(ft.Image(src=f"src/img/icons/site_yelow.png"),width=28,height=28),
                            ft.Container(ft.Image(src=f"src/img/icons/tg_yelow.png"),width=28,height=28),
                            ft.Container(ft.Image(src=f"src/img/icons/vk_yelow.png"),width=28,height=28),
                            ft.Container(ft.Image(src=f"src/img/icons/youtube_yelow.png"),width=28,height=28),
                        ]),
                        width=215,
                        height=41,
                        border = ft.border.all(1, c_white),
                        padding=ft.padding.only(left=36,),
                    ), 
                ]
            )
        )
        
        return self.socsety