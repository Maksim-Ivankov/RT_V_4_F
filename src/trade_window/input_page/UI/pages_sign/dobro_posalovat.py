
import flet as ft
from variable import *

class Dobro_posalovat(ft.UserControl):

    def build(self):
        
        self.dobro_posalovat = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Image(
                            src=f"src/img/logo_1.png",
                            width=254,
                            height=51,
                        ),
                        alignment=ft.alignment.center,
                        # margin = ft.margin.only(bottom=-10,top=-5)
                    ),
                    ft.Text(
                        'Добро пожаловать в RoboTrade - место для тестирования стратегий на исторических данных, торговли роботом, индикаторами и нейронными сетями. Графическая торговля и торговля в стакане',
                        color=c_blue,
                        text_align='center',
                        )
                ]
            ),
            bgcolor=c_yelow,
            width=301,
            height=230,
            padding=20,
            margin=0,
            border = ft.border.all(1, c_white)
        )
        
        return self.dobro_posalovat