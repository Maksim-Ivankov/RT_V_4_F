import flet as ft
from variable import *
from imports import *

class Print_graph(ft.UserControl):
    def __init__(self,set):
        super().__init__()
        self.set = set
        self.height_canvas = self.set['width_graph']
        self.width_canvas = self.set['height_graph']
        self.df = pd.read_csv(self.set['path_df'])
        self.VOLUME = len(self.df)
        # self.step_input = self.set['step_input']
        self.trend = self.set['trend']
        self.TP = self.set['TP']
        self.SL = self.set['SL']
        
        self.width_telo = 2 # Ширина тела свечи
        self.width_spile = 1 # Ширина хвоста, шпиля
        
        self.flag_move_to = 0 # флаг - было ли перемещение по графику мышкой
        
        self.print_canvas_arr = [] #сюда сохраняем все, что нужно отрисовать в канвасе

    def pan_start(self,e: ft.DragStartEvent):
        # self.canvas.scan_dragto(event.x, event.y, gain=1)
        # self.canvas_price.scan_dragto(0, event.y, gain=1)
        # self.canvas_date.scan_dragto(event.x, 0, gain=1)
        # self.canvas_volume.scan_dragto(event.x, 60, gain=1)
        # print(f'x = {e.local_x} | y = {e.local_y}')
        # print(e.local_x)
        # self.graph_trade.animate_position(e.local_x)
        # if self.flag_move_to == 0:
        #     self.drag_To_y0 = e.local_y
        #     self.flag_move_to = 1
            
        # self.drag_To_y = e.local_y
        # self.graph_trade.offset = (self.drag_To_y-self.drag_To_y0)
        # # self.drag_To_y0 = self.drag_To_y
        # self.graph_trade.scale
        # print(self.graph_trade.shapes)
        # pass
        # self.line_price.y1 = e.local_y
        # self.line_price.y2 = e.local_y
        # self.update()
        pass
        
    
    # рисуем бары свечей
    def paint_bar(self):
        # определяем границы для масштабирования графика цены
        self.price_max = (self.df.loc[self.df['close'] == self.df['close'].max()].iloc[0]['close'])
        self.price_min = (self.df.loc[self.df['close'] == self.df['close'].min()].iloc[0]['close'])
        self.OldRange = (self.price_max - self.price_min) 
        self.OldRange1 = len(self.df)
        self.NewRange1 = self.set['width_graph']/(len(self.df)/self.OldRange1)  # МАГИЧЕСКОЕ ЧИСЛО - 144 ЧТО ЭТО?
        # определяем границы для масштабирования графика объёмов
        price_max_volume = (self.df.loc[self.df['VOLUME'] == self.df['VOLUME'].max()].iloc[0]['VOLUME'])
        price_min_volume = (self.df.loc[self.df['VOLUME'] == self.df['VOLUME'].min()].iloc[0]['VOLUME'])
        OldRange_volume = (price_max_volume - price_min_volume) 
        NewRange_volume = 110                                           # МАГИЧЕСКОЕ ЧИСЛО - 110 ЧТО ЭТО?
        
        # self.mass_date_interval_graph = {}
        self.mass_date_line = []
        
        for i in range(0,3000,20):
            self.mass_date_line.append(((i * self.NewRange1) / self.OldRange1))
        for index, row in self.df.iterrows():
            x0 = ((index * self.NewRange1) / self.OldRange1)*0.95
            # self.mass_date_interval_graph[(x0,x0)] = datetime.fromtimestamp(int(row['open_time']/1000)).strftime('%d.%m.%Y %H:%M')
            y0 = self.set['width_graph']*0.7 - (((row['open'] - self.price_min) * self.set['height_graph']*0.7) / self.OldRange)
            y1 = self.set['width_graph']*0.7 - (((row['close'] - self.price_min) * self.set['height_graph']*0.7) / self.OldRange)
            high = self.set['width_graph']*0.7 - (((row['high'] - self.price_min) * self.set['height_graph']*0.7) / self.OldRange)
            low = self.set['width_graph']*0.7 - (((row['low'] - self.price_min) * self.set['height_graph']*0.7) / self.OldRange)
            if index == int(self.set['index_entry']):
                self.print_trade_point('entry',x0,y1)
            if index == int(self.set['index_exit']):
                self.print_trade_point('exit',x0,y1)
            self.paint_candle(x0,y0,y1,high,low)
            VOLUME_y =(((row['VOLUME'] - price_min_volume) * NewRange_volume) / OldRange_volume)*0.8
            self.paint_one_volume(x0,y0,y1,VOLUME_y)
        
            
        # рисуем одну свечу    
    def paint_candle(self,x0,y0,y1,high,low):
        if y0>=y1:
            self.print_canvas_arr.append(cv.Line(x0,high,x0,y0, self.line_green))
            self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.Rect(0, 0,self.width_telo, y1-y0)],x0, y0)],paint=self.fill_green))
            self.print_canvas_arr.append(cv.Line(x0,low,x0,y0, self.line_green))
        if y0<y1:
            self.print_canvas_arr.append(cv.Line(x0,high,x0,y0, self.line_red))
            self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.Rect(0, 0,self.width_telo, y1-y0)],x0, y0)],paint=self.fill_red))
            self.print_canvas_arr.append(cv.Line(x0,low,x0,y0, self.line_red))

    # рисуем один объём
    def paint_one_volume(self,x0,y0,y1,VOLUME_y):
        if y0>=y1: # красный
            self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.Rect(0, 0,self.width_telo, -VOLUME_y)],x0, self.set['height_graph']-14)],paint=self.fill_green))
        if y0<y1: # зеленый
            self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.Rect(0, 0,self.width_telo, -VOLUME_y)],x0, self.set['height_graph']-14)],paint=self.fill_red))
            
    def print_trade_point(self,point,x0,y1):
        # print('Рисуем треугольник')
        # if point == 'entry':
        #     if self.set['trend'] == 'long':
        #         self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.MoveTo(x0+10,y1+5),cv.Path.LineTo(x0+20,y1+20),cv.Path.LineTo(x0+0,y1+20),cv.Path.LineTo(x0+10,y1+5),],0, 0)],paint=self.fill_green))
        #     elif self.set['trend'] == 'short':
        #         self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.MoveTo(x0,y1),cv.Path.LineTo(x0-10,y1-10),cv.Path.LineTo(x0+10,y1-10),cv.Path.LineTo(x0,y1),],0, 0)],paint=self.fill_red))
        # if point == 'exit':
        #     if self.set['trend'] == 'long':
        #         self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.MoveTo(x0,y1),cv.Path.LineTo(x0+10,y1+10),cv.Path.LineTo(x0-10,y1+10),cv.Path.LineTo(x0,y1),],0, 0)],paint=self.fill_green))
        #     elif self.set['trend'] == 'short':
        #         self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.MoveTo(x0,y1),cv.Path.LineTo(x0-10,y1-10),cv.Path.LineTo(x0+10,y1-10),cv.Path.LineTo(x0,y1),],0, 0)],paint=self.fill_red))
        
        if self.set['trend'] == 'long':
            if point == 'entry': self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.MoveTo(x0,y1),cv.Path.LineTo(x0+10,y1+10),cv.Path.LineTo(x0-10,y1+10),cv.Path.LineTo(x0,y1),],0, 0)],paint=self.fill_green))
            if point == 'exit':self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.MoveTo(x0,y1),cv.Path.LineTo(x0-10,y1-10),cv.Path.LineTo(x0+10,y1-10),cv.Path.LineTo(x0,y1),],0, 0)],paint=self.fill_red))
        elif self.set['trend'] == 'short':
            if point == 'entry': self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.MoveTo(x0,y1),cv.Path.LineTo(x0-10,y1-10),cv.Path.LineTo(x0+10,y1-10),cv.Path.LineTo(x0,y1),],0, 0)],paint=self.fill_red))
            if point == 'exit': self.print_canvas_arr.append(cv.Path([cv.Path.SubPath([cv.Path.MoveTo(x0,y1),cv.Path.LineTo(x0+10,y1+10),cv.Path.LineTo(x0-10,y1+10),cv.Path.LineTo(x0,y1),],0, 0)],paint=self.fill_green))
            


    def print_page(self):
        
        # стили для фигур
        self.line_green = ft.Paint(stroke_width=self.width_spile, style=ft.PaintingStyle.STROKE,color=c_green_binance)
        self.line_red = ft.Paint(stroke_width=self.width_spile, style=ft.PaintingStyle.STROKE,color=c_red_binance)
        self.line_depo_red = ft.Paint(stroke_width=self.width_spile, style=ft.PaintingStyle.STROKE,color=c_red_binance)
        self.fill_rect_price = ft.Paint(style=ft.PaintingStyle.FILL,color=c_gray_binance)
        self.fill_green = ft.Paint(style=ft.PaintingStyle.FILL,color=c_green_binance)
        self.fill_red = ft.Paint(style=ft.PaintingStyle.FILL,color=c_red_binance)
        self.fill_blue = ft.Paint(style=ft.PaintingStyle.FILL,color=c_blue)
        line_price_paint = ft.Paint(stroke_width=2, style=ft.PaintingStyle.STROKE,color=c_gray_binance)
        
        self.paint_bar()
        
        # # линия прайса
        # self.line_price = cv.Line(0,0,self.set['width_graph'],0, line_price_paint)
        # self.print_canvas_arr.append(self.line_price)
          
        self.graph_trade = cv.Canvas(self.print_canvas_arr,content=ft.GestureDetector(
            # on_pan_start=self.pan_start,
            # on_hover=self.pan_start,
            on_hover = self.pan_start,
            drag_interval=10,
        ))
           
        return self.graph_trade

   
    def build(self):
        return self.print_page()