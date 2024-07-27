
import flet as ft
from variable import *
from imports import *

class Hisorical_trade_page(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def build(self):
        
        self.hisorical_trade_page = ft.Container(
            ft.Text('Историческая торговля')
        )
        
        return self.hisorical_trade_page