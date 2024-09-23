
import flet as ft
from variable import *
from imports import *

from src.controllers.settings.set_settings import HisTrade_Svoboda_OneSettings

class Core_trade():
    def __init__(self,regime,strategy):
        super().__init__()
        self.regime = regime
        self.strategy = strategy
        
        get_settings_our = {
            'Историческая торговля|Свободный фрейм|Ода настройка': HisTrade_Svoboda_OneSettings(),
        }
        get_settings_strat = {
           'MA':'1', 
        }

        var = get_settings_our[regime]
        

