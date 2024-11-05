# страница выбора стратегии торговли
import flet as ft
from variable import *
from imports import *

class CDLHARAMICROSS_set(ft.UserControl):
    def __init__(self,callback):
        super().__init__()
        self.callback = callback
        

    def print_page(self):

        config = configparser.ConfigParser()         
        config.read(path_ini_CDLHARAMICROSS_set)
        count_settings = len(config.sections())
        
        if os.path.exists(path_ini_CDLHARAMICROSS_set):
            text_info = ft.Container(ft.Text(f'Обнаружен сет из {count_settings} строк настроек',size=12,color=c_white,text_align='center'),width = 280)
        else:
            text_info = ft.Container(ft.Text('Сет настроек не обнаружен',size=12,color=c_white,text_align='center'),width = 280)
            

        self.MA_set = ft.Container(
            ft.Container(
                
                    ft.Column(
                        controls=[
                            ft.Container(
                                ft.Container(ft.Text('Шаблон пересечения Харами',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))
                            ),
                            ft.Container(
                                ft.Column(controls=[
                                    text_info,
                                    ft.Container(ft.ElevatedButton(content = ft.Text('Сгенерировать новый сет настроек',size=12,text_align='center'),data='CDLHARAMICROSS',on_click=self.callback,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,padding=ft.padding.only(top=10)),
                                ]),
                                width=280,
                                border = ft.border.all(1, c_white),
                                padding=ft.padding.only(top=14,bottom=14,left=0),
                            ),
                            
                        ]
                    ),     
            ),
        )
        
        return self.MA_set

    def build(self):
        return self.print_page()