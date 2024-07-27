
import flet as ft
from variable import *
from imports import *

class Prifile_page(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def build(self):
        
        self.prifile_page = ft.Container(
            ft.Text('Профиль')
        )
        
        return self.prifile_page