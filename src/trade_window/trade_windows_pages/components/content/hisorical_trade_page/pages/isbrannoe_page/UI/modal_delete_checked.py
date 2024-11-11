
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_coin.component_change_strategy_coin import Component_change_strategy_coin


class Modal_delete_checked(ft.UserControl):
    def __init__(self,name_strat,change_page,number_favorite,regime):
        super().__init__()
        self.name_strat = name_strat
        self.change_page = change_page
        self.number_favorite = number_favorite
        self.regime = regime
     
     
    def delete_favorite(self,e):
        shutil.rmtree(f'{path_favorites}\\{self.number_favorite}')
        self.change_page(e)
        self.controls[0].open = False
        self.update()
        
    def clear_favorite(self,e):
        if len(os.listdir(f'{path_favorites}\\{self.number_favorite}\\folder_trade'))>0:
            for i in os.listdir(f'{path_favorites}\\{self.number_favorite}\\folder_trade'):
                shutil.rmtree(f'{path_favorites}\\{self.number_favorite}\\folder_trade\\{i}')
        self.change_page(e)
        self.controls[0].open = False
        self.update()
    
    
    def close_modal(self,e):
        self.controls[0].open = False
        self.update()
        

    def build(self):
            
        if self.regime == 'delete':
            self.cgange_coin_window = ft.BottomSheet(
                    ft.Container(
                        ft.Container(ft.Column(controls=[
                            ft.Container(ft.Text('Подтверждение удаления',color=c_blue,size=14,text_align='center'),width=444,height=28,bgcolor=c_yelow,padding=ft.padding.only(top=5)),
                            ft.Container(ft.Text(f'Вы точно хотите удалить торговую стратегию "{self.name_strat}"? ',color=c_white,size=12,text_align='center'),width=444),
                            ft.Container(ft.Row(controls=[
                                ft.Container(ft.ElevatedButton(content = ft.Text('Да, удалить',size=12,),data='Избранные стратегии',on_click=self.delete_favorite,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30,margin=ft.margin.only(right=40)),
                                ft.Container(ft.ElevatedButton(content = ft.Text('Нет, оставить',size=12,),on_click=self.close_modal,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                            ]),margin=ft.margin.only(left=80,top=20))
                        ])),
                        width=444,
                        height=150,
                        bgcolor=c_blue,
                        border=ft.border.all(1,c_white),
                        # margin=ft.margin.only(bottom=500,)
                        margin=ft.margin.only(bottom=320,top=-100)
                        ),
                    open=True,
                    bgcolor='transparent',
                    elevation = 0
                )
        elif self.regime == 'clear':
            self.cgange_coin_window = ft.BottomSheet(
                    ft.Container(
                        ft.Container(ft.Column(controls=[
                            ft.Container(ft.Text('Подтверждение очистки',color=c_blue,size=14,text_align='center'),width=444,height=28,bgcolor=c_yelow,padding=ft.padding.only(top=5)),
                            ft.Container(ft.Text(f'Вы точно хотите очистить трейды торговой стратегии "{self.name_strat}"? Вернуть трейды обратно можно будет только если снова проторговать данные на стратегии.',color=c_white,size=12,text_align='center'),width=444,padding=10),
                            ft.Container(ft.Row(controls=[
                                ft.Container(ft.ElevatedButton(content = ft.Text('Да, очистить',size=12,),data='Избранные стратегии',on_click=self.clear_favorite,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30,margin=ft.margin.only(right=40)),
                                ft.Container(ft.ElevatedButton(content = ft.Text('Нет, оставить',size=12,),on_click=self.close_modal,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                            ]),margin=ft.margin.only(left=80,top=10))
                        ])),
                        width=444,
                        height=180,
                        bgcolor=c_blue,
                        border=ft.border.all(1,c_white),
                        # margin=ft.margin.only(bottom=500,)
                        margin=ft.margin.only(bottom=290,top=-100)
                        ),
                    open=True,
                    bgcolor='transparent',
                    elevation = 0
                )

        
        return self.cgange_coin_window