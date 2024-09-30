
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
path_ini_general_set = appdata + '\\general_set.ini' # файл общего сета настроек
path_ini_one_set = appdata + '\\one_set.ini' # файл сета настроек one
path_ini_MA_set = appdata + '\\MA_set.ini' # файл сета настроек MA
path_data_map_coin = appdata + '\\map_coin.json' # должен обновляться каждые n минут. С него рисуется тепловая карта и берутся монеты для получения датафреймов
path_data_user_tg_chat = appdata + '\\channel_users_tg.json' 
path_data_message_tg_chat = appdata + '\\channel_messages_tg.json'
path_JSON_coins_info_our = appdata + '\\coins_info_our.json'
path_svoboda_freym = appdata + '\\svoboda_freym' # начало пути для сохранения датафреймов - историческая торговля/свободный фрейм
#--------------------------------------------------
# проверяем есть ли папка в директории
if os.path.isdir(f'{appdata}\\trade'): 
    path_save_trade = appdata+'\\trade' # сюда будем сохранять трейды
else:
    os.mkdir(f'{appdata}\\trade') # если папки нет, создаем её
    path_save_trade = appdata+'\\trade' # сюда будем сохранять трейды


#--------------------------------------------------

c_blue = '#222831'
c_white = '#FFFFFF'
c_yelow = '#FBD46D'
c_green = '#0AFF89'
c_red = '#FF0A0A'

c_blue_binance = '#161A1E'

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









