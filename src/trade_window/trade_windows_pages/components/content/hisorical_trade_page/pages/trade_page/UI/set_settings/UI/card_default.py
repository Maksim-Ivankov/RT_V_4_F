
import flet as ft
from variable import *
from imports import *


class Card_default(ft.UserControl):
    def __init__(self):
        super().__init__()

    


    def print_page(self,number):
        # self.trade_page = ft.Container(ft.Text(number),width=170,height=200,bgcolor='red')
        self.trade_page = ft.Container(ft.Column(controls=[
            
            ft.Container(ft.Text(number,color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white)),
            ft.Container(ft.Container(ft.Text('В очереди',color=c_white,text_align='CENTER'),bgcolor=c_blue_binance,padding=ft.padding.only(top=90)),width=170,height=200,border=ft.border.all(1,c_white))
        ]),data=number,key=number)
           
        return self.trade_page

   
    # def build(self):
    #     return self.print_page(self.number_trade)