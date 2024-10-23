
import flet as ft
from variable import *
from imports import *

class Graph_dohod(ft.UserControl):
    def __init__(self,number_folder):
        super().__init__()
        self.number_folder = number_folder
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
        self.width_graph = 400
        self.height_graph = 200
        self.print_canvas_arr = []
    
    def pan_start(self,e: ft.DragStartEvent):
        self.line_price.y1 = e.local_y
        self.line_price.y2 = e.local_y
        self.line_price_rect.elements[0].elements[0].y = e.local_y-10
        self.price_value_line.y = e.local_y-8
        text_price = (((self.height_graph - e.local_y)*self.OldRange)/self.NewRange)+self.price_min
        self.price_value_line.text = int(round(text_price,0))
        self.update()

    def print_page(self):
        
        # штука ниже вытаскивает из файла с трейдом все данные и делает статистику
        self.path_save_trade_log = f'{path_save_trade}\\{self.number_folder}\\trade.txt' # путь сохранения логов в папке трейда
        if os.path.isfile(self.path_save_trade_log):
            with open(self.path_save_trade_log) as file:
                self.array_data_row = [row.strip() for row in file]
        for trade_once in self.array_data_row:
            self.depo_start = float(trade_once.split('|')[1])
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
            
        self.trade_balance_procent = round(((depo-self.depo_start)/self.depo_start)*100,2)
        self.price_max = max(self.depo_max_min_stat_arr) # максимальное депо
        if self.price_max<self.depo_start:self.price_max = self.depo_start
        
        for i in self.depo_max_min_stat_arr:
            if i>self.depo_start:
                self.price_min = self.depo_start
            else: 
                self.price_min = min(self.depo_max_min_stat_arr) # минимальное депо
                break
        
        # print(f'min = {self.price_min} | max = {self.price_max}')
        # рисуем график
        self.OldRange = (self.price_max - self.price_min) # старая высота = 39,78
        self.NewRange = self.height_graph # новая высота = 200
        self.x0 = 30
        self.NewRange1 = ((self.width_graph-self.x0)/(len(self.array_data_row))) # новая ширина = 36,81
        self.y0 = self.height_graph - (((self.depo_start - self.price_min) * self.NewRange) / self.OldRange)
        
        # стили для фигур
        line_depo_start = ft.Paint(stroke_width=2, style=ft.PaintingStyle.STROKE,color=c_gray_binance)
        fill_rect_price = ft.Paint(style=ft.PaintingStyle.FILL,color=c_gray_binance)
        fill_green = ft.Paint(style=ft.PaintingStyle.FILL,color=c_green_binance)
        fill_red = ft.Paint(style=ft.PaintingStyle.FILL,color=c_red_binance)
        fill_blue = ft.Paint(style=ft.PaintingStyle.FILL,color=c_blue)
        
        # добавляем элементы легенды для цены
        self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.Rect(0, 0, 30, 200)],0, 0)],paint=fill_blue))
        self.print_canvas_arr.append(cv.Line(0,self.y0,self.width_graph,self.y0, line_depo_start))
        
        # линия прайса
        self.line_price = cv.Line(0,0,self.width_graph,0, line_depo_start)
        # прямоугольник прайса
        self.line_price_rect = cv.Path([cv.Path.SubPath([cv.Path.Rect(0, 0, 30, 20)],0, 0)],paint=fill_rect_price)
        # прайс
        self.price_value_line = cv.Text(5,5,'111',ft.TextStyle(size=12,color='#b6b8b1'))
        
        if int(self.OldRange/5)!=0:
        # рисуем цену
            step_price_arr = []
            for i in range(int(self.price_min),int(self.price_max),int(self.OldRange/5)):
                step_price_arr.append(i)
            for index in range(len(step_price_arr)):
                y = self.height_graph - (((step_price_arr[index] - self.price_min) * self.NewRange) / self.OldRange) - 10
                self.print_canvas_arr.append(cv.Text(5,y,step_price_arr[index],ft.TextStyle(size=12,color='#b6b8b1')))
            
        self.y0 = self.height_graph - (((self.depo_start - self.price_min) * self.NewRange) / self.OldRange)
        # self.y0 = self.height_graph - (((self.depo_start - self.price_min) * self.NewRange) / self.OldRange)
        
        
        # рисуем свечи доходности
        for index in range(len(self.array_data_row)):
            self.value = float(self.array_data_row[index].split('|')[2])
            self.x = ((index) * self.NewRange1)
            self.y = self.height_graph - (((self.value - self.price_min) * self.NewRange) / self.OldRange)
            if float(self.array_data_row[index].split('|')[3])>=0:
                self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.Rect(self.x0, 0, self.NewRange1, self.y0-self.y)],self.x, self.y)],paint=fill_green))
            else:
                self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.Rect(self.x0, 0, self.NewRange1, self.y0-self.y)],self.x, self.y)],paint=fill_red))
            # print(f' x {self.x} | y {self.y} | y0 {self.y0} ||| self.y0-self.y = {self.y0-self.y}')
            self.y0 = self.y   
        # # рисуем свечи доходности
        # for index in range(len(self.array_data_row)):
        #     self.value = float(self.array_data_row[index].split('|')[2])
        #     self.x = ((index) * self.NewRange1)
        #     self.y = self.height_graph - (((self.value - self.price_min) * self.NewRange) / self.OldRange)
        #     if float(self.array_data_row[index].split('|')[3])>=0:
        #         self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.Rect(self.x0, 0, self.NewRange1, self.y0-self.y)],self.x, self.y)],paint=fill_green))
        #     else:
        #         self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.Rect(self.x0, 0, self.NewRange1, self.y0-self.y)],self.x, self.y)],paint=fill_red))
        #     self.y0 = self.y   
        
        self.graph_profit = cv.Canvas(self.print_canvas_arr,width=self.width_graph,height=self.height_graph,content=ft.GestureDetector(
            # on_pan_start=self.pan_start,
            on_hover=self.pan_start,
            drag_interval=10,
        ))
        
        self.print_canvas_arr.append(self.line_price)
        self.print_canvas_arr.append(self.line_price_rect)
        self.print_canvas_arr.append(self.price_value_line)
            
        self.trade_page = ft.Container(
            ft.Container(ft.Column(controls=[
                # для канваса
                ft.Container(
                    self.graph_profit,
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