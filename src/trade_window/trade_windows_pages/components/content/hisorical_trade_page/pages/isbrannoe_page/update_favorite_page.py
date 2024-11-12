
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.UI.input import Input
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.isbrannoe_page.UI.modal_delete_checked import Modal_delete_checked

class Update_favorite_page(ft.UserControl):
    def __init__(self,change_page,number_favorite):
        super().__init__()
        self.change_page = change_page
        self.number_favorite = number_favorite
        self.name_strat = strategys_our
        

# Функция добавляет общие настройки из торговли по одной нсатройке
    def def_print_our_settings(self,number_favorite):
        path_settings =f'{path_favorites}\\{number_favorite}\\settings_our.txt'
        if os.path.isfile(path_settings):
            with open(path_settings) as file:
                array_data_row = [row.strip() for row in file]
                # ["top_value&1m&5m&24h&6&BTCUSDT|ETHUSDT|SOLUSDT|BOMEUSDT|BTCUSDC|1000PEPEUSDT&24&5&False&fiks&fiks&fiks&fiks&V 22_07_24_1&0.2&100&20&0.1&0.3&0.3&200000&1500000&['MA']"]
                strategi_coin_data = array_data_row[0].split('&')[0] # top_value
                # sledim_money_data = array_data_row[0].split('&')[1] # 1m
                work_tf_data = array_data_row[0].split('&')[2] # 5m
                dlitelnost_data = array_data_row[0].split('&')[3] # 24h
                how_mach_money_data = array_data_row[0].split('&')[4] # 6
                # coins_trade_data = array_data_row[0].split('&')[5]# 
                # number_trade_data = array_data_row[0].split('&')[6] # 24
                # use_last_number_data = array_data_row[0].split('&')[7] # 5
                # use_last_sost_data = array_data_row[0].split('&')[8] # false
                regim_tp_data = array_data_row[0].split('&')[9] # fiks
                regim_sl_data = array_data_row[0].split('&')[10] # fiks
                regim_volume_min_data = array_data_row[0].split('&')[11] # fiks
                regim_volume_max_data = array_data_row[0].split('&')[12] # fiks
                name_bot_data = array_data_row[0].split('&')[13] # V 22_07_24_1
                komission_mayker_data = array_data_row[0].split('&')[14]#  0.2
                # deposit_data = array_data_row[0].split('&')[15] # 100
                leverage_data = array_data_row[0].split('&')[16] # 20
                komission_taker_data = array_data_row[0].split('&')[17] # 0.1
                tp_data = array_data_row[0].split('&')[18] # 0.5
                sl_data = array_data_row[0].split('&')[19] # 4 
                volume_min_data = array_data_row[0].split('&')[20] # 500
                volume_max_data = array_data_row[0].split('&')[21] # 200000000
                strategys_data = array_data_row[0].split('&')[22] # ['MA']

        print_our_settings = ft.Container(
            ft.Row(controls=[
                ft.Container(
                    ft.Column(controls=[
                        ft.Text(f'Имя робота для логов: {name_bot_data}',size=12),
                        ft.Text(f'Режим монеты: {strategi_coin_data}',size=12),
                        ft.Text(f'Сколько монет торговать: {how_mach_money_data}',size=12),
                        ft.Text(f'Комиссия мейкер: {komission_mayker_data}',size=12),
                        ft.Text(f'Комиссия тейкер: {komission_taker_data}',size=12),
                        ft.Text(f'Таймфрейм: {work_tf_data}',size=12),
                        ft.Text(f'Длительность торговли: {dlitelnost_data}',size=12),
                    ],scroll=ft.ScrollMode.ALWAYS,),
                    width=230,height=140),
                ft.Container(width=1,height=140,bgcolor=c_white),
                ft.Container(
                    ft.Column(controls=[
                        ft.Text(f'Режим тейка/стопа: {regim_tp_data}/{regim_sl_data}',size=12),
                        ft.Text(f'Тейк профит: {tp_data}',size=12),
                        ft.Text(f'Стоп лосс: {sl_data}',size=12),
                        ft.Text(f'Режим объёмов: {regim_volume_min_data}/{regim_volume_max_data}',size=12),
                        ft.Text(f'Объём торгов мин: {volume_min_data}',size=12),
                        ft.Text(f'Объём торгов макс: {volume_max_data}',size=12),
                        ft.Text(f'Плечо: {leverage_data}',size=12),
                    ],scroll=ft.ScrollMode.ALWAYS,),
                    width=230,height=140),
            ]),padding=10
        )

        return print_our_settings
        

# Фукция добавляет настройки стратегии из торговли по одной настройке
    def def_print_set_settings(self,number_folder):
        
        strat_mas = []
        # вытаскиваем название стратегии
        folder_strat = os.listdir(f'{path_favorites}\\{number_folder}')
        for file in folder_strat:
            if file!='folder_trade' and file!='settings_our.txt' and file!='property.txt':
                strat_mas.append(file.rstrip('.txt'))


        if len(strat_mas) == 1: 
            folder_strat = f'{path_favorites}\\{number_folder}\\{strat_mas[0]}.txt'
            if os.path.isfile(folder_strat):
                with open(folder_strat) as file:
                    array_data_row = [row.strip() for row in file]
            # ------------------------------------------
            # проходимся по массив параметров стратегий и добавляем отрисовку этих параметров    
            controls_for_strat = []
            for key in strategys_parametry_rus:
                if strat_mas[0] == key:
                    count_parametr = 0
                    controls_for_strat[:] = []
                    for parametr in strategys_parametry_rus[key]:
                        controls_for_strat.append(ft.Text(f'{parametr} - {array_data_row[0].split('&')[count_parametr]}',size=12))
                        count_parametr+=1
                    strat_set_print = ft.Container(ft.Column(controls=controls_for_strat))
             # ------------------------------------------

        path_settings = f'{path_favorites}\\{number_folder}\\settings_our.txt'
        if os.path.isfile(path_settings):
            with open(path_settings) as file:
                array_data_row = [row.strip() for row in file]
                strategys_data = array_data_row[0].split('&')[22] # ['MA']
        # print(strategys_data)
        strat_elements = []
        count_strat = 0
        for strat in strat_mas:
            strat_elements.append(ft.Container(ft.Column(controls=[
                ft.Text(f'Стратегия: {self.name_strat[strat]}'),
                strat_set_print
            ])))
            count_strat+=1
            if len(strategys_data) != count_strat:
                strat_elements.append(ft.Container(width=350,height=1,bgcolor=c_white))


        print_set_settings = ft.Container(
            ft.Container(
                ft.Column(controls=strat_elements,scroll=ft.ScrollMode.ALWAYS,),
                width=350,height=140),padding=10
        )
        return print_set_settings


    # Обработка инпута имся
    def input_name_strat(self,e):
       self.input_name_strat_value = e.control.value
    
    # обработка инпута описание
    def input_description_strat(self,e):
       self.input_description_strat_value = e.control.value
       print(e.control.value)

    def save_to_changes(self,e):
        file = open(f'{path_favorites}\\{self.number_favorite}\\property.txt', 'w')
        file.write(f'{self.input_name_strat_value}\n{self.input_description_strat_value}')
        file.close()
        self.change_page(e)
        
    # открывает модалку - точно удалить
    def delete_favorite(self,e):
        bs = Modal_delete_checked(self.name_strat_favorites,self.change_page,self.number_favorite,'delete')
        self.page.overlay.append(bs)
        self.page.update()

    # кнопка - очистить трейды
    def clear_trade(self,e):
        bs = Modal_delete_checked(self.name_strat_favorites,self.change_page,self.number_favorite,'clear')
        self.page.overlay.append(bs)
        self.page.update()
        

    def build(self):
        
        print_our_settings_ret_fun = self.def_print_our_settings(self.number_favorite)
        def_print_set_settings_ret_fun = self.def_print_set_settings(self.number_favorite)
        
        if os.path.isfile(f'{path_favorites}\\{self.number_favorite}\\property.txt'):
            with open(f'{path_favorites}\\{self.number_favorite}\\property.txt') as file: # открываем настройки стратегии, которую хотим сохранить
                array_data_2 = [row.strip() for row in file]
                self.name_strat_favorites = array_data_2[0]
                self.subtitle_strat_favorites = array_data_2[1]
                self.input_name_strat_value = array_data_2[0]
                self.input_description_strat_value = array_data_2[1]
        
        
        self.ferst_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text('Избранные стратегии - стратегии с задаными настройками, которые были добавлены в избранное',size=12,color=c_white,text_align='center'),
                                             width=850,margin=ft.margin.only(bottom=15)),
                                ft.Container(
                                    ft.Column(controls=[
                                        ft.Container(
                                        ft.Row(controls=[
                                            ft.Container(ft.Container(
                                                ft.Column(controls=[
                                                    ft.Column(
                                                        controls=[
                                                            ft.Container(ft.Container(ft.Text('Общие настройки',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                            ft.Container(
                                                                ft.Container(
                                                                    print_our_settings_ret_fun,
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
                                                                        def_print_set_settings_ret_fun,
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
                                            ft.Container(ft.Row(controls=[
                                                    ft.Container(
                                                        ft.Container(
                                                            ft.Column(controls=[
                                                                ft.Column(
                                                                    controls=[
                                                                        ft.Container(
                                                                            ft.Container(ft.Text('Название',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                                        ft.Container(
                                                                            ft.Container(ft.Column(controls=[
                                                                                ft.Container(ft.Text('Название стратегии или группы стратегий для избранного',size=14,color=c_white,text_align='center'),width=450,margin=ft.margin.only(top=15)),
                                                                                ft.Container(Input(self.input_name_strat,self.name_strat_favorites,400),margin=10),
                                                                            ])),
                                                                            width=500,
                                                                            # height=148,
                                                                            border = ft.border.all(1, c_white),
                                                                            bgcolor=c_blue,
                                                    )]),])),width=425,margin=ft.margin.only(left=20)),
                                                    ft.Container(
                                                        ft.Container(
                                                            ft.Column(controls=[
                                                                ft.Column(
                                                                    controls=[
                                                                        ft.Container(
                                                                            ft.Container(ft.Text('Описание',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                                        ft.Container(
                                                                            ft.Container(ft.Column(controls=[
                                                                                ft.Container(ft.Text('Описание стратегии',size=14,color=c_white,text_align='center'),width=450,margin=ft.margin.only(top=15)),
                                                                                ft.Container(Input(self.input_description_strat,self.subtitle_strat_favorites,400),margin=10),
                                                                            ])),
                                                                            width=500,
                                                                            # height=148,
                                                                            border = ft.border.all(1, c_white),
                                                                            bgcolor=c_blue,
                                                    )]),])),width=425,)
                                                ]),margin=ft.margin.only(top=10)),
                                        ft.Container(ft.Text('',color=c_red,text_align='center'),width=900,margin=5),
                                        ft.Container(
                                            ft.Container(
                                                ft.Row(controls=[
                                                ft.Container(ft.ElevatedButton(content = ft.Text('Назад',size=12,),data='Избранные стратегии',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                                ft.Container(ft.ElevatedButton(content = ft.Text('Сохранить изменения',size=12,),data='Избранные стратегии',on_click=self.save_to_changes,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                            ]),padding=ft.padding.only(left=320,top=5)
                                            ),
                                            width=500
                                        ),
                                        ft.Container(
                                            ft.Container(
                                                ft.Row(controls=[
                                                ft.Container(ft.ElevatedButton(content = ft.Text('Удалить из избранного',size=12,),on_click=self.delete_favorite,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                                ft.Container(ft.ElevatedButton(content = ft.Text('Очистить трейды',size=12,),data='Избранные стратегии',on_click=self.clear_trade,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                            ]),padding=ft.padding.only(left=280,top=5)
                                            ),
                                            width=700
                                        ),
                                    ]),width=900
                                ),
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.ferst_page