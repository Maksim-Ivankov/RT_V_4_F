
import flet as ft
from variable import *
from imports import *

class Output_info_trade(ft.UserControl):#1
    def __init__(self):
        super().__init__()


    def print_page(self):
        self.trade_page = ft.Container(ft.Text('1111111111'))
            
        
        return self.trade_page

   
    def build(self):
        return self.print_page()