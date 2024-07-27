
import flet as ft
from variable import *
from imports import *

class Main_page(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def build(self):
        
        self.main_page = ft.Container(
            ft.Text('Главная')
        )
        
        return self.main_page