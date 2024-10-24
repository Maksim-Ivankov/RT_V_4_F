
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.UI.header import Header
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.ferst_page import Ferst_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.historical_trade_page import Historical_trade_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.svoboda_freym_page import Svoboda_freym_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.tred_so_smeseniem_page import Tred_so_smeseniem_page

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_coin.page_last_data.page_last_data import Page_last_data
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.settings_robot_page.settings_robot_page import Settings_robot_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_strategy_trade_page.change_strategy_trade_page import Change_strategy_trade_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regime_trade_page.regime_trade_page import Regime_trade_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.regim_set_settings_page import Regim_set_settings_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.regim_trade_one_settings_page import Regim_trade_one_settings_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.trade_page import Trade_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.istoriya_treyd_page.istoriya_treyd_page import Istoriya_treyd_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.isbrannoe_page.isbrannoe_page import Isbrannoe_page

class Hisorical_trade_page(ft.UserControl):
    def __init__(self,page):
        super().__init__()
        self.ferst_page = 'Первая'
        # self.ferst_page = 'История торговли'
        self.page = page

    def print_page(self,page):

        pages_list={
            'Первая':Ferst_page(self.change_page),
            'Историческая торговля':Historical_trade_page(self.change_page),
            'Свободный фрейм':Svoboda_freym_page(self.change_page,self.page),
            'Торговля со смещением':Tred_so_smeseniem_page(self.change_page),
            'Хранилище торговых данных':Page_last_data(self.change_page),
            'Настройки робота':Settings_robot_page(self.change_page),
            'Выбрать стратегию торговли':Change_strategy_trade_page(self.change_page),
            'Выбрать режим торговли':Regime_trade_page(self.change_page),
            'Одна настройка':Regim_trade_one_settings_page(self.change_page),
            'Сет настроек':Regim_set_settings_page(self.change_page),
            'Запустить торговлю':Trade_page(self.change_page),
            'Запустить торговлю сет':Trade_page(self.change_page,'much_set'),
            'История торговли':Istoriya_treyd_page(self.change_page),
            'Избранные стратегии':Isbrannoe_page(self.change_page),
        }

        title_list={
            'Первая':'Торговля по историческим данным',
            'Историческая торговля':'Торговля по историческим данным | Историческая торговля',
            'Свободный фрейм':'Торговля по историческим данным | Свободный фрейм',
            'Торговля со смещением':'Торговля по историческим данным | Торговля со смещением',
            'Хранилище торговых данных':'Хранилище торговых данных',
            'Настройки робота':'Торговля по историческим данным | Настройки робота',
            'Выбрать стратегию торговли':'Торговля по историческим данным | Выбор стратегии торговли',
            'Выбрать режим торговли':'Торговля по историческим данным | Выбор режима торговли',
            'Одна настройка':'Торговля по историческим данным | Настройки стратегии',
            'Сет настроек':'Торговля по историческим данным | Задание сета настроек',
            'Запустить торговлю':'Торговля по историческим данным | Торговля',
            'Запустить торговлю сет':'Торговля по историческим данным | Торговля по сету настроек',
            'История торговли':'Торговля по историческим данным | История торговли',
            'Избранные стратегии':'Торговля по историческим данным | Избранные стратегии',
        }

        return ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(ft.Text(title_list[page],color=c_blue),alignment=ft.alignment.center),bgcolor=c_yelow,height=28,margin=ft.margin.only(top=-10,left=-10,right=-10),border = ft.border.all(1,c_white), 
                    ),
                    ft.Container(
                        ft.Column(controls=[
                            Header(self.change_page),
                            pages_list[page]
                        ]),
                        expand=2,
                    )
                ]
            ),expand=2
        )
    
    def change_page(self,e):
        self.controls = []
        self.controls.append(self.print_page(e.control.data))
        self.update()

    def build(self):
        
        return self.print_page(self.ferst_page)

# import flet as ft
# from variable import *
# from imports import *

# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.UI.header import Header
# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.ferst_page import Ferst_page
# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.historical_trade_page import Historical_trade_page
# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.svoboda_freym_page import Svoboda_freym_page
# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.tred_so_smeseniem_page import Tred_so_smeseniem_page

# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_coin.page_last_data.page_last_data import Page_last_data

# class Hisorical_trade_page(ft.UserControl):
#     def __init__(self,page):
#         super().__init__()
#         # self.ferst_page = 'Первая'
#         self.ferst_page = 'Свободный фрейм'
#         self.page = page

#     def print_page(self,page):

#         pages_list={
#             'Первая':Ferst_page(self.change_page),
#             'Историческая торговля':Historical_trade_page(self.change_page),
#             'Свободный фрейм':Svoboda_freym_page(self.change_page,self.page),
#             'Торговля со смещением':Tred_so_smeseniem_page(self.change_page),
#             # 'Хранилище торговых данных':Page_last_data(self.change_page),
#         }

#         title_list={
#             'Первая':'Торговля по историческим данным',
#             'Историческая торговля':'Торговля по историческим данным | Историческая торговля',
#             'Свободный фрейм':'Торговля по историческим данным | Свободный фрейм',
#             'Торговля со смещением':'Торговля по историческим данным | Торговля со смещением',
#             # 'Хранилище торговых данных':'Хранилище торговых данных'
#         }

#         return ft.Container(
#             ft.Column(
#                 controls=[
#                     ft.Container(
#                         ft.Container(ft.Text(title_list[page],color=c_blue),alignment=ft.alignment.center),bgcolor=c_yelow,height=28,margin=ft.margin.only(top=-10,left=-10,right=-10),border = ft.border.all(1,c_white), 
#                     ),
#                     ft.Container(
#                         ft.Column(controls=[
#                             Header(),
#                             pages_list[page]
#                         ]),
#                         expand=2,
#                     )
#                 ]
#             ),expand=2
#         )
    
#     def change_page(self,e):
#         self.controls = []
#         self.controls.append(self.print_page(e.control.data))
#         self.update()

#     def build(self):
        
#         return self.print_page(self.ferst_page)
