# страница выбора стратегии торговли
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.general_table import General_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.MA_table import MA_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.one_table import One_table

class Table_set_print(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.strategy_translate = {
            'general':'Общие настройки',
            'one':'Канал, тренд, локаль, объём',
            'MA':'Скользящие средние'
        }
        self.strategy_component = {
            'general':General_table(),
            'one':MA_table(),
            'MA':One_table()
        }
        self.strategy_translate_checked = 'general'
        

    def checked_menu_table(self,e):
        self.strategy_translate_checked = e.control.data
        self.controls = []
        self.controls.append(self.print_page())
        self.update()

    def print_page(self):

        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.strategys = literal_eval(config.get('param_trade_historical_trade_svobodniy_freym', 'strategys'))
        self.strategys.insert(0,'general')
        # datas_print = []
        # config_general_set = configparser.ConfigParser()  
        # config_general_set.read(path_ini_general_set)
        # count = 1
        # for i in config_general_set.sections():
        #     datas_print.append(
        #         ft.DataRow(cells=[
        #             ft.DataCell(ft.Text(count,text_align='center',color=c_blue,size=12,width=20)),
        #             ft.DataCell(ft.Text(config_general_set.get(i, 'start_time'),text_align='center',color=c_blue,size=12,width=74)),
        #             ft.DataCell(ft.Text(config_general_set.get(i, 'stop_time'),text_align='center',color=c_blue,size=12,width=100)),
        #             ft.DataCell(ft.Text(config_general_set.get(i, 'depo'),text_align='center',color=c_blue,size=12,width=50)),
        #             ft.DataCell(ft.Text(config_general_set.get(i, 'leveradg'),text_align='center',color=c_blue,size=12,width=40)),
        #             ft.DataCell(ft.Text(config_general_set.get(i, 'diapazon_tp'),text_align='center',color=c_blue,size=12,width=30)),
        #             ft.DataCell(ft.Text(config_general_set.get(i, 'diapazon_sl'),text_align='center',color=c_blue,size=12,weight=40)),
        #             ft.DataCell(ft.Text(config_general_set.get(i, 'diapazon_volume_min'),text_align='center',color=c_blue,size=12,width=60)),
        #             ft.DataCell(ft.Text(config_general_set.get(i, 'diapazon_volume_max'),text_align='center',color=c_blue,size=12,width=60)),
                    
        #         ]
        #         )
        #     )
        #     count+=1      

        data_menu_mas = []
        data_menu_mas.append(ft.Container(ft.Container(ft.Text('Сет настроек',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))))
        for i in self.strategys:
            if i == self.strategy_translate_checked:
                data_menu_mas.append(ft.Container(ft.Container(ft.Text(self.strategy_translate[i],color=c_yelow,),bgcolor=c_blue,padding=5,margin=ft.margin.only(bottom=-10)),data=i,on_click=self.checked_menu_table))
            else:
                data_menu_mas.append(ft.Container(ft.Container(ft.Text(self.strategy_translate[i],color=c_white,),bgcolor=c_blue,padding=5,margin=ft.margin.only(bottom=-10)),data=i,on_click=self.checked_menu_table))


        self.table_set_print = ft.Container(
            ft.Container(
                ft.Column(controls=[
                    ft.Column(
                        controls=[
                            ft.Row(controls=data_menu_mas),
                            ft.Container(
                                self.strategy_component[self.strategy_translate_checked],
                                # ft.Column(controls=[
                                #     ft.Container(
                                #         ft.Column(controls=[
                                #             ft.DataTable(columns=[
                                #                 ft.DataColumn(ft.Text('№',text_align='center',color=c_blue,size=12)),
                                #                 ft.DataColumn(ft.Text('Время старта',text_align='center',color=c_blue,size=12)),
                                #                 ft.DataColumn(ft.Text('Время остановки',text_align='center',color=c_blue,size=12)),
                                #                 ft.DataColumn(ft.Text('Депозит',text_align='center',color=c_blue,size=12)),
                                #                 ft.DataColumn(ft.Text('Плечо',text_align='center',color=c_blue,size=12)),
                                #                 ft.DataColumn(ft.Text('Тейк',text_align='center',color=c_blue,size=12)),
                                #                 ft.DataColumn(ft.Text('Стоп',text_align='center',color=c_blue,size=12)),
                                #                 ft.DataColumn(ft.Text('Объём мин',text_align='center',color=c_blue,size=12)),
                                #                 ft.DataColumn(ft.Text('Объём макс',text_align='center',color=c_blue,size=12)),
                                                
                                #             ],rows = datas_print,
                                #             column_spacing = 42,
                                #             data_row_max_height = 30,
                                #             data_row_min_height = 30,
                                #             show_checkbox_column = False,
                                #         )
                                #         ],scroll=ft.ScrollMode.ALWAYS,),
                                #         width=880,
                                #         height=200,
                                #         bgcolor=c_white,

                                #     ),
                                # ]),
                                width=860,
                                border = ft.border.only(right=ft.border.BorderSide(1, c_white),left=ft.border.BorderSide(1, c_white),top=ft.border.BorderSide(1, c_white),bottom=ft.border.BorderSide(1, c_white)),
                                # border = ft.border.all(1, c_white),
                                # padding=14,
                                height = 210,
                                # padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                
                    )]),     
            ])),
            width=860,
        )
        
        return self.table_set_print

    def build(self):
        return self.print_page()