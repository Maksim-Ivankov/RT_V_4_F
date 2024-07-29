
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.UI.input import Input

from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config

class Proksi(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def on_change_addres(self,e):
        self.change_addres = e.control.value

    def on_change_port(self,e):
        self.change_port = e.control.value

    # прокси включили
    def proxi_on(self,e):

        data_save = {
            'addres':self.change_addres,
            'port':self.change_port,
            'status':'on'
        }
        Save_config('Proxi',data_save)
        # print(self.controls[0].content.controls[1].content.controls[0].content.controls[1].content)
        self.controls[0].content.controls[1].content.controls[0].content.controls[1].content.value = 'активен'
        self.controls[0].content.controls[1].content.controls[0].content.controls[1].content.color = c_green
        # e.control.content.value = 'Сохранено'
        # e.control.bgcolor = c_green
        self.controls[0].content.controls[1].content.controls[0].content.controls[1].content.update()

    # прокси включили
    def proxi_off(self,e):

        data_save = {
            'addres':self.change_addres,
            'port':self.change_port,
            'status':'off'
        }
        Save_config('Proxi',data_save)
        self.controls[0].content.controls[1].content.controls[0].content.controls[1].content.value = 'неактивен'
        self.controls[0].content.controls[1].content.controls[0].content.controls[1].content.color = c_red
        self.controls[0].content.controls[1].content.controls[0].content.controls[1].content.update()


    def status_proxi_print(self,status):
        if status == 'on':
            return ft.Container(ft.Text('активен',size=12,color=c_green),margin=ft.margin.only(left=-5),)
        else:
            return ft.Container(ft.Text('неактивен',size=12,color=c_red),margin=ft.margin.only(left=-5),)

    def build(self):

        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        if ('Proxi') in config.sections():
            self.change_addres = config.get('Proxi', 'addres')
            self.change_port = config.get('Proxi', 'port')
            self.status_proxi = config.get('Proxi', 'status')
        else:
            self.change_addres = ''
            self.change_port = ''
            self.status_proxi = 'off'

        self.proksi = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(
                            ft.Text('Прокси',color=c_blue,),
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
                                    ft.Text('Прокси',size=12,color=c_white),
                                    self.status_proxi_print(self.status_proxi)
                                ]),margin=ft.margin.only(left=80)
                                ),
                                ft.Container(
                                    ft.Row(controls=[
                                        ft.Text('Мой ip адрес - ',size=12,color=c_white),
                                        ft.Container(ft.Text('31.181.35.129',size=12,color=c_white),margin=ft.margin.only(left=-10),)
                                    ]),margin=ft.margin.only(left=40,top=-5)
                                ),
                                ft.Container(
                                    ft.Row(controls=[
                                        ft.Text('Адрес',size=12,text_align='center'),
                                        Input(self.on_change_addres,self.change_addres,150)
                                ]),margin=ft.margin.only(left=30,top=-2)
                                ),
                                ft.Container(
                                    ft.Row(controls=[
                                        ft.Text('Порт',size=12,text_align='center'),
                                        Input(self.on_change_port,self.change_port,150)
                                ]),margin=ft.margin.only(left=36,top=-2)
                                ),
                                ft.Container(
                                    ft.Row(
                                    controls=[
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Выключить прокси',size=12,),on_click=self.proxi_off,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),padding=ft.padding.only(left=0,right=0))),alignment=ft.alignment.center,height=30),
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Включить прокси',size=12,),on_click=self.proxi_on,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),padding=ft.padding.only(left=0,right=0))),alignment=ft.alignment.center,height=30)
                                    ]
                                ),margin=ft.margin.only(top=0,left=3)
                                )
                            ]
                        ),
                        width=283,
                        height=180,
                        border = ft.border.all(1, c_white),
                        padding=ft.padding.only(top=10,left=10)
                    ),
                ]
            )
        )
        
        return self.proksi