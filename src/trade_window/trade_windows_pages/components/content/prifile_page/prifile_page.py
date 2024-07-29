
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.prifile_page.UI.birgi import Birgi
from src.trade_window.trade_windows_pages.components.content.prifile_page.UI.data_profile import Data_profile
from src.trade_window.trade_windows_pages.components.content.prifile_page.UI.telegram import Telegram
from src.trade_window.trade_windows_pages.components.content.prifile_page.UI.type_profile import Type_profile
from src.trade_window.trade_windows_pages.components.content.UI.dropdown import Dropdown

from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config

class Prifile_page(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.birga_trade = 'Binance'

    def colback_change_birga_trade(self,e):
        self.birga_trade = e.control.value
        data_save = {
            'birga_trade':e.control.value,
        }
        Save_config('Birga_trade',data_save)
        e.control.border_color = c_green
        e.control.update()

    def build(self):
        
        self.prifile_page = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(ft.Text('Профиль',color=c_blue),alignment=ft.alignment.center),bgcolor=c_yelow,height=28,margin=ft.margin.only(top=-10,left=-10,right=-10),border = ft.border.all(1,c_white), 
                    ),
                    ft.Container(
                        ft.Column(controls=[
                            ft.Container(
                                ft.Row(
                                controls=[
                                    Data_profile(),
                                    Type_profile(),
                                ]
                                ),padding=30
                            ),
                            ft.Container(
                                ft.Row(
                                controls=[
                                    Birgi(),
                                    Telegram()
                                ]
                                ),padding=ft.padding.only(left=30,top=-20)
                            ),
                            ft.Container(ft.Row(controls=[
                                ft.Text('Биржа для торговли в RoboTrade',size=12,color=c_white),
                                Dropdown(self.colback_change_birga_trade,'Binance',['Binance','OKX','ByBit'],150)
                            ]),padding=ft.padding.only(left=30,top=10)
                            ),
                            ft.Container(ft.ElevatedButton(content = ft.Text('Смотреть избранные стратегии',size=12,),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),height=30,margin=ft.margin.only(left=30,top=10))
                        ])
                    )
                ]
            ),expand=2
        )
        
        return self.prifile_page