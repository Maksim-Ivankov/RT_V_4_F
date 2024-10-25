
import flet as ft
from variable import *
from imports import *
#1
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.data_settings import print_our_settings,print_set_settings,print_mach_our_settings
from src.controllers.trade.core_trade import Core_trade
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.output_info_trade import Output_info_trade
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.one_settings.one_settings import One_settings_def
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.set_settings.set_settings import Set_settings_def

class Trade_page(ft.UserControl):#1
    def __init__(self,change_page,regime='one_set'):
        super().__init__()
        self.regime = regime
        self.change_page = change_page
        self.count_pb = 0
        self.output_info_trade = Output_info_trade(self.open_mini_graph_trade)
        self.change_trade_from_table = ''
        self.count_trade_table = 0
        self.count_trade_now = 0
    
    #ОТКРЫТЬ МИНИ ГРАФИК 
    def open_mini_graph_trade(self,number_graph):
        # print(f'Внутри графика по кнопке сделка и график сделки- {self.change_trade_from_table}')
        self.controls[0].content.content.content.controls.pop()
        self.controls[0].content.content.content.controls.append(self.output_info_trade.print_itog_and_graph(number_graph,self.change_trade_from_table))
        self.update()
        # print(self.controls[0].content.content.content.content.controls[0].content.controls[1].content.content.controls[0].controls[0].controls)

    # КЛИК ПО КНОПКЕ - НАЧАЛО ТОРГОВЛИ
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
        if self.count_trade_now == 0:
            data_add = ft.Container(ft.Text('Нет сделок',color=c_white,text_align='center'),height=30,bgcolor=c_blue_binance,width=400)
            self.controls[0].content.content.content.controls[3].content.controls[1].content.controls[1].content.content.controls[0].controls[1].content.content.controls.insert(0,data_add)
            self.update()
    
    # ДЛЯ ПРОГРЕССБАРА
    def change_pb(self,procent):
        self.output_info_trade.pb.value = procent
    
    # добавление текста в окно логов
    def add_logi_table(self,data):
        self.controls[0].content.content.content.controls[3].content.controls[1].content.controls[0].content.content.controls[0].controls[1].content.content.controls.insert(0,ft.Text(data))
        self.update()

    # обработка нажатия по сделке в окне сделок1
    def click_trade(self,e):
        self.change_trade_from_table = e.control.data
        self.controls[0].content.content.content.controls.pop()
        self.controls[0].content.content.content.controls.append(self.output_info_trade.print_itog_and_graph('graph_1',self.change_trade_from_table))
        self.update()
        
    # добавление сделок в окно сделок
    def add_trade_table(self,data):
        self.count_trade_now += 1
        if data['result'] == '+': 
            data_add = ft.Container(ft.Text(data['data'],color=c_blue,text_align='center'),data=str(self.count_trade_table),height=30,bgcolor=c_green,width=400,on_click=self.click_trade)
            self.count_trade_table+=1
        else: 
            data_add = ft.Container(ft.Text(data['data'],color=c_blue,text_align='center'),data=str(self.count_trade_table),height=30,bgcolor=c_red,width=400,on_click=self.click_trade)
            self.count_trade_table+=1
        self.controls[0].content.content.content.controls[3].content.controls[1].content.controls[1].content.content.controls[0].controls[1].content.content.controls.insert(0,data_add)
    
    # print('Отрисовали низ 1 раз после логов и сделок')
    def print_trade_end(self):
        self.controls[0].content.content.content.controls.append(self.output_info_trade.print_itog_and_graph('graph_1'))
        self.content.scroll_to(key="itog", duration=1000)


    # One_settings()
    def print_page(self):
        # ЕСЛИ РЕЖИМ - ОДНА НАСТРОЙКА
        if self.regime=='one_set':
            self.content = One_settings_def(print_our_settings,print_set_settings,self.change_page,self.start_trade)
            
        # ЕСЛИ РЕЖИМ - СЕТ НАСТРОЕК
        elif self.regime=='much_set':
            self.content = Set_settings_def(print_mach_our_settings,self.change_page,self.start_trade)
            
            
            
            
        self.trade_page = ft.Container(
            ft.Container(ft.Container(
                            self.content,
                            alignment=ft.alignment.center),
                            padding=ft.padding.only(top=10)
            ),expand=2)
        
        
        return self.trade_page

   
    def build(self):
        return self.print_page()
