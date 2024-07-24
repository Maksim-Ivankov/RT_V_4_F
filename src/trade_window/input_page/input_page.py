import flet as ft
from src.trade_window.input_page.UI.img_raketa import Img_raketa
from src.trade_window.input_page.UI.form_wrap import Form_wrap

class Input_page(ft.UserControl):
    def __init__(self):
        super().__init__()


    def build(self):
        
        self.stakan = ft.Column(
            controls=[
                Img_raketa(),
                Form_wrap()
                ],
            
        )
            
        return self.stakan
    









