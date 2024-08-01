
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.UI.header import Header
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.ferst_page import Ferst_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.historical_trade_page import Historical_trade_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.svoboda_freym_page import Svoboda_freym_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.tred_so_smeseniem_page import Tred_so_smeseniem_page

class Hisorical_trade_page(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.ferst_page = 'Первая'

    def change_page(self,e):
        # print(e.control.data)
        # self.controls = []
        print(e.control.data)
        # self.controls.append(self.print_page(e.control.data))
        # self.update()

    def print_page(self,page):

        pages_list={
            'Первая':Ferst_page(self.change_page),
            'Историческая торговля':Historical_trade_page(self.change_page),
            'Свободный фрейм':Svoboda_freym_page(self.change_page),
            'Торговля со смещением':Tred_so_smeseniem_page(self.change_page),
        }

        return ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(ft.Text('Торговля по историческим данным',color=c_blue),alignment=ft.alignment.center),bgcolor=c_yelow,height=28,margin=ft.margin.only(top=-10,left=-10,right=-10),border = ft.border.all(1,c_white), 
                    ),
                    ft.Container(
                        ft.Column(controls=[
                            Header(),
                            pages_list[page]
                        ]),
                        expand=2,
                    )
                ]
            ),expand=2
        )

    def build(self):
        
        # return self.print_page(self.ferst_page)

        return ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(ft.Text('Торговля по историческим данным',color=c_blue),alignment=ft.alignment.center),bgcolor=c_yelow,height=28,margin=ft.margin.only(top=-10,left=-10,right=-10),border = ft.border.all(1,c_white), 
                    ),
                    ft.Container(
                        ft.Column(controls=[
                            Header(),
                            Ferst_page(self.change_page)
                        ]),
                        expand=2,
                    )
                ]
            ),expand=2
        )