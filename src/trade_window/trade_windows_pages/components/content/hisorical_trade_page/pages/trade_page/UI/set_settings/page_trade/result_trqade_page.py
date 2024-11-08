#1111212
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.set_settings.page_trade.UI.trade_page import Trade_page

class Result_trqade_page(ft.UserControl):
    def __init__(self,back_trade_page,number_trade,strategy_now,regime='None',number_trade_folder=(len(os.listdir(path_save_trade))),change_page=''):
        super().__init__()
        self.change_page = change_page
        self.back_trade_page = back_trade_page
        self.number_trade = number_trade
        self.strategy_now = strategy_now
        self.regime = regime
        self.number_trade_folder = number_trade_folder

    def build(self):
        if self.regime != 'istorija_trade':     
            btn_this = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(
                            ft.Container(
                                ft.Row(controls=[
                                    ft.Container(ft.ElevatedButton(content = ft.Text('Назад к результатам торговли',size=12,),on_click=self.back_trade_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7,height=30),
                                    ft.Container(ft.ElevatedButton(content = ft.Text('Добавить в избранное',size=12,),data='Добавить в избранное',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                ]),width=435),alignment=ft.alignment.center),height=60,margin=ft.margin.only(top=-14,left=-10,right=-10,bottom=-14),      
                    ),
                    # ft.Container(
                    #     ft.Container(alignment=ft.alignment.center),height=1,bgcolor=c_white,margin=ft.margin.only(top=2,left=-10,right=-10),      
                    # ),
                    
                ]
            ),expand=2
            
        )
            
            
            
            
        elif self.regime == 'istorija_trade':
             btn_this = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(
                            ft.Container(
                                ft.Row(controls=[
                                    ft.Container(ft.ElevatedButton(content = ft.Text('Назад к результатам торговли',size=12,),on_click=self.back_trade_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7,height=30),
                                    ft.Container(ft.ElevatedButton(content = ft.Text('Добавить в избранное',size=12,),data='Добавить в избранное',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                ]),width=435),alignment=ft.alignment.center),height=60,margin=ft.margin.only(top=-4,left=-10,right=-10,bottom=-7),      
                    ),
                    # ft.Container(
                    #     ft.Container(alignment=ft.alignment.center),height=1,bgcolor=c_white,margin=ft.margin.only(top=2,left=-10,right=-10),      
                    # ),
                    
                ]
            ),expand=2,margin=ft.margin.only(bottom=-10,top=-20)
            
        )
             
             
             
        self.ferst_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                btn_this,
                                Trade_page(self.number_trade_folder,self.number_trade,self.strategy_now)
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        
        return self.ferst_page