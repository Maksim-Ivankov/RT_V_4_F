
import flet as ft
from variable import *
from imports import *
from functools import partial

class ModernNavBar(ft.UserControl):

    def __init__(self,func):
        super().__init__()
        self.func = func
        # self.page = page

    # при наведении на пункты меню
    def HighLight(self,e):
        if e.data == 'true':
            e.control.border = ft.border.only(bottom=ft.border.BorderSide(1, c_white),top=ft.border.BorderSide(1, c_white))
            e.control.update()
        else:
            e.control.border = None
            e.control.update()


    def ContainerIcon(self,icon_path:str,text:str):
        return ft.Container(
            on_hover=lambda e: self.HighLight(e),
            width=200,
            height=40,
            border_radius=0,
            margin=ft.margin.only(bottom=-10),
            content=ft.Row(
                controls=[
                    # ft.Container(
                    #     ft.IconButton(
                    #         icon=icon_name,
                    #         icon_size=18,
                    #         icon_color=c_white,
                            
                    #     ),
                    #     padding=ft.padding.only(left=10)
                    # ),
                    ft.Container(ft.Image(src=icon_path,width=23,height=23,),padding = ft.padding.only(left=18)),
                    ft.Container(ft.Text(value=text,color=c_white,size=12,opacity=1,animate_opacity=200,),)
                ]
            )
        )


    def build(self):
        return ft.Container(
            
            width=200,
            height=height_window_platforma-40,
            padding=ft.padding.only(top=20),
            alignment=ft.alignment.center,

            content=ft.Column(
                horizontal_alignment='center',
                controls=[
                    ft.Container(ft.Image(src=f"src/img/logo_2.png",width=140,height=28,),margin = ft.margin.only(bottom=10)),
                    ft.Container(ft.Image(src=f"src/img/icons/resize.png"),width=24,height=24,on_click=partial(self.func)),
                    self.ContainerIcon('src/img/icons/1.png','Главная',),
                    self.ContainerIcon('src/img/icons/2.png','Историческая торговля'),
                    self.ContainerIcon('src/img/icons/3.png','Тестовая торговля'),
                    self.ContainerIcon('src/img/icons/4.png','Торговый робот'),
                    self.ContainerIcon('src/img/icons/5.png','FAQ'),
                    self.ContainerIcon('src/img/icons/6.png','Профиль'),
                    self.ContainerIcon('src/img/icons/7.png','Настройки программы'),
                ],
            )
        )