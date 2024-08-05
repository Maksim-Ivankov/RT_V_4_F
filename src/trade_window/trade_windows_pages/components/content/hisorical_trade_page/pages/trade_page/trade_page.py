
import flet as ft
from variable import *
from imports import *

class Trade_page(ft.UserControl):
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page

    def print_page(self):
        self.trade_page = ft.Container(
            ft.Text('ФИНАЛ')
        )
        
        return self.trade_page

   
    def build(self):
        return self.print_page()