import flet as ft
from variable import *
from imports import *

from test2 import Stakan_column

class Main:
    def __init__(self):
        None


    def run(self, page):
        self.page: ft.Page = page
        self.page.window_height, self.page.window_width = 400, 400
        self.main_print = ft.Container(
           content = Stakan_column(),
        )
        self.page.add(self.main_print)




if __name__ == '__main__':
    main = Main()
    ft.app(target=Main().run, assets_dir="assets")














































































