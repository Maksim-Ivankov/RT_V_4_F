
import flet as ft
from variable import *
from imports import *

from src.trade_window.input_page.UI.pages_sign.dobro_posalovat import Dobro_posalovat
from src.trade_window.input_page.UI.pages_sign.registration import Registration
from src.trade_window.input_page.UI.pages_sign.sign_in import Sign_in
from src.trade_window.input_page.UI.navigation import Navigation

class Form_wrap(ft.UserControl):
    
    def build(self):
        
        
        def change_page(num):
            self.controls = []
            if num == '0': 
                self.controls.append(ft.Column(controls=[Navigation(change_page,'0'),Dobro_posalovat()]))
            if num == '1': 
                self.controls.append(ft.Column(controls=[Navigation(change_page,'1'),Registration()]))
            if num == '2': 
                self.controls.append(ft.Column(controls=[Navigation(change_page,'2'),Sign_in()]))
            self.update()
       
        self.form_wrap = ft.Column(
            controls=[
                Navigation(change_page,'1'),
                Registration()
                # Navigation(change_page,'0'),
                # Dobro_posalovat()
            ]
        )
        
        
        return self.form_wrap