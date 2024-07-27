
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.settings_page.UI.settings import Settings
from src.trade_window.trade_windows_pages.components.content.settings_page.UI.proksi import Proksi
from src.trade_window.trade_windows_pages.components.content.settings_page.UI.change_folder import Change_folder

class Settings_page(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def build(self):
        
        self.settings_page = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        
                        # ft.Text('Настройки программы',color=c_blue,expand=True),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    # expand=1,
                                    width=10,
                                    height=28,
                                    bgcolor='red',
                                ),
                                ft.Container(
                                    # expand=1,
                                    ft.Text('Настройки программы',color=c_blue),
                                    
                                ),
                            ],
                            # expand = True,
                        ),
                        bgcolor=c_yelow,
                        # width=12000,
                        # expand=1,
                        height=28,
                        # margin=ft.margin.only(top=-10,left=-10),
                        # border=ft.border.all(1,c_white),
                        
                        # expand = True,
                        
                    ),
                    ft.Container(
                        ft.Row(
                            controls=[
                                Settings(),
                                Proksi(),
                                Change_folder(),
                            ]
                        ),bgcolor='red'
                    )
                ]
            ),expand=2
        )
        
        
        return self.settings_page