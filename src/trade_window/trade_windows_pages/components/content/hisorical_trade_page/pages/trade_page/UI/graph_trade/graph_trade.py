
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.graph_trade.print_graph import Print_graph

class Graph_trade(ft.UserControl):
    def __init__(self,number_folder,regime_set = 'none',number_trade_folder='0'):
        super().__init__()
        # self.form_graph = form_graph
        self.number_trade_folder = number_trade_folder
        self.regime_set = regime_set
        self.number_folder = number_folder
        # self.number_trade = int(number_trade)
        self.settings_print_graph = {}
        self.settings_print_graph['width_graph'] = 425
        self.settings_print_graph['height_graph'] = 400
        self.array_data_row = []
        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.regime_trade_page = config.get('param_trade_historical_trade_svobodniy_freym', 'regime_trade_page')
    


    def print_page(self,number_trade,form_graph='max'):
        self.number_trade = int(number_trade)
        self.form_graph = form_graph
        # print(f'Рисуем график - {number_trade} | {form_graph}')
        # print(f'Номер папки = {self.number_folder}| Номер трейда = {self.number_trade}')
        # print('1111')
        # print(self.form_graph)
        # штука ниже вытаскивает из файла с трейдом все данные и делает статистику1
        if self.regime_set == 'none':
            self.path_save_trade_log = f'{path_save_trade}\\{self.number_folder}\\trade.txt' # путь сохранения логов в папке трейда
        if self.regime_set == 'set' or self.regime_trade_page == 'historical':
            self.path_save_trade_log = f'{path_save_trade}\\{self.number_folder}\\folder_trade\\{self.number_trade_folder}\\trade.txt' # путь сохранения логов в папке трейдаc
        if os.path.isfile(self.path_save_trade_log):
            with open(self.path_save_trade_log) as file:
                self.array_data_row = [row.strip() for row in file]
        # print(self.array_data_row)
        self.settings_print_graph['coin'] = self.array_data_row[self.number_trade].split('|')[6]
        self.settings_print_graph['TP'] = float(self.array_data_row[self.number_trade].split('|')[7])
        self.settings_print_graph['SL'] = float(self.array_data_row[self.number_trade].split('|')[8])
        self.settings_print_graph['price_treyd'] = float(self.array_data_row[self.number_trade].split('|')[9])
        self.settings_print_graph['open_time_trade'] = int(self.array_data_row[self.number_trade].split('|')[10])
        self.settings_print_graph['close_time_trade'] = int(self.array_data_row[self.number_trade].split('|')[11])
        self.settings_print_graph['path_df'] = self.array_data_row[self.number_trade].split('|')[12]
        # print(f"==>> self.settings_print_graph['path_df']: {self.settings_print_graph['path_df']}")
        self.settings_print_graph['trend'] = self.array_data_row[self.number_trade].split('|')[0]
        self.settings_print_graph['index_entry'] = self.array_data_row[self.number_trade].split('|')[13]
        self.settings_print_graph['index_exit'] = self.array_data_row[self.number_trade].split('|')[14]
        

        if self.form_graph == 'max':
            # print(f'Рисуем график макс - {number_trade}')
            # print('graph_trade max')
            self.trade_page = ft.Container(
                Print_graph(self.settings_print_graph,'max'),
                width=425,
                height=400,
                border = ft.border.all(1, c_white),
                bgcolor=c_blue_binance,
                padding=10,
            )
        if self.form_graph == 'min':
            # print(f'Рисуем график мин - {number_trade}')
            # print('graph_trade min')
            self.trade_page = ft.Container(
                Print_graph(self.settings_print_graph,'min'),
                width=425,
                height=400,
                border = ft.border.all(1, c_white),
                bgcolor=c_blue_binance,
                padding=10,
            )
           
        return self.trade_page

   
    # def build(self):
    #     return self.print_page(self.number_trade)