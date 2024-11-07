
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.UI.header import Header

class Ferst_page(ft.UserControl):
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page


    def build(self):
        self.ferst_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                # ft.Container(width=300,height=400,bgcolor='red'),
                                # ft.Text('Свободный фрейм - торговля на 1 стратегии по выбранному небольшому фрейму данных \nТорговля со смещением - торговля на заданном небольшом фрейме данных интервалами со смещением \nИсторическая торговля  - торговля на длинном фрейме данных',
                                #         size=12,color=c_white,text_align='center'),
                                ft.Container(#11
                                    ft.Row(controls=[
                                        ft.Container(ft.Column(controls=[
                                            ft.Container(ft.Text('Дневная торговля',text_align='CENTER',size=20,color=c_yelow),width=385,margin=ft.margin.only(top=10,bottom=0)),
                                            ft.Container(ft.Text('Торговля выбранной стратегией на коротком фрейме исотрических данных. Можно получить фрейм максимум на 2 дня назад по выбранным монетам без возможности выбора даты получения фрейма',text_align='CENTER'),width=385,margin=ft.margin.only(top=10,bottom=5)),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nДневная\nторговля',size=12,text_align='center',height=70),data='Свободный фрейм',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7),
                                            ft.Container(ft.Text('Подход дневной торговли можно использовать для быстрого тестирования стратегий или группы стратегий на коротком фрейме для определения лучших настроек торговли в моменте и запуска полученной стратегии в работу на реальных данных',text_align='CENTER'),width=385,margin=ft.margin.only(top=5,bottom=0)),
                                        ]),width=385,height=390,margin=ft.margin.only(right=20),border=ft.border.all(1,c_white),padding=10),
                                        ft.Container(ft.Column(controls=[
                                            ft.Container(ft.Text('Историческая торговля',text_align='CENTER',size=20,color=c_yelow),width=385,margin=ft.margin.only(top=10,bottom=0)),
                                            ft.Container(ft.Text('Торговля стратегией или группой стратегий на длинном фрейме данных. Допустимо использование исторических данных от нескольких дней до одного года. ',text_align='CENTER'),width=385,margin=ft.margin.only(top=10,bottom=5)),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nИсторическая\nторговля',size=12,text_align='center',height=70),data='Историческая торговля',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7),
                                            ft.Container(ft.Text('Подход исотической торговли используется для тестирования стратегии на длянном фрейме с целью получения точных результатов на разных циклах рынка. Метод исторической торговли занимает много времени (от 10 минут до нескольких часов)',text_align='CENTER'),width=385,margin=ft.margin.only(top=5,bottom=0)),
                                        ]),width=385,height=390,border=ft.border.all(1,c_white),padding=10),
                                    ]),
                                    width=800,
                                    height=400,
                                    # margin=ft.margin.only(left=90),
                                ),
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.ferst_page

# import flet as ft
# from variable import *
# from imports import *

# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.UI.header import Header

# class Ferst_page(ft.UserControl):
#     def __init__(self,change_page):
#         super().__init__()
#         self.change_page = change_page


#     def build(self):
#         self.ferst_page = ft.Container(
#             ft.Container(
#                         ft.Container(
#                             ft.Column(controls=[
#                                 ft.Text('Свободный фрейм - торговля на 1 стратегии по выбранному небольшому фрейму данных \nТорговля со смещением - торговля на заданном небольшом фрейме данных интервалами со смещением \nИсторическая торговля  - торговля на длинном фрейме данных',
#                                         size=12,color=c_white,text_align='center'),
#                                 ft.Container(#11
#                                     ft.Row(controls=[
#                                         ft.Container(ft.ElevatedButton(content = ft.Text('\nСвободный\nфрейм',size=12,text_align='center',height=70),data='Свободный фрейм',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7),
#                                         # ft.Container(ft.ElevatedButton(content = ft.Text('\nТорговля\nсо смещением',size=12,text_align='center',height=70),data='Торговля со смещением',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7),
#                                         ft.Container(ft.ElevatedButton(content = ft.Text('\nИсторическая\nторговля',size=12,text_align='center',height=70),data='Историческая торговля',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=7),
#                                     ]),
#                                     width=280,
#                                     height=80,
#                                     margin=ft.margin.only(left=90),
#                                 ),
#                             ]),
#                             alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
#                     ),expand=2
#         )
        
#         return self.ferst_page