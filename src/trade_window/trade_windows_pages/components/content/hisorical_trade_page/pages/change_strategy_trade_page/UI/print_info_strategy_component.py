# компонент информации о стратегии, которая отображается справа от чекбоксов выбора стратегии
import flet as ft
from variable import *
from imports import *
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_strategy_trade_page.UI.info_strat import info_strat

class Print_info_strategy_component(ft.UserControl):
    def __init__(self):
        super().__init__()


    def print_component(self,strategy='none'):
        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.strategys = config.get('param_trade_historical_trade_svobodniy_freym', 'strategys')
        if strategy == 'none':
            if len(literal_eval(self.strategys))==0:self.component_info_strat = ft.Container(ft.Text('Выберите стратегию для отоборажения информации',text_align='CENTER'),padding=ft.padding.only(top=180),width=560)
            else: self.component_info_strat = ft.Container(info_strat[literal_eval(self.strategys)[0]])
        else:
            self.component_info_strat = ft.Container(info_strat[strategy])
        return self.component_info_strat

    def build(self):
        return self.print_component()
        