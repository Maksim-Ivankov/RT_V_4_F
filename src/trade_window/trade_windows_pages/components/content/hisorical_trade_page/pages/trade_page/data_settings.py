import flet as ft
from variable import *
from imports import *

# config = configparser.ConfigParser()  
# config.read(path_imports_config)

# # ----------------------------------------
# name_strat = {
#     'one':'Канал, тренд, локаль, объём',
#     'MA':'Скользящие средние'
# }
# strat_set_print = {
#     'one': ft.Container(ft.Column(controls=[
#         ft.Text(f'Верх канала - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_up_chanal')}',size=12),
#         ft.Text(f'Низ канала - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_down_chanal')}',size=12),
#         ft.Text(f'Угол тренда лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_corner_long')}',size=12),
#         ft.Text(f'Угол тренда шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_corner_short')}',size=12),
#         ])),
#     'MA': ft.Container(ft.Column(controls=[
#         ft.Text(f'Коэф. быстрой скольз. средней - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_koef_bistro')}',size=12),
#         ft.Text(f'Коэф. медленной скольз. средней - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_koef_medleno')}',size=12),
#         ft.Text(f'Кол-во совпадений в прошлом - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_sovpad_last')}',size=12),
#         ft.Text(f'Прижатие к верху коридора - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_up_chanal')}',size=12),
#         ft.Text(f'Прижатие к низу коридора - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_down_chanal')}',size=12),
#         ])),
# }

# mas_strat_siroy = literal_eval(config.get('param_trade_historical_trade_svobodniy_freym', 'strategys'))
# strat_elements = []
# count_strat = 0
# for strat in mas_strat_siroy:
#     strat_elements.append(ft.Container(ft.Column(controls=[
#         ft.Text(f'Стратегия: {name_strat[strat]}'),
#         strat_set_print[strat]
#     ])))
#     count_strat+=1
#     if len(mas_strat_siroy) != count_strat:
#         strat_elements.append(ft.Container(width=350,height=1,bgcolor=c_white))
    
# ----------------------------------------

# возвращает общие настройки проги для отрисовки в блоке
def print_our_settings():

    config = configparser.ConfigParser()  
    config.read(path_imports_config)

    return  ft.Container(
        ft.Row(controls=[
            ft.Container(
                ft.Column(controls=[
                    ft.Text(f'Имя робота для логов: {config.get('param_trade_historical_trade_svobodniy_freym', 'name_bot')}',size=12),
                    ft.Text(f'Режим монеты: {config.get('param_trade_historical_trade_svobodniy_freym', 'strategi_coin')}',size=12),
                    ft.Text(f'Сколько монет торговать: {config.get('param_trade_historical_trade_svobodniy_freym', 'how_mach_money')}',size=12),
                    ft.Text(f'Комиссия мейкер: {config.get('param_trade_historical_trade_svobodniy_freym', 'komission_mayker')}',size=12),
                    ft.Text(f'Комиссия тейкер: {config.get('param_trade_historical_trade_svobodniy_freym', 'komission_taker')}',size=12),
                    ft.Text(f'Таймфрейм: {config.get('param_trade_historical_trade_svobodniy_freym', 'work_tf')}',size=12),
                    ft.Text(f'Длительность торговли: {config.get('param_trade_historical_trade_svobodniy_freym', 'dlitelnost')}',size=12),
                ],scroll=ft.ScrollMode.ALWAYS,),
                width=230,height=140),
            ft.Container(width=1,height=140,bgcolor=c_white),
            ft.Container(
                ft.Column(controls=[
                    ft.Text(f'Режим тейка/стопа: {config.get('param_trade_historical_trade_svobodniy_freym', 'regim_tp')}/{config.get('param_trade_historical_trade_svobodniy_freym', 'regim_sl')}',size=12),
                    ft.Text(f'Тейк профит: {config.get('param_trade_historical_trade_svobodniy_freym', 'tp')}',size=12),
                    ft.Text(f'Стоп лосс: {config.get('param_trade_historical_trade_svobodniy_freym', 'sl')}',size=12),
                    ft.Text(f'Режим объёмов: {config.get('param_trade_historical_trade_svobodniy_freym', 'regim_volume_min')}/{config.get('param_trade_historical_trade_svobodniy_freym', 'regim_volume_max')}',size=12),
                    ft.Text(f'Объём торгов мин: {config.get('param_trade_historical_trade_svobodniy_freym', 'volume_min')}',size=12),
                    ft.Text(f'Объём торгов макс: {config.get('param_trade_historical_trade_svobodniy_freym', 'volume_max')}',size=12),
                    ft.Text(f'Плечо: {config.get('param_trade_historical_trade_svobodniy_freym', 'leverage')}',size=12),
                ],scroll=ft.ScrollMode.ALWAYS,),
                width=230,height=140),
        ]),padding=10
    )

# возвращает настройки стратегий для отрисовки в блоке
def print_set_settings():

    config = configparser.ConfigParser()  
    config.read(path_imports_config)

    # ----------------------------------------
    name_strat = {
        'one':'Канал, тренд, локаль, объём',
        'MA':'Скользящие средние'
    }
    strat_set_print = {
        'one': ft.Container(ft.Column(controls=[
            ft.Text(f'Верх канала - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_up_chanal')}',size=12),
            ft.Text(f'Низ канала - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_down_chanal')}',size=12),
            ft.Text(f'Угол тренда лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_corner_long')}',size=12),
            ft.Text(f'Угол тренда шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_corner_short')}',size=12),
            ])),
        'MA': ft.Container(ft.Column(controls=[
            ft.Text(f'Коэф. быстрой скольз. средней - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_koef_bistro')}',size=12),
            ft.Text(f'Коэф. медленной скольз. средней - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_koef_medleno')}',size=12),
            ft.Text(f'Кол-во совпадений в прошлом - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_sovpad_last')}',size=12),
            ft.Text(f'Прижатие к верху коридора - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_up_chanal')}',size=12),
            ft.Text(f'Прижатие к низу коридора - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_down_chanal')}',size=12),
            ])),
    }

    mas_strat_siroy = literal_eval(config.get('param_trade_historical_trade_svobodniy_freym', 'strategys'))
    strat_elements = []
    count_strat = 0
    for strat in mas_strat_siroy:
        strat_elements.append(ft.Container(ft.Column(controls=[
            ft.Text(f'Стратегия: {name_strat[strat]}'),
            strat_set_print[strat]
        ])))
        count_strat+=1
        if len(mas_strat_siroy) != count_strat:
            strat_elements.append(ft.Container(width=350,height=1,bgcolor=c_white))

    return ft.Container(
        ft.Container(
            ft.Column(controls=strat_elements,scroll=ft.ScrollMode.ALWAYS,),
            width=350,height=140),padding=10
    )

# ВОЗВРАЩАЕТ НАСТРОЙКИ ДЛЯ ОТРИСОВКИ ОБЩИХ НАСТРОЕК СЕТА НАСТРОЕК
def print_mach_our_settings():
    config = configparser.ConfigParser()  
    config.read(path_imports_config)
    config_set = configparser.ConfigParser()  
    config_set.read(path_ini_general_set)

    return  ft.Container(
        ft.Row(controls=[
            ft.Container(
                ft.Column(controls=[
                    ft.Text(f'Имя робота для логов: {config.get('param_trade_historical_trade_svobodniy_freym', 'name_bot')}',size=12),
                    ft.Text(f'Режим монеты: {config.get('param_trade_historical_trade_svobodniy_freym', 'strategi_coin')}',size=12),
                ],scroll=ft.ScrollMode.ALWAYS,),
                width=230,height=140),
            ft.Container(width=1,height=140,bgcolor=c_white),
            ft.Container(
                ft.Column(controls=[
                    ft.Text(f'Комиссия мейкер: {config.get('param_trade_historical_trade_svobodniy_freym', 'komission_mayker')}',size=12),
                    ft.Text(f'Комиссия тейкер: {config.get('param_trade_historical_trade_svobodniy_freym', 'komission_taker')}',size=12),
                ],scroll=ft.ScrollMode.ALWAYS,),
                width=150,height=140),
            ft.Container(width=1,height=140,bgcolor=c_white),
            ft.Container(
                ft.Column(controls=[
                    ft.Text(f'Сколько монет торговать: {config.get('param_trade_historical_trade_svobodniy_freym', 'how_mach_money')}',size=12),
                    ft.Text(f'Таймфрейм: {config.get('param_trade_historical_trade_svobodniy_freym', 'work_tf')}',size=12),
                ],scroll=ft.ScrollMode.ALWAYS,),
                width=200,height=140),
            ft.Container(width=1,height=140,bgcolor=c_white),
            ft.Container(
                ft.Column(controls=[
                    ft.Text(f'Длительность торговли: {config.get('param_trade_historical_trade_svobodniy_freym', 'dlitelnost')}',size=12),
                    ft.Text(f'Кол-во настроек в сете: {len(config_set.sections())}',size=12),
                ],scroll=ft.ScrollMode.ALWAYS,),
                width=200,height=140),
        ]),padding=10
    )





# import flet as ft
# from variable import *
# from imports import *

# config = configparser.ConfigParser()  
# config.read(path_imports_config)

# # ----------------------------------------
# name_strat = {
#     'one':'Канал, тренд, локаль, объём',
#     'MA':'Скользящие средние'
# }
# strat_set_print = {
#     'one': ft.Container(ft.Column(controls=[
#         ft.Text(f'Верх канала - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_up_chanal')}',size=12),
#         ft.Text(f'Низ канала - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_down_chanal')}',size=12),
#         ft.Text(f'Угол тренда лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_corner_long')}',size=12),
#         ft.Text(f'Угол тренда шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_one_corner_short')}',size=12),
#         ])),
#     'MA': ft.Container(ft.Column(controls=[
#         ft.Text(f'Коэф. быстрой скольз. средней - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_koef_bistro')}',size=12),
#         ft.Text(f'Коэф. медленной скольз. средней - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_koef_medleno')}',size=12),
#         ft.Text(f'Кол-во совпадений в прошлом - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_sovpad_last')}',size=12),
#         ft.Text(f'Прижатие к верху коридора - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_up_chanal')}',size=12),
#         ft.Text(f'Прижатие к низу коридора - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_ma_down_chanal')}',size=12),
#         ])),
# }

# mas_strat_siroy = literal_eval(config.get('param_trade_historical_trade_svobodniy_freym', 'strategys'))
# strat_elements = []
# count_strat = 0
# for strat in mas_strat_siroy:
#     strat_elements.append(ft.Container(ft.Column(controls=[
#         ft.Text(f'Стратегия: {name_strat[strat]}'),
#         strat_set_print[strat]
#     ])))
#     count_strat+=1
#     if len(mas_strat_siroy) != count_strat:
#         strat_elements.append(ft.Container(width=350,height=1,bgcolor=c_white))
    
# # ----------------------------------------



# print_our_settings = ft.Container(
#     ft.Row(controls=[
#         ft.Container(
#             ft.Column(controls=[
#                 ft.Text(f'Имя робота для логов: {config.get('param_trade_historical_trade_svobodniy_freym', 'name_bot')}',size=12),
#                 ft.Text(f'Режим монеты: {config.get('param_trade_historical_trade_svobodniy_freym', 'strategi_coin')}',size=12),
#                 ft.Text(f'Сколько монет торговать: {config.get('param_trade_historical_trade_svobodniy_freym', 'how_mach_money')}',size=12),
#                 ft.Text(f'Комиссия мейкер: {config.get('param_trade_historical_trade_svobodniy_freym', 'komission_mayker')}',size=12),
#                 ft.Text(f'Комиссия тейкер: {config.get('param_trade_historical_trade_svobodniy_freym', 'komission_taker')}',size=12),
#                 ft.Text(f'Таймфрейм: {config.get('param_trade_historical_trade_svobodniy_freym', 'work_tf')}',size=12),
#                 ft.Text(f'Длительность торговли: {config.get('param_trade_historical_trade_svobodniy_freym', 'dlitelnost')}',size=12),
#             ],scroll=ft.ScrollMode.ALWAYS,),
#             width=230,height=140),
#         ft.Container(width=1,height=140,bgcolor=c_white),
#         ft.Container(
#             ft.Column(controls=[
#                 ft.Text(f'Режим тейка/стопа: {config.get('param_trade_historical_trade_svobodniy_freym', 'regim_tp')}/{config.get('param_trade_historical_trade_svobodniy_freym', 'regim_sl')}',size=12),
#                 ft.Text(f'Тейк профит: {config.get('param_trade_historical_trade_svobodniy_freym', 'tp')}',size=12),
#                 ft.Text(f'Стоп лосс: {config.get('param_trade_historical_trade_svobodniy_freym', 'sl')}',size=12),
#                 ft.Text(f'Режим объёмов: {config.get('param_trade_historical_trade_svobodniy_freym', 'regim_volume_min')}/{config.get('param_trade_historical_trade_svobodniy_freym', 'regim_volume_max')}',size=12),
#                 ft.Text(f'Объём торгов мин: {config.get('param_trade_historical_trade_svobodniy_freym', 'volume_min')}',size=12),
#                 ft.Text(f'Объём торгов макс: {config.get('param_trade_historical_trade_svobodniy_freym', 'volume_max')}',size=12),
#                 ft.Text(f'Плечо: {config.get('param_trade_historical_trade_svobodniy_freym', 'leverage')}',size=12),
#             ],scroll=ft.ScrollMode.ALWAYS,),
#             width=230,height=140),
#     ]),padding=10
# )

# print_set_settings = ft.Container(
#     ft.Container(
#         ft.Column(controls=strat_elements,scroll=ft.ScrollMode.ALWAYS,),
#         width=350,height=140),padding=10
# )









