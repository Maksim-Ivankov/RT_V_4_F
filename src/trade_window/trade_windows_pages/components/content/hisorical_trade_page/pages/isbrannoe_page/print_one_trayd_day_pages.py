
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.graph_dohod.graph_dohod import Graph_dohod
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.isbrannoe_page.UI.graph_trade import Graph_trade

class Print_one_trayd_day_pages(ft.UserControl):
    def __init__(self,change_page,number_favorite,number_trade):
        super().__init__()
        self.change_page = change_page
        self.number_favorite = number_favorite
        self.number_trade = number_trade
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
        self.path_folder_favorites = f'{path_favorites}\\{self.number_favorite}\\folder_trade\\{self.number_trade}'
        self.cl_graph_trade = Graph_trade(self.number_favorite,self.number_trade)
        
        
        
    def btn_graph_1(self,e):
        self.state_graph_btn = 'graph_1'
        # self.colback('graph_1')
        # self.controls[0].content.content.content.controls.pop()
        # self.controls[0].content.content.content.controls.append(self.print_itog_and_graph(self.state_graph_btn,self.change_trade_from_table))
        self.controls[0].content.content.content.controls[1] = self.print_itog_and_graph(self.state_graph_btn,self.change_trade_from_table)
        self.update()

    def btn_graph_2(self,e):
        self.state_graph_btn = 'graph_2'
        # self.colback('graph_2')
        # self.controls[0].content.content.content.controls.pop()
        # self.controls[0].content.content.content.controls.append(self.print_itog_and_graph(self.state_graph_btn,self.change_trade_from_table))
        self.controls[0].content.content.content.controls[1] = self.print_itog_and_graph(self.state_graph_btn,self.change_trade_from_table)
        self.update()
        
    # собираем данные для отрисовки логов в окне логов
    def def_print_log(self):
        log_mas = []
        path_settings = f'{self.path_folder_favorites}\\log_trade.txt'
        if os.path.isfile(path_settings):
            with open(path_settings) as file:
                array_data_row = [row.strip() for row in file]
                for i in array_data_row:
                    if int(i.split('|')[0])>20:
                        if i.split('|')[3]=='no':
                            log_mas.append(ft.Container(ft.Text(
                                f'{i.split('|')[0]} | Депозит {i.split('|')[1]} | нет сигнала',
                            )))
                        else:
                            log_mas.append(ft.Container(ft.Text(
                                f'{i.split('|')[0]} | Депозит {i.split('|')[1]} | Сделка {i.split('|')[3]} {i.split('|')[4]}',
                            )))
        return log_mas        
        
    # данные для отрисовки сделок в окне сделок
    def def_print_trade(self):
        trade_mas = []
        path_settings = f'{self.path_folder_favorites}\\trade.txt'
        if os.path.isfile(path_settings):
            with open(path_settings) as file:
                array_data_row = [row.strip() for row in file]
                count_trade_table = 0
                for i in array_data_row:
                    if float(i.split('|')[3]) > 0: 
                        trade_mas.append(ft.Container(ft.Text(f'{i.split('|')[0]} | Результат {i.split('|')[3]} | Монета {i.split('|')[6]}',color=c_blue,text_align='center'),data=str(count_trade_table),height=30,bgcolor=c_green,width=400,on_click=self.click_trade))
                        count_trade_table+=1
                    else: 
                        trade_mas.append(ft.Container(ft.Text(f'{i.split('|')[0]} | Результат {i.split('|')[3]} | Монета {i.split('|')[6]}',color=c_blue,text_align='center'),data=str(count_trade_table),height=30,bgcolor=c_red,width=400,on_click=self.click_trade))
                        count_trade_table+=1
        else:
            trade_mas.append(ft.Container(ft.Text('Нет сделок',color=c_white,text_align='center'),height=30,bgcolor=c_blue_binance,width=400))
        return trade_mas

    def print_itog_and_graph(self,number_graph='graph_1',print_trade=''):
        self.state_graph_btn = number_graph
        if print_trade!='':
            if number_graph == 'graph_1':
                # print('Слетает')
                # print('Рисуем график большой')
                # print('Рисуем не пустой график')
                self.number_trade_for_click = int(print_trade)
                self.trade_page_two = ft.Container(ft.Column(controls=[
                    ft.Container(ft.Row(controls=[
                        ft.Container(
                            ft.Container(ft.Column(controls=[ft.Column(controls=[
                                ft.Container(
                                    ft.Container(ft.Text('Доходность',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                    ft.Container(
                                        Graph_dohod(self.number_favorite,'favorites',self.number_trade),
                                        width=425,
                                        height = 400,
                                        padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                    )]),])),width=425,),
                            ft.Container(ft.Container(
                                ft.Column(controls=[ft.Column(controls=[
                                            self.state_graph_btn_print[number_graph],
                                            ft.Container(
                                                self.cl_graph_trade.print_page(self.number_trade_for_click),
                                                width=425,
                                                height = 400,
                                                padding=ft.padding.only(left=-1,top=-1,bottom=-1)    
                                    )]),])),width=425,),]),
                    width=900,height=450,padding=ft.padding.only(left=20))
                ]),key='itog',width=900)
            else:
                # print('Рисуем график малый')
                # print('Рисуем не пустой график')
                self.number_trade_for_click = int(print_trade)
                self.trade_page_two = ft.Container(ft.Column(controls=[
                    ft.Container(ft.Row(controls=[
                        ft.Container(
                            ft.Container(ft.Column(controls=[ft.Column(controls=[
                                ft.Container(
                                    ft.Container(ft.Text('Доходность',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                    ft.Container(
                                        Graph_dohod(self.number_favorite,'favorites',self.number_trade),
                                        width=425,
                                        height = 400,
                                        padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                    )]),])),width=425,),
                            ft.Container(ft.Container(
                                ft.Column(controls=[ft.Column(controls=[
                                            self.state_graph_btn_print[number_graph],
                                            ft.Container(
                                                self.cl_graph_trade.print_page(self.number_trade_for_click,'min'),
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
                                                                Graph_dohod(self.number_favorite,'favorites',self.number_trade),
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
        # self.controls[0].content.content.content.controls.pop()
        # self.controls[0].content.content.content.controls.append(self.print_itog_and_graph('graph_1',self.change_trade_from_table))
        self.controls[0].content.content.content.controls[1] = self.print_itog_and_graph('graph_1',self.change_trade_from_table)
        self.update()

    def build(self):    
        
        if os.path.isfile(f'{path_favorites}\\{self.number_favorite}\\property.txt'):
            with open(f'{path_favorites}\\{self.number_favorite}\\property.txt') as file: # открываем настройки стратегии, которую хотим сохранить
                array_data_2 = [row.strip() for row in file]
                 
        self.content = ft.Column(controls=[
            # ft.Container(
            #     ft.Column(
            #         controls=[
            #             ft.Container(
            #                 ft.Container(
            #                     ft.Container(
            #                         ft.Row(controls=[
            #                             ft.Container(ft.ElevatedButton(content = ft.Text('Назад',size=12,),data={'page':'Избранные стратегии | Показать трейды','number_favorite':self.number_favorite,'name_favorite':array_data_2[0]},on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
            #                         ]),width=240),alignment=ft.alignment.center),height=60,margin=ft.margin.only(top=-14,left=-10,right=-10,bottom=0)      
            #             ),
            #         ]
            #     ),expand=2
            # ),
            #------------------------------
            #------------------------------------------
            ft.Container(ft.Row(controls=[ft.Container(
                ft.Container(ft.Column(controls=[ft.Column(controls=[
                                ft.Container(
                                    ft.Container(ft.Text('Логи работы',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                    ft.Container(
                                        ft.Container(
                                            ft.Column(controls=self.def_print_log(),scroll=ft.ScrollMode.ALWAYS),
                                            width=425,
                                            height=260,
                                            border = ft.border.all(1, c_white),
                                            bgcolor=c_blue,
                                            padding=10,
                                        ),
                                        width=425,
                                        height = 260,
                                        padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                    )]),])),width=425,),
                ft.Container(ft.Container(
                        ft.Column(controls=[ft.Column(controls=[
                                    ft.Container(
                                        ft.Container(ft.Text('Сделки',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                    ft.Container(
                                        ft.Container(
                                            ft.Column(controls=self.def_print_trade(),scroll=ft.ScrollMode.ALWAYS),
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
            self.print_itog_and_graph(),
            
            ft.Container(
                ft.Column(
                    controls=[
                        ft.Container(
                            ft.Container(
                                ft.Container(
                                    ft.Row(controls=[
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Назад',size=12,),data={'page':'Избранные стратегии | Показать трейды','number_favorite':self.number_favorite,'name_favorite':array_data_2[0]},on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                    ]),width=86),alignment=ft.alignment.center),height=60,margin=ft.margin.only(top=-14,left=-10,right=-10,bottom=0)      
                        ),
                    ]
                ),expand=2
            ),
                          
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