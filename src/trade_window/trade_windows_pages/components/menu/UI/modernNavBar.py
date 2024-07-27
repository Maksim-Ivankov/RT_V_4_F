
import flet as ft
from variable import *
from imports import *
from functools import partial

class ModernNavBar(ft.UserControl):

    def __init__(self,func,callback):
        super().__init__()
        self.func = func
        self.callback = callback

    # при наведении на пункты меню
    def HighLight(self,e):
        if e.data == 'true':
            e.control.border = ft.border.only(bottom=ft.border.BorderSide(1, c_white),top=ft.border.BorderSide(1, c_white))
            e.control.update()
        else:
            e.control.border = None
            e.control.update()
    # выбор пункта меню
    def change_menu(self,e):
        self.change_punkt_menu = e.control.data
        self.callback(e.control.data)


    def build(self):
        
        self.change_punkt_menu = 'Главная'

        punkts_menu = [
            'Главная',
            'Историческая торговля',
            'Тестовая торговля',
            'Торговый робот',
            'FAQ',
            'Профиль',
            'Настройки программы',
        ]
        img_menu_white = {
            'Главная': 'src/img/icons/1.png',
            'Историческая торговля': 'src/img/icons/2.png',
            'Тестовая торговля': 'src/img/icons/3.png',
            'Торговый робот': 'src/img/icons/4.png',
            'FAQ': 'src/img/icons/5.png',
            'Профиль': 'src/img/icons/6.png',
            'Настройки программы': 'src/img/icons/7.png',
        }
        self.items = []
        for punkt in punkts_menu:
            self.items.append(
                ft.Container(
                    data = punkt,
                    on_hover=lambda e: self.HighLight(e),
                    on_click=lambda e: self.change_menu(e),
                    width=200,
                    height=40,
                    border_radius=0,
                    margin=ft.margin.only(bottom=-10),
                    content=ft.Row(
                        controls=[
                            ft.Container(ft.Image(src=img_menu_white[punkt],width=23,height=23,),padding = ft.padding.only(left=18)),
                            ft.Container(ft.Text(value=punkt,color=c_white,size=12,opacity=1,animate_opacity=200,),)
                ]))
            )

        modern_nav_bar =  ft.Container(  
            width=200,
            expand=True,
            # height=height_window_platforma-40,
            padding=ft.padding.only(top=20),
            alignment=ft.alignment.center,
            content=ft.Column(
                controls=[
                    ft.Container(ft.Image(src=f"src/img/logo_2.png",width=140,height=28,),margin = ft.margin.only(bottom=10)),
                    ft.Container(ft.Image(src=f"src/img/icons/resize.png"),width=24,height=24,on_click=partial(self.func)),
                    ft.Column(self.items),
                ],
                # expand = True,
                horizontal_alignment='center',
                expand=True,
            )
        )

        return modern_nav_bar