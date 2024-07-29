
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.UI.dropdown import Dropdown
from src.trade_window.trade_windows_pages.components.content.UI.input import Input

from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config

class Settings(ft.UserControl):
    # def __init__(self):
    #     super().__init__()


    def on_change_tema(self,e):
        self.change_tema = e.control.value

    def on_change_count_coin(self,e):
        self.change_count_coin = e.control.value

    # сохранение насйтроек программы1111
    def save_set_programm(self,e):

        data_save = {
            'thema':self.change_tema,
            'count_coin':self.change_count_coin
        }
        Save_config('settings_program',data_save)
        e.control.content.value = 'Сохранено'
        e.control.bgcolor = c_green
        e.control.update()

    def build(self):

        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        if ('settings_program') in config.sections():
            self.change_tema = config.get('settings_program', 'thema')
            self.change_count_coin = config.get('settings_program', 'count_coin')
        else:
            self.change_tema = 'Dark'
            self.change_count_coin = '10'

        
        self.settings = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(
                            ft.Text(
                            'Настройки программы',
                            color=c_blue,
                            ),
                            bgcolor=c_yelow,
                            padding=5,
                            margin=ft.margin.only(bottom=-10),
                            border=ft.border.all(1,c_white)
                        )
                    ),
                    ft.Container(
                        ft.Column(
                            controls=[
                                ft.Container(
                                    ft.Row(controls=[
                                        ft.Container(ft.Text('Выбор темы',size=12),margin=ft.margin.only(right=10)),
                                        Dropdown(self.on_change_tema,self.change_tema,["Dark","Light"],150)
                                ]),margin=ft.margin.only(left=10)
                                ),
                                ft.Container(
                                    ft.Row(controls=[
                                        ft.Text('Кол-во монет\nтепловой карты',size=12,text_align='center'),
                                        Input(self.on_change_count_coin,self.change_count_coin,150)
                                ])
                                ),
                                ft.Container(ft.ElevatedButton(content = ft.Text('Сохранить',size=12,),on_click=self.save_set_programm,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7,height=30)
                     
                            ]
                        ),
                        width=283,
                        height=180,
                        border = ft.border.all(1, c_white),
                        padding=ft.padding.only(top=30,left=10)
                    ),
                ]
            )
        )
        
        return self.settings