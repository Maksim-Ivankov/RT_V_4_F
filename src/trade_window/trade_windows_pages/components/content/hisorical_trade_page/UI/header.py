
import flet as ft
from variable import *
from imports import *

class Header(ft.UserControl):
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page

    def build(self):
        
        self.header = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(
                            ft.Container(
                                ft.Row(controls=[
                                    ft.Container(ft.ElevatedButton(content = ft.Text('Информация',size=12,),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7,height=30),
                                    ft.Container(ft.ElevatedButton(content = ft.Text('История торговли',size=12,),data='История торговли',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7,height=30),
                                ]),width=320),alignment=ft.alignment.center),height=60,margin=ft.margin.only(top=-14,left=-10,right=-10,bottom=-14),      
                    ),
                    ft.Container(
                        ft.Container(alignment=ft.alignment.center),height=1,bgcolor=c_white,margin=ft.margin.only(top=2,left=-10,right=-10),      
                    ),
                    
                ]
            ),expand=2
            
        )
        
        return self.header