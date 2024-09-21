
import flet as ft
from variable import *
from imports import *

class Trade_page(ft.UserControl):#1
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page
        config = configparser.ConfigParser()  
        config.read(path_imports_config)
        self.data_print_row = [
            ['Имя робота для логов',config.get('param_trade_historical_trade_svobodniy_freym', 'name_bot'),'Режим тейка/стопа',f'{config.get('param_trade_historical_trade_svobodniy_freym', 'regim_tp')}/{config.get('param_trade_historical_trade_svobodniy_freym', 'regim_sl')}'],
            ['Режим монеты',config.get('param_trade_historical_trade_svobodniy_freym', 'strategi_coin'),'Тейк профит',config.get('param_trade_historical_trade_svobodniy_freym', 'tp')],
            ['Сколько монет торговать',config.get('param_trade_historical_trade_svobodniy_freym', 'how_mach_money'),'Стоп лосс',config.get('param_trade_historical_trade_svobodniy_freym', 'sl')],
            ['Комиссия мейкер',config.get('param_trade_historical_trade_svobodniy_freym', 'komission_mayker'),'Режим объёмов',f'{config.get('param_trade_historical_trade_svobodniy_freym', 'regim_volume_min')}/{config.get('param_trade_historical_trade_svobodniy_freym', 'regim_volume_max')}'],
            ['Комиссия тейкер',config.get('param_trade_historical_trade_svobodniy_freym', 'komission_taker'),'Объём торгов мин',config.get('param_trade_historical_trade_svobodniy_freym', 'volume_min')],
            ['Таймфрейм',config.get('param_trade_historical_trade_svobodniy_freym', 'work_tf'),'Объём торгов макс',config.get('param_trade_historical_trade_svobodniy_freym', 'volume_max')],
            ['Длительность торговли',config.get('param_trade_historical_trade_svobodniy_freym', 'dlitelnost'),'Плечо',config.get('param_trade_historical_trade_svobodniy_freym', 'leverage')],
        ]

    def print_page(self):

        datas_print = []
        config_general_set = configparser.ConfigParser()  
        config_general_set.read(path_ini_general_set)
        for i in self.data_print_row:
            datas_print.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(i[0],text_align='center',color=c_white,size=12)),
                    ft.DataCell(ft.Text(i[1],text_align='center',color=c_white,size=12)),
                    ft.DataCell(ft.Text(i[2],text_align='center',color=c_white,size=12)),
                    ft.DataCell(ft.Text(i[3],text_align='center',color=c_white,size=12)),
                    
                    
                ]
                )
            )  

        self.trade_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
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
                                                            ft.Column(
                                                                controls=[
                                                            
                                                            ],
                                                            scroll=ft.ScrollMode.ALWAYS,),
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
                                                                ft.Column(
                                                                    controls=[
                                                                
                                                                ],
                                                                scroll=ft.ScrollMode.ALWAYS,),
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
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Запустить торговлю',size=12,),data='Выбрать режим торговли',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                    ]),padding=ft.padding.only(left=320,top=10)
                                    ),
                                    width=500,
                                    # bgcolor='red'
                                    # height=920
                                )
                            ]),alignment=ft.alignment.center),
                        padding=ft.padding.only(top=10)
                    ),expand=2
        )
        
        return self.trade_page

   
    def build(self):
        return self.print_page()