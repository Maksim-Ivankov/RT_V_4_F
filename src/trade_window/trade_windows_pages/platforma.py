
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.menu.menu import Menu
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.hisorical_trade_page import Hisorical_trade_page
from src.trade_window.trade_windows_pages.components.content.main_page.main_page import Main_page
from src.trade_window.trade_windows_pages.components.content.test_trade_page.test_trade_page import Test_trade_page
from src.trade_window.trade_windows_pages.components.content.trade_robot_page.trade_robot_page import Trade_robot_page
from src.trade_window.trade_windows_pages.components.content.faq_page.faq_page import Faq_page
from src.trade_window.trade_windows_pages.components.content.prifile_page.prifile_page import Prifile_page
from src.trade_window.trade_windows_pages.components.content.settings_page.settings_page import Settings_page

class Platforma(ft.UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page

    def build(self):

        # отрисовка страницы согласно выбранному пункту меню
        def print_window(page):
            platforma = ft.Container(
                ft.Row(
                    controls=[
                        Menu(self.page,callback),
                        page
                    ]),expand = True,
            )
            return platforma
        
        # выбор пункта меню
        def callback(punkt_menu='Главная'):
            self.page_select = punkts[punkt_menu]
            self.controls = []
            self.controls.append(print_window(self.page_select))
            self.update()

        
        punkts = {
                'Главная':Main_page(),
                'Историческая торговля':Hisorical_trade_page(),
                'Тестовая торговля':Test_trade_page(),
                'Торговый робот':Trade_robot_page(),
                'FAQ':Faq_page(),
                'Профиль':Prifile_page(),
                'Настройки программы':Settings_page(),
            }
        # Страница по умолчанию
        self.page_select = punkts['Главная']
        
        return print_window(self.page_select)