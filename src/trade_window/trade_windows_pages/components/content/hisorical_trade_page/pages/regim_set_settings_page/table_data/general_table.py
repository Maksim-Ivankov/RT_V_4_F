# страница выбора стратегии торговли1
import flet as ft
from variable import *
from imports import *

class General_table(ft.UserControl):
    def __init__(self):
        super().__init__()
        

    def print_page(self):

        datas_print = []
        config_general_set = configparser.ConfigParser()  
        config_general_set.read(path_ini_general_set)
        count = 1
        for i in config_general_set.sections():
            datas_print.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(count,text_align='center',color=c_white,size=12,width=20)),
                    ft.DataCell(ft.Text(config_general_set.get(i, 'start_time'),text_align='center',color=c_white,size=12,width=74)),
                    ft.DataCell(ft.Text(config_general_set.get(i, 'stop_time'),text_align='center',color=c_white,size=12,width=100)),
                    ft.DataCell(ft.Text(config_general_set.get(i, 'depo'),text_align='center',color=c_white,size=12,width=50)),
                    ft.DataCell(ft.Text(config_general_set.get(i, 'leveradg'),text_align='center',color=c_white,size=12,width=40)),
                    ft.DataCell(ft.Text(config_general_set.get(i, 'diapazon_tp'),text_align='center',color=c_white,size=12,width=30)),
                    ft.DataCell(ft.Text(config_general_set.get(i, 'diapazon_sl'),text_align='center',color=c_white,size=12,weight=40)),
                    ft.DataCell(ft.Text(config_general_set.get(i, 'diapazon_volume_min'),text_align='center',color=c_white,size=12,width=60)),
                    ft.DataCell(ft.Text(config_general_set.get(i, 'diapazon_volume_max'),text_align='center',color=c_white,size=12,width=60)),
                    
                ]
                )
            )
            count+=1      
        
        self.general_table = ft.Column(controls=[
            ft.Container(
                ft.Column(controls=[
                    ft.DataTable(columns=[
                        ft.DataColumn(ft.Text('№',text_align='center',color=c_white,size=12)),
                        ft.DataColumn(ft.Text('Время старта',text_align='center',color=c_white,size=12)),
                        ft.DataColumn(ft.Text('Время остановки',text_align='center',color=c_white,size=12)),
                        ft.DataColumn(ft.Text('Депозит',text_align='center',color=c_white,size=12)),
                        ft.DataColumn(ft.Text('Плечо',text_align='center',color=c_white,size=12)),
                        ft.DataColumn(ft.Text('Тейк',text_align='center',color=c_white,size=12)),
                        ft.DataColumn(ft.Text('Стоп',text_align='center',color=c_white,size=12)),
                        ft.DataColumn(ft.Text('Объём мин',text_align='center',color=c_white,size=12)),
                        ft.DataColumn(ft.Text('Объём макс',text_align='center',color=c_white,size=12)),
                        
                    ],rows = datas_print,
                    column_spacing = 42,
                    data_row_max_height = 30,
                    data_row_min_height = 30,
                    show_checkbox_column = False,
                )
                ],scroll=ft.ScrollMode.ALWAYS,),
                width=880,
                height=200,
                bgcolor=c_blue,
            ),
        ])
        
        if os.path.exists(path_ini_general_set):
            return self.general_table
        else:
            return ft.Container(ft.Text('Сет настроек не обнаружен',color=c_white,size=12,text_align='center'),width=880,margin=ft.margin.only(top=82))
        
    def build(self):
        return self.print_page()