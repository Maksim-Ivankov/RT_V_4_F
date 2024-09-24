
import flet as ft
from variable import *
from imports import *

class Output_info_trade(ft.UserControl):#1
    def __init__(self):
        super().__init__()
        self.pb = ft.ProgressBar(width=900,bgcolor=c_blue,color=c_yelow)


    def print_page(self):
        self.trade_page = ft.Container(ft.Column(controls=[
            ft.Container(self.pb,margin=ft.margin.only(top=20,bottom=20),key='pb'),
            ft.Container(width=900,height=1200,bgcolor='red')
        ]),width=900)
            
        
        return self.trade_page

   
    def build(self):
        return self.print_page()