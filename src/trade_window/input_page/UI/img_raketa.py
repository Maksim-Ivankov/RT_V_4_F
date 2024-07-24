
import flet as ft


class Img_raketa(ft.UserControl):

    def build(self):
        
        self.img_raketa = ft.Container(
            ft.Image(
                src=f"src/img/raketa.png",
                width=170,
                height=273,
                
            ),
            alignment=ft.alignment.center
        )
        
        return self.img_raketa