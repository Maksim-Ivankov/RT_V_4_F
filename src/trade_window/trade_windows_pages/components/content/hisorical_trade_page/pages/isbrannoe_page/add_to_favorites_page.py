
import flet as ft
from variable import *
from imports import *

# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.istoriya_treyd_page.UI.table_trade.table_trade import Table_trade

class Add_to_favorites_page(ft.UserControl):
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page
        


    def build(self):
        self.ferst_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text('Добавление торговой стратегии в избранные стратегии. Поможет эффективнее протестировать преспективные настройки прибыльных торговых стратегий.',size=12,color=c_white,text_align='center'),
                                             margin=ft.margin.only(left=40)),
                                ft.Container(#11
                                    # Table_trade(),
                                    ft.Text('Здесь будет добавление'),
                                    width=850,
                                    # height=80,
                                    # margin=ft.margin.only(left=90),
                                ),
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.ferst_page