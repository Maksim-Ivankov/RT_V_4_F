
import flet as ft
from variable import *
from imports import *

class Proksi(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def build(self):
        
        self.proksi = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(
                            ft.Text(
                            'Прокси',
                            color=c_blue,
                            ),
                            bgcolor=c_yelow,
                            padding=5,
                            margin=ft.margin.only(bottom=-10),
                            border=ft.border.all(1,c_white)
                        )
                    ),
                    ft.Container(
                        width=283,
                        height=162,
                        border = ft.border.all(1, c_white)
                    ),
                ]
            )
        )
        
        return self.proksi