
import flet as ft
from variable import *
from imports import *

class Componen_log(ft.UserControl):
    def __init__(self,data_detect):
        super().__init__()
        self.data_detect = data_detect
        
    def update_page(self,data):
        self.controls = []
        self.controls.append(self.print_page(data))
        self.update()

    def print_page(self,data):
        self.componen_log = ft.Container(
            ft.Column(controls=data,
            scroll=ft.ScrollMode.ALWAYS,),
            width=360,
            height=298,
            bgcolor=c_white,
            padding=10
        )
        return self.componen_log


    def build(self):
        return self.print_page(self.data_detect)
        