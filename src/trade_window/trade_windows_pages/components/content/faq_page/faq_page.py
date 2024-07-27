
import flet as ft
from variable import *
from imports import *

class Faq_page(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def build(self):
        
        self.faq_page = ft.Container(
            ft.Text('FAQ')
        )
        
        return self.faq_page