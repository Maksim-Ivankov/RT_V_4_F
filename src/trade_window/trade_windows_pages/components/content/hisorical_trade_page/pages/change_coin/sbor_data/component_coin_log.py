
import flet as ft
from variable import *
from imports import *

class Component_coin_log(ft.UserControl):
    def __init__(self,data_detect,regime='day_trade'):
        super().__init__()
        self.data_detect = data_detect
        self.regime = regime
        
    def update_page(self,data):
        self.controls = []
        self.controls.append(self.print_page(data))
        self.update()

    def print_page(self,data):
        if self.regime=='day_trade':
            widt_component = 150
        elif self.regime=='his_trade':
            widt_component = 130
        self.component_coin_log = ft.Container(
            ft.Column(controls=data,
            scroll=ft.ScrollMode.ALWAYS,),
            width=widt_component,
            height=298,
            bgcolor=c_white,
            padding=10
        )

        return self.component_coin_log


    def build(self):
        return self.print_page(self.data_detect)