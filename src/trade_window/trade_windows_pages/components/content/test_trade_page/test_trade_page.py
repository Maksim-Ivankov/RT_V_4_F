
import flet as ft
from variable import *
from imports import *

class Test_trade_page(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def build(self):
        
        self.test_trade_page = ft.Container(
            ft.Text('Тестовая торговля')
        )
        
        return self.test_trade_page