import flet as ft
from variable import *
from imports import *

import asyncio

from src.trade_window.input_page.input_page import Input_page
from src.trade_window.trade_windows_pages.platforma import Platforma

class Main:
    def __init__(self):
        None



    def run(self, page):
        self.page: ft.Page = page
        self.page.title = "RoboTrade"
        self.page.window_height, self.page.window_width = height_window_platforma, width_window_platforma
        self.page.theme_mode = "dark" 
        # self.page.window_resizable = False
        # self.page.window_center()
        self.page.bgcolor = c_blue
        self.main_print = ft.Container( # общий контейнер на страницу45rк
           content = Platforma(self.page),
           expand = True,
           padding=ft.padding.only(bottom=-10)
        )
        self.page.add(self.main_print)

        # self.page: ft.Page = page
        # self.page.title = "RoboTrade"
        # self.page.window_height, self.page.window_width = 672, 423
        # self.page.theme_mode = "dark" 
        # self.page.window_resizable = False
        # # self.page.window_center()
        # self.page.bgcolor = c_blue

        # self.main_print = ft.Container( # общий контейнер на страницу45r6
        #    content = Input_page(self.page)
        # )
        # self.page.add(self.main_print)




if __name__ == '__main__':
    main = Main()
    ft.app(target=Main().run, assets_dir="assets")














































































