import flet as ft
from variable import *
from imports import *


# основные настройки лежат здесь11

# вытаскиваем название стратегии
# # настройки стратегий лежат здесь
def def_print_set_settings(number_folder,number_trade_folder,strategy_now):

    config = configparser.ConfigParser()         
    config.read(path_imports_config)
    regime_trade_page = config.get('param_trade_historical_trade_svobodniy_freym', 'regime_trade_page')
    if regime_trade_page == 'svoboda':
        name_strat = strategys_our
        strat_mas = []
        strat_mas = strategy_now
        if len(strat_mas) == 1: 
            folder_strat = f'{path_save_trade}\\{number_folder}\\{strat_mas[0]}_set.ini'
            config_set = configparser.ConfigParser()  
            config_set.read(folder_strat)
            # ------------------------------------------
            # проходимся по массив параметров стратегий и добавляем отрисовку этих параметров
            controls_for_strat = []
            for key in strategys_parametry_rus:
                if strat_mas[0] == key:
                    count_parametr = 0
                    controls_for_strat[:] = []
                    for parametr in strategys_parametry_rus[key]:
                        controls_for_strat.append(ft.Text(f'{parametr} - {config_set.get(f'{str(number_trade_folder)}_section', strategys_parametry_for_section[key][count_parametr])}',size=12))
                        count_parametr+=1
                    strat_set_print = ft.Container(ft.Column(controls=controls_for_strat))
            # ------------------------------------------
        path_settings = f'{path_save_trade}\\{number_folder}\\settings_our.txt'
        if os.path.isfile(path_settings):
            with open(path_settings) as file:
                array_data_row = [row.strip() for row in file]
                strategys_data = literal_eval(array_data_row[0].split('&')[22]) # ['MA']
        strat_elements = []
        count_strat = 0
        for strat in strat_mas:
            strat_elements.append(ft.Container(ft.Column(controls=[
                ft.Text(f'Стратегия: {name_strat[strat]}'),
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
    elif regime_trade_page == 'historical':
        name_strat = strategys_our
        strat_mas = []
        # вытаскиваем название стратегии
        folder_strat = os.listdir(f'{path_save_trade}\\{number_folder}')
        for file in folder_strat:
            if file!='folder_trade' and file!='settings_our.txt':
                strat_mas.append(file.rstrip('.txt'))
    
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
                ft.Text(f'Стратегия: {name_strat[strat]}'),
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

def def_print_our_settings(number_folder,number_trade_folder,strategy_now):
    
    config = configparser.ConfigParser()         
    config.read(path_imports_config)
    regime_trade_page = config.get('param_trade_historical_trade_svobodniy_freym', 'regime_trade_page')
    path_settings = f'{path_save_trade}\\{number_folder}\\settings_our.txt'
    if regime_trade_page == 'svoboda':
        folder_strat = f'{path_save_trade}\\{number_folder}\\general_set.ini'
        config_set = configparser.ConfigParser()  
        config_set.read(folder_strat)
        if os.path.isfile(path_settings):
            with open(path_settings) as file:
                array_data_row = [row.strip() for row in file]
        strategi_coin_data = array_data_row[0].split('&')[0] # top_value
        work_tf_data = array_data_row[0].split('&')[2] # 5m
        dlitelnost_data = array_data_row[0].split('&')[3] # 24h
        how_mach_money_data = array_data_row[0].split('&')[4] # 6
        regim_tp_data = '???' 
        regim_sl_data = '???'
        regim_volume_min_data = '???'
        regim_volume_max_data = '???'
        name_bot_data = array_data_row[0].split('&')[13] # V 22_07_24_1
        komission_mayker_data = array_data_row[0].split('&')[14]#  0.2
        leverage_data = config_set.get(f'{str(number_trade_folder)}_section', 'leveradg')
        komission_taker_data = array_data_row[0].split('&')[17] # 0.1
        tp_data = config_set.get(f'{str(number_trade_folder)}_section', 'diapazon_tp')
        sl_data = config_set.get(f'{str(number_trade_folder)}_section', 'diapazon_sl')
        volume_min_data = config_set.get(f'{str(number_trade_folder)}_section', 'diapazon_volume_min')
        volume_max_data = config_set.get(f'{str(number_trade_folder)}_section', 'diapazon_volume_max')
        strategys_data = array_data_row[0].split('&')[22] # ['MA']
    elif regime_trade_page == 'historical':
        if os.path.isfile(path_settings):
            with open(path_settings) as file:
                array_data_row = [row.strip() for row in file]
        strategi_coin_data = array_data_row[0].split('&')[0] # top_value
        work_tf_data = array_data_row[0].split('&')[2] # 5m
        dlitelnost_data = array_data_row[0].split('&')[3] # 24h
        how_mach_money_data = array_data_row[0].split('&')[4] # 6
        regim_tp_data = array_data_row[0].split('&')[9]
        regim_sl_data = array_data_row[0].split('&')[10]
        regim_volume_min_data = array_data_row[0].split('&')[11]
        regim_volume_max_data = array_data_row[0].split('&')[12]
        name_bot_data = array_data_row[0].split('&')[13] # V 22_07_24_1
        komission_mayker_data = array_data_row[0].split('&')[14]#  0.2
        leverage_data = array_data_row[0].split('&')[16]
        komission_taker_data = array_data_row[0].split('&')[17] # 0.1
        tp_data = array_data_row[0].split('&')[18]
        sl_data = array_data_row[0].split('&')[19]
        volume_min_data = array_data_row[0].split('&')[20]
        volume_max_data = array_data_row[0].split('&')[21]
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

# собираем данные для отрисовки логов в окне логов
def def_print_log(number_folder,number_trade_folder,strategy_now):
    log_mas = []
    path_settings = f'{path_save_trade}\\{number_folder}\\folder_trade\\{number_trade_folder}\\log_trade.txt'
    if os.path.isfile(path_settings):
        with open(path_settings) as file:
            array_data_row = [row.strip() for row in file]
            for i in array_data_row:
                if int(i.split('|')[0])>20:
                    if i.split('|')[3]=='no':
                        log_mas.append(ft.Container(ft.Text(
                            f'{i.split('|')[0]} | Депозит {i.split('|')[1]} | нет сигнала',
                        )))
                    else:
                        log_mas.append(ft.Container(ft.Text(
                            f'{i.split('|')[0]} | Депозит {i.split('|')[1]} | Сделка {i.split('|')[3]} {i.split('|')[4]}',
                        )))
    return log_mas



    

# данные для отрисовки сделок в окне сделок
def def_print_trade(number_folder,click_trade,number_trade_folder,strategy_now):
    trade_mas = []
    path_settings = f'{path_save_trade}\\{number_folder}\\folder_trade\\{number_trade_folder}\\trade.txt'
    # print(path_settings)
    if os.path.isfile(path_settings):
        with open(path_settings) as file:
            array_data_row = [row.strip() for row in file]
            count_trade_table = 0
            for i in array_data_row:
                if float(i.split('|')[3]) > 0: 
                    trade_mas.append(ft.Container(ft.Text(f'{i.split('|')[0]} | Результат {i.split('|')[3]} | Монета {i.split('|')[6]}',color=c_blue,text_align='center'),data=str(count_trade_table),height=30,bgcolor=c_green,width=400,on_click=click_trade))
                    count_trade_table+=1
                else: 
                    trade_mas.append(ft.Container(ft.Text(f'{i.split('|')[0]} | Результат {i.split('|')[3]} | Монета {i.split('|')[6]}',color=c_blue,text_align='center'),data=str(count_trade_table),height=30,bgcolor=c_red,width=400,on_click=click_trade))
                    count_trade_table+=1
    else:
        trade_mas.append(ft.Container(ft.Text('Нет сделок',color=c_white,text_align='center'),height=30,bgcolor=c_blue_binance,width=400))
    return trade_mas






