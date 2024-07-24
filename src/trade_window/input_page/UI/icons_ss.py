
import flet as ft
from variable import *

class Icons_ss(ft.UserControl):

    def build(self):
        
        self.icons_ss = ft.Container(
            ft.Row(
                controls=[
                    ft.Image(src=f"src/img/site.png",width=23,height=23,),
                    ft.Image(src=f"src/img/tg.png",width=23,height=23,),
                    ft.Image(src=f"src/img/vk.png",width=23,height=23,),
                    ft.Image(src=f"src/img/youtube.png",width=23,height=23,),
                ],
                width=119,
            ),
        alignment=ft.alignment.center,
        padding=10
        )
        
        return self.icons_ss