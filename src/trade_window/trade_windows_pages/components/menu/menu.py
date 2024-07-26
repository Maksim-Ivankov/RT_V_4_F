
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.menu.UI.modernNavBar import ModernNavBar

class Menu(ft.UserControl):

    def __init__(self,page):
        super().__init__()
        self.page = page

    def build(self):

        # логика сворачивания окнак
        def AnimateSidebar(e):
            if self.controls[0].width !=62:
                self.controls[0].content.controls[0].content.controls[0].content.src = 'src/img/logo_2_min.png'
                self.controls[0].content.controls[0].content.controls[0].update()
                for items in self.controls[0].content.controls[0].content.controls[2:]:
                    if isinstance(items,ft.Container):
                        items.content.controls[1].opacity = 0
                        items.content.update()
                self.controls[0].width = 62
                self.controls[0].update()
            else:
                self.controls[0].width = 200
                self.controls[0].update()
                self.controls[0].content.controls[0].content.controls[0].content.src = 'src/img/logo_2.png'
                self.controls[0].content.controls[0].content.controls[0].update()

                for items in self.controls[0].content.controls[0].content.controls[2:]:
                    if isinstance(items,ft.Container):
                        items.content.controls[1].opacity = 1
                        items.content.update()
        # Контейнер меню
        self.menu = ft.Container(
                width=200,
                height=height_window_platforma-39,
                bgcolor=c_blue,
                border_radius=0,
                border = ft.border.all(1, c_white),
                alignment=ft.alignment.center,
                animate=ft.animation.Animation(500,'decelerate'),
                content=ModernNavBar(AnimateSidebar),
                margin = ft.margin.only(left=-10,top=-10)
                

            
        )
        
        return self.menu