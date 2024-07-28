
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.prifile_page.UI.birgi import Birgi
from src.trade_window.trade_windows_pages.components.content.prifile_page.UI.data_profile import Data_profile
from src.trade_window.trade_windows_pages.components.content.prifile_page.UI.telegram import Telegram
from src.trade_window.trade_windows_pages.components.content.prifile_page.UI.type_profile import Type_profile

class Prifile_page(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def build(self):
        
        self.prifile_page = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        
                        # ft.Text('Настройки программы',color=c_blue,expand=True),
                        ft.Container(
                                    ft.Text('Профиль',color=c_blue),
                                    alignment=ft.alignment.center
                                    
                        ),
                        bgcolor=c_yelow,
                        height=28,
                        margin=ft.margin.only(top=-10,left=-10,right=-10),
                        border = ft.border.all(1,c_white),
                        
                    ),
                    ft.Container(
                        ft.Row(
                            controls=[
                                Data_profile(),
                                Type_profile(),
                            ]
                        ),padding=30
                    )
                ]
            ),expand=2
        )
        
        return self.prifile_page