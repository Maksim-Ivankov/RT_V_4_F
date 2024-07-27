
import flet as ft
from variable import *
from imports import *
from functools import partial

class ModernNavBar(ft.UserControl):

    def __init__(self,func,callback,punkt_menu_one):
        super().__init__()
        self.func = func
        self.callback = callback
        self.punkt_menu_one = punkt_menu_one
        self.change_punkt_menu = self.punkt_menu_one
        self.time_ref = ft.Ref[ft.Text]()

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

    # элемент меню
    def element_menu(self,punkt,img_path,color_text):
        return ft.Container(
            data = punkt,
            on_hover=lambda e: self.HighLight(e),
            on_click=lambda e: self.change_menu(e),
            width=200,
            height=40,
            border_radius=0,
            margin=ft.margin.only(bottom=-10),
            content=ft.Row(
                controls=[
                    ft.Container(ft.Image(src=img_path,width=23,height=23,),padding = ft.padding.only(left=18)),
                    ft.Container(ft.Text(value=punkt,color=color_text,size=12,opacity=1,animate_opacity=200,),)
        ]))
    
    # рисуем время
    def date_time(self):
        return ft.Container(
            ft.Column(
            controls = [ft.Container(
                ft.Column(
                    controls=[
                        # ft.Container(ft.Text(version_desctop),padding=ft.padding.only(left=40)),
                        ft.Row(
                            controls=[
                                ft.Container(bgcolor=c_green,width=9,height=9,border_radius=5,),
                                ft.Text(ref = self.time_ref,value=time.strftime("%d.%m.%Y г. %H:%M:%S", time.localtime()),size=12)
                            ]),
                    ]
                ),padding=25
                ),
            ],
            alignment = ft.MainAxisAlignment.END,
        ),expand = True,
        )
 

    def build(self):

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
            'Главная': 'src/img/icons/1_white.png',
            'Историческая торговля': 'src/img/icons/2_white.png',
            'Тестовая торговля': 'src/img/icons/3_white.png',
            'Торговый робот': 'src/img/icons/4_white.png',
            'FAQ': 'src/img/icons/5_white.png',
            'Профиль': 'src/img/icons/6_white.png',
            'Настройки программы': 'src/img/icons/7_white.png',
        }
        img_menu_yelow = {
            'Главная': 'src/img/icons/1_yelow.png',
            'Историческая торговля': 'src/img/icons/2_yelow.png',
            'Тестовая торговля': 'src/img/icons/3_yelow.png',
            'Торговый робот': 'src/img/icons/4_yelow.png',
            'FAQ': 'src/img/icons/5_yelow.png',
            'Профиль': 'src/img/icons/6_yelow.png',
            'Настройки программы': 'src/img/icons/7_yelow.png',
        }
        self.items = []
        for punkt in punkts_menu:
            if punkt != self.change_punkt_menu:
                self.items.append(self.element_menu(punkt,img_menu_white[punkt],c_white))
            else:
                self.items.append(self.element_menu(punkt,img_menu_yelow[punkt],c_yelow))
              
        modern_nav_bar =  ft.Container(  
            width=200,
            expand=True,
            padding=ft.padding.only(top=20),
            alignment=ft.alignment.center,
            content=ft.Column(
                controls=[
                    ft.Container(ft.Image(src=f"src/img/logo_2.png",width=140,height=28,),margin = ft.margin.only(bottom=10)),
                    ft.Container(ft.Image(src=f"src/img/icons/resize.png"),width=24,height=24,on_click=partial(self.func)),
                    ft.Column(self.items),
                    self.date_time()
                ],
                horizontal_alignment='center',
                expand=True,
            )
        )

        return modern_nav_bar