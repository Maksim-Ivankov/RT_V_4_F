import flet as ft
from variable import *
from imports import *


# основные настройки лежат здесь1

# вытаскиваем название стратегии
# # настройки стратегий лежат здесб
def def_print_set_settings(number_folder):

    name_strat = strategys_our
    strat_mas = []
    # вытаскиваем название стратегии
    folder_strat = os.listdir(f'{path_save_trade}\\{number_folder}')
    for file in folder_strat:
        if file!='log_trade.txt' and file!='settings_our.txt' and file!='trade.txt':
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

def def_print_our_settings(number_folder):
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

# собираем данные для отрисовки логов в окне логов
def def_print_log(number_folder):
    log_mas = []
    path_settings = f'{path_save_trade}\\{number_folder}\\log_trade.txt'
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
def def_print_trade(number_folder,click_trade):
    trade_mas = []
    path_settings = f'{path_save_trade}\\{number_folder}\\trade.txt'
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






