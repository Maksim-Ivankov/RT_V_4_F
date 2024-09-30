
import flet as ft
from variable import *
from imports import *

class Graph_dohod(ft.UserControl):
    def __init__(self,number_trade):
        super().__init__()
        self.number_trade = number_trade
        self.array_data_row = []
        self.trade_plus = 0
        self.trade_minus = 0
        self.trade_balance_dolar = 0
        self.trade_balance_procent = 0
        self.trade_plus_dolar = 0
        self.trade_minus_dolar = 0
        self.trade_komission = 0
        

    def print_page(self):
        
        self.path_save_trade_log = f'{path_save_trade}\\{self.number_trade}\\trade.txt' # путь сохранения логов в папке трейда
        if os.path.isfile(self.path_save_trade_log):
            with open(self.path_save_trade_log) as file:
                self.array_data_row = [row.strip() for row in file]
        for trade_once in self.array_data_row:
            trend = trade_once.split('|')[0]
            depo_start = float(trade_once.split('|')[1])
            depo = float(trade_once.split('|')[2])
            result = float(trade_once.split('|')[3])
            komission = float(trade_once.split('|')[4])
            result_none_komission = float(trade_once.split('|')[5])
            if result>0:
                self.trade_plus+=1
                self.trade_plus_dolar+=result_none_komission
            else: 
                self.trade_minus+=1
                self.trade_minus_dolar += result_none_komission
            self.trade_balance_dolar = round(depo,2)
            self.trade_komission+=komission
        self.trade_balance_procent = round(((depo-depo_start)/depo_start)*100,2)
        # print(f'{depo} | {depo_start} | {((depo-depo_start)/depo)}')
            
            
            
            # print(f'{trend} {depo} {result} {komission} {result_none_komission}')
            
        
        # stroke_paint = ft.Paint(stroke_width=2, style=ft.PaintingStyle.STROKE)
        # fill_paint = ft.Paint(style=ft.PaintingStyle.FILL)
            
        self.trade_page = ft.Container(
            # cv.Canvas(
            #     [
            #         cv.Circle(100, 100, 50, stroke_paint),
            #         cv.Circle(80, 90, 10, stroke_paint),
            #         cv.Circle(84, 87, 5, fill_paint),
            #         cv.Circle(120, 90, 10, stroke_paint),
            #         cv.Circle(124, 87, 5, fill_paint),
            #         cv.Arc(70, 95, 60, 40, 0, math.pi, paint=stroke_paint),
            #     ],
            #     width=float("inf"),
            #     expand=True,
            # ),
            ft.Container(ft.Column(controls=[
                # для канваса
                ft.Container(
                    
                    width=405,
                    height=200,
                    bgcolor=c_blue_binance,
                    ),
                # для статистики под канвасом
                ft.Container(
                    ft.Row(controls=[
                        ft.Container(ft.Column(controls=[
                            ft.Row(controls=[
                                ft.Text('Сделок всего',width=100),
                                ft.Text(str(len(self.array_data_row)),text_align='right',width=80),
                            ]),
                            ft.Container(width=190,height=1,bgcolor=c_white),
                            ft.Row(controls=[
                                ft.Text('Сделок в +',width=100),
                                ft.Text(f'{self.trade_plus}',text_align='right',width=80),
                            ]),
                            ft.Container(width=190,height=1,bgcolor=c_white),
                            ft.Row(controls=[
                                ft.Text('Сделок в -',width=100),
                                ft.Text(f'{self.trade_minus}',text_align='right',width=80),
                            ]),
                            ft.Container(width=190,height=1,bgcolor=c_white),
                            ft.Row(controls=[
                                ft.Text('Баланс Итог $',width=100),
                                ft.Text(f'{self.trade_balance_dolar} $',text_align='right',width=80),
                            ]),
                        ])),
                        ft.Container(width=1,height=160,bgcolor=c_white),
                        ft.Container(ft.Column(controls=[
                            ft.Row(controls=[
                                ft.Text('Баланс Итог %',width=100),
                                ft.Text(f'{self.trade_balance_procent} %',text_align='right',width=80),
                            ]),
                            ft.Container(width=190,height=1,bgcolor=c_white),
                            ft.Row(controls=[
                                ft.Text('Сделок в + $',width=100),
                                ft.Text(f'{round(self.trade_plus_dolar,2)} $',text_align='right',width=80),
                            ]),
                            ft.Container(width=190,height=1,bgcolor=c_white),
                            ft.Row(controls=[
                                ft.Text('Сделок в - $',width=100),
                                ft.Text(f'{round(self.trade_minus_dolar,2)} $',text_align='right',width=80),
                            ]),
                            ft.Container(width=190,height=1,bgcolor=c_white),
                            ft.Row(controls=[
                                ft.Text('Комиссия',width=100),
                                ft.Text(f'{round(self.trade_komission,2)} $',text_align='right',width=80),
                            ]),
                        ])),
                    ])
                    ),
                ])),
            width=425,
            height=400,
            border = ft.border.all(1, c_white),
            bgcolor=c_blue,
            padding=10,
        )
           
        return self.trade_page

   
    def build(self):
        return self.print_page()