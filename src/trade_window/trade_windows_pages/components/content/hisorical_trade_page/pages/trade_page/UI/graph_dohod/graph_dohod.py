
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
        
        self.depo_max_min_stat_arr = []
        # график
        self.width_graph = 405
        self.height_graph = 200
        self.print_canvas_arr = []
    
    def pan_start(self,e: ft.DragStartEvent):
        print(e.local_x)
        print(e.local_y)
        # x = e.local_x
        # y = e.local_y

    def print_page(self):
        
        # штука ниже вытаскивает из файла с трейдом все данные и делает статистику
        self.path_save_trade_log = f'{path_save_trade}\\{self.number_trade}\\trade.txt' # путь сохранения логов в папке трейда
        if os.path.isfile(self.path_save_trade_log):
            with open(self.path_save_trade_log) as file:
                self.array_data_row = [row.strip() for row in file]
        for trade_once in self.array_data_row:
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
            self.depo_max_min_stat_arr.append(depo)
            
        self.trade_balance_procent = round(((depo-depo_start)/depo_start)*100,2)
        self.price_max = max(self.depo_max_min_stat_arr) # максимальное депо
        if self.price_max<depo_start:self.price_max = depo_start
        self.price_min = min(self.depo_max_min_stat_arr) # минимальное депо
        
        
        # рисуем график
        self.OldRange = (self.price_max - self.price_min) # старая высота = 39,78
        self.NewRange = self.height_graph # новая высота = 200
        self.NewRange1 = (self.width_graph/(len(self.array_data_row))) # новая ширина = 36,81
        self.y0 = self.height_graph - (((depo_start - self.price_min) * self.NewRange) / self.OldRange)
        self.x0 = 0
        
        # print(self.OldRange)
        # print(self.NewRange)
        # print(self.OldRange1)
        # print(self.NewRange1)
        # print(self.y0)
        # print(self.x0)
        
        # стили для фигур
        # stroke_paint = ft.Paint(stroke_width=1, style=ft.PaintingStyle.STROKE,color=ft.colors.GREEN)
        fill_green = ft.Paint(style=ft.PaintingStyle.FILL,color=c_green_binance)
        fill_red = ft.Paint(style=ft.PaintingStyle.FILL,color=c_red_binance)
        
        # self.print_canvas_arr.append(cv.Line(0,self.height_graph-self.y0,self.width_graph,self.height_graph-self.y0, stroke_paint))
        
        for index in range(len(self.array_data_row)):
            self.value = float(self.array_data_row[index].split('|')[2])
            # print(self.value)
            self.x = ((index) * self.NewRange1)
            self.y = self.height_graph - (((self.value - self.price_min) * self.NewRange) / self.OldRange)
            print(f'x0={self.x0} | y0={self.y0} | x={self.x} | y={self.y}')
            if float(self.array_data_row[index].split('|')[3])>=0:
                # graph_profit.tag_lower(graph_profit.create_rectangle(x0, self.height-y0, x, self.height-y,outline="#0ECB81", fill="#0ECB81")) # зеленая
                # self.print_canvas_arr.append(cv.Rect(self.x0, self.height_graph-self.y0, self.x, self.height_graph-self.y,fill_green))
                self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.Rect(0, 0, self.NewRange1, self.y0-self.y)],self.x, self.y)],paint=fill_green))
            # self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.Rect(self.x0, self.y0, self.x, self.y)],0, 0)],paint=fill_green))
            # self.y0 = self.y
            # self.x0 = self.x
                # self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.Rect(self.x0, self.height_graph - self.y0, self.x, self.height_graph - self.y)],0, 0)],paint=fill_green))
            else:
                self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.Rect(0, 0, self.NewRange1, self.y0-self.y)],self.x, self.y)],paint=fill_red))
                # self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.Rect(0, self.y0, self.NewRange1, self.y)],self.x, 0)],paint=fill_red))
            #     print(f'красн | x0={self.x0} | y0={self.y0} | x={self.x} | y={self.y}')
            #     self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.Rect(0, self.height_graph - self.y0, self.x, self.height_graph - self.y)],0, 0)],paint=fill_red))
                # self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.Rect(self.x0, self.height_graph - self.y0, self.x, self.height_graph - self.y)],0, 0)],paint=fill_red))
                # self.print_canvas_arr.append(cv.Rect(self.x0, self.height_graph-self.y0, self.x, self.height_graph-self.y,fill_red))
            self.y0 = self.y
            self.x0 = self.x
                
        # self.print_canvas_arr.append(cv.Line(0,0,50,50, stroke_paint))
        # self.print_canvas_arr.append(cv.Rect(50,50,100,100))
        # self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.Rect(0,0,50,50)],50,50,)],paint=fill_green))
        
        
        self.graph_profit = cv.Canvas(self.print_canvas_arr,width=self.width_graph,height=self.height_graph,content=ft.GestureDetector(
            on_pan_start=self.pan_start,
            # on_pan_update=pan_update,
            drag_interval=10,
        ))
            
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
                    self.graph_profit,
                    # width=405,
                    # height=200,
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