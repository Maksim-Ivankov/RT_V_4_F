
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.UI.header import Header
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.ferst_page import Ferst_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.historical_trade_page import Historical_trade_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.svoboda_freym_page import Svoboda_freym_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.tred_so_smeseniem_page import Tred_so_smeseniem_page

class Hisorical_trade_page(ft.UserControl):
    def __init__(self,page):
        super().__init__()
        # self.ferst_page = 'Первая'
        self.ferst_page = 'Свободный фрейм'
        self.page = page

    def print_page(self,page):

        pages_list={
            'Первая':Ferst_page(self.change_page),
            'Историческая торговля':Historical_trade_page(self.change_page),
            'Свободный фрейм':Svoboda_freym_page(self.change_page,self.page),
            'Торговля со смещением':Tred_so_smeseniem_page(self.change_page),
        }

        title_list={
            'Первая':'Торговля по историческим данным',
            'Историческая торговля':'Торговля по историческим данным | Историческая торговля',
            'Свободный фрейм':'Торговля по историческим данным | Свободный фрейм',
            'Торговля со смещением':'Торговля по историческим данным | Торговля со смещением',
        }

        return ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(ft.Text(title_list[page],color=c_blue),alignment=ft.alignment.center),bgcolor=c_yelow,height=28,margin=ft.margin.only(top=-10,left=-10,right=-10),border = ft.border.all(1,c_white), 
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
    
    def change_page(self,e):
        self.controls = []
        self.controls.append(self.print_page(e.control.data))
        self.update()

    # def will_unmount(self):
    #     print('Размонтирование')
    #     # self.disabled = False


    def build(self):
        
        return self.print_page(self.ferst_page)
