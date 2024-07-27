
import flet as ft
from variable import *
from imports import *

class Trade_robot_page(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def build(self):
        
        self.trade_robot_page = ft.Container(
            ft.Text('Торговый робот')
        )
        
        return self.trade_robot_page