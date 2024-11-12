
import flet as ft
from variable import *
from imports import *


from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.set_settings.page_trade.UI.data_settings import def_print_our_settings as def_print_our_settings_2
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.trade_page.UI.set_settings.page_trade.UI.data_settings import def_print_set_settings as def_print_set_settings_2
from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config
from src.trade_window.trade_windows_pages.components.content.UI.input import Input


class Add_to_favorites_page(ft.UserControl):
    def __init__(self,change_page,place_down = ''):
        super().__init__()
        self.place_down = place_down
        self.change_page = change_page
        self.name_strat = strategys_our
        self.input_name_strat_value = ''
        self.input_description_strat_value = 'Хорошие результаты. Тестировать'
        self.flag_dublicate = 0
        
# Функция добавляет общие настройки из торговли по одной нсатройке
    def def_print_our_settings(self,number_folder):
        path_settings = f'{path_save_trade}\\{number_folder}\\settings_our.txt'
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
        folder_strat = os.listdir(f'{path_save_trade}\\{number_folder}')
        for file in folder_strat:
            if file!='log_trade.txt' and file!='settings_our.txt' and file!='trade.txt':
                strat_mas.append(file.rstrip('.txt'))

        if len(strat_mas)!=1:
                self.name_strat_favorites = 'Сет стратегий'
        else:
            self.name_strat_favorites = self.name_strat[strat_mas[0]]


        if len(strat_mas) == 1: 
            folder_strat = f'{path_save_trade}\\{number_folder}\\{strat_mas[0]}.txt'
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
                    

        path_settings = f'{path_save_trade}\\{number_folder}\\settings_our.txt'
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

    def dublicate_strat(self,status,number_same_strat):
        self.controls[0].content.content.content.controls[1].content.controls[2].content.value = f'{status} № {str(number_same_strat)}'
        self.update()

    def save_to_favorites(self,e):
        self.flag_dublicate = 0
        if len(os.listdir(path_favorites)) == 0:
            self.path_folder_favorites = f'{path_favorites}\\1'
        else:
            self.path_folder_favorites = f'{path_favorites}\\{int(os.listdir(path_favorites)[-1])+1}'
        if len(self.folder_trade) == 1: # если в массиве одно число, значит торговля на одной настройке
            # блок поиска дубликатов тсратегий
            #--------------------------------
            if len(os.listdir(path_favorites))>=1: # если сохранено больше одной стратегии
                # print(path_favorites)
                for i in os.listdir(path_favorites): # итерируемся по папкам с сохранененными стратегиями
                    # проверка на дубликаты через settings_our
                    if os.path.isfile(f'{path_save_trade}\\{self.folder_trade[0]}\\settings_our.txt'):
                        with open(f'{path_save_trade}\\{self.folder_trade[0]}\\settings_our.txt') as file: # открываем настройки стратегии, которую хотим сохранить
                            array_data_1 = [row.strip() for row in file]
                    if os.path.isfile(f'{path_favorites}\\{i}\\settings_our.txt'):
                        with open(f'{path_favorites}\\{i}\\settings_our.txt') as file: # открываем настройки стратегии, которую хотим сохранить
                            array_data_2 = [row.strip() for row in file]
                    if array_data_1==array_data_2:
                        self.dublicate_strat('Совпадают настройки стратегий',i)
                        self.flag_dublicate = 1
                        break
                    # проверка на дубликаты через property - название
                    if os.path.isfile(f'{path_favorites}\\{i}\\property.txt'):
                        with open(f'{path_favorites}\\{i}\\property.txt') as file: # открываем настройки стратегии, которую хотим сохранить
                            array_data_2 = [row.strip() for row in file]
                    if self.input_name_strat_value == '': proverka_name = self.name_strat_favorites
                    else: proverka_name = self.input_name_strat_value
                    if array_data_2[0]==proverka_name:
                        self.dublicate_strat('Совпадают названия стратегий',i)
                        self.flag_dublicate = 1
                        break
                    
            if self.flag_dublicate==0:
                # создаем номерную папку в фаворитах
                os.mkdir(self.path_folder_favorites)
                # создаем папку folder_trade внутри созданной папки избранной стратегии
                os.mkdir(f'{self.path_folder_favorites}\\folder_trade')
                self.path_folder_favorites_number_trade = f'{self.path_folder_favorites}\\folder_trade\\1'
                os.mkdir(self.path_folder_favorites_number_trade)
                # копируем settings_our.txt из трейда в избранное
                shutil.copy(
                    os.path.join(f'{path_save_trade}\\{self.folder_trade[0]}', 'settings_our.txt'),
                    os.path.join(f'{self.path_folder_favorites}') # путь сохранения 
                )
                # получаем стратегию торговли
                path_settings = f'{self.path_folder_favorites}\\settings_our.txt'
                if os.path.isfile(path_settings):
                    with open(path_settings) as file:
                        array_data_row = [row.strip() for row in file]
                        strategys_data = literal_eval(array_data_row[0].split('&')[22]) # ['MA']
                        coins_mas = array_data_row[0].split('&')[5]
                        number_data_df = array_data_row[0].split('&')[6]
                # копируем файлы с настройками стратегии торговли
                for i in strategys_data:
                    shutil.copy(
                        os.path.join(f'{path_save_trade}\\{self.folder_trade[0]}', f'{i}.txt'),
                        os.path.join(f'{self.path_folder_favorites}') # путь сохранения 
                    )
                # копируем данные трейда
                shutil.copy(
                os.path.join(f'{path_save_trade}\\{self.folder_trade[0]}', 'log_trade.txt'),
                os.path.join(f'{self.path_folder_favorites_number_trade}') # путь сохранения 
                )
                shutil.copy(
                os.path.join(f'{path_save_trade}\\{self.folder_trade[0]}', 'trade.txt'),
                os.path.join(f'{self.path_folder_favorites_number_trade}') # путь сохранения 
                )
                if self.input_name_strat_value=='':self.input_name_strat_value=self.name_strat_favorites
                file = open(f'{self.path_folder_favorites}\\property.txt', 'a')
                file.write(f'{self.input_name_strat_value}\n{self.input_description_strat_value}')
                file.close()
                file = open(f'{self.path_folder_favorites_number_trade}\\df_data.txt', 'a')
                file.write(f'{coins_mas}\n{number_data_df}')
                file.close()
                self.change_page(e)
                
        if len(self.folder_trade) == 2:
            # блок поиска дубликатов тсратегий
            #--------------------------------
            array_data_2 = self.get_settings_set_real(self.folder_trade[0],self.folder_trade[1])
            if len(os.listdir(path_favorites))>=1: # если сохранено больше одной стратегии
                for i in os.listdir(path_favorites): # итерируемся по папкам с сохранененными стратегиями
                    # проверка на дубликаты через settings_our
                    if os.path.isfile(f'{path_favorites}\\{i}\\settings_our.txt'):
                        with open(f'{path_favorites}\\{i}\\settings_our.txt') as file: # открываем настройки стратегии, которую хотим сохранить
                            array_data_1 = [row.strip() for row in file]
                    array_data_01 = array_data_1[0].split('&')
                    if array_data_01==array_data_2:
                        self.dublicate_strat('Совпадают настройки стратегий',i)
                        self.flag_dublicate = 1
                        break
                    # проверка на дубликаты через property - название
                    if os.path.isfile(f'{path_favorites}\\{i}\\property.txt'):
                        with open(f'{path_favorites}\\{i}\\property.txt') as file: # открываем настройки стратегии, которую хотим сохранить
                            array_data_2 = [row.strip() for row in file]
                    if self.input_name_strat_value == '': proverka_name = self.name_strat_favorites
                    else: proverka_name = self.input_name_strat_value
                    if array_data_2[0]==proverka_name:
                        self.dublicate_strat('Совпадают названия стратегий',i)
                        self.flag_dublicate = 1
                        break
            if self.flag_dublicate==0:
                # создаем номерную папку в фаворитах
                os.mkdir(self.path_folder_favorites)
                # создаем папку folder_trade внутри созданной папки избранной стратегии
                os.mkdir(f'{self.path_folder_favorites}\\folder_trade')
                self.path_folder_favorites_number_trade = f'{self.path_folder_favorites}\\folder_trade\\1'
                os.mkdir(self.path_folder_favorites_number_trade)
                # копируем settings_our.txt из трейда в избранное
                array_data_2 = self.get_settings_set_real(self.folder_trade[0],self.folder_trade[1])
                file = open(f'{self.path_folder_favorites}\\settings_our.txt', 'a')
                file.write(self.convert_mas_to_str(array_data_2))
                file.close()
                coins_mas = array_data_2[5]
                number_data_df = array_data_2[6]
                # копируем файлы с настройками стратегии торговли
                for i in literal_eval(array_data_2[22]):
                    config_set_54 = configparser.ConfigParser()  
                    config_set_54.read(f'{path_save_trade}\\{self.folder_trade[0]}\\{i}_set.ini')
                    deposit_data = config_set_54.items(f'{self.folder_trade[1]}_section')
                    # print(deposit_data[1][1])
                    stroka_strategy_settings = ''
                    for j in deposit_data:
                        if j!=deposit_data[-1]:stroka_strategy_settings = stroka_strategy_settings + str(j[1]) + '&'
                        else: stroka_strategy_settings = stroka_strategy_settings + str(j[1])
                    file = open(f'{self.path_folder_favorites}\\{i}.txt', 'a')
                    file.write(stroka_strategy_settings)
                    file.close()

                # копируем данные трейда
                shutil.copy(
                    os.path.join(f'{path_save_trade}\\{self.folder_trade[0]}\\folder_trade\\{self.folder_trade[1]}', 'log_trade.txt'),
                    os.path.join(f'{self.path_folder_favorites_number_trade}') # путь сохранения 
                )
                shutil.copy(
                    os.path.join(f'{path_save_trade}\\{self.folder_trade[0]}\\folder_trade\\{self.folder_trade[1]}', 'trade.txt'),
                    os.path.join(f'{self.path_folder_favorites_number_trade}') # путь сохранения 
                )
                if self.input_name_strat_value=='':self.input_name_strat_value=self.name_strat_favorites
                file = open(f'{self.path_folder_favorites}\\property.txt', 'a')
                file.write(f'{self.input_name_strat_value}\n{self.input_description_strat_value}')
                file.close()
                file = open(f'{self.path_folder_favorites_number_trade}\\df_data.txt', 'a')
                file.write(f'{coins_mas}\n{number_data_df}')
                file.close()
                self.change_page(e)



                    
    # конвертируем массив с параметрами в строку          
    def convert_mas_to_str(self,mas):
        stroka = ''
        for i in mas:
            if i!=mas[-1]:stroka = stroka + str(i) + '&'
            else: stroka = stroka + str(i)
        return stroka
                   
                    
                    
                    
    # передаем номер трейда и папки в сете, возвращает правильный массив, слепленный из настроек текущей папки и генеральных
    def get_settings_set_real(self,number_trade,number_folder):
        if os.path.isfile(f'{path_save_trade}\\{number_trade}\\settings_our.txt'):
            with open(f'{path_save_trade}\\{number_trade}\\settings_our.txt') as file: # открываем настройки стратегии, которую хотим сохранить
                array_data_row = [row.strip() for row in file]
        config_set = configparser.ConfigParser()  
        config_set.read(f'{path_save_trade}\\\\{number_trade}\\general_set.ini')
        strategi_coin_data = array_data_row[0].split('&')[0] # top_value
        sledim_money_data = array_data_row[0].split('&')[1] # 1m
        work_tf_data = array_data_row[0].split('&')[2] # 5m
        dlitelnost_data = array_data_row[0].split('&')[3] # 24h
        how_mach_money_data = array_data_row[0].split('&')[4] # 6
        coins_trade_data = array_data_row[0].split('&')[5]# 
        number_trade_data = array_data_row[0].split('&')[6] # 24
        use_last_number_data = array_data_row[0].split('&')[7] # 5
        use_last_sost_data = array_data_row[0].split('&')[8] # false
        regim_tp_data = array_data_row[0].split('&')[9] # fiks
        regim_sl_data = array_data_row[0].split('&')[10] # fiks
        regim_volume_min_data = array_data_row[0].split('&')[11] # fiks
        regim_volume_max_data = array_data_row[0].split('&')[12] # fiks
        name_bot_data = array_data_row[0].split('&')[13] # V 22_07_24_1
        komission_mayker_data = array_data_row[0].split('&')[14]#  0.2
        deposit_data = config_set.get(f'{str(number_folder)}_section', 'depo')
        leverage_data = config_set.get(f'{str(number_folder)}_section', 'leveradg')
        komission_taker_data = array_data_row[0].split('&')[17] # 0.1
        tp_data = config_set.get(f'{str(number_folder)}_section', 'diapazon_tp')
        sl_data = config_set.get(f'{str(number_folder)}_section', 'diapazon_sl')
        volume_min_data = str(float(config_set.get(f'{str(number_folder)}_section', 'diapazon_volume_min')))
        volume_max_data = str(float(config_set.get(f'{str(number_folder)}_section', 'diapazon_volume_max')))
        strategys_data = array_data_row[0].split('&')[22] # ['MA']
        change_time_settings = array_data_row[0].split('&')[23] # 1
        time_on_work = config_set.get(f'{str(number_folder)}_section', 'start_time')
        time_off_work = config_set.get(f'{str(number_folder)}_section', 'stop_time')
        
        return [strategi_coin_data,sledim_money_data,work_tf_data,dlitelnost_data,how_mach_money_data,coins_trade_data,number_trade_data,use_last_number_data,use_last_sost_data,regim_tp_data,regim_sl_data,regim_volume_min_data,regim_volume_max_data,name_bot_data,komission_mayker_data,deposit_data,leverage_data,komission_taker_data,tp_data,sl_data,volume_min_data,volume_max_data,strategys_data,change_time_settings,time_on_work,time_off_work,]
           
                

    def build(self):
        config = configparser.ConfigParser()  
        config.read(path_imports_config)
        self.folder_trade = literal_eval(config.get('param_trade_historical_trade_svobodniy_freym', 'now_trade'))
        # self.name_strat = config.get('param_trade_historical_trade_svobodniy_freym', 'name_strat_favorites')
        
        # формируем кнопки назад
        if self.place_down!='':
            if self.place_down['place'] == 'История торговли - из сета':
                self.data_for_back = {'page':'История торговли | Сет','number_trade':self.folder_trade[0]}
            elif self.place_down['place'] == 'Торговля на сете настроек':
                self.data_for_back = {'page':'История торговли | Сет','number_trade':self.folder_trade[0]}
            elif self.place_down['place'] == 'История торговли':
                self.data_for_back = {'page':'История торговли | Одна настройка','number_trade':self.folder_trade[0]}
            elif self.place_down['place'] == 'Торговля на одной настройке':
                self.data_for_back = {'page':'История торговли | Одна настройка','number_trade':self.folder_trade[0]}
        else:self.data_for_back = 'Первая'
        
        # если папка торговли с одной настрокой
        if len(self.folder_trade) == 1:
            print_our_settings_ret_fun = self.def_print_our_settings(self.folder_trade[0])
            def_print_set_settings_ret_fun = self.def_print_set_settings(self.folder_trade[0])
        elif len(self.folder_trade) == 2:
            strat_mas = []
            # вытаскиваем название стратегии
            folder_strat = os.listdir(f'{path_save_trade}\\{self.folder_trade[0]}')
            for file in folder_strat:
                if file!='folder_trade' and file!='settings_our.txt' and file!='general_set.ini':
                    strat_mas.append(file.rstrip('_set.ini'))
            print_our_settings_ret_fun = def_print_our_settings_2(self.folder_trade[0],self.folder_trade[1],strat_mas)
            def_print_set_settings_ret_fun = def_print_set_settings_2(self.folder_trade[0],self.folder_trade[1],strat_mas)
            if len(strat_mas)!=1:
                self.name_strat_favorites = 'Сет стратегий'
            else:
                self.name_strat_favorites = self.name_strat[strat_mas[0]]
        
        print_settings = ft.Container(
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
        width=900,padding=ft.padding.only(left=20))


        self.ferst_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text('Добавление торговой стратегии в избранные стратегии. Поможет эффективнее протестировать преспективные\nнастройки прибыльных торговых стратегий.',size=12,color=c_white,text_align='center'),width=900,margin=ft.margin.only(bottom=10)),
                                ft.Container(#11
                                    ft.Column(controls=[
                                        print_settings,
                                        # ft.Container(height=1,width=900,bgcolor=c_white,margin=ft.margin.only(top=20)),
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
                                                                        ft.Container(Input(self.input_description_strat,'Хорошие результаты. Тестировать',400),margin=10),
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
                                                ft.Container(ft.ElevatedButton(content = ft.Text('Назад',size=12,),data=self.data_for_back,on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                                ft.Container(ft.ElevatedButton(content = ft.Text('Сохранить в избранное',size=12,),data='Избранные стратегии',on_click=self.save_to_favorites,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                            ]),padding=ft.padding.only(left=320,top=5)
                                            ),
                                            width=500
                                        ),
                                    ]),width=900
                                ),
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.ferst_page