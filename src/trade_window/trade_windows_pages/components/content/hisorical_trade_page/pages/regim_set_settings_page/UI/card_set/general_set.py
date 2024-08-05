# страница выбора стратегии торговли
import flet as ft
from variable import *
from imports import *

class General_set(ft.UserControl):
    def __init__(self):
        super().__init__()
        

    def print_page(self):

        # config = configparser.ConfigParser()         
        # config.read(path_imports_config)
        # self.strategys = literal_eval(config.get('param_trade_historical_trade_svobodniy_freym', 'strategys'))
        
        if os.path.exists(path_ini_general_set):
            text_info = ft.Container(ft.Text('Обнаружен сет из 50 строк настроек',size=12,color=c_white,text_align='center'),width = 280)
        else:
            text_info = ft.Container(ft.Text('Сет настроек не обнаружен',size=12,color=c_white,text_align='center'),width = 280)
            

        self.general_set = ft.Container(
            ft.Container(
                
                    ft.Column(
                        controls=[
                            ft.Container(
                                ft.Container(ft.Text('Общие настройки',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))
                            ),
                            ft.Container(
                                ft.Column(controls=[
                                    text_info,
                                    # ft.Container(ft.ElevatedButton(content = ft.Text('Сгенерировать\nновый сет настроек',size=12,text_align='center'),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,padding=10),
                                    ft.Container(ft.ElevatedButton(content = ft.Text('Сгенерировать\nновый сет настроек\nwef\nwef',size=12,text_align='center'),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,padding=ft.padding.only(top=10)),
                                ]),
                                width=280,
                                border = ft.border.all(1, c_white),
                                padding=ft.padding.only(top=14,bottom=14,left=20),
                                
                                # padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                
                            ),
                            
                        ]
                    ),     
                alignment=ft.alignment.center
            ),
            # width=860,
            # bgcolor='red'
        )
        
        return self.general_set

    def build(self):
        return self.print_page()