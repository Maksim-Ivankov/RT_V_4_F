

import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.settings_page.UI.settings import Settings
from src.trade_window.trade_windows_pages.components.content.settings_page.UI.proksi import Proksi
from src.trade_window.trade_windows_pages.components.content.settings_page.UI.change_folder import Change_folder

class Settings_page(ft.UserControl):

    def build(self):
        
        self.settings_page = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        
                        # ft.Text('Настройки программы',color=c_blue,expand=True),
                        ft.Container(
                                    ft.Text('Настройки программы',color=c_blue),
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
                                Settings(),
                                Proksi(),
                                Change_folder(),
                            ]
                        ),padding=30
                    )
                ]
            ),expand=2
        )
        
        
        return self.settings_page