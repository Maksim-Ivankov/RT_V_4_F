
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.set_settings.page_trade.UI.trade_page import Trade_page

class Result_trqade_page(ft.UserControl):
    def __init__(self,back_trade_page,number_trade,strategy_now):
        super().__init__()
        self.back_trade_page = back_trade_page
        self.number_trade = number_trade
        self.strategy_now = strategy_now


    def build(self):
        print(len(os.listdir(path_save_trade)))
        self.ferst_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(#11
                                    ft.Container(ft.ElevatedButton(content = ft.Text('Назад к результатам торговли',size=12,),on_click=self.back_trade_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7,height=30),
                                    width=850,
                                ),
                                Trade_page(len(os.listdir(path_save_trade)),self.number_trade,self.strategy_now)
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        
        return self.ferst_page