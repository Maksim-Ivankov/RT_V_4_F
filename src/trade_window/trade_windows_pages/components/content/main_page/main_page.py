
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.main_page.UI.balance import Balance
from src.trade_window.trade_windows_pages.components.content.main_page.UI.dinamic_dohodnost import Dinamic_dohodnost
from src.trade_window.trade_windows_pages.components.content.main_page.UI.socsety import Socsety
from src.trade_window.trade_windows_pages.components.content.main_page.UI.statistic_now_day import Statistic_now_day
from src.trade_window.trade_windows_pages.components.content.main_page.UI.status_trade import Status_trade
from src.trade_window.trade_windows_pages.components.content.main_page.UI.status_work import Status_work
from src.trade_window.trade_windows_pages.components.content.main_page.UI.stistica_our_period import Stistica_our_period
from src.trade_window.trade_windows_pages.components.content.main_page.UI.telegram_chat import Telegram_chat
from src.trade_window.trade_windows_pages.components.content.main_page.UI.teplowaya_map import Teplowaya_map

class Main_page(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def build(self):
        
        self.main_page = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(ft.Text('Доход за месяц: 12% - 1400$    Общий доход:12% - 1400$     Возраст аккаунта: 28 дней   Доход за 24 часа: 5% - 120$',color=c_blue),alignment=ft.alignment.center),bgcolor=c_yelow,height=28,margin=ft.margin.only(top=-10,left=-10,right=-10),border = ft.border.all(1,c_white), 
                    ),
                    ft.Container(
                        ft.Column(controls=[
                            ft.Row(controls=[
                                Dinamic_dohodnost(),
                                Stistica_our_period(),
                                Statistic_now_day()
                            ]),
                            ft.Row(controls=[
                                Status_work(),
                                Status_trade(),
                                Balance(),
                                Socsety()
                            ]),
                            ft.Row(controls=[
                                Teplowaya_map(),
                                Telegram_chat()
                            ]),
                        ]),padding=ft.padding.only(left=30)
                    )
                ]
            ),expand=2
        )
        
        return self.main_page