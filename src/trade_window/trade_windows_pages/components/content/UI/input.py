
import flet as ft
from variable import *
from imports import *

class Input(ft.UserControl):
    def __init__(self,collback,po_umolchaniy,width_input):
        super().__init__()
        self.collback = collback
        self.po_umolchaniy = po_umolchaniy
        self.width_input = width_input


    def build(self):
        
        self.input = ft.TextField(
            on_change=self.collback,
            value=self.po_umolchaniy,
            width=self.width_input,
            border_radius=0,
            border_color=c_white,
            height=30,
            content_padding=ft.padding.only(left=5,right=5),
            text_align='center',
            text_size=12
        )
        
        return self.input
    







