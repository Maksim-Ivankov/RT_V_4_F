
import flet as ft
from variable import *
from imports import *

# from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.istoriya_treyd_page.UI.table_trade.table_trade import Table_trade
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.istoriya_treyd_page.UI.trade_page.data_settings import def_print_our_settings,def_print_set_settings,def_print_log,def_print_trade

class Trade_page(ft.UserControl):
    def __init__(self,number_folder):
        super().__init__()
        self.number_folder = number_folder
        


    def build(self):
        self.content = ft.Column(controls=[
                                # ft.Container(ft.Text('Проверьте настройки и запустите торговлю',size=12,color=c_white,text_align='center'),padding=ft.padding.only(left=320)),
                                ft.Container(
                                    ft.Row(controls=[
                                        ft.Container(ft.Container(
                                            ft.Column(controls=[
                                                ft.Column(
                                                    controls=[
                                                        ft.Container(
                                                            ft.Container(ft.Text('Общие настройки робота',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                            ft.Container(
                                                                ft.Container(
                                                                    def_print_our_settings(self.number_folder),
                                                                    width=500,
                                                                    height=148,
                                                                    border = ft.border.all(1, c_white),
                                                                    bgcolor=c_blue,
                                                                ),
                                                                width=500,
                                                                height = 148,
                                                                padding=ft.padding.only(left=-1,top=-1,bottom=-1)

                                        )]),])),width=500,),
                                        ft.Container(
                                            ft.Container(
                                                ft.Column(controls=[
                                                    ft.Column(
                                                        controls=[
                                                            ft.Container(
                                                                ft.Container(ft.Text('Настройки стратегий',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                            ft.Container(
                                                                ft.Container(
                                                                    # print_set_settings,
                                                                    def_print_set_settings(self.number_folder),
                                                                    width=350,
                                                                    height=148,
                                                                    border = ft.border.all(1, c_white),
                                                                    bgcolor=c_blue,
                                                                ),
                                                                width=350,
                                                                height = 148,
                                                                padding=ft.padding.only(left=-1,top=-1,bottom=-1)    
                                        )]),])),width=400,),]),
                                width=900,padding=ft.padding.only(left=20)),
                                

                                # ft.Container(self.pb,margin=ft.margin.only(top=20,bottom=20),key='pb'),


                                ft.Container(ft.Row(controls=[ft.Container(
                                    ft.Container(ft.Column(controls=[ft.Column(controls=[
                                                    ft.Container(
                                                        ft.Container(ft.Text('Логи работы',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                        ft.Container(
                                                            ft.Container(
                                                                ft.Column(controls=def_print_log(self.number_folder),scroll=ft.ScrollMode.ALWAYS),
                                                                width=425,
                                                                height=260,
                                                                border = ft.border.all(1, c_white),
                                                                bgcolor=c_blue,
                                                                padding=10,
                                                            ),
                                                            width=425,
                                                            # border = ft.border.all(1, c_white),
                                                            # padding=14,
                                                            height = 260,
                                                            padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                                        )]),])),width=425,),
                                    ft.Container(ft.Container(
                                            ft.Column(controls=[ft.Column(controls=[
                                                        ft.Container(
                                                            ft.Container(ft.Text('Сделки',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                        ft.Container(
                                                            ft.Container(
                                                                ft.Column(controls=def_print_trade(self.number_folder),scroll=ft.ScrollMode.ALWAYS),
                                                                width=425,
                                                                height=260,
                                                                border = ft.border.all(1, c_white),
                                                                bgcolor=c_blue,
                                                                padding=10,
                                                            ),
                                                            width=425,
                                                            # border = ft.border.all(1, c_white),
                                                            # padding=14,
                                                            height = 260,
                                                            padding=ft.padding.only(left=-1,top=-1,bottom=-1)    
                                                )]),])),width=425,),]),
                width=900,height=450,padding=ft.padding.only(left=20))



                                
                            ],scroll=ft.ScrollMode.ALWAYS)
        
        self.trade_page = ft.Container(
            ft.Container(
                        ft.Container(
                            self.content,
                            alignment=ft.alignment.center),
                            padding=ft.padding.only(top=10)
                    ),expand=2
        )
        
        return self.trade_page
    










    # self.trade_page = ft.Container(ft.Column(controls=[
    #         ft.Container(self.pb,margin=ft.margin.only(top=20,bottom=20),key='pb'),
    #         ft.Container(ft.Row(controls=[
    #                 ft.Container(
    #                                 ft.Container(ft.Column(controls=[ft.Column(controls=[
    #                                                 ft.Container(
    #                                                     ft.Container(ft.Text('Логи работы',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
    #                                                     ft.Container(
    #                                                         ft.Container(
    #                                                             ft.Column(scroll=ft.ScrollMode.ALWAYS),
    #                                                             width=425,
    #                                                             height=400,
    #                                                             border = ft.border.all(1, c_white),
    #                                                             bgcolor=c_blue,
    #                                                             padding=10,
    #                                                         ),
    #                                                         width=425,
    #                                                         # border = ft.border.all(1, c_white),
    #                                                         # padding=14,
    #                                                         height = 400,
    #                                                         padding=ft.padding.only(left=-1,top=-1,bottom=-1)
    #                                                     )]),])),width=425,),
    #                                 ft.Container(ft.Container(
    #                                         ft.Column(controls=[ft.Column(controls=[
    #                                                     ft.Container(
    #                                                         ft.Container(ft.Text('Сделки',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
    #                                                     ft.Container(
    #                                                         ft.Container(
    #                                                             ft.Column(scroll=ft.ScrollMode.ALWAYS),
    #                                                             width=425,
    #                                                             height=400,
    #                                                             border = ft.border.all(1, c_white),
    #                                                             bgcolor=c_blue,
    #                                                             padding=10,
    #                                                         ),
    #                                                         width=425,
    #                                                         # border = ft.border.all(1, c_white),
    #                                                         # padding=14,
    #                                                         height = 400,
    #                                                         padding=ft.padding.only(left=-1,top=-1,bottom=-1)    
    #                                             )]),])),width=425,),]),
    #             width=900,height=450,padding=ft.padding.only(left=20))
    #     ]),width=900)
    #     return self.trade_page