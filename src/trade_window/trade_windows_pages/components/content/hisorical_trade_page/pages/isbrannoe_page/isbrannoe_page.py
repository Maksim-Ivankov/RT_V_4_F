
import flet as ft
from variable import *
from imports import *

# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.istoriya_treyd_page.UI.table_trade.table_trade import Table_trade

class Isbrannoe_page(ft.UserControl):
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page
        self.mas_print_card = []

    def print_name_card(self,name):
        if len(name)>30:
            return ft.Container(ft.Row(controls=[ft.Text(name,text_align='center',color=c_yelow,height=30)],scroll=ft.ScrollMode.ALWAYS),width=200,margin=ft.margin.only(top=10))
        else:
            return ft.Container(ft.Text(name,text_align='center',color=c_yelow,height=30),width=200,margin=ft.margin.only(top=10))

    def build(self):
        
        if len(os.listdir(path_favorites))==0:
            data_print_favorites = ft.Container(ft.Text('Добавьте избранные стратегии для отображения',text_align='center'),padding=ft.padding.only(top=220),width=850)
        else:
            for i in os.listdir(path_favorites): # итерируемся по папкам с сохранененными стратегиями
                if os.path.isfile(f'{path_favorites}\\{i}\\property.txt'):
                    with open(f'{path_favorites}\\{i}\\property.txt') as file: # открываем настройки стратегии, которую хотим сохранить
                        array_data_1 = [row.strip() for row in file]
                    self.mas_print_card.append(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(
                                    ft.Container(ft.Text(f'Стартегия {i}',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                    ft.Container(
                                        ft.Container(ft.Column(controls=[
                                                self.print_name_card(array_data_1[0]),
                                                # ft.Container(ft.Text(array_data_1[0],text_align='center',color=c_yelow),width=200),
                                                ft.Container(ft.Column(controls=[ft.Text(array_data_1[1],text_align='center')],scroll=ft.ScrollMode.ALWAYS,height=100),width=200),
                                                ft.Container(ft.Text('Трейдов: 15 | Сделок: 92',text_align='center'),width=200),
                                                ft.Container(ft.Text('Дневная доходность: 3.72%',text_align='center'),width=200,margin=ft.margin.only(bottom=8)),
                                                ft.Container(ft.Row(controls=[
                                                        ft.Container(ft.ElevatedButton(content = ft.Text('Смотреть трейды',size=12,),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30,width=150),
                                                        ft.Container(ft.Image(src='src/trade_window/trade_windows_pages/components/content/hisorical_trade_page/pages/isbrannoe_page/UI/img/pancil_blue.png'),bgcolor=c_yelow,width=30,height=30,padding=7,data={'page':'Избранные стратегии | Измеить данные стартегии','number_favorite':i},on_click=self.change_page),
                                                    ]),width=850,margin=ft.margin.only(left=5))
                                            ]),padding=5),
                                        width=210,
                                        height = 276,
                                        padding=ft.padding.only(left=-1,top=-1,bottom=-1),
                                        border=ft.border.all(1,c_white)
                                    )]
                        )
                    ))
                    
            data_print_favorites = ft.Row(
                controls=self.mas_print_card,
                wrap=True,
                spacing=10,
                run_spacing=10,
            )
                        
        
        self.ferst_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text('Избранные стратегии - стратегии с задаными настройками, которые были добавлены в избранное',size=12,color=c_white,text_align='center'),
                                             width=900,margin=ft.margin.only(bottom=15)),
                                ft.Container(
                                    data_print_favorites,
                                    width=900,
                                ),
                            ],scroll=ft.ScrollMode.ALWAYS,height=600),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.ferst_page