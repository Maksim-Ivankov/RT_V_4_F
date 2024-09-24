
import flet as ft
from variable import *
from imports import *

class Output_info_trade(ft.UserControl):#1
    def __init__(self):
        super().__init__()
        self.pb = ft.ProgressBar(width=900,bgcolor=c_blue,color=c_yelow)

    
    def print_itog_and_graph(self):
        stroke_paint = ft.Paint(stroke_width=2, style=ft.PaintingStyle.STROKE)
        fill_paint = ft.Paint(style=ft.PaintingStyle.FILL)
        self.trade_page_two = ft.Container(ft.Column(controls=[
            ft.Container(ft.Row(controls=[
                    ft.Container(
                                    ft.Container(ft.Column(controls=[ft.Column(controls=[
                                                    ft.Container(
                                                        ft.Container(ft.Text('График доходности',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                        ft.Container(
                                                            ft.Container(
                                                                cv.Canvas(
                                                                    [
                                                                        cv.Circle(100, 100, 50, stroke_paint),
                                                                        cv.Circle(80, 90, 10, stroke_paint),
                                                                        cv.Circle(84, 87, 5, fill_paint),
                                                                        cv.Circle(120, 90, 10, stroke_paint),
                                                                        cv.Circle(124, 87, 5, fill_paint),
                                                                        cv.Arc(70, 95, 60, 40, 0, math.pi, paint=stroke_paint),
                                                                    ],
                                                                    width=float("inf"),
                                                                    expand=True,
                                                                ),
                                                                width=425,
                                                                height=400,
                                                                border = ft.border.all(1, c_white),
                                                                bgcolor=c_blue,
                                                                padding=10,
                                                            ),
                                                            width=425,
                                                            # border = ft.border.all(1, c_white),
                                                            # padding=14,
                                                            height = 400,
                                                            padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                                        )]),])),width=425,),
                                    ft.Container(ft.Container(
                                            ft.Column(controls=[ft.Column(controls=[
                                                        ft.Container(
                                                            ft.Container(ft.Text('График сделки',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                        ft.Container(
                                                            ft.Container(
                                                                ft.Column(scroll=ft.ScrollMode.ALWAYS),
                                                                width=425,
                                                                height=400,
                                                                border = ft.border.all(1, c_white),
                                                                bgcolor=c_blue,
                                                                padding=10,
                                                            ),
                                                            width=425,
                                                            # border = ft.border.all(1, c_white),
                                                            # padding=14,
                                                            height = 400,
                                                            padding=ft.padding.only(left=-1,top=-1,bottom=-1)    
                                                )]),])),width=425,),]),
                width=900,height=450,padding=ft.padding.only(left=20))
        ]),key='itog',width=900)
        return self.trade_page_two
    
    def print_page(self):
            
        self.trade_page = ft.Container(ft.Column(controls=[
            ft.Container(self.pb,margin=ft.margin.only(top=20,bottom=20),key='pb'),
            ft.Container(ft.Row(controls=[
                    ft.Container(
                                    ft.Container(ft.Column(controls=[ft.Column(controls=[
                                                    ft.Container(
                                                        ft.Container(ft.Text('Логи работы',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                        ft.Container(
                                                            ft.Container(
                                                                ft.Column(scroll=ft.ScrollMode.ALWAYS),
                                                                width=425,
                                                                height=400,
                                                                border = ft.border.all(1, c_white),
                                                                bgcolor=c_blue,
                                                                padding=10,
                                                            ),
                                                            width=425,
                                                            # border = ft.border.all(1, c_white),
                                                            # padding=14,
                                                            height = 400,
                                                            padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                                        )]),])),width=425,),
                                    ft.Container(ft.Container(
                                            ft.Column(controls=[ft.Column(controls=[
                                                        ft.Container(
                                                            ft.Container(ft.Text('Сделки',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                        ft.Container(
                                                            ft.Container(
                                                                ft.Column(scroll=ft.ScrollMode.ALWAYS),
                                                                width=425,
                                                                height=400,
                                                                border = ft.border.all(1, c_white),
                                                                bgcolor=c_blue,
                                                                padding=10,
                                                            ),
                                                            width=425,
                                                            # border = ft.border.all(1, c_white),
                                                            # padding=14,
                                                            height = 400,
                                                            padding=ft.padding.only(left=-1,top=-1,bottom=-1)    
                                                )]),])),width=425,),]),
                width=900,height=450,padding=ft.padding.only(left=20))
        ]),width=900)
        return self.trade_page

   
    def build(self):
        return self.print_page()