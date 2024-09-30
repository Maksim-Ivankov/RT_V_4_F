
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.graph_dohod.graph_dohod import Graph_dohod

class Output_info_trade(ft.UserControl):#1
    def __init__(self):
        super().__init__()
        self.pb = ft.ProgressBar(width=900,bgcolor=c_blue,color=c_yelow)
        # self.number_trade = len(os.listdir(path_save_trade))
        self.number_trade = len(os.listdir(path_save_trade))+1

    
    def print_itog_and_graph(self):
        self.trade_page_two = ft.Container(ft.Column(controls=[
            ft.Container(ft.Row(controls=[
                    ft.Container(
                                    ft.Container(ft.Column(controls=[ft.Column(controls=[
                                                    ft.Container(
                                                        ft.Container(ft.Text('Доходность',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                        ft.Container(
                                                            Graph_dohod(self.number_trade),
                                                            width=425,
                                                            # border = ft.border.all(1, c_white),
                                                            # padding=14,
                                                            height = 400,
                                                            padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                                        )]),])),width=425,),
                                    ft.Container(ft.Container(
                                            ft.Column(controls=[ft.Column(controls=[
                                                        ft.Container(
                                                            ft.Container(ft.Text('График сделки',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                        ft.Container(
                                                            ft.Container(
                                                                ft.Column(scroll=ft.ScrollMode.ALWAYS),
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
                width=900,height=450,padding=ft.padding.only(left=20))
        ]),key='itog',width=900)
        return self.trade_page_two
    
    def print_page(self):
            
        self.trade_page = ft.Container(ft.Column(controls=[
            ft.Container(self.pb,margin=ft.margin.only(top=20,bottom=20),key='pb'),
            ft.Container(ft.Row(controls=[
                    ft.Container(
                                    ft.Container(ft.Column(controls=[ft.Column(controls=[
                                                    ft.Container(
                                                        ft.Container(ft.Text('Логи работы',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                        ft.Container(
                                                            ft.Container(
                                                                ft.Column(scroll=ft.ScrollMode.ALWAYS),
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
                                                                ft.Column(scroll=ft.ScrollMode.ALWAYS),
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
                width=900,height=450,padding=ft.padding.only(left=20))
        ]),width=900)
        return self.trade_page

   
    def build(self):
        return self.print_page()