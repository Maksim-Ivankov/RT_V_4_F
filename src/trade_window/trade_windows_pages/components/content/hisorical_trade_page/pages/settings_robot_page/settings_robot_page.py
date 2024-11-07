
import flet as ft
from variable import *
from imports import *


from src.trade_window.trade_windows_pages.components.content.UI.input import Input
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.settings_robot_page.UI.component_tp import Component_tp
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.settings_robot_page.UI.component_sl import Component_sl
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.settings_robot_page.UI.component_volume_min import Component_volume_min
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.settings_robot_page.UI.component_volume_max import Component_volume_max
from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config

class Settings_robot_page(ft.UserControl):
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page

    def input_name_bot(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'name_bot':str(e.control.value)})
    def input_komission_mayker(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'komission_mayker':str(e.control.value)})
    def input_komission_taker(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'komission_taker':str(e.control.value)})
    def input_deposit(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'deposit':str(e.control.value)})
    def input_leverage(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'leverage':str(e.control.value)})
    def input_tp(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'tp':str(e.control.value)})
    def input_sl(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'sl':str(e.control.value)})
    def input_volume_min(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'volume_min':str(e.control.value)})
    def input_volume_max(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'volume_max':str(e.control.value)})
    def input_time_on_work(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'time_on_work':str(e.control.value)})
    def input_time_off_work(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'time_off_work':str(e.control.value)})


    def change_time_settings(self,e):
        # print(e.control.content.controls[0].value)
        config = configparser.ConfigParser()  
        config.read(path_imports_config)
        self.change_time_settings_get = int(config.get('param_trade_historical_trade_svobodniy_freym', 'change_time_settings'))
        if e.control.data=='надпись':
            if self.change_time_settings_get==0:
                e.control.content.controls[0].value = True
                Save_config('param_trade_historical_trade_svobodniy_freym',{'change_time_settings':'1'})
            elif self.change_time_settings_get==1:
                e.control.content.controls[0].value = False
                Save_config('param_trade_historical_trade_svobodniy_freym',{'change_time_settings':'0'})
        elif e.control.data=='чекбокс':
            if self.change_time_settings_get==0:
                # e.control.content.controls[0].value = True
                Save_config('param_trade_historical_trade_svobodniy_freym',{'change_time_settings':'1'})
            elif self.change_time_settings_get==1:
                # e.control.content.controls[0].value = False
                Save_config('param_trade_historical_trade_svobodniy_freym',{'change_time_settings':'0'})
        self.update()

    def build(self):


        config = configparser.ConfigParser()  
        config.read(path_imports_config)
        name_robot_log = config.get('param_trade_historical_trade_svobodniy_freym', 'name_bot')
        komis_mayk_log = config.get('param_trade_historical_trade_svobodniy_freym', 'komission_mayker')
        komis_teyk_log = config.get('param_trade_historical_trade_svobodniy_freym', 'komission_taker')
        depo_log = config.get('param_trade_historical_trade_svobodniy_freym', 'deposit')
        leverage_log = config.get('param_trade_historical_trade_svobodniy_freym', 'leverage')
        time_on_work = config.get('param_trade_historical_trade_svobodniy_freym', 'time_on_work')
        time_off_work = config.get('param_trade_historical_trade_svobodniy_freym', 'time_off_work')
        self.change_time_settings_get = int(config.get('param_trade_historical_trade_svobodniy_freym', 'change_time_settings'))
        if self.change_time_settings_get==0:self.change_time_settings_param = False
        elif self.change_time_settings_get==1:self.change_time_settings_param = True


        self.settings_robot = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text('Настройте робота для торговли на свободном фрейме',
                                        size=12,color=c_white,text_align='center',),padding=ft.padding.only(left=120)),
                                ft.Container(
                                    ft.Container(
                                        ft.Column(controls=[
                                            ft.Column(
                                                controls=[
                                                    ft.Container(
                                                        ft.Container(ft.Text('Настройки робота',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                    ft.Container(
                                                        ft.Row(
                                                            controls=[
                                                                ft.Column(controls=[
                                                                    ft.Container(ft.Text('Имя робота для логов',size=12,text_align='center'),width=170,padding=0),
                                                                    ft.Container(Input(self.input_name_bot,name_robot_log,170)),
                                                                    ft.Container(ft.Text('Комиссия мейкер, %',size=12,text_align='center'),width=170),
                                                                    Input(self.input_komission_mayker,komis_mayk_log,170)
                                                                ]),
                                                                ft.Column(controls=[
                                                                    ft.Container(ft.Text('Депозит,$',size=12,text_align='center'),width=170,padding=0),
                                                                    ft.Container(Input(self.input_deposit,depo_log,170)),
                                                                    ft.Container(ft.Text('Комиссия тейкер, %',size=12,text_align='center'),width=170),
                                                                    Input(self.input_komission_taker,komis_teyk_log,170)
                                                                ]),
                                                                ft.Container(ft.Column(controls=[
                                                                    ft.Container(ft.Text('Плечо',size=12,text_align='center'),width=170,padding=0),
                                                                    ft.Container(Input(self.input_leverage,leverage_log,170)),
                                                                    
                                                                ]),margin=ft.margin.only(bottom=66)),
                                                            ]
                                                        ),
                                                        width=560,
                                                        border = ft.border.all(1, c_white),
                                                        padding=14
                                            )]),
                                            ft.Row(controls=[
                                                Component_tp(self.input_tp),
                                                Component_sl(self.input_sl)
                                            ]),
                                            ft.Row(controls=[
                                                Component_volume_min(self.input_volume_min),
                                                Component_volume_max(self.input_volume_max)
                                            ]),
                                            ft.Column(
                                                controls=[
                                                    ft.Container(
                                                        ft.Container(ft.Text('Время смещения',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                    ft.Container(
                                                        ft.Column(controls=[
                                                            ft.Container(ft.Row(controls=[
                                                                ft.CupertinoCheckbox(value=self.change_time_settings_param,check_color=c_blue,active_color=c_yelow,inactive_color=c_white,data='чекбокс',on_change=self.change_time_settings),
                                                                ft.Container(ft.Text('Включить настройку времени смещения торговли',color=c_white),margin = ft.margin.only(left=-15))
                                                            ]),margin=ft.margin.only(left=80),width=380,data='надпись',on_click=self.change_time_settings),
                                                            ft.Container(ft.Row(controls=[
                                                                ft.Container(ft.Column(controls=[
                                                                        ft.Container(ft.Text('Время включения торговли, час',size=12,text_align='center'),width=260,padding=0),
                                                                        ft.Container(Input(self.input_time_on_work,time_on_work,170),margin=ft.margin.only(left=46)),
                                                                    ])),
                                                                ft.Container(ft.Column(controls=[
                                                                        ft.Container(ft.Text('Время остановки торговли, час',size=12,text_align='center'),width=260,padding=0),
                                                                        ft.Container(Input(self.input_time_off_work,time_off_work,170),margin=ft.margin.only(left=46)),
                                                                    ])),
                                                            ]))
                                                            ]),
                                                        width=560,
                                                        border = ft.border.all(1, c_white),
                                                        padding=14
                                            )]),
                                                
                                    ],scroll=ft.ScrollMode.ALWAYS)),
                                    width=560,height=520,padding=ft.padding.only(right=-18)
                                ),
                                ft.Container(
                                    ft.Container(
                                        ft.Row(controls=[
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Назад',size=12,),data='Свободный фрейм',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Выбрать стратегию торговли',size=12,),data='Выбрать стратегию торговли',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                    ]),padding=ft.padding.only(left=130,top=10)
                                    ),
                                    width=560,
                                    # height=100
                                )
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.settings_robot