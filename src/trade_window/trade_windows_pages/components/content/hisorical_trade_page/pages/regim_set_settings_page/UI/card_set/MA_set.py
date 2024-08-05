# страница выбора стратегии торговли
import flet as ft
from variable import *
from imports import *

class MA_set(ft.UserControl):
    def __init__(self):
        super().__init__()
        

    def print_page(self):

        # config = configparser.ConfigParser()         
        # config.read(path_imports_config)
        # self.strategys = literal_eval(config.get('param_trade_historical_trade_svobodniy_freym', 'strategys'))
        

        self.MA_set = ft.Container(
           ft.Text('12312312')
        )
        
        return self.MA_set

    def build(self):
        return self.print_page()