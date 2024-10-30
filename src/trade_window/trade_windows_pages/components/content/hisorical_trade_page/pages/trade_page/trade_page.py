
import flet as ft
from variable import *
from imports import *
#1
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.data_settings import print_our_settings,print_set_settings,print_mach_our_settings
from src.controllers.trade.core_trade import Core_trade
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.output_info_trade import Output_info_trade
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.one_settings.one_settings import One_settings_def
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.set_settings.set_settings import Set_settings_def
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.set_settings.flex_card import Flex_card
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.set_settings.UI.table_result import Table_result
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.set_settings.page_trade.result_trqade_page import Result_trqade_page

class Trade_page(ft.UserControl):#1
    def __init__(self,change_page,regime='one_set'):
        super().__init__()
        self.regime = regime
        self.change_page = change_page
        self.count_pb = 0
        self.output_info_trade = Output_info_trade(self.open_mini_graph_trade)
        self.flex_card = Flex_card()
        self.change_trade_from_table = ''
        self.count_trade_table = 0
        self.count_trade_now = 0
        self.our_frame = []
    
    #ОТКРЫТЬ МИНИ ГРАФИК 
    def open_mini_graph_trade(self,number_graph):
        # print(f'Внутри графика по кнопке сделка и график сделки- {self.change_trade_from_table}')
        self.controls[0].content.content.content.controls.pop()
        self.controls[0].content.content.content.controls.append(self.output_info_trade.print_itog_and_graph(number_graph,self.change_trade_from_table))
        self.update()
        # print(self.controls[0].content.content.content.content.controls[0].content.controls[1].content.content.controls[0].controls[0].controls)

    # КЛИК ПО КНОПКЕ - НАЧАЛО ТОРГОВЛИ
    def start_trade(self,e):
        if self.regime=='one_set':
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
        elif self.regime=='much_set':
            self.table_result = Table_result(self.reptint_table_result,self.print_page_one_trade_oura_set)
            # получаем кол-во настроек в сете
            config_set = configparser.ConfigParser()  
            config_set.read(path_ini_general_set)
            count_set_trade = len(config_set.sections())
            
            # Flex_card
            self.controls[0].content.content.content.controls.append(self.flex_card.print_page(count_set_trade))
            self.controls[0].content.content.content.height=600
            # self.content.scroll_to(key="pb", duration=1000)
            self.update()
            regime = 'Историческая торговля|Свободный фрейм|Сет настроек'
            config = configparser.ConfigParser()  
            config.read(path_imports_config)
            strategy = literal_eval(config.get('param_trade_historical_trade_svobodniy_freym', 'strategys'))
            core_trade_ob = Core_trade(regime,strategy)
            # print(self.controls[0].content.content.content.controls[4].content.controls[0].content.controls)
            # print(self.controls[0].content.content.content.controls[4].content.controls[0].content.controls[0].controls)
            # print(len(self.controls[0].content.content.content.controls[4].content.controls[0].content.controls[0].controls))
            for number_trade in range(1,count_set_trade+1):
                self.number_trade_in_set_settings = number_trade
                # Получаем карточку, с которой будем работать на текущем шаге
                count_td = len(self.controls[0].content.content.content.controls[4].content.controls[0].content.controls[0].controls) # [Row(), Row()]
                if float(self.number_trade_in_set_settings/count_td)<1.00001:
                    self.count_element_tr = 0
                    if self.number_trade_in_set_settings%count_td == 0:
                        self.count_element_td = len(self.controls[0].content.content.content.controls[4].content.controls[0].content.controls[0].controls)-1 # заходим в первый row и получаем длину ряда
                    else:self.count_element_td = int(self.number_trade_in_set_settings)-1
                else: 
                    self.count_element_tr = int((int(self.number_trade_in_set_settings)-1)/count_td)
                    if self.number_trade_in_set_settings%count_td == 0:
                        self.count_element_td = len(self.controls[0].content.content.content.controls[4].content.controls[0].content.controls[0].controls)-1 # заходим в первый row и получаем длину ряда
                    else:self.count_element_td = int(self.number_trade_in_set_settings%count_td)-1
                # print(self.controls[0].content.content.content.controls[4].content.controls[0].content.controls[self.count_element_tr].controls[self.count_element_td].content.controls[1].content)
                # print(number_trade)
                self.treyd_polosa = []
                self.treyd_polosa[:] = []
                self.content.scroll_to(key=str(number_trade), duration=1000)
                self.myThread = threading.Thread(target=core_trade_ob.start_trade(self.change_pb,self.add_logi_table,self.add_trade_table,self.print_trade_end,number_trade), args=(), daemon=True)
                self.myThread.start()
            self.controls[0].content.content.content.controls.append(self.table_result.print_page(self.update_component))
            self.content.scroll_to(key="table_result", duration=1000)
            self.update()
            
            # Сохраянем сеты настроек в папку торговли1
            shutil.copy(
               os.path.join(path_appdata, 'general_set.ini'),
               os.path.join(f'{path_save_trade}\\{len(os.listdir(path_save_trade))}') # путь сохранения логов в папке трейда)
            )
            for i in strategy:
                shutil.copy(
                       os.path.join(path_appdata, f'{i}_set.ini'),
                       os.path.join(f'{path_save_trade}\\{len(os.listdir(path_save_trade))}') # путь сохранения логов в папке трейда)
                )
            self.strategy_now = strategy
                    
                    

    
    # перерисовывает таблицу результатов
    def reptint_table_result(self,regime):
        self.controls[0].content.content.content.controls.pop()
        self.controls[0].content.content.content.controls.append(self.table_result.print_page(self.update_component,regime))
        self.update()
    
    # просто обновляет self
    def update_component(self):
        self.update()
        
    # возвращаемся на страницу торговли по сету настроек после клика по таблице результатов
    def return_old_data(self,e):
        self.controls[:] = []
        self.controls.append(self.trade_page)
        self.update()
        self.content.scroll_to(key="table_result", duration=1000)
        
        
    # открыть страницу с трейдом из таблицы результатов торговли по сету настроек
    def print_page_one_trade_oura_set(self,number_trade):
        # self.our_frame = self.controls.copy()
        self.our_frame = list(self.controls)
        self.controls[:] = []
        self.controls.append(Result_trqade_page(self.return_old_data,number_trade,self.strategy_now))
        self.update()
    
    # ДЛЯ ПРОГРЕССБАРА
    def change_pb(self,procent,data={}):
        if self.regime=='one_set':
            self.output_info_trade.pb.value = procent
        elif self.regime=='much_set':
            # print(procent)
            
            if data!={}:
                if data['result'] == '+':
                    self.treyd_polosa.append(ft.Container(ft.Text(data['data'],color=c_blue,text_align='CENTER',size=12),bgcolor=c_green,width=150,height=20))
                else:
                    self.treyd_polosa.append(ft.Container(ft.Text(data['data'],color=c_white,text_align='CENTER',size=12),bgcolor=c_red,width=150,height=20))
                self.treyd_polosa = list(reversed(self.treyd_polosa))
            self.controls[0].content.content.content.controls[4].content.controls[0].content.controls[self.count_element_tr].controls[self.count_element_td].content.controls[1].content.bgcolor=c_blue
            self.controls[0].content.content.content.controls[4].content.controls[0].content.controls[self.count_element_tr].controls[self.count_element_td].content.controls[1].content.padding=10
            self.controls[0].content.content.content.controls[4].content.controls[0].content.controls[self.count_element_tr].controls[self.count_element_td].content.controls[1].content.content = ft.Column(controls=[
                ft.Container(ft.Column(controls=self.treyd_polosa,scroll=ft.ScrollMode.ALWAYS),height=150),
                ft.Container(ft.ProgressBar(width=150,bgcolor=c_blue,color=c_yelow,value=procent))
            ])
            if procent>0.99:
                self.controls[0].content.content.content.controls[4].content.controls[0].content.controls[self.count_element_tr].controls[self.count_element_td].content.controls[1].content.content.controls.pop()
                if len(self.treyd_polosa) == 0:
                    self.controls[0].content.content.content.controls[4].content.controls[0].content.controls[self.count_element_tr].controls[self.count_element_td].content.controls[1].content.content = ft.Container(ft.Container(ft.Text('Нет сделок',color=c_white,text_align='CENTER'),bgcolor=c_blue_binance,padding=ft.padding.only(top=90)),width=170,height=200,margin=-10)
                    
            self.controls[0].content.content.content.controls[4].content.controls[0].content.controls[self.count_element_tr].controls[self.count_element_td].update()
            
        
            
    
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
