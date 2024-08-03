
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_coin.component_table import Component_table

class Component_change_strategy_coin(ft.UserControl):
    def __init__(self,close_modal,coin_save):
        super().__init__()
        self.close_modal = close_modal
        self.coin_save = coin_save
        self.strategy_coin_list = {
            'top_dvigeniya':'Топ движения за день до текущего',
            'top_value':'Топ объёма за день до текущего',
            'change_list':'Выбрать из списка'
        }

        self.flags_this = {
            'top_dvigeniya':False,
            'top_value':False,
            'change_list':False
        }

        self.top_dvigeniya = ft.Ref[ft.CupertinoCheckbox]()
        self.top_value = ft.Ref[ft.CupertinoCheckbox]()
        self.change_list = ft.Ref[ft.CupertinoCheckbox]()

        self.refs_this = {
            'top_dvigeniya':self.top_dvigeniya,
            'top_value':self.top_value,
            'change_list':self.change_list
        }
        

    # выбор чекбокса
    def checed_var(self,e):
        self.change_coin = e.control.content.controls[1].content.data # выбранный сейчас тип монеты
        if self.flags_this[e.control.content.controls[1].content.data] == False: # если сейчас 0
            e.control.content.controls[0].value=True # сделай чекбокс 1
            self.flags_this[e.control.content.controls[1].content.data] = True # измени флаг на 1
            for i in self.flags_this.keys(): 
                if i != e.control.content.controls[1].content.data: # если текущий ключ не равен выбранному
                    self.refs_this[i].current.value=False # тушим чекбокс в ноль
                    self.flags_this[i] = False # меняем флаг на ноль
                else:
                    self.refs_this[i].current.value=True
                    self.flags_this[i] = True
        else:
            e.control.content.controls[0].value=False
            self.flags_this[e.control.content.controls[1].content.data] = False
        self.update()
        data_save = {
            'strategi_coin':self.change_coin
        }
        Save_config('param_trade_historical_trade_svobodniy_freym',data_save)
        

    # кнопка продолжить нажатие
    def save_change_type_coin(self,e):
        if self.change_coin != 'change_list':
            self.close_modal()
            self.coin_save()
        else: 
            self.controls = []
            self.controls.append(Component_table(self.close_modal,self.coin_save))
            self.update()
        

    def build(self):

        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        if ('param_trade_historical_trade_svobodniy_freym') in config.sections():
            self.change_coin = config.get('param_trade_historical_trade_svobodniy_freym', 'strategi_coin')
            self.flags_this[self.change_coin] = True
        else:
            self.change_coin = 'top_dvigeniya'
            self.flags_this['top_dvigeniya'] = True


        item_strategy = []
        for i in self.strategy_coin_list.keys():
            if i == self.change_coin:
                item_strategy.append(
                    ft.Container(ft.Row(
                        controls=[
                            ft.CupertinoCheckbox(value=self.flags_this[i],check_color=c_blue,active_color=c_yelow,inactive_color=c_white,ref=self.refs_this[i]),
                            ft.Container(ft.Text(self.strategy_coin_list[i],color=c_white,data=i),margin = ft.margin.only(left=-15))
                        ]),on_click=self.checed_var,padding=0,margin=ft.margin.only(bottom=-10)))
            else:
                item_strategy.append(
                    ft.Container(ft.Row(
                        controls=[
                            ft.CupertinoCheckbox(value=self.flags_this[i],check_color=c_blue,active_color=c_yelow,inactive_color=c_white,ref=self.refs_this[i]),
                            ft.Container(ft.Text(self.strategy_coin_list[i],color=c_white,data=i),margin = ft.margin.only(left=-15))
                        ]),on_click=self.checed_var,padding=0,margin=ft.margin.only(bottom=-10)))
                
        self.component_change_strategy_coin = ft.Container(
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
                                margin=ft.margin.only(left=15,bottom=-65)
                            ), 
                            ft.Container(ft.ElevatedButton(content = ft.Text('Продолжить',size=12,text_align='center'),on_click=self.save_change_type_coin,data='Свободный фрейм',bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7),
                        ]
                        )
                    ])),
                    width=444,
                    height=320,
                    bgcolor=c_blue,
                    border=ft.border.all(1,c_white),
                    # margin=ft.margin.only(bottom=500,)
                    margin=ft.margin.only(bottom=180,top=-100)
                    )
        
        return self.component_change_strategy_coin


