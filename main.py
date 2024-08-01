import flet as ft
from variable import *
from imports import *

from src.trade_window.input_page.input_page import Input_page
from src.trade_window.trade_windows_pages.platforma import Platforma

class Main:
    def __init__(self):
        None

    def run(self, page):

        def start_new_page():
            p = subPage(controls=[ft.Text("Hello from the new page!!")])
            p.start()

        

        self.page: ft.Page = page
        self.page.title = "RoboTrade"
        self.page.window_height, self.page.window_width = height_window_platforma, width_window_platforma
        self.page.theme_mode = "dark" 
        # self.page.window_resizable = False
        # self.page.window_center()
        self.page.bgcolor = c_blue
        self.main_print = ft.Container( # общий контейнер на страницу45rк
        #    content = ft.Text('123123123'),
           content = Platforma(self.page),
           expand = True,
           padding=ft.padding.only(bottom=-10)
        )
        self.page.add(self.main_print)
        # self.page.overlay.append(ft.Text('123123123'))
        # self.page.update()

        # self.page: ft.Page = page
        # self.page.title = "RoboTrade"
        # self.page.window_height, self.page.window_width = 672, 423
        # self.page.theme_mode = "dark" 
        # self.page.window_resizable = False
        # # self.page.window_center()
        # self.page.bgcolor = c_blue

        # self.main_print = ft.Container( # общий контейнер на страницу45r6
        #    content = Input_page(self.page)
        # )
        # self.page.add(self.main_print)




if __name__ == '__main__':
    main = Main()
    ft.app(target=Main().run, assets_dir="assets")

# df133d2
# import flet as ft

# def main(page: ft.Page):

#     page.window_height, page.window_width = 500, 400


#     def row_with_vertical_alignment():
#         return ft.Container(
#             ft.MenuBar(
#                 expand=True,
                
#                 style=ft.MenuStyle(
#                     bgcolor=c_white,
                    
#                 ),
#                 controls=[
#                     ft.SubmenuButton(
                        
#                         content=ft.Text("Темная",color=c_blue), 
#                         width=140,
#                         height=30,
#                     #     alignment = ft.alignment.center,
#                         controls=[
#                             ft.MenuItemButton(
#                                 content=ft.Text("Темная"),
                                
#                                 # style=ft.ButtonStyle(
#                                 #     bgcolor={ft.ControlState.HOVERED: ft.colors.GREEN_100}
#                                 # ),
#                                 # on_click=handle_menu_item_click,
#                             ),
#                             ft.MenuItemButton(
#                                 content=ft.Text("Светлая"),
                                
#                                 # style=ft.ButtonStyle(
#                                 #     bgcolor={ft.ControlState.HOVERED: ft.colors.GREEN_100}
#                                 # ),
#                                 # on_click=handle_menu_item_click,
#                             ),

#                         ],
#                     )
#                 ]
#             )

            
#         )

#     page.add(
#         row_with_vertical_alignment(),
#     )

# ft.app(target=main)


# def main(page: ft.Page):

#     page.window_height, page.window_width = 500, 400

#     def row_with_vertical_alignment():
#        return ft.Container(
#             ft.Dropdown(
#                 # elevation = 15,
#                 # fill_color = c_white,
#                 # focused_bgcolor=c_white,
#                 autofocus=False,
#                 color=c_blue,
#                 width=150,
#                 # focused_bgcolor=c_white,
#                 # focused_color = c_white,
#                 height=30,
#                 value='Темная',
#                 filled = True,
#                 content_padding = -5,
#                 bgcolor=c_white,
#                 alignment = ft.Alignment(0, 0),
#                 # content_padding=ft.padding.only(top=-10),
#                 text_style = ft.TextStyle(
#                     size=12,
#                     color=c_white
                    
#                 ),
                
#                 border = ft.border.all(0,c_white),
#                 border_radius=0,
#                 options=[
#                     ft.dropdown.Option("Темная"),
#                     ft.dropdown.Option("Светлая"),
                    
#                 ],)
#         )

#     page.add(
#         row_with_vertical_alignment(),
#     )

# ft.app(target=main)
#         return ft.Container(
            
#             ft.Dropdown(
#                 # elevation = 15,
#                 # fill_color = c_white,
#                 # focused_bgcolor=c_white,
#                 autofocus=False,
#                 color=c_blue,
#                 width=150,
#                 height=30,
#                 value='Темная',
#                 filled = True,
#                 content_padding = -5,
#                 bgcolor=c_white,
#                 alignment = ft.Alignment(0, 0),
#                 # content_padding=ft.padding.only(top=-10),
#                 text_style = ft.TextStyle(
#                     size=12,
#                     color=c_blue
                    
#                 ),
                
#                 border = ft.border.all(0,c_white),
#                 border_radius=0,
#                 options=[
#                     ft.dropdown.Option("Темная"),
#                     ft.dropdown.Option("Светлая"),
#                 ],)
#         )

#     page.add(
#         row_with_vertical_alignment(),
#     )

# ft.app(target=main)



# пример с гита с вопроса
# def row_with_vertical_alignment():
#         return  ft.Dropdown(
#         label='Status',
#         width=150,
#         color=ft.colors.GREY_700,
#         bgcolor=ft.colors.WHITE,
#         border_color=ft.colors.GREY_700,
#         border_width=1,
#         hint_text='  Status',
#         hint_style=ft.TextStyle(size=12,color=ft.colors.GREY_700,weight="BOLD",font_family='Tahoma'),
#         text_style=ft.TextStyle(size=12,color=ft.colors.GREY_700,font_family='Tahoma'),
#         dense=True,
#         filled=True,
#         border_radius=1,
#         content_padding=4,
#         alignment=ft.alignment.center_left,
#         options=[
#             ft.dropdown.Option('Todos'),
#             ft.dropdown.Option('Pendente'),
#             ft.dropdown.Option('Andamento'),
#             ft.dropdown.Option('Finalizado'),
#         ],
#         # on_change=inputsearch,
#         autofocus=True
#         )




































































