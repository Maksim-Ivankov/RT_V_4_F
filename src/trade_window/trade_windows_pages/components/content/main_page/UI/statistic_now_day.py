
import flet as ft
from variable import *
from imports import *

class Statistic_now_day(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu


    def build(self):
        
        self.statistic_now_day = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(ft.Text('Статистика за сегодня',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white),
                    )),
                    ft.Container(
                        ft.Column(controls=[
                            ft.Container(ft.Row(controls=[
                                ft.Container(ft.Text('Доход',color=c_white,size=12,text_align='center'),width=49),
                                ft.Container(ft.Text('Лонг',color=c_white,size=12,text_align='center'),width=49),
                                ft.Container(ft.Text('Шорт',color=c_white,size=12,text_align='center'),width=49),
                                ft.Container(ft.Text('Смотреть\nпо дням',text_align='center',color=c_blue,size=11),bgcolor=c_yelow,width=70,height=40,margin=ft.margin.only(bottom=-45,left=10),padding=ft.padding.only(top=5))
                                
                            ]),margin=ft.margin.only(top=-5,bottom=-5)
                            ),
                            ft.Container(height=1,bgcolor=c_yelow,width=170),
                            ft.Container(ft.Row(controls=[
                                ft.Container(ft.Text('+126$\n+17%',color=c_yelow,size=10,text_align='center'),width=50),
                                ft.Container(ft.Text('+101$\n+15%',color=c_yelow,size=10,text_align='center'),width=50),
                                ft.Container(ft.Text('+25$\n+3.18%',color=c_yelow,size=10,text_align='center'),width=50),
                                
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
                                ft.Container(ft.Text('12',color=c_yelow,size=10,text_align='center'),width=50),
                                ft.Container(ft.Text('43$',color=c_yelow,size=10,text_align='center'),width=50),
                                ft.Container(ft.Text('+138$\n8',color=c_yelow,size=10,text_align='center'),width=50),
                                ft.Container(ft.Text('-54$\n4',color=c_yelow,size=10,text_align='center'),width=90),
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
        
        return self.statistic_now_day