# страница выбора стратегии торговли
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_strategy_trade_page.UI.component_info_strat import Component_info_strat
from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.MA import MA
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.one import One

class Regim_trade_one_settings_page(ft.UserControl):
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page
        self.strategy_translate = {
            'one':'Канал, тренд, локаль, объём',
            'MA':'Скользящие средние'
        }
        self.strategy_print = {
            'one':One(),
            'MA':MA()
        }


    def build(self):

        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.strategys = literal_eval(config.get('param_trade_historical_trade_svobodniy_freym', 'strategys'))
        
        strat_mas = []
        for strat in self.strategys:
            strat_mas.append(self.strategy_print[strat])

        self.regim_trade_one_settings_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text('Настройте выбранные ранее стратегии',size=12,color=c_white,text_align='center',),padding=ft.padding.only(left=310,bottom=14)),
                                ft.Container(ft.Column(controls=strat_mas,scroll=ft.ScrollMode.ALWAYS),height=500),
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
        
        return self.regim_trade_one_settings_page