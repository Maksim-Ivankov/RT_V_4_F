
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.menu.menu import Menu
from src.trade_window.trade_windows_pages.components.content.content import Content

class Platforma(ft.UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page

    def build(self):
        def __init__(self,page):
            super().__init__()
            self.page = page
        
        self.platforma = ft.Container(
            ft.Row(
                controls=[
                    Menu(self.page),
                    Content()
                ]
            )
        )
        
        return self.platforma