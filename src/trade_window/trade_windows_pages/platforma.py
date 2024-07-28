
# import flet as ft
# from variable import *
# from imports import *

# from src.trade_window.trade_windows_pages.components.menu.menu import Menu
# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.hisorical_trade_page import Hisorical_trade_page
# from src.trade_window.trade_windows_pages.components.content.main_page.main_page import Main_page
# from src.trade_window.trade_windows_pages.components.content.test_trade_page.test_trade_page import Test_trade_page
# from src.trade_window.trade_windows_pages.components.content.trade_robot_page.trade_robot_page import Trade_robot_page
# from src.trade_window.trade_windows_pages.components.content.faq_page.faq_page import Faq_page
# from src.trade_window.trade_windows_pages.components.content.prifile_page.prifile_page import Prifile_page
# from src.trade_window.trade_windows_pages.components.content.settings_page.settings_page import Settings_page

# class Platforma(ft.UserControl):
#     def __init__(self,page):
#         super().__init__()
#         self.page = page
#         self.page_one = 'Настройки программы'

#     # # запуск в потоке пересчета времени
#     # def did_mount(self):
#     #     self.running = True
#     #     self.myThread = threading.Thread(target=self.update_data, args=(), daemon=True)
#     #     self.myThread.start()

#     # #то что крутится в потоке - пересчет времени 
#     # def update_data(self):
#     #     while self.running:
#     #         self.controls[0].content.controls[0].controls[0].content.controls[0].content.controls[3].content.controls[0].content.controls[0].controls[1].value = time.strftime("%d.%m.%Y г. %H:%M:%S", time.localtime())
#     #         time.sleep(1)
#     #         self.controls[0].content.controls[0].controls[0].content.controls[0].content.controls[3].content.controls[0].content.controls[0].controls[1].update()

#     def build(self):
#         # отрисовка страницы согласно выбранному пункту меню
#         def print_window(page,punkt_menu):
#             platforma = ft.Container(
#                 ft.Row(
#                     controls=[
#                         ft.Container(
                            
#                             content=Menu(self.page,callback,punkt_menu),
#                             bgcolor='red',
#                         ),
#                         ft.Container(
#                             expand=2, content=page, bgcolor='red'
#                         ),
#                     ],
#                 ),expand = True,
#             )
#             return platforma
        
#         # выбор пункта меню
#         def callback(punkt_menu=self.page_one):
#             self.page_select = punkts[punkt_menu]
#             self.controls = []
#             self.controls.append(print_window(self.page_select,punkt_menu))
#             self.update()

        
#         punkts = {
#                 'Главная':Main_page(),
#                 'Историческая торговля':Hisorical_trade_page(),
#                 'Тестовая торговля':Test_trade_page(),
#                 'Торговый робот':Trade_robot_page(),
#                 'FAQ':Faq_page(),
#                 'Профиль':Prifile_page(),
#                 'Настройки программы':Settings_page(),
#             }

#         self.page_select = punkts[self.page_one]
        
#         return print_window(self.page_select,self.page_one)

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
        self.page_one = 'Профиль'

    # запуск в потоке пересчета времени
    def did_mount(self):
        self.running = True
        self.myThread = threading.Thread(target=self.update_data, args=(), daemon=True)
        self.myThread.start()

    #то что крутится в потоке - пересчет времени 
    def update_data(self):
        while self.running:
            # print(self.controls[0].content.controls[0].content.controls[0].content.controls[0].content.controls[3].content.controls[0].content.controls[0].controls[1])
            self.controls[0].content.controls[0].content.controls[0].content.controls[0].content.controls[3].content.controls[0].content.controls[0].controls[1].value = time.strftime("%d.%m.%Y г. %H:%M:%S", time.localtime())
            time.sleep(1)
            self.controls[0].content.controls[0].content.controls[0].content.controls[0].content.controls[3].content.controls[0].content.controls[0].controls[1].update()

    def build(self):
        # отрисовка страницы согласно выбранному пункту меню
        def print_window(page,punkt_menu):
            platforma = ft.Container(
                ft.Row(
                    controls=[
                        ft.Container(
                            content=Menu(self.page,callback,punkt_menu),
                        ),
                        ft.Container(
                            expand=2, content=page
                        ),
                    ]),
            )
            return platforma
        
        # выбор пункта меню
        def callback(punkt_menu=self.page_one):
            self.page_select = punkts[punkt_menu]
            self.controls = []
            self.controls.append(print_window(self.page_select,punkt_menu))
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

        self.page_select = punkts[self.page_one]
        
        return print_window(self.page_select,self.page_one)