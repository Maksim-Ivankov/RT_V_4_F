
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.set_settings.UI.card_default import Card_default


class Trade_page_set(ft.UserControl):
    def __init__(self,number_trade):
        super().__init__()
        self.number_trade = number_trade
        self.card_mas_print = []
        self.stolb = 5 # количество карточек в ряду
        self.mas_card_riad = [] # массив карточек в локальном ряду
        self.mas_card = [] # массив всех карточек
        self.card_default = Card_default()
        self.number_card = 1
        
   
    def create_mas_card(self):
        count_set_trade = len(os.listdir(f'{path_save_trade}\\{self.number_trade}\\folder_trade'))
        if int(count_set_trade)%self.stolb:riad = int(int(count_set_trade)/self.stolb)+1 # кол-во рядов если не делится на self.stolb нацело
        else: riad = int(int(count_set_trade)/self.stolb) # кол-во рядов если делится на self.stolb нацело
        for i in range(riad):
            for j in range(1,self.stolb+1):
                self.mas_card_riad.append(self.card_default.print_page(self.number_card,'istorija_trade',self.number_trade))
                self.number_card+=1
                if self.number_card == count_set_trade+1:
                    break
            self.mas_card.append(ft.Row(controls=self.mas_card_riad))
            self.mas_card_riad[:] = []
        return self.mas_card
    

    def print_page(self):
        
        # folder_strat = os.listdir(f'{path_save_trade}\\{self.number_trade}\\folder_trade')
        # for file_trade in folder_strat:
        #     self.path_trade_set = f'{path_save_trade}\\{self.number_trade}\\folder_trade\\{file_trade}\\trade.txt' # по очереди проходимся по каждой папке
        #     if os.path.isfile(self.path_trade_set):
        #         with open(self.path_trade_set) as file:
        #             self.array_data_row_set = [row.strip() for row in file]
        #             self.card_mas_print.append()
                    
        
        
        self.trade_page = ft.Container(ft.Column(controls=[
            ft.Container(ft.Column(
                controls=self.create_mas_card(),
                height=520,
                scroll=ft.ScrollMode.ALWAYS,
                ))
        ]),width=900,margin=ft.margin.only(top=15,left=-20,right=-20))
        
        return self.trade_page

    def build(self):                      
        return self.print_page()
    
