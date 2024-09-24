
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.data_settings import print_our_settings,print_set_settings
from src.controllers.trade.core_trade import Core_trade
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.output_info_trade import Output_info_trade

class Trade_page(ft.UserControl):#1
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page
        self.output_info_trade = Output_info_trade()
        self.count_pb = 0
        
    def start_trade(self,e):
        regime = 'Историческая торговля|Свободный фрейм|Ода настройка'
        config = configparser.ConfigParser()  
        config.read(path_imports_config)
        strategy = literal_eval(config.get('param_trade_historical_trade_svobodniy_freym', 'strategys'))
        core_trade_ob = Core_trade(regime,strategy)
        self.controls[0].content.content.content.controls.append(self.output_info_trade.print_page())
        self.controls[0].content.content.content.height=600
        self.content.scroll_to(key="pb", duration=1000)
        self.myThread = threading.Thread(target=core_trade_ob.start_trade(self.change_pb), args=(), daemon=True)
        self.myThread.start()
        
    def change_pb(self,procent):
        self.output_info_trade.pb.value = procent
        self.update()
        

    def print_page(self):
        self.content = ft.Column(controls=[
                                ft.Container(ft.Text('Проверьте настройки и запустите торговлю',size=12,color=c_white,text_align='center'),padding=ft.padding.only(left=320)),
                                ft.Container(
                                    ft.Row(controls=[
                                    ft.Container(
                                    ft.Container(
                                        ft.Column(controls=[
                                            ft.Column(
                                                controls=[
                                                    ft.Container(
                                                        ft.Container(ft.Text('Общие настройки робота',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                        ft.Container(
                                                            ft.Container(
                                                                print_our_settings,
                                                                width=500,
                                                                height=148,
                                                                border = ft.border.all(1, c_white),
                                                                bgcolor=c_blue,
                                                            ),
                                                            width=500,
                                                            # border = ft.border.all(1, c_white),
                                                            # padding=14,
                                                            height = 148,
                                                            padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                                        
                                                        )]),     
                                    ])),
                                    width=500,
                                    # bgcolor='red'
                                    ),
                                    ft.Container(
                                        ft.Container(
                                            ft.Column(controls=[
                                                ft.Column(
                                                    controls=[
                                                        ft.Container(
                                                            ft.Container(ft.Text('Настройки стратегий',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                        ft.Container(
                                                            ft.Container(
                                                                print_set_settings,
                                                                width=350,
                                                                height=148,
                                                                border = ft.border.all(1, c_white),
                                                                bgcolor=c_blue,
                                                            ),
                                                            width=350,
                                                            # border = ft.border.all(1, c_white),
                                                            # padding=14,
                                                            height = 148,
                                                            padding=ft.padding.only(left=-1,top=-1,bottom=-1)    
                                                )]),     
                                        ])),
                                        width=400,
                                        # bgcolor='red'
                                    ),
                                    ]),
                                width=900,padding=ft.padding.only(left=20)),
                                ft.Container(
                                    ft.Container(
                                        ft.Row(controls=[
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Назад',size=12,),data='Выбрать режим торговли',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Запустить торговлю',size=12,),data='Выбрать режим торговли',bgcolor=c_yelow,on_click=self.start_trade,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                    ]),padding=ft.padding.only(left=320,top=10)
                                    ),
                                    width=500,
                                    # bgcolor='red'
                                    # height=920
                                ),
                                
                            ],scroll=ft.ScrollMode.ALWAYS)
        
        self.trade_page = ft.Container(
            ft.Container(
                        ft.Container(
                            self.content,
                            alignment=ft.alignment.center),
                            padding=ft.padding.only(top=10)
                    ),expand=2
        )
        
        
        return self.trade_page

   
    def build(self):
        return self.print_page()