
import flet as ft
from variable import *
from imports import *

class Print_graph(ft.UserControl):
    def __init__(self,number_folder,number_trade):
        super().__init__()
        self.number_folder = number_folder
        self.number_trade = number_trade
    

    def print_page(self):
        
        # штука ниже вытаскивает из файла с трейдом все данные и делает статистику
        self.path_save_trade_log = f'{path_save_trade}\\{self.number_folder}\\trade.txt' # путь сохранения логов в папке трейда
        if os.path.isfile(self.path_save_trade_log):
            with open(self.path_save_trade_log) as file:
                self.array_data_row = [row.strip() for row in file]
        self.coin = self.array_data_row[self.number_trade].split('|')[6]
        self.take_profit_price = float(self.array_data_row[self.number_trade].split('|')[7])
        self.stop_loss_price = float(self.array_data_row[self.number_trade].split('|')[8])
        self.price_treyd = float(self.array_data_row[self.number_trade].split('|')[9])
        self.open_time_trade = int(self.array_data_row[self.number_trade].split('|')[10])
        self.close_time_trade = int(self.array_data_row[self.number_trade].split('|')[11])
        
        print(self.coin)
        print(self.take_profit_price)
        print(self.stop_loss_price)
        print(self.price_treyd)
        print(self.open_time_trade)
        print(self.close_time_trade)

            
        self.trade_page = ft.Container(
            ft.Text('dfgdfgdf'),
            width=425,
            height=400,
            border = ft.border.all(1, c_white),
            bgcolor=c_blue,
            padding=10,
        )
           
        return self.trade_page

   
    def build(self):
        return self.print_page()