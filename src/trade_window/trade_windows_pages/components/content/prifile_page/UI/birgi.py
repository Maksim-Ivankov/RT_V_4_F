
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.UI.input import Input
from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config

class Birgi(ft.UserControl):
    def __init__(self,):
        super().__init__()
        self.change_birga_now = 'Binance'
        

    def colback_api_key(self,e):
            self.api_key_value = e.control.value

    def colback_secret_key(self,e):
            self.secret_key_value = e.control.value

    # выбор вкладки с биржей, перерисовка
    def change_birga(self,e):
        self.change_birga_now = e.control.content.value
        self.controls = []
        self.controls.append(self.print_change_birga(self.change_birga_now))
        self.update()

    # рисуем весь модуль блока подключения к бирже  
    def print_change_birga(self,birga):
        birgas = ['Binance','OKX','BiBit']
        item_birgas = []
        for i in birgas:
            if i == birga:
                item_birgas.append(
                     ft.Container(ft.Container(ft.Text(value=i,color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white),on_click=self.change_birga))
                )
            else:
                 item_birgas.append(
                     ft.Container(ft.Container(ft.Text(value=i,color=c_white,),bgcolor=c_blue,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_blue),on_click=self.change_birga))
                )
                 
        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        if (self.change_birga_now+'_key') in config.sections():
            api_key_birga = config.get(self.change_birga_now+'_key', 'api_key')
            secret_key_birga = config.get(self.change_birga_now+'_key', 'secret_key')
        else:
            api_key_birga = ''
            secret_key_birga = ''
        self.api_key_value = api_key_birga
        self.secret_key_value = secret_key_birga

        return ft.Container(
            ft.Column(
                controls=[
                    ft.Text('Подключение бирж для торговли роботом',size=12,color=c_white),
                    ft.Row(controls=item_birgas),
                    ft.Container(
                        ft.Column(controls=[
                            ft.Container(ft.Row(controls=[
                                ft.Container(ft.Text('Api-key',size=12,color=c_white),margin=ft.margin.only(left=8,right=8)),
                                Input(self.colback_api_key,api_key_birga,350)
                            ]),margin = ft.margin.only(left=10)
                            ),
                            ft.Container(ft.Row(controls=[
                                ft.Text('Secret-key',size=12,color=c_white),
                                Input(self.colback_secret_key,secret_key_birga,350)
                            ]),margin = ft.margin.only(left=10)
                            ),
                            ft.Container(ft.ElevatedButton(content = ft.Text('Сохранить',size=12,),on_click=self.save_birga_api_secret,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=3,height=30)
                        ]),
                        width=467,
                        height=140,
                        border = ft.border.all(1, c_white),
                        padding=10,
                    ), 
                ]
            )
        )

    # сохранение данных ключа и сикрета бирж1
    def save_birga_api_secret(self,e):
        config = configparser.ConfigParser()
        config.read(path_imports_config)

        data_save = {
            'api_key':self.api_key_value,
            'secret_key':self.secret_key_value
        }

        Save_config(self.change_birga_now+'_key',data_save)
        
        e.control.content.value = 'Сохранено'
        e.control.bgcolor = c_green
        e.control.update()
        

    def build(self):

        birgas = ['Binance','OKX','BiBit']
        item_birgas = []
        for i in birgas:
            if i == self.change_birga_now:
                item_birgas.append(
                     ft.Container(ft.Container(ft.Text(value=i,color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white),on_click=self.change_birga))
                )
            else:
                 item_birgas.append(
                     ft.Container(ft.Container(ft.Text(value=i,color=c_white,),bgcolor=c_blue,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_blue),on_click=self.change_birga))
                )

        return self.print_change_birga('Binance')
        
        
        