
import flet as ft
from variable import *
from imports import *

# ОТРИСОВКА ВЕРХА СТРНИЫ ТОРГОВЛИ

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.table_set_print import Table_set_print
       
def Set_settings_def(print_mach_our_settings,change_page,start_trade):
    
    return ft.Column(controls=[
                ft.Container(ft.Text('Проверьте настройки и запустите торговлю',size=12,color=c_white,text_align='center'),padding=ft.padding.only(left=320)),
                ft.Container(
                    ft.Row(controls=[
                    ft.Container(
                    ft.Container(
                        ft.Column(controls=[
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        ft.Container(ft.Text('Общие настройки робота',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                        ft.Container(
                                            ft.Container(
                                                print_mach_our_settings(),
                                                width=860,
                                                height=70,
                                                border = ft.border.all(1, c_white),
                                                bgcolor=c_blue,
                                            ),
                                            width=860,
                                            height = 70,
                                            padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                
                                        )]),     
                    ])),
                    width=860,
                    ),
                    # Table_set_print(),
                    ]),
                width=900,padding=ft.padding.only(left=20)),
                ft.Container(Table_set_print(),width=900,padding=ft.padding.only(left=20,top=20)),
                
                ft.Container(
                    ft.Container(
                        ft.Row(controls=[
                        ft.Container(ft.ElevatedButton(content = ft.Text('Назад',size=12,),data='Выбрать режим торговли',bgcolor=c_yelow,on_click=change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                        ft.Container(ft.ElevatedButton(content = ft.Text('Запустить торговлю',size=12,),data='Выбрать режим торговли',bgcolor=c_yelow,on_click=start_trade,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                    ]),padding=ft.padding.only(left=320,top=10)
                    ),
                    width=500,
                ),

            ],scroll=ft.ScrollMode.ALWAYS)