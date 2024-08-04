
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_strategy_trade_page.UI.component_info_strat import Component_info_strat
from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config

class Change_strategy_trade_page(ft.UserControl):
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page
        self.strategy_translate = {
            'one':'Канал, тренд, локаль, объём',
            'MA':'Скользящие средние'
        }
        self.flags_this = {
            'one':False,
            'MA':False,
        }
        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        for i in literal_eval(config.get('param_trade_historical_trade_svobodniy_freym', 'strategys')):
            self.flags_this[i] = True
        self.ref_one = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_MA = ft.Ref[ft.CupertinoCheckbox]()
        self.refs_this = {
            'one':self.ref_one,
            'MA':self.ref_MA,
        }

    # выбор чекбокса
    def checed_var(self,e):
        self.change_coin = e.control.content.controls[1].content.data # выбранная стратегия1
        if self.flags_this[e.control.content.controls[1].content.data] == False: # если сейчас 0
           e.control.content.controls[0].value=True # сделай чекбокс 1
           self.flags_this[e.control.content.controls[1].content.data] = True
        else: 
            e.control.content.controls[0].value=False # сделай чекбокс 1
            self.flags_this[e.control.content.controls[1].content.data] = False
        self.update()
        self.changed_strategys = []
        for i in self.flags_this.keys():
            if self.flags_this[i] == True:
                self.changed_strategys.append(i)
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strategys':str(self.changed_strategys)})
        self.print_info_strategy.update_component()


    def build(self):
        item_strategy = []
        for i in self.strategy_translate.keys():
            item_strategy.append(
                ft.Container(ft.Row(
                    controls=[
                        ft.CupertinoCheckbox(data=i,value=self.flags_this[i],check_color=c_blue,active_color=c_yelow,inactive_color=c_white,ref=self.refs_this[i]),
                        ft.Container(ft.Text(self.strategy_translate[i],color=c_white,data=i),margin = ft.margin.only(left=-15))
                    ]),on_click=self.checed_var,padding=ft.padding.only(bottom=-10,top=-10),width=300))

        self.print_info_strategy = Component_info_strat()

        self.change_strategy_trade_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text('Выберите одну или несколько стратегий реальной тестовой торговли',
                                        size=12,color=c_white,text_align='center',),padding=ft.padding.only(left=230)),
                                ft.Container(
                                    ft.Container(
                                        ft.Column(controls=[
                                            ft.Column(
                                                controls=[
                                                    ft.Container(
                                                        ft.Container(ft.Text('Выбор стратегии',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                    ft.Container(
                                                        ft.Row(controls=[
                                                            ft.Container(
                                                                ft.Column(controls=item_strategy),
                                                                width=300,
                                                                border = ft.border.all(1, c_white),
                                                                padding=ft.padding.only(left=10,top=20),
                                                            ),
                                                            ft.Container(
                                                                self.print_info_strategy,
                                                                width=560,
                                                                height = 460,
                                                                border = ft.border.all(1, c_white),
                                                                padding=ft.padding.only(left=10,top=20),
                                                                margin=ft.margin.only(left=-11)
                                                            ),
                                                        ]), 
                                                        width=860,
                                                        border = ft.border.all(1, c_white),
                                                        # padding=14,
                                                        height = 460,
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
        
        return self.change_strategy_trade_page