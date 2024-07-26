import flet as ft
from imports import *
from src.trade_window.input_page.UI.img_raketa import Img_raketa
from src.trade_window.input_page.UI.form_wrap import Form_wrap
from src.trade_window.input_page.UI.icons_ss import Icons_ss

class Input_page(ft.UserControl):

    def __init__(self,page):
        super().__init__()
        self.page = page

    def build(self):  
        self.stakan = ft.Column(
            controls=[
                Img_raketa(),
                ft.Container(
                    ft.Container(
                        ft.Column(
                            controls=[
                                Form_wrap(self.page)
                            ],
                            width=301,
                        ),
                    ),
                    alignment=ft.alignment.center,
                ),
                Icons_ss()
                ],
            
        )
            
        return self.stakan
    









