
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.UI.input import Input
from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config

class Component_tp(ft.UserControl):
    def __init__(self,collback):
        super().__init__()
        # self.btn_click = 'fiks'
        self.btn_translate = {
            'fiks':'Фиксированный',
            'dinamo':'Динамический',
        }
        self.btn_mas = ['fiks','dinamo']
        self.collback = collback

    # выбираем фикс или динамик
    def chech_fiks_dinamo(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'set_general_regim_tp':e.control.data})
        print(e.control.data)
        self.btn_click = e.control.data
        self.controls = []
        self.controls.append(self.print_component())
        self.update()

    def print_component(self):

        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.btn_click = config.get('param_trade_historical_trade_svobodniy_freym', 'set_general_regim_tp')

        min_menu = []
        for i in self.btn_mas:
            if i == self.btn_click:
                min_menu.append(ft.Container(ft.Text(self.btn_translate[i],color=c_yelow,),padding=5,margin=ft.margin.only(bottom=-10),data=i,on_click=self.chech_fiks_dinamo))
            else: 
                min_menu.append(ft.Container(ft.Text(self.btn_translate[i],color=c_white,),padding=5,margin=ft.margin.only(bottom=-10),data=i,on_click=self.chech_fiks_dinamo))
        if self.btn_click == 'fiks':
            self.text_info = 'Процент от движения цены, %'
            self.input_celka_text = '0.7,0.9,1.2,1.5,2,4'
        elif self.btn_click == 'dinamo':
            self.text_info = 'Процент от движения монеты за день, %'
            self.input_celka_text = '0.005,0.007,0.009,0.012'

        self.component_tp = ft.Column(
            controls=[
                ft.Container(ft.Container(ft.Text('Тейк профит',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white)),),
                ft.Container(
                    ft.Column(
                        controls=[
                           ft.Container(ft.Row(controls=min_menu),margin=ft.margin.only(left=80)),
                           ft.Container(ft.Text(self.text_info,color=c_white,size=12,text_align='center'),width=376,margin=ft.margin.only(top=10,bottom=3)),
                           ft.Container(Input(self.collback,self.input_celka_text,330),margin=ft.margin.only(left=22)),
                        ]
                    ),
                    width=376,
                    height=120,
                    border = ft.border.all(1, c_white),
                    padding=ft.padding.only(top=5)
            )])
        
        return self.component_tp

    def build(self):
        return self.print_component()