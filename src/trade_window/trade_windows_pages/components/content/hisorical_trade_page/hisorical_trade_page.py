
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.UI.header import Header
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.ferst_page import Ferst_page

class Hisorical_trade_page(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def build(self):
        self.hisorical_trade_page = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(ft.Text('Торговля по историческим данным',color=c_blue),alignment=ft.alignment.center),bgcolor=c_yelow,height=28,margin=ft.margin.only(top=-10,left=-10,right=-10),border = ft.border.all(1,c_white), 
                    ),
                    ft.Container(
                        ft.Column(controls=[
                            Header(),
                            Ferst_page()
                        ]),
                        expand=2,
                    )
                ]
            ),expand=2
        )
        
        return self.hisorical_trade_page