
import flet as ft
from variable import *
from imports import *

# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.istoriya_treyd_page.UI.table_trade.table_trade import Table_trade
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.set_settings.page_trade.UI.data_settings import def_print_our_settings,def_print_set_settings,def_print_log,def_print_trade

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.graph_dohod.graph_dohod import Graph_dohod
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.graph_trade.graph_trade import Graph_trade

class Trade_page(ft.UserControl):
    def __init__(self,number_folder,number_trade_folder,strategy_now):
        super().__init__()
        self.number_trade_folder = number_trade_folder
        self.number_folder = number_folder
        self.strategy_now = strategy_now
        self.number_trade = 0
        self.change_trade_from_table = ''
        self.state_graph_btn = 'graph_1'
        self.state_graph_btn_print = {
            'graph_1': ft.Row(controls=[
                ft.Container(ft.Container(ft.Text('График сделки',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white)),on_click=self.btn_graph_1),
                ft.Container(ft.Container(ft.Text('Сделка',color=c_white,),padding=5,margin=ft.margin.only(bottom=-10)),on_click=self.btn_graph_2),
            ]),
            'graph_2': ft.Row(controls=[
                ft.Container(ft.Container(ft.Text('График сделки',color=c_white,),padding=5,margin=ft.margin.only(bottom=-10)),on_click=self.btn_graph_1),
                ft.Container(ft.Container(ft.Text('Сделка',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white)),on_click=self.btn_graph_2),
            ]),
        }

        self.cl_graph_trade = Graph_trade(self.number_folder,'set',self.number_trade_folder)
        
    def btn_graph_1(self,e):
        self.state_graph_btn = 'graph_1'
        # self.colback('graph_1')
        self.controls[0].content.content.content.controls.pop()
        self.controls[0].content.content.content.controls.append(self.print_itog_and_graph(self.state_graph_btn,self.change_trade_from_table))
        self.update()

    def btn_graph_2(self,e):
        self.state_graph_btn = 'graph_2'
        # self.colback('graph_2')
        self.controls[0].content.content.content.controls.pop()
        self.controls[0].content.content.content.controls.append(self.print_itog_and_graph(self.state_graph_btn,self.change_trade_from_table))
        self.update()


    def print_itog_and_graph(self,number_graph='graph_1',print_trade=''):
        # print(f'{number_graph}|{print_trade}')
        # готовим объект графика1
        # cl_graph_trade = Graph_trade(self.number_folder,self.number_trade)
        self.state_graph_print = {
            'graph_1': self.cl_graph_trade.print_page(self.number_trade),
            'graph_2': self.cl_graph_trade.print_page(self.number_trade,'min'),
        }
        self.state_graph_btn = number_graph
        if print_trade!='':
            if number_graph == 'graph_1':
                # print('Рисуем график большой')
                # print('Рисуем не пустой график')
                self.number_trade = int(print_trade)
                self.trade_page_two = ft.Container(ft.Column(controls=[
                    ft.Container(ft.Row(controls=[
                        ft.Container(
                            ft.Container(ft.Column(controls=[ft.Column(controls=[
                                ft.Container(
                                    ft.Container(ft.Text('Доходность',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                    ft.Container(
                                        Graph_dohod(self.number_folder,'set',self.number_trade_folder),
                                        width=425,
                                        height = 400,
                                        padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                    )]),])),width=425,),
                            ft.Container(ft.Container(
                                ft.Column(controls=[ft.Column(controls=[
                                            self.state_graph_btn_print[number_graph],
                                            ft.Container(
                                                self.cl_graph_trade.print_page(self.number_trade),
                                                width=425,
                                                height = 400,
                                                padding=ft.padding.only(left=-1,top=-1,bottom=-1)    
                                    )]),])),width=425,),]),
                    width=900,height=450,padding=ft.padding.only(left=20))
                ]),key='itog',width=900)
            else:
                # print('Рисуем график малый')
                # print('Рисуем не пустой график')
                self.number_trade = int(print_trade)
                self.trade_page_two = ft.Container(ft.Column(controls=[
                    ft.Container(ft.Row(controls=[
                        ft.Container(
                            ft.Container(ft.Column(controls=[ft.Column(controls=[
                                ft.Container(
                                    ft.Container(ft.Text('Доходность',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                    ft.Container(
                                        Graph_dohod(self.number_folder,'set',self.number_trade_folder),
                                        width=425,
                                        height = 400,
                                        padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                    )]),])),width=425,),
                            ft.Container(ft.Container(
                                ft.Column(controls=[ft.Column(controls=[
                                            self.state_graph_btn_print[number_graph],
                                            ft.Container(
                                                self.cl_graph_trade.print_page(self.number_trade,'min'),
                                                width=425,
                                                height = 400,
                                                padding=ft.padding.only(left=-1,top=-1,bottom=-1)    
                                    )]),])),width=425,),]),
                    width=900,height=450,padding=ft.padding.only(left=20))
                ]),key='itog',width=900)
        else:
            # print('Нарисовали пустой')
            self.trade_page_two = ft.Container(ft.Column(controls=[
                ft.Container(ft.Row(controls=[
                        ft.Container(
                                        ft.Container(ft.Column(controls=[ft.Column(controls=[
                                                        ft.Container(
                                                            ft.Container(ft.Text('Доходность',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                            ft.Container(
                                                                Graph_dohod(self.number_folder,'set',self.number_trade_folder),
                                                                width=425,
                                                                height = 400,
                                                                padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                                            )]),])),width=425,),
                                        ft.Container(ft.Container(
                                                ft.Column(controls=[ft.Column(controls=[
                                                            self.state_graph_btn_print[number_graph],
                                                            ft.Container(
                                                                ft.Container(
                                                                    ft.Text('Выберите сделку для отображения графика',text_align='CENTER'),
                                                                    width=425,
                                                                    height=400,
                                                                    border = ft.border.all(1, c_white),
                                                                    bgcolor=c_blue_binance,
                                                                    padding=ft.padding.only(top=200)
                                                                ),
                                                                width=425,
                                                                height = 400,
                                                                padding=ft.padding.only(left=-1,top=-1,bottom=-1)    
                                                    )]),])),width=425,),]),
                    width=900,height=450,padding=ft.padding.only(left=20))
            ]),key='itog',width=900)
        return self.trade_page_two

    # обработка нажатия по сделке в окне сделок1
    def click_trade(self,e):
        # print(e.control.data)
        self.change_trade_from_table = e.control.data
        self.controls[0].content.content.content.controls.pop()
        self.controls[0].content.content.content.controls.append(self.print_itog_and_graph('graph_1',self.change_trade_from_table))
        self.update()


    def build(self):
        self.content = ft.Column(controls=[
                                # ft.Container(ft.Text('Проверьте настройки и запустите торговлю',size=12,color=c_white,text_align='center'),padding=ft.padding.only(left=320)),
                                ft.Container(
                                    ft.Row(controls=[
                                        ft.Container(ft.Container(
                                            ft.Column(controls=[
                                                ft.Column(
                                                    controls=[
                                                        ft.Container(
                                                            ft.Container(ft.Text('Общие настройки робота',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                            ft.Container(
                                                                ft.Container(
                                                                    def_print_our_settings(self.number_folder,self.number_trade_folder,self.strategy_now),
                                                                    width=500,
                                                                    height=148,
                                                                    border = ft.border.all(1, c_white),
                                                                    bgcolor=c_blue,
                                                                ),
                                                                width=500,
                                                                height = 148,
                                                                padding=ft.padding.only(left=-1,top=-1,bottom=-1)

                                        )]),])),width=500,),
                                        ft.Container(
                                            ft.Container(
                                                ft.Column(controls=[
                                                    ft.Column(
                                                        controls=[
                                                            ft.Container(
                                                                ft.Container(ft.Text('Настройки стратегий',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                            ft.Container(
                                                                ft.Container(
                                                                    # print_set_settings,
                                                                    def_print_set_settings(self.number_folder,self.number_trade_folder,self.strategy_now),
                                                                    width=350,
                                                                    height=148,
                                                                    border = ft.border.all(1, c_white),
                                                                    bgcolor=c_blue,
                                                                ),
                                                                width=350,
                                                                height = 148,
                                                                padding=ft.padding.only(left=-1,top=-1,bottom=-1)    
                                        )]),])),width=400,)
                                        ]),
                                width=900,padding=ft.padding.only(left=20)),
                                
                                ft.Container(ft.Row(controls=[ft.Container(
                                    ft.Container(ft.Column(controls=[ft.Column(controls=[
                                                    ft.Container(
                                                        ft.Container(ft.Text('Логи работы',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                        ft.Container(
                                                            ft.Container(
                                                                ft.Column(controls=def_print_log(self.number_folder,self.number_trade_folder,self.strategy_now),scroll=ft.ScrollMode.ALWAYS),
                                                                width=425,
                                                                height=260,
                                                                border = ft.border.all(1, c_white),
                                                                bgcolor=c_blue,
                                                                padding=10,
                                                            ),
                                                            width=425,
                                                            # border = ft.border.all(1, c_white),
                                                            # padding=14,
                                                            height = 260,
                                                            padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                                        )]),])),width=425,),
                                    ft.Container(ft.Container(
                                            ft.Column(controls=[ft.Column(controls=[
                                                        ft.Container(
                                                            ft.Container(ft.Text('Сделки',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                        ft.Container(
                                                            ft.Container(
                                                                ft.Column(controls=def_print_trade(self.number_folder,self.click_trade,self.number_trade_folder,self.strategy_now),scroll=ft.ScrollMode.ALWAYS),
                                                                width=425,
                                                                height=260,
                                                                border = ft.border.all(1, c_white),
                                                                bgcolor=c_blue,
                                                                padding=10,
                                                            ),
                                                            width=425,
                                                            # border = ft.border.all(1, c_white),
                                                            # padding=14,
                                                            height = 260,
                                                            padding=ft.padding.only(left=-1,top=-1,bottom=-1)    
                                                )]),])),width=425,),]),
                width=900,height=295,padding=ft.padding.only(left=20)),
                self.print_itog_and_graph()



                                
                            ],scroll=ft.ScrollMode.ALWAYS,height=550)
        
        self.trade_page = ft.Container(
            ft.Container(
                        ft.Container(
                            self.content,
                            alignment=ft.alignment.center),
                            padding=ft.padding.only(top=10)
                    ),expand=2
        )
        
        return self.trade_page
    


