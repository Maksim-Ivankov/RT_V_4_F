
import flet as ft
from variable import *
from imports import *

class Graph_dohod(ft.UserControl):
    def __init__(self):
        super().__init__()
        

    def print_page(self):
            
        self.trade_page = ft.Container()
           
        return self.trade_page

   
    def build(self):
        return self.print_page()