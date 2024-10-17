
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.data_settings import print_our_settings,print_set_settings
from src.controllers.trade.core_trade import Core_trade
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.output_info_trade import Output_info_trade

class Trade_page(ft.UserControl):#1
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page
        self.count_pb = 0
        self.output_info_trade = Output_info_trade(self.open_mini_graph_trade)
        self.change_trade_from_table = ''
        self.count_trade_table = 0
        
    def open_mini_graph_trade(self,number_graph):
        print(f'Внутри графика по кнопке сделка и график сделки- {self.change_trade_from_table}')
        self.controls[0].content.content.content.controls.pop()
        self.controls[0].content.content.content.controls.append(self.output_info_trade.print_itog_and_graph(number_graph,self.change_trade_from_table))
        self.update()
        # print(self.controls[0].content.content.content.content.controls[0].content.controls[1].content.content.controls[0].controls[0].controls)

    def start_trade(self,e):
        regime = 'Историческая торговля|Свободный фрейм|Ода настройка'
        config = configparser.ConfigParser()  
        config.read(path_imports_config)
        strategy = literal_eval(config.get('param_trade_historical_trade_svobodniy_freym', 'strategys'))
        core_trade_ob = Core_trade(regime,strategy)
        self.controls[0].content.content.content.controls.append(self.output_info_trade.print_page())
        self.controls[0].content.content.content.height=600
        self.content.scroll_to(key="pb", duration=1000)
        self.myThread = threading.Thread(target=core_trade_ob.start_trade(self.change_pb,self.add_logi_table,self.add_trade_table,self.print_trade_end), args=(), daemon=True)
        self.myThread.start()
        
    def change_pb(self,procent):
        self.output_info_trade.pb.value = procent
    
    # добавление текста в окно логов
    def add_logi_table(self,data):
        self.controls[0].content.content.content.controls[3].content.controls[1].content.controls[0].content.content.controls[0].controls[1].content.content.controls.insert(0,ft.Text(data))
        self.update()

    # обработка нажатия по сделке в окне сделок
    def click_trade(self,e):

        # print(e.control.data) # здесь все четко, проблема тут, но глубже
        self.change_trade_from_table = e.control.data
        self.controls[0].content.content.content.controls.pop()
        self.controls[0].content.content.content.controls.append(self.output_info_trade.print_itog_and_graph('graph_1',self.change_trade_from_table))
        self.update()
        
    # добавление сделок в окно сделок
    def add_trade_table(self,data):
        if data['result'] == '+': 
            data_add = ft.Container(ft.Text(data['data'],color=c_blue,text_align='center'),data=str(self.count_trade_table),height=30,bgcolor=c_green,width=400,on_click=self.click_trade)
            self.count_trade_table+=1
        else: 
            data_add = ft.Container(ft.Text(data['data'],color=c_blue,text_align='center'),data=str(self.count_trade_table),height=30,bgcolor=c_red,width=400,on_click=self.click_trade)
            self.count_trade_table+=1
        self.controls[0].content.content.content.controls[3].content.controls[1].content.controls[1].content.content.controls[0].controls[1].content.content.controls.insert(0,data_add)
    
    def print_trade_end(self):
        # print('Отрисовали низ 1 раз после логов и сделок')
        self.controls[0].content.content.content.controls.append(self.output_info_trade.print_itog_and_graph('graph_1'))
        self.content.scroll_to(key="itog", duration=1000)



    def print_page(self):
        self.content = ft.Column(controls=[
                                ft.Container(ft.Text('Проверьте настройки и запустите торговлю',size=12,color=c_white,text_align='center'),padding=ft.padding.only(left=320)),
                                ft.Container(
                                    ft.Row(controls=[
                                    ft.Container(
                                    ft.Container(
                                        ft.Column(controls=[
                                            ft.Column(
                                                controls=[
                                                    ft.Container(
                                                        ft.Container(ft.Text('Общие настройки робота',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                        ft.Container(
                                                            ft.Container(
                                                                print_our_settings,
                                                                width=500,
                                                                height=148,
                                                                border = ft.border.all(1, c_white),
                                                                bgcolor=c_blue,
                                                            ),
                                                            width=500,
                                                            height = 148,
                                                            padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                                        
                                                        )]),     
                                    ])),
                                    width=500,
                                    ),
                                    ft.Container(
                                        ft.Container(
                                            ft.Column(controls=[
                                                ft.Column(
                                                    controls=[
                                                        ft.Container(
                                                            ft.Container(ft.Text('Настройки стратегий',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                        ft.Container(
                                                            ft.Container(
                                                                print_set_settings,
                                                                width=350,
                                                                height=148,
                                                                border = ft.border.all(1, c_white),
                                                                bgcolor=c_blue,
                                                            ),
                                                            width=350,
                                                            height = 148,
                                                            padding=ft.padding.only(left=-1,top=-1,bottom=-1)    
                                                )]),     
                                        ])),
                                        width=400,
                                    ),
                                    ]),
                                width=900,padding=ft.padding.only(left=20)),
                                ft.Container(
                                    ft.Container(
                                        ft.Row(controls=[
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Назад',size=12,),data='Выбрать режим торговли',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Запустить торговлю',size=12,),data='Выбрать режим торговли',bgcolor=c_yelow,on_click=self.start_trade,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                    ]),padding=ft.padding.only(left=320,top=10)
                                    ),
                                    width=500,
                                ),
                                
                            ],scroll=ft.ScrollMode.ALWAYS)
        
        self.trade_page = ft.Container(
            ft.Container(
                        ft.Container(
                            self.content,
                            alignment=ft.alignment.center),
                            padding=ft.padding.only(top=10)
                    ),expand=2
        )
        
        
        return self.trade_page

   
    def build(self):
        return self.print_page()
