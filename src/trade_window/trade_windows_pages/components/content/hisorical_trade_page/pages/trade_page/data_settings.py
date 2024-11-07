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
    
# ----------------------------------------11

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

    # ----------------------------------------1
    name_strat = {
        'one':'Канал, тренд, локаль, объём',
        'MA':'Скользящие средние',
        'BBANDS':'Полосы Боллинджера',
        'EMA':'Эксп скользящая средняя',
        'DEMA':'Двойная эксп скользящая средняя',
        'KAMA':'Адаптивная скользящая Кауфмана',
        'MAVP':'Сколь средняя с пер периодом',
        'SAR':'Параболический SAR',
        'TEMA':'Тройная эксп сколь средняя',
        'TRIMA':'Треугольная скользящая средняя',
        'WMA':'Взвешенная скользящая средняя',
        'CDL2CROWS':'Две вороны',
        'CDL3BLACKCROWS':'Три черных ворона',
        'CDL3INSIDE':'Три внутри Вверх / вниз',
        'CDL3LINESTRIKE':'Трехстрочный удар',
        'CDL3OUTSIDE':'Три внешних элемента Вверх / вниз',
        'CDL3STARSINSOUTH':'Три звезды на юге',
        'CDL3WHITESOLDIERS':'Трое наступающих белых солдат',
        'CDLABANDONEDBABY':'Брошенный ребенок',
        'CDLADVANCEBLOCK':'Предварительный блок',
        'CDLBELTHOLD':'Удержание за ремень',
        'CDLCLOSINGMARUBOZU':'Marubozu',
        'CDLCOUNTERATTACK':'Контратака',
        'CDLDARKCLOUDCOVER':'Темный облачный покров',
        'CDLENGULFING':'Шаблон поглощения',
        'CDLEVENINGDOJISTAR':'Вечерняя звезда Доджи',
        'CDLGRAVESTONEDOJI':'Надгробный камень Доджи',
        'CDLHAMMER':'Молоток',
        'CDLHANGINGMAN':'Висельник',
        'CDLHARAMI':'шаблон Харами',
        'CDLHARAMICROSS':'Шаблон пересечения Харами',
        'CDLHOMINGPIGEON':'Почтовый голубь',
        'CDLINVERTEDHAMMER':'Перевернутый молоток',
        'CDLLADDERBOTTOM':'Основание лестницы',
        'CDLLONGLEGGEDDOJI':'Длинноногий доджи',
        'CDLMATCHINGLOW':'Низкий уровень соответствия',
        'CDLMORNINGSTAR':'Утренняя звезда',
        'CDLRICKSHAWMAN':'Рикша',
        'CDLSPINNINGTOP':'Волчок',
        'CDLTASUKIGAP':'Разрыв Тасуки',
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
        'BBANDS':ft.Container(ft.Column(controls=[
            ft.Text(f'Отклонение для установки верхней полосы - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_BBANDS_timeperiod')}',size=12),
            ft.Text(f'Временной промежуток - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_BBANDS_nbdevup')}',size=12),
            ft.Text(f'Отклонение для установки нижней полосы - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_BBANDS_nbdevdn')}',size=12),
            ft.Text(f'Тип движущейся средней - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_BBANDS_matype')}',size=12),
            ])),
        'EMA':ft.Container(ft.Column(controls=[
            ft.Text(f'Временной промежуток - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_EMA_timeperiod')}',size=12),
            ])),
        'DEMA':ft.Container(ft.Column(controls=[
            ft.Text(f'Временной промежуток - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_DEMA_timeperiod')}',size=12),
            ])),
        'KAMA':ft.Container(ft.Column(controls=[
            ft.Text(f'Временной промежуток - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_KAMA_timeperiod')}',size=12),
            ])),
        'MAVP':ft.Container(ft.Column(controls=[
            ft.Text(f'Минимальный период - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_MAVP_minperiod')}',size=12),
            ft.Text(f'Максимальный период - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_MAVP_maxperiod')}',size=12),
            ft.Text(f'Тип скользящей средней - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_MAVP_matype')}',size=12),
            ])),
        'SAR':ft.Container(ft.Column(controls=[
            ft.Text(f'Ускорение - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_SAR_acceleration')}',size=12),
            ft.Text(f'Максимум - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_MSAR_maximum')}',size=12),
            ])),
        'TEMA':ft.Container(ft.Column(controls=[
            ft.Text(f'Временной промежуток - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_TEMA_timeperiod')}',size=12),
            ])),
        'TRIMA':ft.Container(ft.Column(controls=[
            ft.Text(f'Временной промежуток - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_TRIMA_timeperiod')}',size=12),
            ])),
        'WMA':ft.Container(ft.Column(controls=[
            ft.Text(f'Временной промежуток - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_WMA_timeperiod')}',size=12),
            ])),
        'CDL2CROWS':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL2CROWS_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL2CROWS_short')}',size=12),
            ])),
        'CDL3BLACKCROWS':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3BLACKCROWS_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3BLACKCROWS_short')}',size=12),
            ])),
        'CDL3INSIDE':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3INSIDE_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3INSIDE_short')}',size=12),
            ])),
        'CDL3LINESTRIKE':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3LINESTRIKE_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3LINESTRIKE_short')}',size=12),
            ])),
        'CDL3OUTSIDE':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3OUTSIDE_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3OUTSIDE_short')}',size=12),
            ])),
        'CDL3STARSINSOUTH':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3STARSINSOUTH_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3STARSINSOUTH_short')}',size=12),
            ])),
        'CDL3WHITESOLDIERS':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3WHITESOLDIERS_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDL3WHITESOLDIERS_short')}',size=12),
            ])),
        'CDLABANDONEDBABY':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент проникновения одной свечи внутри другой свечи - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLABANDONEDBABY_penetration')}',size=12),
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLABANDONEDBABY_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLABANDONEDBABY_short')}',size=12),
            ])),
        'CDLADVANCEBLOCK':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLADVANCEBLOCK_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLADVANCEBLOCK_short')}',size=12),
            ])),
        'CDLBELTHOLD':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLBELTHOLD_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLBELTHOLD_short')}',size=12),
            ])),
        'CDLCLOSINGMARUBOZU':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLCLOSINGMARUBOZU_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLCLOSINGMARUBOZU_short')}',size=12),
            ])),
        'CDLCOUNTERATTACK':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLCOUNTERATTACK_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLCOUNTERATTACK_short')}',size=12),
            ])),
        'CDLDARKCLOUDCOVER':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент проникновения одной свечи внутри другой свечи - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLDARKCLOUDCOVER_penetration')}',size=12),
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLDARKCLOUDCOVER_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLDARKCLOUDCOVER_short')}',size=12),
            ])),
        'CDLENGULFING':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLENGULFING_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLENGULFING_short')}',size=12),
            ])),
        'CDLEVENINGDOJISTAR':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент проникновения одной свечи внутри другой свечи - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLEVENINGDOJISTAR_penetration')}',size=12),
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLEVENINGDOJISTAR_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLEVENINGDOJISTAR_short')}',size=12),
            ])),
        'CDLGRAVESTONEDOJI':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLGRAVESTONEDOJI_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLGRAVESTONEDOJI_short')}',size=12),
            ])),
        'CDLHAMMER':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLHAMMER_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLHAMMER_short')}',size=12),
            ])),
        'CDLHANGINGMAN':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLHANGINGMAN_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLHANGINGMAN_short')}',size=12),
            ])),
        'CDLHARAMI':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLHARAMI_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLHARAMI_short')}',size=12),
            ])),
        'CDLHARAMICROSS':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLHARAMICROSS_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLHARAMICROSS_short')}',size=12),
            ])),
        'CDLHOMINGPIGEON':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLHOMINGPIGEON_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLHOMINGPIGEON_short')}',size=12),
            ])),
        'CDLINVERTEDHAMMER':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLINVERTEDHAMMER_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLINVERTEDHAMMER_short')}',size=12),
            ])),
        'CDLLADDERBOTTOM':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLLADDERBOTTOM_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLLADDERBOTTOM_short')}',size=12),
            ])),
        'CDLLONGLEGGEDDOJI':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLLONGLEGGEDDOJI_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLLONGLEGGEDDOJI_short')}',size=12),
            ])),
        'CDLMATCHINGLOW':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLMATCHINGLOW_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLMATCHINGLOW_short')}',size=12),
            ])),
        'CDLMORNINGSTAR':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент проникновения одной свечи внутри другой свечи - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLMORNINGSTAR_penetration')}',size=12),
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLMORNINGSTAR_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLMORNINGSTAR_short')}',size=12),
            ])),
        'CDLRICKSHAWMAN':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLRICKSHAWMAN_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLRICKSHAWMAN_short')}',size=12),
            ])),
        'CDLSPINNINGTOP':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLSPINNINGTOP_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLSPINNINGTOP_short')}',size=12),
            ])),
        'CDLTASUKIGAP':ft.Container(ft.Column(controls=[
            ft.Text(f'Процент сигнала в лонг - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLTASUKIGAP_long')}',size=12),
            ft.Text(f'Процент сигнала в шорт - {config.get('param_trade_historical_trade_svobodniy_freym', 'strat_CDLTASUKIGAP_short')}',size=12),
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









