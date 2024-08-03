
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.UI.header import Header
from src.trade_window.trade_windows_pages.components.content.UI.dropdown import Dropdown
from src.trade_window.trade_windows_pages.components.content.UI.input import Input

from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_coin.cgange_coin_window import Cgange_coin_window

# Dropdown(self.on_change_tema,self.change_tema,["Dark","Light"],150)
# Input(self.on_change_count_coin,self.change_count_coin,150)

class Svoboda_freym_page(ft.UserControl):
    def __init__(self,change_page,page):
        super().__init__()
        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        if ('param_trade_historical_trade_svobodniy_freym') in config.sections():
            self.change_sledim_sa_cenoy = config.get('param_trade_historical_trade_svobodniy_freym', 'sledim_money')
            self.change_work_tf = config.get('param_trade_historical_trade_svobodniy_freym', 'work_tf')
            self.change_how_mach_time = config.get('param_trade_historical_trade_svobodniy_freym', 'dlitelnost')
            self.change_count_coin = config.get('param_trade_historical_trade_svobodniy_freym', 'how_mach_money')
        else:
            self.change_sledim_sa_cenoy = '1m'
            self.change_work_tf = '5m'
            self.change_how_mach_time = '24h'
            self.change_count_coin = '10'
        self.page = page
        self.change_page = change_page
    
    # выбор выпадашки - следим за ценой
    def on_change_sledim_sa_cenoy(self,e):
        data_save = {
            'sledim_money':e.control.value
        }
        Save_config('param_trade_historical_trade_svobodniy_freym',data_save)

    # выбор выпадашки - рабочий таймфрейм
    def on_change_work_tf(self,e):
        data_save = {
            'work_tf':e.control.value
        }
        Save_config('param_trade_historical_trade_svobodniy_freym',data_save)

    # выбор выпадашки - длителоьность
    def on_change_how_mach_time(self,e):
        data_save = {
            'dlitelnost':e.control.value
        }
        Save_config('param_trade_historical_trade_svobodniy_freym',data_save)

    # выбор выпадашки - сколько монет торговать
    def on_change_how_mach_coin(self,e):
        data_save = {
            'how_mach_money':e.control.value
        }
        Save_config('param_trade_historical_trade_svobodniy_freym',data_save)

    # нажали на кнопку сохранить в модалке
    def coin_save(self):
        print('1111')

    # окно выбора стратегии монет
    def chage_coin(self,e):
        bs = Cgange_coin_window(self.coin_save)
        self.page.overlay.append(bs)
        self.page.update()
    

    def build(self):
        self.svoboda_freym_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text('Получите данные по монетам для исторической торговли\nс биржи, либо используйте загруженные ранее данные',
                                        size=12,color=c_white,text_align='center'),padding=ft.padding.only(left=180)),
                                ft.Container(
                                    ft.Column(
                                        controls=[
                                            ft.Container(
                                                ft.Container(ft.Text('Сбор данных',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white),
                                            )),
                                            ft.Container(
                                                ft.Row(controls=[
                                                    ft.Container(
                                                        ft.Column(controls=[
                                                            ft.Text('Следим за ценой',size=12,color=c_white,text_align='center',width=150),
                                                            Dropdown(self.on_change_sledim_sa_cenoy,self.change_sledim_sa_cenoy,["1m","5m"],150),
                                                            ft.Text('Рабочий таймфрейм',size=12,color=c_white,text_align='center',width=150),
                                                            Dropdown(self.on_change_work_tf,self.change_work_tf,['1m','5m','15m','30m','1h','4h'],150),
                                                            ft.Text('Длительность',size=12,color=c_white,text_align='center',width=150),
                                                            Dropdown(self.on_change_how_mach_time,self.change_how_mach_time,['12h','24h','48h'],150),
                                                            ft.Text('Выбор монет',size=12,color=c_white,text_align='center',width=150),
                                                            ft.Container(ft.ElevatedButton(content = ft.Text('Выбрать монеты',size=12,),on_click=self.chage_coin,bgcolor=c_white,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,width=150,height=30,margin=ft.margin.only(top=0,bottom=0)),
                                                            ft.Text('Сколько монет торговать',size=12,color=c_white,text_align='center',width=150),
                                                            Input(self.on_change_how_mach_coin,self.change_count_coin,150),
                                                            ft.Container(ft.ElevatedButton(content = ft.Text('Получить данные',size=12,),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30,margin=ft.margin.only(top=0,bottom=0)),
                                                        ])
                                                    ),
                                                    ft.Container(
                                                        ft.Column(controls=[
                                                            ft.Text('Монеты для торговли',size=12,color=c_white,text_align='center',width=170),
                                                            ft.Container(
                                                                ft.Column(controls=[
                                                                    ft.Text('rwefwerf'),
                                                                    ft.Text('rwefwerf'),
                                                                    ft.Text('rwefwerf'),
                                                                    ft.Text('rwefwerf'),
                                                                    ft.Text('rwefwerf'),
                                                                    ft.Text('rwefwerf'),
                                                                    ft.Text('rwefwerf'),
                                                                    ft.Text('rwefwerf'),
                                                                    ft.Text('rwefwerf'),
                                                                    ft.Text('rwefwerf'),
                                                                    ft.Text('rwefwerf'),
                                                                    ft.Text('rwefwerf'),
                                                                    ft.Text('rwefwerf'),
                                                                    ft.Text('rwefwerf'),
                                                                    ft.Text('rwefwerf'),
                                                                    ft.Text('rwefwerf'),
                                                                    ft.Text('rwefwerf'),
                                                                ],scroll=ft.ScrollMode.ALWAYS,),
                                                                width=170,
                                                                height=338,
                                                                bgcolor=c_white,
                                                            )
                                                        ])
                                                    ),
                                                    ft.Container(ft.Column(controls=[
                                                        ft.Text('Логи торговли',size=12,color=c_white,text_align='center',width=170),
                                                        ft.Container(
                                                                ft.Column(controls=[
                                                                    ],scroll=ft.ScrollMode.ALWAYS,),
                                                                width=340,
                                                                height=338,
                                                                bgcolor=c_white,
                                                            )
                                                    ])),
                                                ]),
                                                width=709,
                                                height=392,
                                                border = ft.border.all(1, c_white),
                                                padding=10,
                                            ), 
                                        ]
                                    )
                                ),
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.svoboda_freym_page