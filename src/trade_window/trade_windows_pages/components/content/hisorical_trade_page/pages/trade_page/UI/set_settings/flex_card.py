
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.set_settings.UI.card_default import Card_default


class Flex_card(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.mas_card = [] # массив всех карточек
        self.mas_card_riad = [] # массив карточек в локальном ряду
        self.stolb = 5 # количество карточек в ряду
        self.card_default = Card_default()
        self.number_card = 1

    def create_mas_card(self,count_set_trade):
        if int(count_set_trade)%self.stolb:riad = int(int(count_set_trade)/self.stolb)+1 # кол-во рядов если не делится на self.stolb нацело
        else: riad = int(int(count_set_trade)/self.stolb) # кол-во рядов если делится на self.stolb нацело
        for i in range(riad):
            for j in range(1,self.stolb+1):
                self.mas_card_riad.append(self.card_default.print_page(self.number_card))
                self.number_card+=1
                if self.number_card == count_set_trade+1:
                    break
            self.mas_card.append(ft.Row(controls=self.mas_card_riad))
            self.mas_card_riad[:] = []
        return self.mas_card


    def print_page(self,count_set_trade):
        self.trade_page = ft.Container(ft.Column(controls=[
            # ft.Container(key='pb'),
            ft.Container(ft.Column(controls=self.create_mas_card(count_set_trade)))
        ]),width=900,margin=ft.margin.only(top=15))
           
        return self.trade_page

   
    # def build(self):
    #     return self.print_page(self.number_trade)