# страница выбора стратегии торговли
import flet as ft
from variable import *
from imports import *

class One_table(ft.UserControl):
    def __init__(self):
        super().__init__()
        

    def print_page(self):

        datas_print = []
        config_general_set = configparser.ConfigParser()  
        config_general_set.read(path_ini_one_set)
        count = 1
        for i in config_general_set.sections():
            datas_print.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(count,text_align='center',color=c_white,size=12,width=20)),
                    ft.DataCell(ft.Text(config_general_set.get(i, 'up_chanal'),text_align='center',color=c_white,size=12,width=60)),
                    ft.DataCell(ft.Text(config_general_set.get(i, 'down_chanal'),text_align='center',color=c_white,size=12,width=60)),
                    ft.DataCell(ft.Text(config_general_set.get(i, 'corner_long'),text_align='center',color=c_white,size=12,width=100)),
                    ft.DataCell(ft.Text(config_general_set.get(i, 'corner_short'),text_align='center',color=c_white,size=12,width=100)),  
                ])
            )
            count+=1      

        self.general_table = ft.Column(controls=[
            ft.Container(
                ft.Column(controls=[
                    ft.DataTable(columns=[
                        ft.DataColumn(ft.Text('№',text_align='center',color=c_white,size=12)),
                        ft.DataColumn(ft.Text('Верх канала',text_align='center',color=c_white,size=12)),
                        ft.DataColumn(ft.Text('Низ канала',text_align='center',color=c_white,size=12)),
                        ft.DataColumn(ft.Text('Угол тренда лонг',text_align='center',color=c_white,size=12)),
                        ft.DataColumn(ft.Text('Угол тренда шорт',text_align='center',color=c_white,size=12)),
   
                        
                    ],rows = datas_print,
                    column_spacing = 108,
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
        
        if os.path.exists(path_ini_one_set):
            return self.general_table
        else:
            return ft.Container(ft.Text('Сет настроек не обнаружен',color=c_white,size=12,text_align='center'),width=880,margin=ft.margin.only(top=82))
        

    def build(self):
        return self.print_page()