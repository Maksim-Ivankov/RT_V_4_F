
import flet as ft
from variable import *
from imports import *

class Settings_page(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def build(self):
        
        self.settings_page = ft.Container(
            ft.Text('Настройки профиля')
        )
        
        return self.settings_page