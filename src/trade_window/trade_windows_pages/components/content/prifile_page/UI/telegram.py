
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.UI.input import Input
from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config

class Telegram(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def colback_api_key(self,e):
        self.api_key_value = e.control.value
    
    def colback_id_group(self,e):
        self.id_group_value = e.control.value

    # сохранение данных ключа и ID телеграм2
    def save_tg_api_id(self,e):

        data_save = {
            'api_key':self.api_key_value,
            'id_group':self.id_group_value
        }

        Save_config('Telegram_key',data_save)
        
        e.control.content.value = 'Сохранено'
        e.control.bgcolor = c_green
        e.control.update()

    def build(self):

        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        if ('Telegram_key') in config.sections():
            api_key_tg = config.get('Telegram_key', 'api_key')
            id_group_tg = config.get('Telegram_key', 'id_group')
        else:
            api_key_tg = ''
            id_group_tg = ''
        self.api_key_value = api_key_tg
        self.id_group_value = id_group_tg
        
        self.telegram = ft.Container(
            ft.Column(
                controls=[
                    ft.Text('Подключение Телеграм канала для оповещения торгового робота',size=12,color=c_white),
                    ft.Container(
                        ft.Container(
                            ft.Text(
                            'Telegram',
                            color=c_blue,
                            ),
                            bgcolor=c_yelow,
                            padding=5,
                            margin=ft.margin.only(bottom=-10),
                            border=ft.border.all(1,c_white),
                            
                        )
                    ),
                    ft.Container(
                        ft.Column(controls=[
                            ft.Container(
                                  ft.Row(controls=[
                                ft.Container(ft.Text('Api-key',size=12,color=c_white),margin=ft.margin.only(left=3,right=3)),
                                Input(self.colback_api_key,self.api_key_value,280)
                            ]),margin = ft.margin.only(left=10)
                            ),
                            ft.Container(ft.Row(controls=[
                                ft.Text('ID group',size=12,color=c_white),
                                Input(self.colback_id_group,self.id_group_value,280)
                            ]),margin = ft.margin.only(left=10)
                            ),
                            ft.Container(ft.ElevatedButton(content = ft.Text('Сохранить',size=12,),on_click=self.save_tg_api_id,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=3,height=30)
                        ]),
                        width=391,
                        height=140,
                        border = ft.border.all(1, c_white),
                        padding=10,
                    ), 
                ]
            )
        )
        
        return self.telegram