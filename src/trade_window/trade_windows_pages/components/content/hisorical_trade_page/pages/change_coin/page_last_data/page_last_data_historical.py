
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_coin.component_change_strategy_coin import Component_change_strategy_coin

class Page_last_data_historical(ft.UserControl):
    def __init__(self,change_storage_data,regime='trade_day'):
        super().__init__()
        self.change_storage_data = change_storage_data
        self.text_for_button_slov = {
            'top_value':'Топ объёма',
            'change_list':'Список монет'
        }
        self.regime = regime

    # нажатие на кнопку выбор1
    def callback(self,e):
        self.change_storage_data(e.control.data)
        
    def print_page(self):
        file_data_dir = []
        file_data_dir_work = []
        file_data_dir_see = []
        folder_data = []
        for (dirpath, dirnames, filenames) in os.walk(f'{path_historical_freym}'):
            file_data_dir.extend(dirnames) # папки с датафреймами, корень 0,1,2
            break
        for dir in file_data_dir:
            file_data_dir_work = []
            file_data_dir_see = []
            for (dirpath, dirnames, filenames) in os.walk(f'{path_historical_freym}/{dir}/work/'):
                file_data_dir_work.extend(dirnames)
            for (dirpath, dirnames, filenames) in os.walk(f'{path_historical_freym}/{dir}/see/'):
                file_data_dir_see.extend(dirnames)
            if len(file_data_dir_work) == len(file_data_dir_see) and len(file_data_dir_work) != 0:
                folder_data.append(int(dir)) # - массив с номерами папок, где ненулевые данные, где количество дф рабочих равно кол-ву дф слежения
        #-----------------
        print_card_last_data_row = []
        config = configparser.ConfigParser()         
        config.read(path_ini_historical_freym)
        for num in reversed(sorted(folder_data)):
            how_mach_coin = config.get(str(num), 'how_mach_coin')
            coin_mas = config.get(str(num), 'coin_mas')
            volume = config.get(str(num), 'volume')
            see_volume = config.get(str(num), 'see_volume')
            tf_see = config.get(str(num), 'tf_see')
            tf_work = config.get(str(num), 'tf_work')
            how_mach_time = config.get(str(num), 'how_mach_time')
            strategy_coin = config.get(str(num), 'strategy_coin')
            time = config.get(str(num), 'time')
            date_start = config.get(str(num), 'date_start')
            date_end = config.get(str(num), 'date_end')
            
            date_format_bin = "%Y-%m-%d"
            a = datetime.strptime(str(date_start).split(' ')[0], date_format_bin)
            b = datetime.strptime(str(date_end).split(' ')[0], date_format_bin)
            delta = (b - a).days
            
            print_card_last_data_row.append(ft.Container(
                ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Container(ft.Text(num,size=12,color=c_white,text_align='center'),border=ft.border.all(1,c_white),padding=ft.padding.only(top=5,bottom=5),width=30,margin=ft.margin.only(top=-6,left=-6)),
                        ft.Container(ft.Text(time,size=12,color=c_white,text_align='center'),border=ft.border.all(1,c_white),padding=ft.padding.only(top=5,bottom=5),width=146,margin=ft.margin.only(top=-6,right=-6,left=-11)),
                    ]),
                    ft.Text(f'Кол-во монет - {how_mach_coin}',color=c_white,size=12),
                    ft.Text(f'Таймфрейм рабочий - {tf_work}',color=c_white,size=12),
                    ft.Text(f'Таймфрейм слежения - {tf_see}',color=c_white,size=12),
                    ft.Text(f'Объём рабочий - {int(float(volume))}',color=c_white,size=12),
                    ft.Text(f'Объём слежения - {int(float(see_volume))}',color=c_white,size=12),
                    ft.Text(f'Длительность фрейма - {how_mach_time}',color=c_white,size=12),
                    ft.Text(f'Стратегия - {self.text_for_button_slov[strategy_coin]}',color=c_white,size=12),
                    ft.Text(f'Дата страт - {date_start.split(' ')[0]}',color=c_white,size=12),
                    ft.Text(f'Дата конец - {date_end.split(' ')[0]}',color=c_white,size=12),
                    ft.Text(f'Торговых дней - {delta}',color=c_white,size=12),
                    ft.Container(ft.ElevatedButton(content = ft.Text('Выбрать',size=12,),data=num,bgcolor=c_yelow,on_click=self.callback,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30,margin=ft.margin.only(top=0,bottom=0)),
                ]),
                # width=500,height=500,bgcolor=c_blue,
                border=ft.border.all(1,c_white),padding=5
            ))



        self.page_last_data = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text('Используйте ранее полученные данные\nдля тестирования новых торговых стратегий',
                                        size=12,color=c_white,text_align='center'),padding=ft.padding.only(left=320)),
                                ft.Container(
                                    ft.Column(
                                        controls=[
                                            ft.Container(
                                                ft.Container(ft.Text('Хранилище торговых данных',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white),
                                            )),
                                            ft.Container(
                                                ft.Container(
                                                    ft.GridView(
                                                        controls = print_card_last_data_row,
                                                        expand=1,
                                                        runs_count=5,
                                                        child_aspect_ratio=0.50,
                                                        spacing=5,
                                                        run_spacing=5,
                                                        
                                                    )
                                                ),
                                                width=920,
                                                height=514,
                                                border = ft.border.all(1, c_white),
                                                padding=10,
                                            ), 
                                        ]
                                    )
                                ),
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )

        return self.page_last_data

    def build(self):
        return self.print_page()