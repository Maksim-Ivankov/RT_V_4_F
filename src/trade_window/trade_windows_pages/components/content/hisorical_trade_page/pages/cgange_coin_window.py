
import flet as ft
from variable import *
from imports import *

class Cgange_coin_window(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.strategy_coin_list = {
            'top_dvigeniya':'Топ движения за день до текущего',
            'top_value':'Топ объёма за день до текущего',
            'change_list':'Выбрать из списка'
        }
        self.change_coin = 'top_dvigeniya'


    def build(self):

        item_strategy = []
        for i in self.strategy_coin_list.keys():
            if i == self.change_coin:
                item_strategy.append(
                    ft.Row(
                        controls=[
                            ft.CupertinoCheckbox(value=True,check_color=c_blue,active_color=c_yelow,inactive_color=c_white),
                            ft.Container(ft.Text(self.strategy_coin_list[i],color=c_white,),margin = ft.margin.only(left=-15))
                        ]))
            else:
                item_strategy.append(
                    ft.Row(
                        controls=[
                            ft.CupertinoCheckbox(value=False,check_color=c_blue,active_color=c_yelow,inactive_color=c_white),
                            ft.Container(ft.Text(self.strategy_coin_list[i],color=c_white,),margin = ft.margin.only(left=-15))
                        ]))

        self.cgange_coin_window = ft.Container(
            ft.Container(ft.Column(controls=[
                ft.Container(ft.Text('Выбор монет',color=c_blue,size=14,text_align='center'),width=444,height=28,bgcolor=c_yelow,padding=ft.padding.only(top=5)),
                ft.Container(ft.Text('Выберите стратегию сбора монет для исторической торговли',color=c_white,size=12,text_align='center'),width=444),
                ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(ft.Text('Выбор стратегии',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10,left=15,top=10),border=ft.border.all(1,c_white),
                    )),
                    ft.Container(
                        ft.Column(controls=item_strategy),
                        width=407,
                        height=194,
                        border = ft.border.all(1, c_white),
                        padding=10,
                        margin=ft.margin.only(left=15)
                    ), 
                ]
            )
            ])),
            width=444,
            height=320,
            bgcolor=c_blue,
            border=ft.border.all(1,c_white),
            margin=ft.margin.only(bottom=250,top=-200)
        )
        
        return self.cgange_coin_window