
import flet as ft
from variable import *
from imports import *

class Graph_trade(ft.UserControl):
    def __init__(self):
        super().__init__()
    

    def print_page(self):
            
        self.trade_page = ft.Container(
            ft.Text('dfgdfgdf'),
            width=425,
            height=400,
            border = ft.border.all(1, c_white),
            bgcolor=c_blue,
            padding=10,
        )
           
        return self.trade_page

   
    def build(self):
        return self.print_page()