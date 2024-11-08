import flet as ft
from variable import *
from imports import *


# основные настройки лежат здесь11

# вытаскиваем название стратегии
# # настройки стратегий лежат здесь
def def_print_set_settings(number_folder,number_trade_folder,strategy_now):

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
        'CDLENGULFING':'шаблон поглощения',
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
        'CDLMATCHINGLOW':'низкий уровень соответствия',
        'CDLMORNINGSTAR':'Утренняя звезда',
        'CDLRICKSHAWMAN':'рикша',
        'CDLSPINNINGTOP':'Волчок',
        'CDLTASUKIGAP':'разрыв Тасуки',
    }
    strat_mas = []
    # вытаскиваем название стратегии
    # folder_strat = os.listdir(f'{path_save_trade}\\{number_folder}')
    # for file in folder_strat:
    #     if file!='log_trade.txt' and file!='settings_our.txt' and file!='folder_trade' and file!='general_set.ini' and file!='folder_trade':
    #         strat_mas.append(file.rstrip('.txt'))
    strat_mas = strategy_now
    if len(strat_mas) == 1: 
        folder_strat = f'{path_save_trade}\\{number_folder}\\{strat_mas[0]}_set.ini'
        config_set = configparser.ConfigParser()  
        config_set.read(folder_strat)
        if strat_mas[0] == 'one':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Верх канала - {config_set.get(f'{str(number_trade_folder)}_section', 'up_chanal')}',size=12),
                ft.Text(f'Низ канала - {config_set.get(f'{str(number_trade_folder)}_section', 'down_chanal')}',size=12),
                ft.Text(f'Угол тренда лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'corner_long')}',size=12),
                ft.Text(f'Угол тренда шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'corner_short')}',size=12),
            ]))
        elif strat_mas[0] == 'MA':
            # print(f'{str(number_trade_folder)}_section')
            # print(config_set.get(f'{str(number_trade_folder)}_section', 'koef_bistro'))
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Коэф. быстрой скольз. средней - {config_set.get(f'{str(number_trade_folder)}_section', 'koef_bistro')}',size=12),
                ft.Text(f'Коэф. медленной скольз. средней - {config_set.get(f'{str(number_trade_folder)}_section', 'koef_medleno')}',size=12),
                ft.Text(f'Кол-во совпадений в прошлом - {config_set.get(f'{str(number_trade_folder)}_section', 'sovpad_last')}',size=12),
                ft.Text(f'Прижатие к верху коридора - {config_set.get(f'{str(number_trade_folder)}_section', 'up_chanal')}',size=12),
                ft.Text(f'Прижатие к низу коридора - {config_set.get(f'{str(number_trade_folder)}_section', 'down_chanal')}',size=12),
            ]))
            
        elif strat_mas[0] == 'BBANDS':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Отклонение для установки верхней полосы - {config_set.get(f'{str(number_trade_folder)}_section', 'timeperiod')}',size=12),
                ft.Text(f'Временной промежуток - {config_set.get(f'{str(number_trade_folder)}_section', 'nbdevup')}',size=12),
                ft.Text(f'Отклонение для установки нижней полосы - {config_set.get(f'{str(number_trade_folder)}_section', 'nbdevdn')}',size=12),
                ft.Text(f'Тип движущейся средней - {config_set.get(f'{str(number_trade_folder)}_section', 'matype')}',size=12),
            ]))
        elif strat_mas[0] == 'EMA':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Временной промежуток - {config_set.get(f'{str(number_trade_folder)}_section', 'timeperiod')}',size=12),
            ]))
        elif strat_mas[0] == 'DEMA':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Временной промежуток - {config_set.get(f'{str(number_trade_folder)}_section', 'timeperiod')}',size=12),
            ]))
        elif strat_mas[0] == 'KAMA':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Временной промежуток - {config_set.get(f'{str(number_trade_folder)}_section', 'timeperiod')}',size=12),
            ]))
        elif strat_mas[0] == 'MAVP':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Минимальный период - {config_set.get(f'{str(number_trade_folder)}_section', 'minperiod')}',size=12),
                ft.Text(f'Максимальный период - {config_set.get(f'{str(number_trade_folder)}_section', 'maxperiod')}',size=12),
                ft.Text(f'Тип скользящей средней - {config_set.get(f'{str(number_trade_folder)}_section', 'matype')}',size=12),
            ]))
        elif strat_mas[0] == 'SAR':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Ускорение - {config_set.get(f'{str(number_trade_folder)}_section', 'acceleration')}',size=12),
                ft.Text(f'Максимум - {config_set.get(f'{str(number_trade_folder)}_section', 'maximum')}',size=12),
            ]))
        elif strat_mas[0] == 'TEMA':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Временной промежуток - {config_set.get(f'{str(number_trade_folder)}_section', 'timeperiod')}',size=12),
            ]))
        elif strat_mas[0] == 'TRIMA':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Временной промежуток - {config_set.get(f'{str(number_trade_folder)}_section', 'timeperiod')}',size=12),
            ]))
        elif strat_mas[0] == 'WMA':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Временной промежуток - {config_set.get(f'{str(number_trade_folder)}_section', 'timeperiod')}',size=12),
            ]))
        elif strat_mas[0] == 'CDL2CROWS':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDL3BLACKCROWS':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDL3INSIDE':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDL3LINESTRIKE':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDL3OUTSIDE':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDL3STARSINSOUTH':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDL3WHITESOLDIERS':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDLABANDONEDBABY':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент проникновения одной свечи внутри другой свечи - {config_set.get(f'{str(number_trade_folder)}_section', 'penetration')}',size=12),
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDLADVANCEBLOCK':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDLBELTHOLD':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDLCLOSINGMARUBOZU':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDLCOUNTERATTACK':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDLDARKCLOUDCOVER':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент проникновения одной свечи внутри другой свечи - {config_set.get(f'{str(number_trade_folder)}_section', 'penetration')}',size=12),
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDLENGULFING':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDLEVENINGDOJISTAR':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент проникновения одной свечи внутри другой свечи - {config_set.get(f'{str(number_trade_folder)}_section', 'penetration')}',size=12),
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDLGRAVESTONEDOJI':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDLHAMMER':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDLHANGINGMAN':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDLHARAMI':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDLHARAMICROSS':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDLHOMINGPIGEON':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDLINVERTEDHAMMER':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDLLADDERBOTTOM':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDLLONGLEGGEDDOJI':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDLMATCHINGLOW':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDLMORNINGSTAR':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент проникновения одной свечи внутри другой свечи - {config_set.get(f'{str(number_trade_folder)}_section', 'penetration')}',size=12),
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDLRICKSHAWMAN':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDLSPINNINGTOP':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
        elif strat_mas[0] == 'CDLTASUKIGAP':
            strat_set_print = ft.Container(ft.Column(controls=[
                ft.Text(f'Процент сигнала в лонг - {config_set.get(f'{str(number_trade_folder)}_section', 'long')}',size=12),
                ft.Text(f'Процент сигнала в шорт - {config_set.get(f'{str(number_trade_folder)}_section', 'short')}',size=12),
            ]))
            
        else:
            strat_set_print = ft.Container(ft.Text('Потом доработать отрисовку множественной стратегии istoriya_treyd_page/UI/trade_page/data_settings'))

    path_settings = f'{path_save_trade}\\{number_folder}\\settings_our.txt'
    if os.path.isfile(path_settings):
        with open(path_settings) as file:
            array_data_row = [row.strip() for row in file]
            strategys_data = literal_eval(array_data_row[0].split('&')[22]) # ['MA']
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
    path_settings = f'{path_save_trade}\\{number_folder}\\settings_our.txt'
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






