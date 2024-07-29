
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
path_imports_config = appdata + '\config.ini'
path_data_map_coin = appdata + '\map_coin.json'

#--------------------------------------------------

c_blue = '#222831'
c_white = '#FFFFFF'
c_yelow = '#FBD46D'
c_green = '#0AFF89'
c_red = '#FF0A0A'

server_ip = 'http://127.0.0.1:5000'

width_window_platforma = 1186
height_window_platforma = 740

version_desctop = 'v1.25.11'

key_bin = 'QIT80MTFskjHSr82dtsteA6bG01CUeODQCg65KoYaQ5LmPcSpYDzyv1Oa7fugW3m'
secret_bin = 'uMLo0WdaCv5FHBauV8QI4LZoDgmmVFf5Jd8TboKYRxHnHx6pmNrhg5bmdBgO54xI'










