
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.set_settings.UI.card_default import Card_default
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.set_settings.UI.table_result import Table_result
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.set_settings.page_trade.result_trqade_page import Result_trqade_page

class Trade_page_set(ft.UserControl):
    def __init__(self,number_trade,change_page):
        super().__init__()
        self.change_page = change_page
        self.number_trade = number_trade
        self.card_mas_print = []
        self.stolb = 5 # количество карточек в ряду
        self.mas_card_riad = [] # массив карточек в локальном ряду
        self.mas_card = [] # массив всех карточек
        self.card_default = Card_default()
        self.number_card = 1
        
    # создает наполнение карточками
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
    
    # перерисовывает таблицу результатов
    def reptint_table_result(self,regime):
        self.controls[0].content.controls.pop()
        self.controls[0].content.controls.append(self.table_result.print_page(self.update_component,regime,self.number_trade))
        self.update()

    # возвращаемся на страницу торговли по сету настроек после клика по таблице результатов
    def return_old_data(self,e):
        self.controls[:] = []
        self.controls.append(self.trade_page)
        self.update()

        # открыть страницу с трейдом из таблицы результатов торговли по сету настроек11111
    def print_page_one_trade_oura_set(self,number_trade):
        # print('Типа открыли страницу')
        if os.path.isfile(f'{path_save_trade}\\{self.number_trade}\\settings_our.txt'):
                with open(f'{path_save_trade}\\{self.number_trade}\\settings_our.txt') as file2:
                    self.array_data_row = [row.strip() for row in file2] # сюда сохраняем, что в ней лежит
        strategy_now = literal_eval(self.array_data_row[0].split('&')[22])
        self.controls[:] = []
        self.controls.append(Result_trqade_page(self.return_old_data,number_trade,strategy_now,'istorija_trade',self.number_trade,self.change_page))
        # back_trade_page,number_trade,strategy_now,regime='None',number_trade_folder=(len(os.listdir(path_save_trade))),change_page=''
        self.update()

        # просто обновляет self
    def update_component(self):
        self.update()
        # print('Просто обновили селф')
        # pass

    # Принтим всю страницу
    def print_page(self):                 
        self.table_result = Table_result(self.reptint_table_result,self.print_page_one_trade_oura_set)
        self.trade_page = ft.Container(ft.Column(controls=[
                ft.Container(ft.Column(
                    controls=self.create_mas_card(),
                    height=520,
                    scroll=ft.ScrollMode.ALWAYS,
                )),
                self.table_result.print_page(self.update_component,'basa',self.number_trade)
            ],scroll=ft.ScrollMode.ALWAYS,
            height=560,
        ),width=900,margin=ft.margin.only(top=15,left=-20,right=-20))
        
        return self.trade_page

    def build(self):                      
        return self.print_page()
    
