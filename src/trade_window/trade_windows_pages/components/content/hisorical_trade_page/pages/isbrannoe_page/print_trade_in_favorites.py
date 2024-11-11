
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.isbrannoe_page.UI.table_trade import Table_trade

class Print_trade_in_favorites(ft.UserControl):
    def __init__(self,change_page,number_favorites,name_favorite):
        super().__init__()
        self.change_page = change_page
        self.number_favorite = number_favorites
        self.name_favorite = name_favorite
        self.name_strat = {
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
            if strat_mas[0] == 'one':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Верх канала - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Низ канала - {array_data_row[0].split('&')[1]}',size=12),
                    ft.Text(f'Угол тренда лонг - {array_data_row[0].split('&')[2]}',size=12),
                    ft.Text(f'Угол тренда шорт - {array_data_row[0].split('&')[3]}',size=12),
                ]))
            elif strat_mas[0] == 'MA':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Коэф. быстрой скольз. средней - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Коэф. медленной скольз. средней - {array_data_row[0].split('&')[1]}',size=12),
                    ft.Text(f'Кол-во совпадений в прошлом - {array_data_row[0].split('&')[2]}',size=12),
                    ft.Text(f'Прижатие к верху коридора - {array_data_row[0].split('&')[3]}',size=12),
                    ft.Text(f'Прижатие к низу коридора - {array_data_row[0].split('&')[4]}',size=12),
                ]))
            elif strat_mas[0] == 'BBANDS':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Отклонение для установки верхней полосы - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Временной промежуток - {array_data_row[0].split('&')[1]}',size=12),
                    ft.Text(f'Отклонение для установки нижней полосы - {array_data_row[0].split('&')[2]}',size=12),
                    ft.Text(f'Тип движущейся средней - {array_data_row[0].split('&')[3]}',size=12),
                ]))
            elif strat_mas[0] == 'EMA':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Временной промежуток - {array_data_row[0].split('&')[0]}',size=12),
                ]))
            elif strat_mas[0] == 'DEMA':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Временной промежуток - {array_data_row[0].split('&')[0]}',size=12),
                ]))
            elif strat_mas[0] == 'KAMA':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Временной промежуток - {array_data_row[0].split('&')[0]}',size=12),
                ]))
            elif strat_mas[0] == 'MAVP':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Минимальный период - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Максимальный период - {array_data_row[0].split('&')[1]}',size=12),
                    ft.Text(f'Тип скользящей средней - {array_data_row[0].split('&')[2]}',size=12),
                ]))
            elif strat_mas[0] == 'SAR':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Ускорение - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Максимум - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'TEMA':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Временной промежуток - {array_data_row[0].split('&')[0]}',size=12),
                ]))
            elif strat_mas[0] == 'TRIMA':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Временной промежуток - {array_data_row[0].split('&')[0]}',size=12),
                ]))
            elif strat_mas[0] == 'WMA':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Временной промежуток - {array_data_row[0].split('&')[0]}',size=12),
                ]))
            elif strat_mas[0] == 'CDL2CROWS':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Временной промежуток - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Временной промежуток - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDL3BLACKCROWS':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Временной промежуток - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Временной промежуток - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDL3INSIDE':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Временной промежуток - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Временной промежуток - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDL3LINESTRIKE':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Временной промежуток - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Временной промежуток - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDL3OUTSIDE':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Временной промежуток - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Временной промежуток - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDL3STARSINSOUTH':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Временной промежуток - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Временной промежуток - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDL3WHITESOLDIERS':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Временной промежуток - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Временной промежуток - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDLABANDONEDBABY':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Процент проникновения одной свечи внутри другой свечи - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Процент сигнала в лонг - {array_data_row[0].split('&')[1]}',size=12),
                    ft.Text(f'Процент сигнала в шорт - {array_data_row[0].split('&')[2]}',size=12),
                ]))
            elif strat_mas[0] == 'CDLADVANCEBLOCK':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Процент сигнала в лонг - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Процент сигнала в шорт - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDLBELTHOLD':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Процент сигнала в лонг - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Процент сигнала в шорт - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDLCLOSINGMARUBOZU':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Процент сигнала в лонг - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Процент сигнала в шорт - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDLCOUNTERATTACK':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Процент сигнала в лонг - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Процент сигнала в шорт - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDLDARKCLOUDCOVER':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Процент проникновения одной свечи внутри другой свечи - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Процент сигнала в лонг - {array_data_row[0].split('&')[1]}',size=12),
                    ft.Text(f'Процент сигнала в шорт - {array_data_row[0].split('&')[2]}',size=12),
                ]))
            elif strat_mas[0] == 'CDLENGULFING':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Процент сигнала в лонг - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Процент сигнала в шорт - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDLEVENINGDOJISTAR':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Процент проникновения одной свечи внутри другой свечи - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Процент сигнала в лонг - {array_data_row[0].split('&')[1]}',size=12),
                    ft.Text(f'Процент сигнала в шорт - {array_data_row[0].split('&')[2]}',size=12),
                ]))
            elif strat_mas[0] == 'CDLGRAVESTONEDOJI':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Процент сигнала в лонг - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Процент сигнала в шорт - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDLHAMMER':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Процент сигнала в лонг - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Процент сигнала в шорт - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDLHANGINGMAN':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Процент сигнала в лонг - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Процент сигнала в шорт - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDLHARAMI':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Процент сигнала в лонг - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Процент сигнала в шорт - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDLHARAMICROSS':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Процент сигнала в лонг - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Процент сигнала в шорт - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDLHOMINGPIGEON':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Процент сигнала в лонг - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Процент сигнала в шорт - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDLINVERTEDHAMMER':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Процент сигнала в лонг - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Процент сигнала в шорт - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDLLADDERBOTTOM':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Процент сигнала в лонг - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Процент сигнала в шорт - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDLLONGLEGGEDDOJI':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Процент сигнала в лонг - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Процент сигнала в шорт - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDLMATCHINGLOW':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Процент сигнала в лонг - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Процент сигнала в шорт - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDLMORNINGSTAR':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Процент проникновения одной свечи внутри другой свечи - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Процент сигнала в лонг - {array_data_row[0].split('&')[1]}',size=12),
                    ft.Text(f'Процент сигнала в шорт - {array_data_row[0].split('&')[2]}',size=12),
                ]))
            elif strat_mas[0] == 'CDLRICKSHAWMAN':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Процент сигнала в лонг - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Процент сигнала в шорт - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDLSPINNINGTOP':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Процент сигнала в лонг - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Процент сигнала в шорт - {array_data_row[0].split('&')[1]}',size=12),
                ]))
            elif strat_mas[0] == 'CDLTASUKIGAP':
                strat_set_print = ft.Container(ft.Column(controls=[
                    ft.Text(f'Процент сигнала в лонг - {array_data_row[0].split('&')[0]}',size=12),
                    ft.Text(f'Процент сигнала в шорт - {array_data_row[0].split('&')[1]}',size=12),
                ]))


            else:
                strat_set_print = ft.Container(ft.Text('Потом доработать отрисовку множественной стратегии istoriya_treyd_page/UI/trade_page/data_settings'))

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


    # отрисовка блока со статистикой
    def print_stata(self):
        return ft.Container(ft.Row(controls=[
            ft.Container(ft.Column(controls=[
                ft.Container(ft.Row(controls=(
                    ft.Container(ft.Text('Дней торговли (Проведено трейдов по стратегии)'),padding=ft.padding.only(left=12,top=12),width=350,height=50,margin=ft.margin.only(top=-1,left=-1)),
                    ft.Container(width=1,height=100,bgcolor=c_white),
                    ft.Container(ft.Text('15',text_align='center'),width=90,padding=ft.padding.only(top=12),height=50,margin=ft.margin.only(top=-1,left=-10)),
                )),width=450,border=ft.border.all(1,c_white),height=50,margin=ft.margin.only(top=-1,left=-1)),
                ft.Container(ft.Row(controls=(
                    ft.Container(ft.Text('Сделок за все трейды'),padding=12,width=350,height=50,margin=ft.margin.only(top=-1,left=-1)),
                    ft.Container(width=1,height=100,bgcolor=c_white),
                    ft.Container(ft.Text('85',text_align='center'),width=90,padding=ft.padding.only(top=12),height=50,margin=ft.margin.only(top=-1,left=-10)),
                )),width=450,border=ft.border.all(1,c_white),height=50,margin=ft.margin.only(top=-11,left=-1)),
                ft.Container(ft.Row(controls=(
                    ft.Container(ft.Text('Сделок, совершенных в плюс, в шт и $'),padding=12,width=350,height=50,margin=ft.margin.only(top=-1,left=-1)),
                    ft.Container(width=1,height=100,bgcolor=c_white),
                    ft.Container(ft.Text('54 | 472$',text_align='center'),width=90,padding=ft.padding.only(top=12),height=50,margin=ft.margin.only(top=-1,left=-10)),
                )),width=450,border=ft.border.all(1,c_white),height=50,margin=ft.margin.only(top=-11,left=-1)),
                ft.Container(ft.Row(controls=(
                    ft.Container(ft.Text('Сделок, совершенных в минус, в шт и $'),padding=12,width=350,height=50,margin=ft.margin.only(top=-1,left=-1)),
                    ft.Container(width=1,height=100,bgcolor=c_white),
                    ft.Container(ft.Text('31 | 181$',text_align='center'),width=90,padding=ft.padding.only(top=12),height=50,margin=ft.margin.only(top=-1,left=-10)),
                )),width=450,border=ft.border.all(1,c_white),height=50,margin=ft.margin.only(top=-11,left=-1)),
            ])),
            ft.Container(ft.Column(controls=[
                ft.Container(ft.Row(controls=(
                    ft.Container(ft.Text('Средний результат в день'),padding=ft.padding.only(left=12,top=12),width=300,height=50,margin=ft.margin.only(top=-1,left=-1)),
                    ft.Container(width=1,height=100,bgcolor=c_white),
                    ft.Container(ft.Text('+3.28%',text_align='center'),width=90,padding=ft.padding.only(top=12),height=50,margin=ft.margin.only(top=-1,left=-10)),
                )),width=412,border=ft.border.all(1,c_white),height=50,margin=ft.margin.only(top=-1,left=-1)),
                ft.Container(ft.Row(controls=(
                    ft.Container(ft.Text('Монет в трейдах'),padding=12,width=300,height=50,margin=ft.margin.only(top=-1,left=-1)),
                    ft.Container(width=1,height=100,bgcolor=c_white),
                    ft.Container(ft.Text('32',text_align='center'),width=90,padding=ft.padding.only(top=12),height=50,margin=ft.margin.only(top=-1,left=-10)),
                )),width=412,border=ft.border.all(1,c_white),height=50,margin=ft.margin.only(top=-11,left=-1)),
                ft.Container(ft.Row(controls=(
                    ft.Container(ft.Text('Профит за день максимум'),padding=12,width=300,height=50,margin=ft.margin.only(top=-1,left=-1)),
                    ft.Container(width=1,height=100,bgcolor=c_white),
                    ft.Container(ft.Text('+12.37%',text_align='center'),width=90,padding=ft.padding.only(top=12),height=50,margin=ft.margin.only(top=-1,left=-10)),
                )),width=412,border=ft.border.all(1,c_white),height=50,margin=ft.margin.only(top=-11,left=-1)),
                ft.Container(ft.Row(controls=(
                    ft.Container(ft.Text('Убыток за день максимум'),padding=12,width=300,height=50,margin=ft.margin.only(top=-1,left=-1)),
                    ft.Container(width=1,height=100,bgcolor=c_white),
                    ft.Container(ft.Text('-3.46%',text_align='center'),width=90,padding=ft.padding.only(top=12),height=50,margin=ft.margin.only(top=-1,left=-10)),
                )),width=412,border=ft.border.all(1,c_white),height=50,margin=ft.margin.only(top=-11,left=-1)),
            ]),margin=ft.margin.only(left=-10)),
        ]))


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def build(self):
        print_our_settings_ret_fun = self.def_print_our_settings(self.number_favorite)
        def_print_set_settings_ret_fun = self.def_print_set_settings(self.number_favorite)
       
                        
        
        self.ferst_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text(f'Статистика и трейды избранной стратегии - {self.name_favorite}',size=12,color=c_white,text_align='center'),
                                             width=850,margin=ft.margin.only(bottom=15)),
                                ft.Container(
                                    ft.Column(controls=[
                                        # верх
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
                                        # серидина
                                        ft.Container(ft.Container(
                                                ft.Column(controls=[
                                                    ft.Column(
                                                        controls=[
                                                            ft.Container(ft.Container(ft.Text('Статистика',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                            ft.Container(
                                                                ft.Container(
                                                                    self.print_stata(),
                                                                    width=900,
                                                                    height=200,
                                                                    border = ft.border.all(1, c_white),
                                                                    bgcolor=c_blue,
                                                                ),
                                                                width=900,
                                                                height = 195,
                                                                padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                            )]),])),width=860,margin=ft.margin.only(left=20)),
                                        Table_trade(self.change_page,self.number_favorite),
                                        ft.Container(
                                            ft.Container(
                                                ft.Row(controls=[
                                                ft.Container(ft.ElevatedButton(content = ft.Text('Назад',size=12,),data='Избранные стратегии',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                            ]),padding=ft.padding.only(left=400,top=5)
                                            ),
                                            width=500
                                        ),
                                    ],height=600,scroll=ft.ScrollMode.ALWAYS),width=900
                                ),
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.ferst_page