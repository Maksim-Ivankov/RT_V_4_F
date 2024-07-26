
import flet as ft
from variable import *
from imports import *

class Content(ft.UserControl):

    def build(self):
        
        self.content = ft.Container(
            ft.Text('Контент')
        )
        
        return self.content