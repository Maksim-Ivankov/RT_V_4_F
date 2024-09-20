
import flet as ft
from variable import *
from imports import *

class Dropdown(ft.UserControl):
    def __init__(self,collback,po_umolchaniy,spisok,width_dropdown):
        super().__init__()
        self.collback = collback
        self.po_umolchaniy = po_umolchaniy
        self.spisok = spisok
        self.width_dropdown = width_dropdown


    def build(self):

        self.items = []
        for punkt in self.spisok:
            self.items.append(ft.dropdown.Option(punkt))
        
        self.dropdown = ft.Container(
            ft.Dropdown(
                value = self.po_umolchaniy,
                height=30,
                width=self.width_dropdown,
                filled = True,
                on_change = self.collback,
                autofocus=False,
                bgcolor=c_blue,
                border_radius=0,
                content_padding = ft.padding.only(left=5,right=5),
                border_color=c_white,
                border_width=1,
                alignment = ft.Alignment(0, 0),
                text_style = ft.TextStyle(
                    size=12,
                    color=c_white
                    
                ),
                # width=100,
                options = self.items
                # options=[
                #     # ft.dropdown.Option("Темная"),
                #     # ft.dropdown.Option("Светлая"),
                #     self.items
                # ],
            )
        )
        
        return self.dropdown
    







