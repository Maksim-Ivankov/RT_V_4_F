
import flet as ft
from variable import *
from imports import *

class Stistica_our_period(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu


    def build(self):
        
        self.stistica_our_period = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(ft.Text('Статистика за весь период',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white),
                    )),
                    ft.Container(
                        ft.Column(controls=[
                            ft.Container(ft.Row(controls=[
                                ft.Container(ft.Text('Доход',color=c_white,size=12,text_align='center'),width=49),
                                ft.Container(ft.Text('Лонг',color=c_white,size=12,text_align='center'),width=49),
                                ft.Container(ft.Text('Шорт',color=c_white,size=12,text_align='center'),width=49),
                                ft.Container(ft.Text('Дней торговли',color=c_white,size=12,text_align='center'),width=90),
                            ]),margin=ft.margin.only(top=-5,bottom=-5)
                            ),
                            ft.Container(height=1,bgcolor=c_yelow),
                            ft.Container(ft.Row(controls=[
                                ft.Container(ft.Text('+4168$\n+218.17%',color=c_yelow,size=10,text_align='center'),width=50),
                                ft.Container(ft.Text('+2168$\n+118.17%',color=c_yelow,size=10,text_align='center'),width=50),
                                ft.Container(ft.Text('+168$\n+15.17%',color=c_yelow,size=10,text_align='center'),width=50),
                                ft.Container(ft.Text('28',color=c_yelow,size=10,text_align='center'),width=90),
                            ]),margin=ft.margin.only(top=-5,bottom=-5)
                            ),
                            ft.Container(ft.Row(controls=[
                                ft.Container(ft.Text('Сделок',color=c_white,size=12,text_align='center'),width=42),
                                ft.Container(ft.Text('Комиссия',color=c_white,size=12,text_align='center'),width=60),
                                ft.Container(ft.Text('В плюс',color=c_white,size=12,text_align='center'),width=45),
                                ft.Container(ft.Text('В минус',color=c_white,size=12,text_align='center'),width=90),
                            ]),margin=ft.margin.only(top=2,bottom=-5)
                            ),
                            ft.Container(height=1,bgcolor=c_yelow),
                            ft.Container(ft.Row(controls=[
                                ft.Container(ft.Text('186',color=c_yelow,size=10,text_align='center'),width=50),
                                ft.Container(ft.Text('578$',color=c_yelow,size=10,text_align='center'),width=50),
                                ft.Container(ft.Text('+7852$\n152',color=c_yelow,size=10,text_align='center'),width=50),
                                ft.Container(ft.Text('-2548$\n34',color=c_yelow,size=10,text_align='center'),width=90),
                            ]),margin=ft.margin.only(top=-5,bottom=-5)
                            ),
                        ]),
                        width=290,
                        height=133,
                        border = ft.border.all(1, c_white),
                        padding=10,
                    ), 
                ]
            )
        )
        
        return self.stistica_our_period