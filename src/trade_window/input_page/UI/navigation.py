
import flet as ft
from variable import *
from imports import *

class Navigation(ft.UserControl):

    def __init__(self,change_page,number_page):
        super().__init__()
        self.change_page = change_page
        self.number_page = number_page

    def build(self):

        def handle_submenu_hover(e):
            self.change_page(e.control.data)


        nav_list = ["Приветствуем!","Регистрация","Авторизация"]
        items_nav = []

        for i in range(len(nav_list)):
            if str(i) == self.number_page:
                items_nav.append(
                    ft.Container(
                        content=ft.Text(nav_list[i],color=c_blue,text_align='center'),
                        padding=ft.padding.only(left=5,right=5,bottom=10,top=10),
                        on_click=handle_submenu_hover,
                        data=str(i),
                        bgcolor=c_yelow,
                        margin = ft.margin.only(right=-10),
                        border = ft.border.all(1, c_white)
                    )
                )
                continue
            items_nav.append(
                ft.Container(
                    content=ft.Text(nav_list[i],color=c_white,text_align='center'),
                    padding=ft.padding.only(left=5,right=6,bottom=10,top=10),
                    on_click=handle_submenu_hover,
                    data=str(i),
                    margin = ft.margin.only(right=-10)

                )
            )
        
        self.navigation = ft.Container(
            ft.Row(
                controls=items_nav,          
            ),
            margin = ft.margin.only(bottom=-11)
        )

        return self.navigation