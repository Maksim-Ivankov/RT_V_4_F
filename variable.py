
# from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config
import configparser

# Работа с директорией
APPNAME = "RoboTrade"
import sys
import os
if sys.platform == 'darwin':
    # from AppKit import NSSearchPathForDirectoriesInDomains
    # # http://developer.apple.com/DOCUMENTATION/Cocoa/Reference/Foundation/Miscellaneous/Foundation_Functions/Reference/reference.html#//apple_ref/c/func/NSSearchPathForDirectoriesInDomains
    # # NSApplicationSupportDirectory = 14
    # # NSUserDomainMask = 1
    # # True for expanding the tilde into a fully qualified path
    # appdata = path.join(NSSearchPathForDirectoriesInDomains(14, 1, True)[0], APPNAME)
    print('СДЕЛАТЬ ПОЗЖЕ ЛОКАЛИЗАЦИЮ ПОД MACOS')
elif sys.platform == 'win32':
    appdata = os.path.join(os.environ['APPDATA'], APPNAME)

# если в системном пути нет папки проекта, то создаем ее
if os.path.isdir(appdata) == False:
    os.makedirs(appdata)
    print('Папка создана')
# путь к файлу конфигурации для авторизации (запомнить меня)
path_imports_config = appdata + '\\config.ini' # основной файл инициализации, всех настроек
path_ini_svoboda_freym = appdata + '\\svoboda_freym.ini' # файл настроек для данных историческая торговля/свободный фрейм
path_ini_historical_freym = appdata + '\\historical_freym.ini' # файл настроек для данных историческая торговля/историческая торговля
path_ini_general_set = appdata + '\\general_set.ini' # файл общего сета настроек
path_ini_one_set = appdata + '\\one_set.ini' # файл сета настроек one
path_ini_MA_set = appdata + '\\MA_set.ini' # файл сета настроек MA
path_ini_BBANDS_set = appdata + '\\BBANDS_set.ini'
path_ini_EMA_set = appdata + '\\EMA_set.ini'
path_ini_DEMA_set = appdata + '\\DEMA_set.ini'
path_ini_KAMA_set = appdata + '\\KAMA_set.ini'
path_ini_MAVP_set = appdata + '\\MAVP_set.ini'
path_ini_SAR_set = appdata + '\\SAR_set.ini'
path_ini_TEMA_set = appdata + '\\TEMA_set.ini'
path_ini_TRIMA_set = appdata + '\\TRIMA_set.ini'
path_ini_WMA_set = appdata + '\\WMA_set.ini'
path_ini_CDL2CROWS_set = appdata + '\\CDL2CROWS_set.ini'
path_ini_CDL3BLACKCROWS_set = appdata + '\\CDL3BLACKCROWS_set.ini'
path_ini_CDL3INSIDE_set = appdata + '\\CDL3INSIDE_set.ini'
path_ini_CDL3LINESTRIKE_set = appdata + '\\CDL3LINESTRIKE_set.ini'
path_ini_CDL3OUTSIDE_set = appdata + '\\CDL3OUTSIDE_set.ini'
path_ini_CDL3STARSINSOUTH_set = appdata + '\\CDL3STARSINSOUTH_set.ini'
path_ini_CDL3WHITESOLDIERS_set = appdata + '\\CDL3WHITESOLDIERS_set.ini'
path_ini_CDLABANDONEDBABY_set = appdata + '\\CDLABANDONEDBABY_set.ini'
path_ini_CDLADVANCEBLOCK_set = appdata + '\\CDLADVANCEBLOCK_set.ini'
path_ini_CDLBELTHOLD_set = appdata + '\\CDLBELTHOLD_set.ini'
path_ini_CDLCLOSINGMARUBOZU_set = appdata + '\\CDLCLOSINGMARUBOZU_set.ini'
path_ini_CDLCOUNTERATTACK_set = appdata + '\\CDLCOUNTERATTACK_set.ini'
path_ini_CDLDARKCLOUDCOVER_set = appdata + '\\CDLDARKCLOUDCOVER_set.ini'
path_ini_CDLENGULFING_set = appdata + '\\CDLENGULFING_set.ini'
path_ini_CDLEVENINGDOJISTAR_set = appdata + '\\CDLEVENINGDOJISTAR_set.ini'
path_ini_CDLGRAVESTONEDOJI_set = appdata + '\\CDLGRAVESTONEDOJI_set.ini'
path_ini_CDLHAMMER_set = appdata + '\\CDLHAMMER_set.ini'
path_ini_CDLHANGINGMAN_set = appdata + '\\CDLHANGINGMAN_set.ini'
path_ini_CDLHARAMI_set = appdata + '\\CDLHARAMI_set.ini'
path_ini_CDLHARAMICROSS_set = appdata + '\\CDLHARAMICROSS_set.ini'
path_ini_CDLHOMINGPIGEON_set = appdata + '\\CDLHOMINGPIGEON_set.ini'
path_ini_CDLINVERTEDHAMMER_set = appdata + '\\CDLINVERTEDHAMMER_set.ini'
path_ini_CDLLADDERBOTTOM_set = appdata + '\\CDLLADDERBOTTOM_set.ini'
path_ini_CDLLONGLEGGEDDOJI_set = appdata + '\\CDLLONGLEGGEDDOJI_set.ini'
path_ini_CDLMATCHINGLOW_set = appdata + '\\CDLMATCHINGLOW_set.ini'
path_ini_CDLMORNINGSTAR_set = appdata + '\\CDLMORNINGSTAR_set.ini'
path_ini_CDLRICKSHAWMAN_set = appdata + '\\CDLRICKSHAWMAN_set.ini'
path_ini_CDLSPINNINGTOP_set = appdata + '\\CDLSPINNINGTOP_set.ini'
path_ini_CDLTASUKIGAP_set = appdata + '\\CDLTASUKIGAP_set.ini'
path_data_map_coin = appdata + '\\map_coin.json' # должен обновляться каждые n минут. С него рисуется тепловая карта и берутся монеты для получения датафреймов
path_data_user_tg_chat = appdata + '\\channel_users_tg.json' 
path_data_message_tg_chat = appdata + '\\channel_messages_tg.json'
path_JSON_coins_info_our = appdata + '\\coins_info_our.json'
path_svoboda_freym = appdata + '\\svoboda_freym' # начало пути для сохранения датафреймов - историческая торговля/свободный фрейм
path_historical_freym = appdata + '\\historical_freym' # начало пути для сохранения датафреймов - историческая торговля/историческая торговля
path_appdata = appdata
#--------------------------------------------------
# проверяем есть ли папка в директории для трейдов
if os.path.isdir(f'{appdata}\\trade'): 
    path_save_trade = appdata+'\\trade' # сюда будем сохранять трейды
else:
    os.mkdir(f'{appdata}\\trade') # если папки нет, создаем её
    path_save_trade = appdata+'\\trade' # сюда будем сохранять трейды
    
# проверяем есть ли папка в директории для избранных стратегий
if os.path.isdir(f'{appdata}\\favorites'): 
    path_favorites = appdata+'\\favorites' # сюда будем сохранять избранное
else:
    os.mkdir(f'{appdata}\\favorites') # если папки нет, создаем её
    path_favorites = appdata+'\\favorites' # сюда будем сохранять избранное
    
# проверяем есть ли папка в директории для сохраненеия датафреймов исторической торговли (дней сетов)
if os.path.isdir(f'{appdata}\\historical_freym'): 
    path_historical_freym = appdata+'\\historical_freym' # сюда будем сохранять избранное
else:
    os.mkdir(f'{appdata}\\historical_freym') # если папки нет, создаем её
    path_historical_freym = appdata+'\\historical_freym' # сюда будем сохранять избранное


#--------------------------------------------------

c_blue = '#222831'
c_white = '#FFFFFF'
c_yelow = '#FBD46D'
c_green = '#0AFF89'
c_red = '#FF0A0A'

c_blue_binance = '#161A1E'
c_green_binance = '#0ECB81'
c_red_binance = '#F6465D'
c_gray_binance = '#363A45'

server_ip = 'http://127.0.0.1:5000'

width_window_platforma = 1186
height_window_platforma = 760

version_desctop = 'v1.25.11'

key_bin = 'QIT80MTFskjHSr82dtsteA6bG01CUeODQCg65KoYaQ5LmPcSpYDzyv1Oa7fugW3m'
secret_bin = 'uMLo0WdaCv5FHBauV8QI4LZoDgmmVFf5Jd8TboKYRxHnHx6pmNrhg5bmdBgO54xI'

api_id_tg = '29054097'
api_hash_id_tg = 'ed0af3e9cb2fb29e47631254716cae92'
username_tg = 'maksimivankov'
data1 = {'sledim_money':'1m'}




strategys_our = {
    'one':'Канал, тренд, локаль, объём',
    'MA':'Скользящие средние',
    'BBANDS':'Полосы Боллинджера',
    'EMA':'Эксп скользящая средняя',                  # ноль показывают
    'DEMA':'Двойная эксп скользящая средняя',                 # ноль показывают
    'KAMA':'Адаптивная скользящая Кауфмана',                  # ноль показывают
    'MAVP':'Сколь средняя с пер периодом',                    # ноль показывают
    'SAR':'Параболический SAR',                   # ноль показывают
    'TEMA':'Тройная эксп сколь средняя',                  # ноль показывают
    'TRIMA':'Треугольная скользящая средняя',                 # ноль показывают
    'WMA':'Взвешенная скользящая средняя',                    # ноль показывают
    'CDL2CROWS':'Две вороны',                 # ноль показывают
    'CDL3BLACKCROWS':'Три черных ворона',                 # ноль показывают
    'CDL3INSIDE':'Три внутри Вверх / вниз',
    'CDL3LINESTRIKE':'Трехстрочный удар',
    'CDL3OUTSIDE':'Три внешних элемента Вверх / вниз',
    'CDL3STARSINSOUTH':'Три звезды на юге',                   # ноль показывают
    'CDL3WHITESOLDIERS':'Трое наступающих белых солдат',                  # ноль показывают
    'CDLABANDONEDBABY':'Брошенный ребенок',                   # ноль показывают
    'CDLADVANCEBLOCK':'Предварительный блок',
    'CDLBELTHOLD':'Удержание за ремень',
    'CDLCLOSINGMARUBOZU':'Marubozu',
    'CDLCOUNTERATTACK':'Контратака',                  # ноль показывают
    'CDLDARKCLOUDCOVER':'Темный облачный покров',                 # ноль показывают
    'CDLENGULFING':'шаблон поглощения',
    'CDLEVENINGDOJISTAR':'Вечерняя звезда Доджи',
    'CDLGRAVESTONEDOJI':'Надгробный камень Доджи',
    'CDLHAMMER':'Молоток',
    'CDLHANGINGMAN':'Висельник',
    'CDLHARAMI':'шаблон Харами',
    'CDLHARAMICROSS':'Шаблон пересечения Харами',
    'CDLHOMINGPIGEON':'Почтовый голубь',                  # ноль показывают
    'CDLINVERTEDHAMMER':'Перевернутый молоток',
    'CDLLADDERBOTTOM':'Основание лестницы',                   # ноль показывают
    'CDLLONGLEGGEDDOJI':'Длинноногий доджи',
    'CDLMATCHINGLOW':'низкий уровень соответствия',
    'CDLMORNINGSTAR':'Утренняя звезда',
    'CDLRICKSHAWMAN':'рикша',
    'CDLSPINNINGTOP':'Волчок',
    'CDLTASUKIGAP':'разрыв Тасуки',                       # ноль показывают
}
mas_name_strategys = ['one','MA','BBANDS','EMA','DEMA','KAMA','MAVP','SAR','TEMA','TRIMA','WMA','CDL2CROWS','CDL3BLACKCROWS','CDL3INSIDE','CDL3LINESTRIKE','CDL3OUTSIDE','CDL3STARSINSOUTH','CDL3WHITESOLDIERS','CDLABANDONEDBABY','CDLADVANCEBLOCK','CDLBELTHOLD','CDLCLOSINGMARUBOZU','CDLCOUNTERATTACK','CDLDARKCLOUDCOVER','CDLENGULFING','CDLEVENINGDOJISTAR','CDLGRAVESTONEDOJI','CDLHAMMER','CDLHANGINGMAN','CDLHARAMI','CDLHARAMICROSS','CDLHOMINGPIGEON','CDLINVERTEDHAMMER','CDLLADDERBOTTOM','CDLLONGLEGGEDDOJI','CDLMATCHINGLOW','CDLMORNINGSTAR','CDLRICKSHAWMAN','CDLSPINNINGTOP','CDLTASUKIGAP'
]

strategys_parametry_rus = {
    'one':['Верх канала','Низ канала','Угол тренда лонг','Угол тренда шорт'],
    'MA':['Коэф. быстрой скольз. средней','Коэф. медленной скольз. средней','Кол-во совпадений в прошлом','Прижатие к верху коридора','Прижатие к низу коридора'],
    'BBANDS':['Отклонение для установки верхней полосы','Временной промежуток','Отклонение для установки нижней полосы','Тип движущейся средней'],
    'EMA':['Временной промежуток'],                   # ноль показывают
    'DEMA':['Временной промежуток'],                  # ноль показывают
    'KAMA':['Временной промежуток'],                  # ноль показывают
    'MAVP':['Минимальный период','Максимальный период','Тип скользящей средней'],                 # ноль показывают
    'SAR':['Ускорение','Максимум'],                   # ноль показывают
    'TEMA':['Временной промежуток'],                  # ноль показывают
    'TRIMA':['Временной промежуток'],                 # ноль показывают
    'WMA':['Временной промежуток'],                   # ноль показывают
    'CDL2CROWS':['Временной промежуток','Временной промежуток'],                  # ноль показывают
    'CDL3BLACKCROWS':['Временной промежуток','Временной промежуток'],                 # ноль показывают
    'CDL3INSIDE':['Временной промежуток','Временной промежуток'],
    'CDL3LINESTRIKE':['Временной промежуток','Временной промежуток'],
    'CDL3OUTSIDE':['Временной промежуток','Временной промежуток'],
    'CDL3STARSINSOUTH':['Временной промежуток','Временной промежуток'],                   # ноль показывают
    'CDL3WHITESOLDIERS':['Временной промежуток','Временной промежуток'],                  # ноль показывают
    'CDLABANDONEDBABY':['Процент проникновения одной свечи внутри другой свечи','Процент сигнала в лонг','Процент сигнала в шорт'],                   # ноль показывают
    'CDLADVANCEBLOCK':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLBELTHOLD':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLCLOSINGMARUBOZU':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLCOUNTERATTACK':['Процент сигнала в лонг','Процент сигнала в шорт'],                   # ноль показывают
    'CDLDARKCLOUDCOVER':['Процент проникновения одной свечи внутри другой свечи','Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLENGULFING':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLEVENINGDOJISTAR':['Процент проникновения одной свечи внутри другой свечи','Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLGRAVESTONEDOJI':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLHAMMER':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLHANGINGMAN':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLHARAMI':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLHARAMICROSS':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLHOMINGPIGEON':['Процент сигнала в лонг','Процент сигнала в шорт'],                    # ноль показывают
    'CDLINVERTEDHAMMER':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLLADDERBOTTOM':['Процент сигнала в лонг','Процент сигнала в шорт'],                    # ноль показывают
    'CDLLONGLEGGEDDOJI':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLMATCHINGLOW':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLMORNINGSTAR':['Процент проникновения одной свечи внутри другой свечи','Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLRICKSHAWMAN':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLSPINNINGTOP':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLTASUKIGAP':['Процент сигнала в лонг','Процент сигнала в шорт'],                   # ноль показывают
}

strategys_parametry_for_section = {
    'one':['up_chanal','down_chanal','corner_long','corner_short'],
    'MA':['koef_bistro','koef_medleno','sovpad_last','up_chanal','down_chanal'],
    'BBANDS':['timeperiod','nbdevup','nbdevdn','matype'],
    'EMA':['timeperiod'],                 # ноль показывают
    'DEMA':['timeperiod'],                    # ноль показывают
    'KAMA':['timeperiod'],                    # ноль показывают
    'MAVP':['minperiod','maxperiod','matype'],                    # ноль показывают
    'SAR':['acceleration','maximum'],                 # ноль показывают
    'TEMA':['timeperiod'],                    # ноль показывают
    'TRIMA':['timeperiod'],                   # ноль показывают
    'WMA':['timeperiod'],                 # ноль показывают
    'CDL2CROWS':['long','short'],                 # ноль показывают
    'CDL3BLACKCROWS':['long','short'],                    # ноль показывают
    'CDL3INSIDE':['long','short'],
    'CDL3LINESTRIKE':['long','short'],
    'CDL3OUTSIDE':['long','short'],
    'CDL3STARSINSOUTH':['long','short'],                  # ноль показывают
    'CDL3WHITESOLDIERS':['long','short'],                 # ноль показывают
    'CDLABANDONEDBABY':['penetration','long','short'],                    # ноль показывают
    'CDLADVANCEBLOCK':['long','short'],
    'CDLBELTHOLD':['long','short'],
    'CDLCLOSINGMARUBOZU':['long','short'],
    'CDLCOUNTERATTACK':['long','short'],                  # ноль показывают
    'CDLDARKCLOUDCOVER':['penetration','long','short'],                   # ноль показывают
    'CDLENGULFING':['long','short'],
    'CDLEVENINGDOJISTAR':['penetration','long','short'],
    'CDLGRAVESTONEDOJI':['long','short'],
    'CDLHAMMER':['long','short'],
    'CDLHANGINGMAN':['long','short'],
    'CDLHARAMI':['long','short'],
    'CDLHARAMICROSS':['long','short'],
    'CDLHOMINGPIGEON':['long','short'],                   # ноль показывают
    'CDLINVERTEDHAMMER':['long','short'],
    'CDLLADDERBOTTOM':['long','short'],                   # ноль показывают
    'CDLLONGLEGGEDDOJI':['long','short'],
    'CDLMATCHINGLOW':['long','short'],
    'CDLMORNINGSTAR':['penetration','long','short'],
    'CDLRICKSHAWMAN':['long','short'],
    'CDLSPINNINGTOP':['long','short'],
    'CDLTASUKIGAP':['long','short'],                  # ноль показывают
}


