# страница выбора стратегии торговли
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_strategy_trade_page.UI.component_info_strat import Component_info_strat
from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.table_set_print import Table_set_print
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.general_set import General_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.MA_set import MA_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.one_set import One_set

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_general_set import Generate_general_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_one_set import Generate_one_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_MA_set import Generate_MA_set

class Regim_set_settings_page(ft.UserControl):
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page
        self.strategy_translate = {
            'one':'Канал, тренд, локаль, объём',
            'MA':'Скользящие средние'
        }
        self.card_set = {
            'one':MA_set(self.click_neral_set),
            'MA':One_set(self.click_neral_set)
        }
        self.open_page_get_set = {
            'Общие настройки':Generate_general_set(self.update_page),
            'MA':Generate_MA_set(self.update_page),
            'one':Generate_one_set(self.update_page),
        }

    def update_page(self):
        self.controls = []
        self.controls.append(self.print_page())
        self.update()

    # нажали на кнопку - получить сет в генеральных настройках
    def click_neral_set(self,e):
        self.controls = []
        self.controls.append(self.open_page_get_set[e.control.data])
        self.update()


    def print_page(self):

        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.strategys = literal_eval(config.get('param_trade_historical_trade_svobodniy_freym', 'strategys'))
        
        grid_component = []
        grid_component.append(General_set(self.click_neral_set))
        str_header = ''
        for strat in self.strategys:
            str_header = str_header + self.strategy_translate[strat] + ' | '
            grid_component.append(self.card_set[strat])

        self.regim_set_settings_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text(f'Установка сета настроек для стратегий:\n{str_header}',size=12,color=c_white,text_align='center',),padding=ft.padding.only(left=288,bottom=10)),
                                # ft.Row(controls=grid_component),
                                ft.Container(
                                    ft.GridView(
                                        controls = grid_component,
                                        # expand=1,
                                        runs_count=3,
                                        # max_extent=150,
                                        # child_aspect_ratio=0.65,
                                        spacing=-140,
                                        # run_spacing=5,
                                    
                                    
                                    ),
                                    width=880,
                                    height=490,
                                ),
                                # Table_set_print(),
                                ft.Container(
                                    ft.Container(
                                        ft.Row(controls=[
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Назад',size=12,),data='Выбрать режим торговли',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Запустить торговлю',size=12,),data='Запустить торговлю',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                    ]),padding=ft.padding.only(left=290,top=10)
                                    ),
                                    width=860,
                                    # height=920
                                )
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.regim_set_settings_page

    def build(self):
        return self.print_page()