# страница выбора режима торговли

import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_strategy_trade_page.UI.component_info_strat import Component_info_strat
from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config

class Regime_trade_page(ft.UserControl):
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page


    def build(self):
       
        self.regime_trade_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text('Торговля по одной настройке - вводим настройки стратегии сами 1 раз и торгуем по ним на всем периоде\nТорговля по сету настроек - поочередная торговля на всем периоде разными настройками для \nнахождения лучших настроек торговли на выбранной стратегии',
                                        size=12,color=c_white,text_align='center',),padding=ft.padding.only(left=0)),
                                ft.Container(
                                    ft.Row(controls=[
                                        ft.Container(ft.ElevatedButton(content = ft.Text('\nТорговля по\nсету настроек',size=12,text_align='center',height=70),data='Одна настройка',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7),
                                        ft.Container(ft.ElevatedButton(content = ft.Text('\nТорговля по\nодной настройке',size=12,text_align='center',height=70),data='Сет настроек',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7),
                                    ]),
                                    width=600,
                                    height=80,
                                    padding=ft.padding.only(left=152),
                                ),
                                ft.Container(ft.ElevatedButton(content = ft.Text('Назад',size=12,),data='Выбрать стратегию торговли',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),height=30,width=100,margin=ft.margin.only(left=250)),
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.regime_trade_page