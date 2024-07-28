
import flet as ft
from variable import *
from imports import *

class Change_folder(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def build(self):
        
        self.change_folder = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(
                            ft.Text(
                            'Данные',
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
                            ft.Text('Указать папку сохранения датафреймов и логов работы робота',size=12,color=c_white,text_align='center'),
                            ft.Container(
                                ft.ElevatedButton(content=ft.Row(controls=[
                                    ft.Text('Выбрать папку',size=12),
                                    ft.Container(ft.Image(src=f"src/img/icons/folder_icon.png",width=33,height=26,),margin = ft.margin.only(top=2)),
                                ]),
                                bgcolor=c_blue,
                                color=c_white,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=0),
                                )
                                ),
                                width=200,
                                height=50,
                                margin=ft.margin.only(left=30,top=10)
                            ),
                            ft.Container(ft.ElevatedButton(content = ft.Text('Сохранить',size=12,),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7,height=30)
                        ]),
                        width=283,
                        height=180,
                        border = ft.border.all(1, c_white),
                        padding=10,
                        # expand= True
                    ), 
                ]
            )
        )
        
        return self.change_folder