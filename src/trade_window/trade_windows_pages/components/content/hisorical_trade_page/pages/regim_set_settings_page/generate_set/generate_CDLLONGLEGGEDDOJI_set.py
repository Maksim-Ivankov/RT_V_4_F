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

class Generate_CDLLONGLEGGEDDOJI_set(ft.UserControl):
    def __init__(self,btn_close):
        super().__init__()
        self.btn_close = btn_close
        

    def input_koef_bistro(self,e):
        self.koef_bistro = e.control.value
        Save_config('param_trade_historical_trade_svobodniy_freym',{'set_MA_input_koef_bistro':str(e.control.value)})
    def input_koef_medleno(self,e):
        self.koef_medleno = e.control.value
        Save_config('param_trade_historical_trade_svobodniy_freym',{'set_MA_input_koef_medleno':str(e.control.value)})
    def input_sovpad_last(self,e):
        self.sovpad_last = e.control.value
        Save_config('param_trade_historical_trade_svobodniy_freym',{'set_MA_input_sovpad_last':str(e.control.value)})
    def input_up_chanal(self,e):
        self.up_chanal = e.control.value
        Save_config('param_trade_historical_trade_svobodniy_freym',{'set_MA_input_up_chanal':str(e.control.value)})
    def input_down_chanal(self,e):
        self.down_chanal = e.control.value
        Save_config('param_trade_historical_trade_svobodniy_freym',{'set_MA_input_down_chanal':str(e.control.value)})
        
    

    def btn_generate(self,e):
        if os.path.exists(path_ini_CDLLONGLEGGEDDOJI_set):
            os.remove(path_ini_CDLLONGLEGGEDDOJI_set)
        for i in range(1,int(self.how_mach_settings)+1):
            Save_config(str(i)+'_section',{'koef_bistro':str(random.choice(self.koef_bistro.split(',')))},path_ini_CDLLONGLEGGEDDOJI_set)
            Save_config(str(i)+'_section',{'koef_medleno':str(random.choice(self.koef_medleno.split(',')))},path_ini_CDLLONGLEGGEDDOJI_set)
            Save_config(str(i)+'_section',{'sovpad_last':str(random.choice(self.sovpad_last.split(',')))},path_ini_CDLLONGLEGGEDDOJI_set)
            Save_config(str(i)+'_section',{'up_chanal':str(random.choice(self.up_chanal.split(',')))},path_ini_CDLLONGLEGGEDDOJI_set)
            Save_config(str(i)+'_section',{'down_chanal':str(random.choice(self.down_chanal.split(',')))},path_ini_CDLLONGLEGGEDDOJI_set)
            self.progress_bar.value = i*(100/int(self.how_mach_settings))*0.01
            self.update()
        self.btn_close()
        pass
            
    def close_page(self,e):
        self.btn_close()

    def print_page(self):
        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.koef_bistro = config.get('param_trade_historical_trade_svobodniy_freym', 'set_MA_input_koef_bistro')
        self.koef_medleno = config.get('param_trade_historical_trade_svobodniy_freym', 'set_MA_input_koef_medleno')
        self.sovpad_last = config.get('param_trade_historical_trade_svobodniy_freym', 'set_MA_input_sovpad_last')
        self.up_chanal = config.get('param_trade_historical_trade_svobodniy_freym', 'set_MA_input_up_chanal')
        self.down_chanal = config.get('param_trade_historical_trade_svobodniy_freym', 'set_MA_input_down_chanal')
        self.how_mach_settings = config.get('param_trade_historical_trade_svobodniy_freym', 'set_general_input_how_mach_settings')
   

        self.progress_bar = ft.ProgressBar(width=880, value=0,color=c_yelow)

        self.generate_general_set = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text(f'Алгоритм сгенерирует сет настроек в заданном кол-ве, получив случайным образом каждую настройку из ряда заданных настроек\nЧерез запятую укажите возможные значения в каждом поле настроек',size=12,color=c_white,text_align='center',),padding=ft.padding.only(left=62,bottom=10)),
                                # ft.Row(controls=grid_component),
                                ft.Container(
                                    ft.Column(controls=[
                                        ft.Container(
                                            ft.Container(

                                                    ft.Column(
                                                        controls=[
                                                            ft.Container(
                                                                ft.Container(ft.Text('Длинноногий доджи',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))
                                                            ),
                                                            ft.Container(
                                                                ft.Row(controls=[
                                                                    ft.Container(
                                                                        ft.Column(controls=[
                                                                        ft.Container(ft.Text('Коэф. быстрой скольз. средней',size=12,color=c_white,text_align='center'),width=250),
                                                                        Input(self.input_koef_bistro,self.koef_bistro,250),
                                                                        ft.Container(ft.Text('Коэф. медленной скольз. средней',size=12,color=c_white,text_align='center'),width=250),
                                                                        Input(self.input_koef_medleno,self.koef_medleno,250),
                                                                    ]),
                                                                    padding=ft.padding.only(bottom=66)
                                                                    ),
                                                                    ft.Column(controls=[
                                                                        ft.Container(ft.Text('Кол-во совпадений в прошлом',size=12,color=c_white,text_align='center'),width=250),
                                                                        Input(self.input_sovpad_last,self.sovpad_last,250),
                                                                        ft.Container(ft.Text('Прижатие к верху коридора',size=12,color=c_white,text_align='center'),width=250),
                                                                        Input(self.input_up_chanal,self.up_chanal,250),
                                                                        ft.Container(ft.Text('Прижатие к низу коридора',size=12,color=c_white,text_align='center'),width=250),
                                                                        Input(self.input_down_chanal,self.down_chanal,250),
                                                                    ])
                                                                ]),
                                                                width=550,
                                                                border = ft.border.all(1, c_white),
                                                                padding=ft.padding.only(top=14,bottom=14,left=20),

                                                                # padding=ft.padding.only(left=-1,top=-1,bottom=-1)

                                                            )
                                                        ]
                                                    ),     
                                                alignment=ft.alignment.center
                                            ),
                                            width=860,
                                        )
                                        
                                    ],scroll=ft.ScrollMode.ADAPTIVE),
                                    width=880,
                                    height=280,
                                    padding=ft.padding.only(left=60),
                                ),
                                self.progress_bar,
                                ft.Container(
                                    ft.Container(
                                        ft.Row(controls=[
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Назад',size=12,),on_click=self.close_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Сгенерировать сет настроек',size=12,),on_click=self.btn_generate,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30,padding=ft.padding.only(left=0)),
                                    ]),padding=ft.padding.only(left=290,top=10)
                                    ),
                                    width=860,
                                )
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.generate_general_set

    def build(self):
        return self.print_page()