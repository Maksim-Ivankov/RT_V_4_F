
import flet as ft
from variable import *
from imports import *

class Output_info_trade(ft.UserControl):#1
    def __init__(self):
        super().__init__()
        self.pb = ft.ProgressBar(width=900,bgcolor=c_blue,color=c_yelow)
        self.logi_data = []
        self.logi_print = []

    def build(self):
    # def print_page(self):
        
        for i in reversed(self.logi_data):
            self.logi_print.append(ft.Container(ft.Text(i)))
            
        self.trade_page = ft.Container(ft.Column(controls=[
            ft.Container(self.pb,margin=ft.margin.only(top=20,bottom=20),key='pb'),
            ft.Container(ft.Row(controls=[
                    ft.Container(
                                    ft.Container(ft.Column(controls=[ft.Column(controls=[
                                                    ft.Container(
                                                        ft.Container(ft.Text('Логи работы',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                        ft.Container(
                                                            ft.Container(
                                                                ft.Column(controls=self.logi_print),
                                                                width=425,
                                                                height=400,
                                                                border = ft.border.all(1, c_white),
                                                                bgcolor=c_blue,
                                                                padding=10,
                                                            ),
                                                            width=425,
                                                            # border = ft.border.all(1, c_white),
                                                            # padding=14,
                                                            height = 400,
                                                            padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                                        )]),])),width=425,),
                                    ft.Container(ft.Container(
                                            ft.Column(controls=[ft.Column(controls=[
                                                        ft.Container(
                                                            ft.Container(ft.Text('Сделки',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                        ft.Container(
                                                            ft.Container(
                                                                
                                                                width=425,
                                                                height=400,
                                                                border = ft.border.all(1, c_white),
                                                                bgcolor=c_blue,
                                                                padding=10,
                                                            ),
                                                            width=425,
                                                            # border = ft.border.all(1, c_white),
                                                            # padding=14,
                                                            height = 400,
                                                            padding=ft.padding.only(left=-1,top=-1,bottom=-1)    
                                                )]),])),width=425,),]),
                width=900,height=1200,padding=ft.padding.only(left=20))
        ]),width=900)
        return self.trade_page

   
    # def build(self):
    #     return self.print_page()