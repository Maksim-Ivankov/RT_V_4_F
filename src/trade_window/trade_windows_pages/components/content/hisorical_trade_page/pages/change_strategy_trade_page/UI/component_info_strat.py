
import flet as ft
from variable import *
from imports import *

class Component_info_strat(ft.UserControl):
    def __init__(self):
        super().__init__()
    
    def update_component(self):
        self.controls = []
        self.controls.append(self.print_component())
        self.update()

    def print_component(self):
        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.strategys = literal_eval(config.get('param_trade_historical_trade_svobodniy_freym', 'strategys'))
        self.component_info_strat = ft.Container(  
            ft.Text(self.strategys)
        )
        
        return self.component_info_strat

    def build(self):
        return self.print_component()
        