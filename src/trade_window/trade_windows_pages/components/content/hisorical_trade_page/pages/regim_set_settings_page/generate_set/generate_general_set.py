# страница выбора стратегии торговли
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.UI.input import Input
from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.UI.component_sl import Component_sl
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.UI.component_tp import Component_tp
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.UI.component_volume_max import Component_volume_max
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.UI.component_volume_min import Component_volume_min

class Generate_general_set(ft.UserControl):
    def __init__(self,btn_close):
        super().__init__()
        self.btn_close = btn_close
        

    def input_start_time(self,e):
        self.start_time = e.control.value
        Save_config('param_trade_historical_trade_svobodniy_freym',{'set_general_input_start_time':str(e.control.value)})
    def input_stop_time(self,e):
        self.stop_time = e.control.value
        Save_config('param_trade_historical_trade_svobodniy_freym',{'set_general_input_stop_time':str(e.control.value)})
    def input_depo(self,e):
        self.depo = e.control.value
        Save_config('param_trade_historical_trade_svobodniy_freym',{'set_general_input_depo':str(e.control.value)})
    def input_leveradg(self,e):
        self.leveradg = e.control.value
        Save_config('param_trade_historical_trade_svobodniy_freym',{'set_general_input_leveradg':str(e.control.value)})
    def input_tp(self,e):
        self.diapazon_tp = e.control.value
        Save_config('param_trade_historical_trade_svobodniy_freym',{'set_general_input_tp':str(e.control.value)})
    def input_sl(self,e):
        self.diapazon_sl = e.control.value
        Save_config('param_trade_historical_trade_svobodniy_freym',{'set_general_input_sl':str(e.control.value)})
    def input_volume_min(self,e):
        self.diapazon_volume_min = e.control.value
        Save_config('param_trade_historical_trade_svobodniy_freym',{'set_general_input_volume_min':str(e.control.value)})
    def input_volume_max(self,e):
        self.diapazon_volume_max = e.control.value
        Save_config('param_trade_historical_trade_svobodniy_freym',{'set_general_input_volume_max':str(e.control.value)})
    def input_how_mach_settings(self,e):
        self.how_mach_settings = e.control.value
        Save_config('param_trade_historical_trade_svobodniy_freym',{'set_general_input_how_mach_settings':str(e.control.value)})

    def btn_generate(self,e):
        os.remove(path_ini_general_set)
        for i in range(1,int(self.how_mach_settings)+1):
            Save_config(i,{'start_time':str(random.choice(self.start_time.split(',')))},path_ini_general_set)
            Save_config(i,{'stop_time':str(random.choice(self.stop_time.split(',')))},path_ini_general_set)
            Save_config(i,{'depo':str(random.choice(self.depo.split(',')))},path_ini_general_set)
            Save_config(i,{'leveradg':str(random.choice(self.leveradg.split(',')))},path_ini_general_set)
            Save_config(i,{'diapazon_tp':str(random.choice(self.diapazon_tp.split(',')))},path_ini_general_set)
            Save_config(i,{'diapazon_sl':str(random.choice(self.diapazon_sl.split(',')))},path_ini_general_set)
            Save_config(i,{'diapazon_volume_min':str(random.choice(self.diapazon_volume_min.split(',')))},path_ini_general_set)
            Save_config(i,{'diapazon_volume_max':str(random.choice(self.diapazon_volume_max.split(',')))},path_ini_general_set)
            self.progress_bar.value = i*(100/int(self.how_mach_settings))*0.01
            self.update()
        self.btn_close()
            
    def close_page(self,e):
        self.btn_close()

    def print_page(self):
        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.start_time = config.get('param_trade_historical_trade_svobodniy_freym', 'set_general_input_start_time')
        self.stop_time = config.get('param_trade_historical_trade_svobodniy_freym', 'set_general_input_stop_time')
        self.depo = config.get('param_trade_historical_trade_svobodniy_freym', 'set_general_input_depo')
        self.leveradg = config.get('param_trade_historical_trade_svobodniy_freym', 'set_general_input_leveradg')
        self.how_mach_settings = config.get('param_trade_historical_trade_svobodniy_freym', 'set_general_input_how_mach_settings')
        self.diapazon_tp = config.get('param_trade_historical_trade_svobodniy_freym', 'set_general_input_tp')
        self.diapazon_sl = config.get('param_trade_historical_trade_svobodniy_freym', 'set_general_input_sl')
        self.diapazon_volume_min = config.get('param_trade_historical_trade_svobodniy_freym', 'set_general_input_volume_min')
        self.diapazon_volume_max = config.get('param_trade_historical_trade_svobodniy_freym', 'set_general_input_volume_max')

        self.progress_bar = ft.ProgressBar(width=880, value=0,color=c_yelow)

        self.generate_general_set = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text(f'Алгоритм сгенерирует сет настроек в заданном кол-ве, получив случайным образом каждую настройку из ряда заданных настроек\nЧерез запятую укажите возможные значения в каждом поле настроек',size=12,color=c_white,text_align='center',),padding=ft.padding.only(left=62,bottom=10)),
                                # ft.Row(controls=grid_component),
                                ft.Container(
                                    ft.Column(controls=[
                                        ft.Row(controls=[
                                            ft.Container(ft.Column(controls=[
                                            ft.Container(ft.Container(ft.Text('Время работы',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                            ft.Container(
                                                ft.Row(controls=[
                                                    ft.Column(controls=[
                                                        ft.Container(ft.Text('Время включения, часы',size=12,color=c_white,text_align='center'),width=170),
                                                        Input(self.input_start_time,self.start_time,170),
                                                        
                                                    ]),
                                                    ft.Column(controls=[
                                                        ft.Container(ft.Text('Время выключения, часы',size=12,color=c_white,text_align='center'),width=170),
                                                        Input(self.input_stop_time,self.stop_time,170),
                                                        
                                                    ])
                                                ]),
                                                width=376,
                                                height=80,
                                                border = ft.border.all(1, c_white),
                                                padding=ft.padding.only(top=10,left=10)
                                            ),
                                            ])),
                                            ft.Container(ft.Column(controls=[
                                            ft.Container(ft.Container(ft.Text('Торговый объём',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                            ft.Container(
                                                ft.Row(controls=[
                                                    ft.Column(controls=[
                                                        ft.Container(ft.Text('Депозит, $',size=12,color=c_white,text_align='center'),width=170),
                                                        Input(self.input_depo,self.depo,170),
                                                        
                                                    ]),
                                                    ft.Column(controls=[
                                                        ft.Container(ft.Text('Плечо',size=12,color=c_white,text_align='center'),width=170),
                                                        Input(self.input_leveradg,self.leveradg,170),
                                                        
                                                    ])
                                                ]),
                                                width=376,
                                                height=80,
                                                border = ft.border.all(1, c_white),
                                                padding=ft.padding.only(top=10,left=10)
                                            ),
                                            ])),
                                        ]),
                                        ft.Row(controls=[
                                                Component_tp(self.input_tp),
                                                Component_sl(self.input_sl)
                                            ]),
                                        ft.Row(controls=[
                                            Component_volume_min(self.input_volume_min),
                                            Component_volume_max(self.input_volume_max)
                                        ]),
                                        ft.Container(ft.Column(controls=[
                                            ft.Container(ft.Container(ft.Text('Количество настроек',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                            ft.Container(
                                                ft.Row(controls=[
                                                    ft.Row(controls=[
                                                        ft.Container(ft.Text('Сколько настроек сгененрировать',size=12,color=c_white,text_align='center'),width=240),
                                                        Input(self.input_how_mach_settings,self.how_mach_settings,100),
                                                        
                                                    ]),
                                                    
                                                ]),
                                                width=376,
                                                height=50,
                                                border = ft.border.all(1, c_white),
                                                padding=ft.padding.only(top=0,left=0)
                                            ),
                                            ]))
                                        
                                    ],scroll=ft.ScrollMode.ADAPTIVE),
                                    width=880,
                                    height=470,
                                    padding=ft.padding.only(left=60),
                                    # bgcolor='red'
                                ),
                                self.progress_bar,
                                # Table_set_print(),
                                ft.Container(
                                    ft.Container(
                                        ft.Row(controls=[
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Назад',size=12,),on_click=self.close_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Сгенерировать сет настроек',size=12,),on_click=self.btn_generate,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30,padding=ft.padding.only(left=0)),
                                    ]),padding=ft.padding.only(left=290,top=10)
                                    ),
                                    width=860,
                                    # height=920
                                )
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.generate_general_set

    def build(self):
        return self.print_page()