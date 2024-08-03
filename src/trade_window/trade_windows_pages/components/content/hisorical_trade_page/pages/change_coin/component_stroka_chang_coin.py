
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config

class Component_stroka_chang_coin(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.mas_print_coin_container = []

# file.read().split('|')
# '|'.join(arr_coin)

    # удаляем из списка
    def remove_one_coin(self,e):
        self.data_mas.remove(e.control.data)
        self.reprint_stroka(self.data_mas)
        data_save = {'coins_trade':'|'.join(self.data_mas)}
        Save_config('param_trade_historical_trade_svobodniy_freym',data_save)
        # config = configparser.ConfigParser()         
        # config.read(path_imports_config)
        # if ('settings_program') in config.sections():
        #     self.change_tema = config.get('settings_program', 'thema')

    def reprint_stroka(self,mas_result_coin):
        self.data_mas = mas_result_coin
        data_save = {'coins_trade':'|'.join(self.data_mas)}
        Save_config('param_trade_historical_trade_svobodniy_freym',data_save)
        self.mas_print_coin_container = []
        for i in reversed(mas_result_coin):
            self.mas_print_coin_container.append(
                ft.Container(
                    ft.Row(controls=[
                        ft.Container(ft.Text(i,size=12,color=c_blue),padding=ft.padding.only(left=4)),
                        ft.Container(ft.Text('X',size=12,color=c_blue),bgcolor=c_white,padding=2,on_click=self.remove_one_coin,data=i)
                    ]),
                    bgcolor=c_yelow
                )
            )

        self.controls = []
        self.controls.append(self.print_component())
        self.update()
        
    def print_component(self):
        self.component_stroka_chang_coin = ft.Container(
                # ft.Row(controls=self.mas_print_coin_container,spacing=8),
                ft.Row(controls=self.mas_print_coin_container,scroll=ft.ScrollMode.ADAPTIVE,width=400),
                width=400,
                height=40,
                margin=ft.margin.only(top=-10)
                
                
            )

        return self.component_stroka_chang_coin


    def build(self):
        return self.print_component()
        