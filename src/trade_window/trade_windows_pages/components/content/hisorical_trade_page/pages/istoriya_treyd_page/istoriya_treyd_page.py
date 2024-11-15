
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.istoriya_treyd_page.UI.table_trade.table_trade import Table_trade
from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config

class Istoriya_treyd_page(ft.UserControl):
    def __init__(self,change_page,data=''):
        super().__init__()
        Save_config('param_trade_historical_trade_svobodniy_freym',{'regime_trade_page':'svoboda'})
        self.change_page = change_page
        self.data = data

    def build(self):
        self.ferst_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text('История торговли - схораненные карточки и статистика по всем проведенным торговым сессиям во вкладке исторической торговли',size=12,color=c_white,text_align='center'),
                                             margin=ft.margin.only(left=40)),
                                ft.Container(#11
                                    Table_trade(self.change_page,self.data),
                                    width=850,
                                    # margin=ft.margin.only(left=90),
                                ),
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.ferst_page