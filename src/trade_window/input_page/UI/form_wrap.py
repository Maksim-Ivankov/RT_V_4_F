
import flet as ft


class Form_wrap(ft.UserControl):

    def build(self):
        
        self.form_wrap = ft.Container(
            ft.Text("Game field"),
            alignment=ft.alignment.center
        )
        
        return self.form_wrap