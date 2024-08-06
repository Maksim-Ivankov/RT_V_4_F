
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
                                ft.Container(ft.Text('Проверьте настройки и запустите торговлю',size=12,color=c_white,text_align='center',),padding=ft.padding.only(left=230)),
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
                                                                ft.DataTable(columns=[
                                                                    # ft.DataColumn(ft.Text('№',text_align='center',color=c_white,size=12)),
                                                                    # ft.DataColumn(ft.Text('Время старта',text_align='center',color=c_white,size=12)),
                                                                    # ft.DataColumn(ft.Text('Время остановки',text_align='center',color=c_white,size=12)),
                                                                    # ft.DataColumn(ft.Text('Депозит',text_align='center',color=c_white,size=12)),
                                                                 

                                                                ],
                                                                rows = datas_print,
                                                                column_spacing = 5,
                                                                data_row_max_height = 30,
                                                                data_row_min_height = 30,
                                                                show_checkbox_column = False,
                                                            )
                                                            ],
                                                            scroll=ft.ScrollMode.ALWAYS,),
                                                            width=600,
                                                            height=148,
                                                            border = ft.border.all(1, c_white),
                                                            bgcolor=c_blue,
                                                        ),
                                                        width=600,
                                                        # border = ft.border.all(1, c_white),
                                                        # padding=14,
                                                        height = 148,
                                                        padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                                        
                                            )]),     
                                    ])),
                                    width=860,
                                ),
                                ft.Container(
                                    ft.Container(
                                        ft.Row(controls=[
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Назад',size=12,),data='Настройки робота',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Выбрать режим торговли',size=12,),data='Выбрать режим торговли',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                    ]),padding=ft.padding.only(left=290,top=10)
                                    ),
                                    width=860,
                                    # height=920
                                )
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.trade_page

   
    def build(self):
        return self.print_page()