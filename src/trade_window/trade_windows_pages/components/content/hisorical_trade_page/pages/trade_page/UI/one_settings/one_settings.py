
import flet as ft
from variable import *
from imports import *

# ОТРИСОВКА ВЕРХА СТРНИЫ ТОРГОВЛИ1
       
def One_settings_def(print_our_settings,print_set_settings,change_page,start_trade):
    
    config = configparser.ConfigParser()         
    config.read(path_imports_config)
    regime_trade_page = config.get('param_trade_historical_trade_svobodniy_freym', 'regime_trade_page')
    
    if regime_trade_page == 'svoboda':
        btn_back = ft.Container(ft.ElevatedButton(content = ft.Text('Назад',size=12,),data='Выбрать режим торговли',bgcolor=c_yelow,on_click=change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30)
    elif regime_trade_page == 'historical':
        btn_back = ft.Container(ft.ElevatedButton(content = ft.Text('Назад',size=12,),data='Одна настройка',bgcolor=c_yelow,on_click=change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30)
    #11
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
                                            print_our_settings(),
                                            width=500,
                                            height=148,
                                            border = ft.border.all(1, c_white),
                                            bgcolor=c_blue,
                                        ),
                                        width=500,
                                        height = 148,
                                        padding=ft.padding.only(left=-1,top=-1,bottom=-1)
            
                                    )]),     
                ])),
                width=500,
                ),
                ft.Container(
                    ft.Container(
                        ft.Column(controls=[
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        ft.Container(ft.Text('Настройки стратегий',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                    ft.Container(
                                        ft.Container(
                                            print_set_settings(),
                                            width=350,
                                            height=148,
                                            border = ft.border.all(1, c_white),
                                            bgcolor=c_blue,
                                        ),
                                        width=350,
                                        height = 148,
                                        padding=ft.padding.only(left=-1,top=-1,bottom=-1)    
                            )]),     
                    ])),
                    width=400,
                ),
                ]),
            width=900,padding=ft.padding.only(left=20)),
            ft.Container(
                ft.Container(
                    ft.Row(controls=[
                    btn_back,
                    ft.Container(ft.ElevatedButton(content = ft.Text('Запустить торговлю',size=12,),data='Выбрать режим торговли',bgcolor=c_yelow,on_click=start_trade,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                ]),padding=ft.padding.only(left=320,top=10)
                ),
                width=500
            ),
        ],scroll=ft.ScrollMode.ALWAYS,data='lol')
    
    # return content