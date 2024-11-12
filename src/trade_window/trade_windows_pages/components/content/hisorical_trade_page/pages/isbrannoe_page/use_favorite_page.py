
import flet as ft
from variable import *
from imports import *


class Use_favorite_page(ft.UserControl):
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page


    def build(self):

        self.ferst_page = ft.Container(
            ft.Text('Здесь будем выбирать, историческая торговля, тестовая торговля или торговый робот и так далее')
        )
        
        return self.ferst_page