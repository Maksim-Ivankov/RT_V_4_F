
import flet as ft
from variable import *
from imports import *

class Balance(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu


    def build(self):
        
        self.balance = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(ft.Text('Баланс кошелька',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white),
                    )),
                    ft.Container(
                        ft.Row(controls=[
                            ft.Text('5128$',color=c_green,size=12),
                            ft.Text('|',color=c_white,size=12),
                            ft.Text('Binance',color=c_yelow,size=12),
                        ]),
                        width=215,
                        height=41,
                        border = ft.border.all(1, c_white),
                        padding=10,
                    ), 
                ]
            )
        )
        
        return self.balance