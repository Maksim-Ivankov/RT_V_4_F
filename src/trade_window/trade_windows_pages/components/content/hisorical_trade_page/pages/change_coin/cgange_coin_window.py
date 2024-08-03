
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_coin.component_change_strategy_coin import Component_change_strategy_coin

class Cgange_coin_window(ft.UserControl):
    def __init__(self,coin_save):
        super().__init__()
        self.coin_save = coin_save
        

    def build(self):

        def close_modal():
            self.controls[0].open = False
            self.update()

        self.cgange_coin_window = ft.BottomSheet(
                Component_change_strategy_coin(close_modal,self.coin_save),
                open=True,
                bgcolor='transparent',
                elevation = 0
            )

        
        return self.cgange_coin_window