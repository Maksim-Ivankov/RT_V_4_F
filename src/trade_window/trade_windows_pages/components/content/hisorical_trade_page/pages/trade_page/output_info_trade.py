
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.graph_dohod.graph_dohod import Graph_dohod
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.graph_trade.graph_trade import Graph_trade

class Output_info_trade(ft.UserControl):#1
    def __init__(self,colback):
        super().__init__()
        self.pb = ft.ProgressBar(width=900,bgcolor=c_blue,color=c_yelow)
        self.colback = colback
        # self.number_folder = len(os.listdir(path_save_trade))
        self.number_folder = len(os.listdir(path_save_trade))+1
        self.number_trade = 0
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

        self.cl_graph_trade = Graph_trade(self.number_folder)
        
        
    def btn_graph_1(self,e):
        self.state_graph_btn = 'graph_1'
        self.colback('graph_1')

    def btn_graph_2(self,e):
        self.state_graph_btn = 'graph_2'
        self.colback('graph_2')
    
    def print_itog_and_graph(self,number_graph='graph_1',print_trade=''):
        # print(f'{number_graph}|{print_trade}')
        # готовим объект графика
        # cl_graph_trade = Graph_trade(self.number_folder,self.number_trade)
        # self.state_graph_print = {
        #     'graph_1': self.cl_graph_trade.print_page(self.number_trade),
        #     'graph_2': self.cl_graph_trade.print_page(self.number_trade,'min'),
        # }
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
                                        Graph_dohod(self.number_folder),
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
                                        Graph_dohod(self.number_folder),
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
                                                                Graph_dohod(self.number_folder),
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
    
    def print_page(self):
            
        self.trade_page = ft.Container(ft.Column(controls=[
            ft.Container(self.pb,margin=ft.margin.only(top=20,bottom=20),key='pb'),
            ft.Container(ft.Row(controls=[
                    ft.Container(
                                    ft.Container(ft.Column(controls=[ft.Column(controls=[
                                                    ft.Container(
                                                        ft.Container(ft.Text('Логи работы',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                        ft.Container(
                                                            ft.Container(
                                                                ft.Column(scroll=ft.ScrollMode.ALWAYS),
                                                                width=425,
                                                                height=400,
                                                                border = ft.border.all(1, c_white),
                                                                bgcolor=c_blue,
                                                                padding=10,
                                                            ),
                                                            width=425,
                                                            # border = ft.border.all(1, c_white),
                                                            # padding=14,
                                                            height = 400,
                                                            padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                                        )]),])),width=425,),
                                    ft.Container(ft.Container(
                                            ft.Column(controls=[ft.Column(controls=[
                                                        ft.Container(
                                                            ft.Container(ft.Text('Сделки',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                        ft.Container(
                                                            ft.Container(
                                                                ft.Column(scroll=ft.ScrollMode.ALWAYS),
                                                                width=425,
                                                                height=400,
                                                                border = ft.border.all(1, c_white),
                                                                bgcolor=c_blue,
                                                                padding=10,
                                                            ),
                                                            width=425,
                                                            # border = ft.border.all(1, c_white),
                                                            # padding=14,
                                                            height = 400,
                                                            padding=ft.padding.only(left=-1,top=-1,bottom=-1)    
                                                )]),])),width=425,),]),
                width=900,height=450,padding=ft.padding.only(left=20))
        ]),width=900)
        return self.trade_page

   
    def build(self):
        return self.print_page()

# import flet as ft
# from variable import *
# from imports import *

# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.graph_dohod.graph_dohod import Graph_dohod
# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.graph_trade.graph_trade import Graph_trade

# class Output_info_trade(ft.UserControl):#1
#     def __init__(self,colback):
#         super().__init__()
#         self.pb = ft.ProgressBar(width=900,bgcolor=c_blue,color=c_yelow)
#         self.colback = colback
#         # self.number_folder = len(os.listdir(path_save_trade))
#         self.number_folder = len(os.listdir(path_save_trade))+1
#         self.number_trade = 0
#         self.state_graph_btn = 'graph_1'
#         self.state_graph_btn_print = {
#             'graph_1': ft.Row(controls=[
#                 ft.Container(ft.Container(ft.Text('График сделки',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white)),on_click=self.btn_graph_1),
#                 ft.Container(ft.Container(ft.Text('Сделка',color=c_white,),padding=5,margin=ft.margin.only(bottom=-10)),on_click=self.btn_graph_2),
#             ]),
#             'graph_2': ft.Row(controls=[
#                 ft.Container(ft.Container(ft.Text('График сделки',color=c_white,),padding=5,margin=ft.margin.only(bottom=-10)),on_click=self.btn_graph_1),
#                 ft.Container(ft.Container(ft.Text('Сделка',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white)),on_click=self.btn_graph_2),
#             ]),
#         }

#         self.cl_graph_trade = Graph_trade(self.number_folder)
        
        
#     def btn_graph_1(self,e):
#         self.state_graph_btn = 'graph_1'
#         self.colback('graph_1')

#     def btn_graph_2(self,e):
#         self.state_graph_btn = 'graph_2'
#         self.colback('graph_2')
    
#     def print_itog_and_graph(self,number_graph='graph_1',print_trade=''):
#         # print(f'{number_graph}|{print_trade}')
#         # готовим объект графика
#         # cl_graph_trade = Graph_trade(self.number_folder,self.number_trade)
#         self.state_graph_print = {
#             'graph_1': self.cl_graph_trade.print_page(self.number_trade),
#             'graph_2': self.cl_graph_trade.print_page(self.number_trade,'min'),
#         }
#         self.state_graph_btn = number_graph
#         if print_trade!='':
#             # print('Рисуем не пустой график')
#             self.number_trade = int(print_trade)
#             self.trade_page_two = ft.Container(ft.Column(controls=[
#                 ft.Container(ft.Row(controls=[
#                         ft.Container(
#                                         ft.Container(ft.Column(controls=[ft.Column(controls=[
#                                                         ft.Container(
#                                                             ft.Container(ft.Text('Доходность',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
#                                                             ft.Container(
#                                                                 Graph_dohod(self.number_folder),
#                                                                 width=425,
#                                                                 height = 400,
#                                                                 padding=ft.padding.only(left=-1,top=-1,bottom=-1)
#                                                             )]),])),width=425,),
#                                         ft.Container(ft.Container(
#                                                 ft.Column(controls=[ft.Column(controls=[
#                                                             self.state_graph_btn_print[number_graph],
#                                                             ft.Container(
#                                                                 self.state_graph_print[number_graph],
#                                                                 width=425,
#                                                                 height = 400,
#                                                                 padding=ft.padding.only(left=-1,top=-1,bottom=-1)    
#                                                     )]),])),width=425,),]),
#                     width=900,height=450,padding=ft.padding.only(left=20))
#             ]),key='itog',width=900)
#         else:
#             # print('Нарисовали пустой')
#             self.trade_page_two = ft.Container(ft.Column(controls=[
#                 ft.Container(ft.Row(controls=[
#                         ft.Container(
#                                         ft.Container(ft.Column(controls=[ft.Column(controls=[
#                                                         ft.Container(
#                                                             ft.Container(ft.Text('Доходность',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
#                                                             ft.Container(
#                                                                 Graph_dohod(self.number_folder),
#                                                                 width=425,
#                                                                 height = 400,
#                                                                 padding=ft.padding.only(left=-1,top=-1,bottom=-1)
#                                                             )]),])),width=425,),
#                                         ft.Container(ft.Container(
#                                                 ft.Column(controls=[ft.Column(controls=[
#                                                             self.state_graph_btn_print[number_graph],
#                                                             ft.Container(
#                                                                 ft.Container(
#                                                                     ft.Text('Выберите сделку для отображения графика',text_align='CENTER'),
#                                                                     width=425,
#                                                                     height=400,
#                                                                     border = ft.border.all(1, c_white),
#                                                                     bgcolor=c_blue_binance,
#                                                                     padding=ft.padding.only(top=200)
#                                                                 ),
#                                                                 width=425,
#                                                                 height = 400,
#                                                                 padding=ft.padding.only(left=-1,top=-1,bottom=-1)    
#                                                     )]),])),width=425,),]),
#                     width=900,height=450,padding=ft.padding.only(left=20))
#             ]),key='itog',width=900)
#         return self.trade_page_two
    
#     def print_page(self):
            
#         self.trade_page = ft.Container(ft.Column(controls=[
#             ft.Container(self.pb,margin=ft.margin.only(top=20,bottom=20),key='pb'),
#             ft.Container(ft.Row(controls=[
#                     ft.Container(
#                                     ft.Container(ft.Column(controls=[ft.Column(controls=[
#                                                     ft.Container(
#                                                         ft.Container(ft.Text('Логи работы',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
#                                                         ft.Container(
#                                                             ft.Container(
#                                                                 ft.Column(scroll=ft.ScrollMode.ALWAYS),
#                                                                 width=425,
#                                                                 height=400,
#                                                                 border = ft.border.all(1, c_white),
#                                                                 bgcolor=c_blue,
#                                                                 padding=10,
#                                                             ),
#                                                             width=425,
#                                                             # border = ft.border.all(1, c_white),
#                                                             # padding=14,
#                                                             height = 400,
#                                                             padding=ft.padding.only(left=-1,top=-1,bottom=-1)
#                                                         )]),])),width=425,),
#                                     ft.Container(ft.Container(
#                                             ft.Column(controls=[ft.Column(controls=[
#                                                         ft.Container(
#                                                             ft.Container(ft.Text('Сделки',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
#                                                         ft.Container(
#                                                             ft.Container(
#                                                                 ft.Column(scroll=ft.ScrollMode.ALWAYS),
#                                                                 width=425,
#                                                                 height=400,
#                                                                 border = ft.border.all(1, c_white),
#                                                                 bgcolor=c_blue,
#                                                                 padding=10,
#                                                             ),
#                                                             width=425,
#                                                             # border = ft.border.all(1, c_white),
#                                                             # padding=14,
#                                                             height = 400,
#                                                             padding=ft.padding.only(left=-1,top=-1,bottom=-1)    
#                                                 )]),])),width=425,),]),
#                 width=900,height=450,padding=ft.padding.only(left=20))
#         ]),width=900)
#         return self.trade_page

   
#     def build(self):
#         return self.print_page()