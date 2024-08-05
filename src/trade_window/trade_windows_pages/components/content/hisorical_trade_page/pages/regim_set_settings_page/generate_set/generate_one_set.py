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

class Generate_one_set(ft.UserControl):
    def __init__(self,btn_close):
        super().__init__()
        self.btn_close = btn_close
        

    def input_up_chanal(self,e):
        self.up_chanal = e.control.value
        Save_config('param_trade_historical_trade_svobodniy_freym',{'set_one_input_up_chanal':str(e.control.value)})
    def input_down_chanal(self,e):
        self.down_chanal = e.control.value
        Save_config('param_trade_historical_trade_svobodniy_freym',{'set_one_input_down_chanal':str(e.control.value)})
    def input_corner_long(self,e):
        self.corner_long = e.control.value
        Save_config('param_trade_historical_trade_svobodniy_freym',{'set_one_input_corner_long':str(e.control.value)})
    def input_corner_short(self,e):
        self.corner_short = e.control.value
        Save_config('param_trade_historical_trade_svobodniy_freym',{'set_one_input_corner_short':str(e.control.value)})


    def btn_generate(self,e):
        if os.path.exists(path_ini_one_set):
            os.remove(path_ini_one_set)
        for i in range(1,int(self.how_mach_settings)+1):
            Save_config(str(i)+'_section',{'up_chanal':str(random.choice(self.up_chanal.split(',')))},path_ini_one_set)
            Save_config(str(i)+'_section',{'down_chanal':str(random.choice(self.down_chanal.split(',')))},path_ini_one_set)
            Save_config(str(i)+'_section',{'corner_long':str(random.choice(self.corner_long.split(',')))},path_ini_one_set)
            Save_config(str(i)+'_section',{'corner_short':str(random.choice(self.corner_short.split(',')))},path_ini_one_set)
            self.progress_bar.value = i*(100/int(self.how_mach_settings))*0.01
            self.update()
        self.btn_close()
        pass
            
    def close_page(self,e):
        self.btn_close()

    def print_page(self):

        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.up_chanal = config.get('param_trade_historical_trade_svobodniy_freym', 'set_one_input_up_chanal')
        self.down_chanal = config.get('param_trade_historical_trade_svobodniy_freym', 'set_one_input_down_chanal')
        self.corner_long = config.get('param_trade_historical_trade_svobodniy_freym', 'set_one_input_corner_long')
        self.corner_short = config.get('param_trade_historical_trade_svobodniy_freym', 'set_one_input_corner_short')
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
                                ft.Container(ft.Text('Канал, тренд, локаль, объём',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))
                            ),
                            ft.Container(
                                ft.Row(controls=[
                                    ft.Column(controls=[
                                        ft.Container(ft.Text('Верх канала, %',size=12,color=c_white,text_align='center'),width=170),
                                        Input(self.input_up_chanal,self.up_chanal,170),
                                        ft.Container(ft.Text('Низ канала, %',size=12,color=c_white,text_align='center'),width=170),
                                        Input(self.input_down_chanal,self.down_chanal,170),
                                    ]),
                                    ft.Column(controls=[
                                        ft.Container(ft.Text('Угол тренда лонг',size=12,color=c_white,text_align='center'),width=170),
                                        Input(self.input_corner_long,self.corner_long,170),
                                        ft.Container(ft.Text('Угол тренда шорт',size=12,color=c_white,text_align='center'),width=170),
                                        Input(self.input_corner_short,self.corner_short,170),
                                    ])
                                ]),
                                width=396,
                                border = ft.border.all(1, c_white),
                                padding=ft.padding.only(top=14,bottom=14,left=20),
                                
                                # padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                
                            ),
                            
                        ]
                    ),     
                alignment=ft.alignment.center
            ),
            width=860,
            # bgcolor='red'
        )
                                        
                                    ],scroll=ft.ScrollMode.ADAPTIVE),
                                    width=880,
                                    height=214,
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