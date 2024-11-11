
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.UI.header import Header
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.ferst_page import Ferst_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.historical_trade_page import Historical_trade_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.svoboda_freym_page import Svoboda_freym_page

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_coin.page_last_data.page_last_data import Page_last_data
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.settings_robot_page.settings_robot_page import Settings_robot_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_strategy_trade_page.change_strategy_trade_page import Change_strategy_trade_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regime_trade_page.regime_trade_page import Regime_trade_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.regim_set_settings_page import Regim_set_settings_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.regim_trade_one_settings_page import Regim_trade_one_settings_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.trade_page import Trade_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.istoriya_treyd_page.istoriya_treyd_page import Istoriya_treyd_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.isbrannoe_page.isbrannoe_page import Isbrannoe_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.isbrannoe_page.add_to_favorites_page import Add_to_favorites_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.istoriya_treyd_page.UI.trade_page.trade_page_set import Trade_page_set as Trade_page_open_set_trade
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.istoriya_treyd_page.UI.trade_page.trade_page import Trade_page as Trade_page_open_one_trade

class Hisorical_trade_page(ft.UserControl):
    def __init__(self,page):
        super().__init__()
        # self.ferst_page = 'Первая'
        self.ferst_page = 'История торговли' 
        self.page = page

    def print_page(self,page,data=''):

        if page == 'Первая':
            pages_list=Ferst_page(self.change_page)
            title_list='Торговля по историческим данным'
        if page == 'Историческая торговля':
            pages_list=Historical_trade_page(self.change_page)
            title_list='Торговля по историческим данным | Историческая торговля'
        if page == 'Свободный фрейм':
            pages_list=Svoboda_freym_page(self.change_page,self.page)
            title_list='Торговля по историческим данным | Дневная торговля'
        if page == 'Хранилище торговых данных':
            pages_list=Page_last_data(self.change_page)
            title_list='Хранилище торговых данных'
        if page == 'Настройки робота':
            pages_list=Settings_robot_page(self.change_page)
            title_list='Торговля по историческим данным | Настройки робота'
        if page == 'Выбрать стратегию торговли':
            pages_list=Change_strategy_trade_page(self.change_page)
            title_list='Торговля по историческим данным | Выбор стратегии торговли'
        if page == 'Выбрать режим торговли':
            pages_list=Regime_trade_page(self.change_page)
            title_list='Торговля по историческим данным | Выбор режима торговли'
        if page == 'Одна настройка':
            pages_list=Regim_trade_one_settings_page(self.change_page)
            title_list='Торговля по историческим данным | Настройки стратегии'
        if page == 'Сет настроек':
            pages_list=Regim_set_settings_page(self.change_page)
            title_list='Торговля по историческим данным | Задание сета настроек'
        if page == 'Запустить торговлю':
            pages_list=Trade_page(self.change_page)
            title_list='Торговля по историческим данным | Торговля'
        if page == 'Запустить торговлю сет':
            pages_list=Trade_page(self.change_page,'much_set')
            title_list='Торговля по историческим данным | Торговля по сету настроек'
        if page == 'История торговли':
            pages_list=Istoriya_treyd_page(self.change_page,data)
            title_list='Торговля по историческим данным | История торговли'
        if page == 'Избранные стратегии':
            pages_list=Isbrannoe_page(self.change_page)
            title_list='Торговля по историческим данным | Избранные стратегии'
        if page == 'Добавить в избранное':
            pages_list=Add_to_favorites_page(self.change_page,data)
            title_list='Торговля по историческим данным | Избранные стратегии'
        if page == 'История торговли | Сет':
            pages_list=ft.Container(Trade_page_open_set_trade(data['number_trade'],self.change_page),margin=ft.margin.only(left=50))
            title_list='Торговля по историческим данным | История торговли'
        if page == 'История торговли | Одна настройка':
            pages_list=Trade_page_open_one_trade(data['number_trade'],self.change_page)
            title_list='Торговля по историческим данным | История торговли'


        return ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(ft.Text(title_list,color=c_blue),alignment=ft.alignment.center),bgcolor=c_yelow,height=28,margin=ft.margin.only(top=-10,left=-10,right=-10),border = ft.border.all(1,c_white), 
                    ),
                    ft.Container(
                        ft.Column(controls=[
                            Header(self.change_page),
                            pages_list
                        ]),
                        expand=2,
                    )
                ]
            ),expand=2
        )
    
    def change_page(self,e):
        if isinstance(e.control.data, dict):
            self.controls = []
            self.controls.append(self.print_page(e.control.data['page'],e.control.data))
            self.update()
        else:
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

# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_coin.page_last_data.page_last_data import Page_last_data
# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.settings_robot_page.settings_robot_page import Settings_robot_page
# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_strategy_trade_page.change_strategy_trade_page import Change_strategy_trade_page
# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regime_trade_page.regime_trade_page import Regime_trade_page
# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.regim_set_settings_page import Regim_set_settings_page
# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.regim_trade_one_settings_page import Regim_trade_one_settings_page
# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.trade_page import Trade_page
# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.istoriya_treyd_page.istoriya_treyd_page import Istoriya_treyd_page
# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.isbrannoe_page.isbrannoe_page import Isbrannoe_page
# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.isbrannoe_page.add_to_favorites_page import Add_to_favorites_page
# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.istoriya_treyd_page.UI.trade_page.trade_page_set import Trade_page_set as Trade_page_open_set_trade
# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.istoriya_treyd_page.UI.trade_page.trade_page import Trade_page as Trade_page_open_one_trade

# class Hisorical_trade_page(ft.UserControl):
#     def __init__(self,page):
#         super().__init__()
#         self.ferst_page = 'Первая'
#         # self.ferst_page = 'Добавить в избранное' 
#         self.page = page

#     def print_page(self,page,data=''):
        
#         if data=='':trade_page_set_number_trade = 1 # условие для открытия истории торговли - сет настроек по выбранной папке, пропуская таблицу
#         else: trade_page_set_number_trade = data['number_trade'] if 'number_trade' in data else 1
#             # if 'number_trade' in data:
#         # else: trade_page_set_number_trade = data['number_trade'] if data.has_key("number_trade") else 1
        
#         pages_list={
#             'Первая':Ferst_page(self.change_page),
#             'Историческая торговля':Historical_trade_page(self.change_page),
#             'Свободный фрейм':Svoboda_freym_page(self.change_page,self.page),
#             'Хранилище торговых данных':Page_last_data(self.change_page),
#             'Настройки робота':Settings_robot_page(self.change_page),
#             'Выбрать стратегию торговли':Change_strategy_trade_page(self.change_page),
#             'Выбрать режим торговли':Regime_trade_page(self.change_page),
#             'Одна настройка':Regim_trade_one_settings_page(self.change_page),
#             'Сет настроек':Regim_set_settings_page(self.change_page),
#             'Запустить торговлю':Trade_page(self.change_page),
#             'Запустить торговлю сет':Trade_page(self.change_page,'much_set'),
#             'История торговли':Istoriya_treyd_page(self.change_page,data),
#             'Избранные стратегии':Isbrannoe_page(self.change_page),
#             'Добавить в избранное':Add_to_favorites_page(self.change_page,data),
#             'История торговли | Сет':ft.Container(Trade_page_open_set_trade(trade_page_set_number_trade,self.change_page),margin=ft.margin.only(left=50)),
#             'История торговли | Одна настройка':ft.Container(Trade_page_open_one_trade(trade_page_set_number_trade,self.change_page),margin=ft.margin.only(left=50)),
#             # 'Старница одного трейда из сета настроек историческая свободный':Result_trqade_page(self.change_page),
#         }
        
#         # if page == 'Первая': pages_list=Ferst_page(self.change_page)

#         title_list={
#             'Первая':'Торговля по историческим данным',
#             'Историческая торговля':'Торговля по историческим данным | Историческая торговля',
#             'Свободный фрейм':'Торговля по историческим данным | Дневная торговля',
#             'Хранилище торговых данных':'Хранилище торговых данных',
#             'Настройки робота':'Торговля по историческим данным | Настройки робота',
#             'Выбрать стратегию торговли':'Торговля по историческим данным | Выбор стратегии торговли',
#             'Выбрать режим торговли':'Торговля по историческим данным | Выбор режима торговли',
#             'Одна настройка':'Торговля по историческим данным | Настройки стратегии',
#             'Сет настроек':'Торговля по историческим данным | Задание сета настроек',
#             'Запустить торговлю':'Торговля по историческим данным | Торговля',
#             'Запустить торговлю сет':'Торговля по историческим данным | Торговля по сету настроек',
#             'История торговли':'Торговля по историческим данным | История торговли',
#             'Избранные стратегии':'Торговля по историческим данным | Избранные стратегии',
#             'Добавить в избранное':'Торговля по историческим данным | Избранные стратегии',
#             'История торговли | Сет':'Торговля по историческим данным | История торговли',
#             'История торговли | Одна настройка':'Торговля по историческим данным | История торговли',
#             # 'Старница одного трейда из сета настроек историческая свободный':'Торговля по историческим данным | Торговля по сету настроек',
#         }

#         return ft.Container(
#             ft.Column(
#                 controls=[
#                     ft.Container(
#                         ft.Container(ft.Text(title_list[page],color=c_blue),alignment=ft.alignment.center),bgcolor=c_yelow,height=28,margin=ft.margin.only(top=-10,left=-10,right=-10),border = ft.border.all(1,c_white), 
#                     ),
#                     ft.Container(
#                         ft.Column(controls=[
#                             Header(self.change_page),
#                             pages_list[page]
#                         ]),
#                         expand=2,
#                     )
#                 ]
#             ),expand=2
#         )
    
#     def change_page(self,e):
#         if isinstance(e.control.data, dict):
#             self.controls = []
#             self.controls.append(self.print_page(e.control.data['page'],e.control.data))
#             self.update()
#         else:
#             self.controls = []
#             self.controls.append(self.print_page(e.control.data))
#             self.update()

#     def build(self):
        
#         return self.print_page(self.ferst_page)
