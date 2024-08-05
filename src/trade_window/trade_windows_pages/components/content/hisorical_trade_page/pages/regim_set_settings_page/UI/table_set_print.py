# страница выбора стратегии торговли
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_strategy_trade_page.UI.component_info_strat import Component_info_strat
from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config

class Table_set_print(ft.UserControl):
    def __init__(self):
        super().__init__()
        

    def print_page(self):

        # config = configparser.ConfigParser()         
        # config.read(path_imports_config)
        # self.strategys = literal_eval(config.get('param_trade_historical_trade_svobodniy_freym', 'strategys'))
        
        # str_header = ''
        # for strat in self.strategys:
        #     str_header = str_header + self.strategy_translate[strat] + ' | '

        self.table_set_print = ft.Container(
            ft.Container(
                ft.Column(controls=[
                    ft.Column(
                        controls=[
                            ft.Container(ft.Container(ft.Text('Сет настроек',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                            ft.Container(
                                
                                width=860,
                                border = ft.border.all(1, c_white),
                                # padding=14,
                                height = 460,
                                padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                
                    )]),     
            ])),
            width=860,
        )
        
        return self.table_set_print

    def build(self):
        return self.print_page()