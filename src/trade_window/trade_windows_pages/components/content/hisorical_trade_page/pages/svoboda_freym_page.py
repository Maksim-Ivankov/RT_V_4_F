
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.UI.header import Header
from src.trade_window.trade_windows_pages.components.content.UI.dropdown import Dropdown
from src.trade_window.trade_windows_pages.components.content.UI.input import Input

from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_coin.cgange_coin_window import Cgange_coin_window

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_coin.sbor_data.componen_log import Componen_log
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_coin.sbor_data.component_coin_log import Component_coin_log
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_coin.page_last_data.page_last_data import Page_last_data

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.ferst_page import Ferst_page

# Dropdown(self.on_change_tema,self.change_tema,["Dark","Light"],150)
# Input(self.on_change_count_coin,self.change_count_coin,150)

class Svoboda_freym_page(ft.UserControl):
    def __init__(self,change_page,page):
        super().__init__()
        self.text_for_button_slov = {
            'top_dvigeniya':'Топ движения',
            'top_value':'Топ объёма',
            'change_list':'Список монет'
        }
        self.work_tf_slov = {
            '1m':1,
            '5m':5,
            '15m':15,
            '30m':30,
            '1h':60,
            '4h':240
        }
        self.dlitelnost_slow = {
            '12h':720,
            '24h':1440,
            '48h':2880
        }
        self.see_tf_slov = {
            "1m":1,
            "5m":5
        }
        self.page = page
        self.change_page = change_page
        Save_config('param_trade_historical_trade_svobodniy_freym',{'regime_trade_page':'svoboda'})
        # if len(os.listdir(path_save_trade))==0:
        #     Save_config('param_trade_historical_trade_svobodniy_freym',{'regime_trade_page':'svoboda'})
    
    # выбор выпадашки - следим за ценой
    def on_change_sledim_sa_cenoy(self,e):
        data_save = {
            'sledim_money':e.control.value
        }
        Save_config('param_trade_historical_trade_svobodniy_freym',data_save)
        self.change_sledim_sa_cenoy = e.control.value

    # выбор выпадашки - рабочий таймфрейм
    def on_change_work_tf(self,e):
        data_save = {
            'work_tf':e.control.value
        }
        Save_config('param_trade_historical_trade_svobodniy_freym',data_save)
        self.change_work_tf = e.control.value

    # выбор выпадашки - длителоьность
    def on_change_how_mach_time(self,e):
        data_save = {
            'dlitelnost':e.control.value
        }
        Save_config('param_trade_historical_trade_svobodniy_freym',data_save)
        self.change_how_mach_time = e.control.value

    # выбор выпадашки - сколько монет торговать
    def on_change_how_mach_coin(self,e):
        data_save = {
            'how_mach_money':e.control.value
        }
        Save_config('param_trade_historical_trade_svobodniy_freym',data_save)
        self.change_count_coin = e.control.value

    # нажали на кнопку сохранить в модалке1
    def coin_save(self,data):
        self.controls = []
        self.controls.append(self.print_page())
        self.controls[0].content.content.content.controls[1].content.controls[1].content.controls[0].content.controls[7].content.content.value = data
        self.update()

    # ЗДЕСЬ МОДАЛКА!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # окно выбора стратегии монет1
    def chage_coin(self,e):
        bs = Cgange_coin_window(self.coin_save)
        self.page.overlay.append(bs)
        self.page.update()

    # кнопка - получить данные
    def get_data_df(self,e):
        thread7654 = threading.Thread(target=self.generate_dataframe)
        thread7654.start()

    #------------------------------------------------------------------------1
    # получить кол-во свечей, объём дф рабочий
    def get_volume(self):
        return self.dlitelnost_slow[self.change_how_mach_time]/self.work_tf_slov[self.change_work_tf]
    # получить кол-во свечей, объём дф слежения
    def get_see_volume(self):
        return self.dlitelnost_slow[self.change_how_mach_time]/self.see_tf_slov[self.change_sledim_sa_cenoy]
    # получить массив монет - топ движения
    def get_mas_coin(self,strat,count):
        # получаем данные из файла
        with open(path_data_map_coin, encoding='utf-8') as json_file:
            data = json.load(json_file)
        if strat == 'Топ движения':
            data = sorted(data, reverse=True,key=lambda d: abs(float(d['priceChangePercent'])))
        elif strat == 'Топ объёма':
            data = sorted(data, reverse=True,key=lambda d: float(d['quoteVolume']))
        data_new = data[:int(count)]
        data_return = []
        for i in data_new:
            data_return.append(i['symbol'])
        # return data
        return data_return
    # Получите последние n свечей по n минут для торговой пары, обрабатываем и записывае данные в датафрейм
    def get_futures_klines(self,symbol,TF,VOLUME):
        # print('https://fapi.binance.com/fapi/v1/klines?symbol='+symbol.upper()+'&limit='+str(VOLUME)+'&interval='+TF)
        x = requests.get('https://fapi.binance.com/fapi/v1/klines?symbol='+symbol.upper()+'&limit='+str(VOLUME)+'&interval='+TF)
        df=pd.DataFrame(x.json())
        df.columns=['open_time','open','high','low','close','VOLUME','close_time','d1','d2','d3','d4','d5']
        df=df.drop(['d1','d2','d3','d4','d5'],axis=1)
        df['open']=df['open'].astype(float)
        df['high']=df['high'].astype(float)
        df['low']=df['low'].astype(float)
        df['close']=df['close'].astype(float)
        df['VOLUME']=df['VOLUME'].astype(float)
        return(df) # возвращаем датафрейм с подготовленными данными

    # рисуем логи в правую колонку
    def print_log(self,msg):
        # print(msg)
        self.print_msg_mas.insert(0,ft.Text(msg,color=c_blue,size=12))
        self.componen_log.update_page(self.print_msg_mas)
        self.update()
        # self.controls[0].content.content.content.controls[1].content.controls[1].content.controls[2].content.controls[1].content.controls = self.print_msg_mas
        # self.controls[0].content.content.content.controls[1].content.controls[1].content.controls[2].content.controls.update()



    # генерируем датафреймы в отдельном потоке
    def generate_dataframe(self):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'use_last_sost':'False'})
        self.print_msg_mas = []
        # сколько получить свечей рабочий
        self.VOLUME = self.get_volume()
        # сколько получить свечей слежения
        self.SEE_VOLUME = self.get_see_volume()
        # получаем массив монет для запроса дф
        if self.strat_coin_text == 'Список монет':
            self.COIN_TRADE = self.coins_trade # массив монет
            self.HOW_MACH_COIN = len(self.COIN_TRADE) # кол-во монет
        elif self.strat_coin_text == 'Топ движения':
            self.HOW_MACH_COIN = self.change_count_coin # кол-во монет
            self.COIN_TRADE = self.get_mas_coin('Топ движения',self.HOW_MACH_COIN) # массив монет
            Save_config('param_trade_historical_trade_svobodniy_freym',{'coins_trade':'|'.join(self.COIN_TRADE)})
        elif self.strat_coin_text == 'Топ объёма':
            self.HOW_MACH_COIN = self.change_count_coin # кол-во монет
            self.COIN_TRADE = self.get_mas_coin('Топ объёма',self.HOW_MACH_COIN) # массив монет
            Save_config('param_trade_historical_trade_svobodniy_freym',{'coins_trade':'|'.join(self.COIN_TRADE)})
        # отрисовываем монеты
        coin_print = []
        for i in self.COIN_TRADE:
            coin_print.append(
                ft.Container(ft.Text(i,color=c_blue,size=12,text_align='center'),width=160)
            )
        self.component_coin_log.update_page(coin_print)
        # получаем и увеличиваем на 1 порядковый номер
        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.number_trade = config.get('param_trade_historical_trade_svobodniy_freym', 'number_trade')
        self.number_trade = int(self.number_trade)+1
        Save_config('param_trade_historical_trade_svobodniy_freym',{'number_trade':str(self.number_trade)})
        # получаем датафреймы и сохраняем в файл
        os.mkdir(f'{path_svoboda_freym}/{self.number_trade}')
        os.mkdir(f'{path_svoboda_freym}/{self.number_trade}/work')
        os.mkdir(f'{path_svoboda_freym}/{self.number_trade}/see')
        self.print_log('Начали сбор данных')
        # Сохраняем данные по текущему сету коинов 
        data_save = {
            'how_mach_coin':str(self.HOW_MACH_COIN),
            'coin_mas':str(self.COIN_TRADE),
            'volume':str(self.VOLUME),
            'see_volume':str(self.SEE_VOLUME),
            'tf_see':str(self.change_sledim_sa_cenoy),
            'tf_work':str(self.change_work_tf),
            'how_mach_time':str(self.change_how_mach_time),
            'strategy_coin':str(self.strat_coin_text_celka),
            'time':str(time.strftime("%d.%m.%Y | %H:%M:%S", time.localtime())),
            }                                   # сюда сохранить данные
        Save_config(str(self.number_trade),data_save,path_ini_svoboda_freym)
        x=1
        for coin in self.COIN_TRADE:
            df = self.get_futures_klines(coin,self.change_work_tf,int(self.VOLUME))
            df.to_csv(f'{path_svoboda_freym}/{self.number_trade}/work/{coin}.csv')
            time.sleep(2)
            df = self.get_futures_klines(coin,self.change_sledim_sa_cenoy,int(self.SEE_VOLUME))
            df.to_csv(f'{path_svoboda_freym}/{self.number_trade}/see/{coin}.csv')
            time.sleep(2)
            self.print_log(f'{x}/{len(self.COIN_TRADE)} | Датафрейм {coin} добавлен')
            x+=1
        self.print_log('Закончили сбор данных')

    # колбэк изнутри - использовать прошлые данные, когда выбираешь данные
    def change_storage_data(self,number):
        data = {
            'use_last_sost':'True',
            'use_last_number':str(number),
        }
        Save_config('param_trade_historical_trade_svobodniy_freym',data)
        self.controls = []
        self.controls.append(self.print_page())
        self.update()
        # СЮДА ДОБАВИТЬ ОБРАБОТКУ, КОГДА ВЫБИРАЕШЬ СТАРЫЕ ДАННЫЕ, НАСТРОЙКИ В КОНФИГЕ ДОЛЖНЫ МЕНЯТЬСЯ НА ЭТИ СТАРЫЕ ДАННЫЕ
        # config = configparser.ConfigParser()         
        # config.read(path_imports_config)
        # self.number_trade = config.get('param_trade_historical_trade_svobodniy_freym', 'number_trade')


    # кнопка - использовать прошлые данные
    def open_modal_last_data(self,e):
        self.controls = []
        self.controls.append(Page_last_data(self.change_storage_data))
        self.update()

    
    def print_page(self):
        # print('Начинаем')
        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        if ('param_trade_historical_trade_svobodniy_freym') in config.sections():
            self.change_sledim_sa_cenoy = config.get('param_trade_historical_trade_svobodniy_freym', 'sledim_money')
            self.change_work_tf = config.get('param_trade_historical_trade_svobodniy_freym', 'work_tf')
            self.change_how_mach_time = config.get('param_trade_historical_trade_svobodniy_freym', 'dlitelnost')
            self.number_trade = config.get('param_trade_historical_trade_svobodniy_freym', 'number_trade')
            self.use_last_sost = config.get('param_trade_historical_trade_svobodniy_freym', 'use_last_sost')
            self.use_last_number = config.get('param_trade_historical_trade_svobodniy_freym', 'use_last_number')
            self.coins_trade = config.get('param_trade_historical_trade_svobodniy_freym', 'coins_trade').split('|')
            self.strat_coin_text_celka = config.get('param_trade_historical_trade_svobodniy_freym', 'strategi_coin')
            self.strat_coin_text = self.text_for_button_slov[config.get('param_trade_historical_trade_svobodniy_freym', 'strategi_coin')]
            if self.strat_coin_text == 'Список монет':
                self.change_count_coin = len(self.coins_trade)
            else: self.change_count_coin = int(config.get('param_trade_historical_trade_svobodniy_freym', 'how_mach_money'))

        else:
            self.change_sledim_sa_cenoy = '1m'
            self.change_work_tf = '5m'
            self.change_how_mach_time = '24h'
            self.change_count_coin = '10'
            self.strat_coin_text = 'Выбрать монеты'
        
        # Если выбраны прошлые данные, нужно показать монеты прошлых данных
        
        
        # если есть датафреймы
        # получаем файлы в указанной директории массивом
        file_work = []
        file_see = []
        for (dirpath, dirnames, filenames) in os.walk(f'{path_svoboda_freym}/{self.number_trade}/work/'):
            file_work.extend(filenames)
            break
        for (dirpath, dirnames, filenames) in os.walk(f'{path_svoboda_freym}/{self.number_trade}/see/'):
            file_see.extend(filenames)
            break
        # если кол-во файлов в рабочем и смотре совпадает с записями в конфигурации, значит все хорошо, файлы найдены
        if self.change_count_coin == len(file_work) and self.change_count_coin == len(file_see):
            data_detect = [
                ft.Text(f'Данные обнаружены, текущий шаг - {self.number_trade}',size=12,color=c_blue),
                ft.Text(f'Кол-во датафреймов: {self.change_count_coin}',size=12,color=c_blue),
                ft.Text(f'Таймфрейм рабочий - {self.change_work_tf} | Слежения - {self.change_sledim_sa_cenoy}',size=12,color=c_blue),
                ft.Text(f'Длительность сбора - {self.change_how_mach_time}',size=12,color=c_blue),
                ft.Text(f'Режим выбора монет - {self.strat_coin_text}',size=12,color=c_blue),
                ft.Text(f'Можно запустить торговлю',size=12,color=c_blue),
            ]
        else:
            data_detect = [ft.Text(f'Данные не найдены, текущий шаг - {self.number_trade}',size=12,color=c_blue),
                           ft.Text(f'Получите новые данные',size=12,color=c_blue),
                           ]
        if self.use_last_sost == 'True':
            config.read(path_ini_svoboda_freym)
            self.tf_work_last = config.get(self.use_last_number, 'tf_work')
            self.tf_see_last = config.get(self.use_last_number, 'tf_see')
            self.how_mach_time_last = config.get(self.use_last_number, 'how_mach_time')
            self.strategy_coin_last = self.text_for_button_slov[config.get(self.use_last_number, 'strategy_coin')]
            self.coin_mas_last = config.get(self.use_last_number, 'coin_mas')
            data_detect = [
                ft.Text(f'Используются данные из хранилища | № {self.use_last_number}',size=12,color=c_blue),
                ft.Text(f'Таймфрейм рабочий - {self.tf_work_last}',size=12,color=c_blue),
                ft.Text(f'Таймфрейм слежения - {self.tf_see_last}',size=12,color=c_blue),
                ft.Text(f'Длительность фрейма - {self.how_mach_time_last}',size=12,color=c_blue),
                ft.Text(f'Стратегия - {self.strategy_coin_last}',size=12,color=c_blue),
                ft.Text(f'Монеты - {self.coin_mas_last}',size=12,color=c_blue),
                ft.Text(f'Данные готовы. Можно приступать к торговле',size=12,color=c_blue),
            ]
            # записываем монеты из выбранного шага и- использовать прошлые данные
            self.coins_trade = literal_eval(self.coin_mas_last)
            data_save = {
               'work_tf':config.get(self.use_last_number, 'tf_work'), 
               'sledim_money':config.get(self.use_last_number, 'tf_see'), 
               'dlitelnost':config.get(self.use_last_number, 'how_mach_time'), 
               'coins_trade':'|'.join(literal_eval(config.get(self.use_last_number, 'coin_mas'))), 
               'strategi_coin':config.get(self.use_last_number, 'strategy_coin'), 
               'how_mach_money':config.get(self.use_last_number, 'how_mach_coin'), 
            }
            Save_config('param_trade_historical_trade_svobodniy_freym',data_save)
            # work_tf  таймфрейм
            # sledim_money  таймфрейм слежения
            # dlitelnost
            # coins_trade монеты

            # how_mach_coin
            # volume
            # see_volume

            
        coins_print = []
        for i in self.coins_trade:
            coins_print.append(
                ft.Container(ft.Text(i,color=c_blue,size=12,text_align='center'),width=160)
            )
            
            # print(self.coin_mas_last)
        self.componen_log = Componen_log(data_detect)
        self.component_coin_log =  Component_coin_log(coins_print)

        self.svoboda_freym_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text('Получите данные по монетам для исторической торговли\nс биржи, либо используйте загруженные ранее данные',
                                        size=12,color=c_white,text_align='center'),padding=ft.padding.only(left=180)),
                                ft.Container(
                                    ft.Column(
                                        controls=[
                                            ft.Container(
                                                ft.Container(ft.Text('Сбор данных',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white),
                                            )),
                                            ft.Container(
                                                ft.Row(controls=[
                                                    ft.Container(
                                                        ft.Column(controls=[
                                                            ft.Text('Следим за ценой',size=12,color=c_white,text_align='center',width=150),
                                                            Dropdown(self.on_change_sledim_sa_cenoy,self.change_sledim_sa_cenoy,["1m","5m"],150),
                                                            ft.Text('Рабочий таймфрейм',size=12,color=c_white,text_align='center',width=150),
                                                            Dropdown(self.on_change_work_tf,self.change_work_tf,['1m','5m','15m','30m','1h','4h'],150),
                                                            ft.Text('Длительность',size=12,color=c_white,text_align='center',width=150),
                                                            Dropdown(self.on_change_how_mach_time,self.change_how_mach_time,['12h','24h','48h'],150),
                                                            ft.Text('Стратегия монет',size=12,color=c_white,text_align='center',width=150),
                                                            ft.Container(ft.ElevatedButton(content = ft.Text(self.strat_coin_text,size=12,),on_click=self.chage_coin,bgcolor=c_white,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,width=150,height=30,margin=ft.margin.only(top=0,bottom=0)),
                                                            ft.Text('Сколько монет торговать',size=12,color=c_white,text_align='center',width=150),
                                                            Input(self.on_change_how_mach_coin,self.change_count_coin,150),
                                                            ft.Container(ft.ElevatedButton(content = ft.Text('Получить данные',size=12,),bgcolor=c_yelow,on_click=self.get_data_df,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30,margin=ft.margin.only(top=0,bottom=0)),
                                                        ])
                                                    ),
                                                    ft.Container(
                                                        ft.Column(controls=[
                                                            ft.Text('Монеты для торговли',size=12,color=c_white,text_align='center',width=150),
                                                            self.component_coin_log,
                                                            ft.Container(ft.ElevatedButton(content = ft.Text('Использовать прошлые данные',size=12,),bgcolor=c_yelow,on_click=self.open_modal_last_data,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30,margin=ft.margin.only(top=0,bottom=0,right=-90)),
                                                        ])
                                                    ),
                                                    ft.Container(ft.Column(controls=[
                                                        ft.Text('Логи торговли',size=12,color=c_white,text_align='center',width=360),
                                                        self.componen_log
                                                    ])),
                                                ]),
                                                width=709,
                                                height=392,
                                                border = ft.border.all(1, c_white),
                                                padding=10,
                                            ), 
                                            ft.Container(
                                                ft.Container(
                                                    ft.Row(controls=[
                                                    ft.Container(ft.ElevatedButton(content = ft.Text('Назад',size=12,),data='Первая',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                                    ft.Container(ft.ElevatedButton(content = ft.Text('Настроить торгового робота',size=12,),data='Настройки робота',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                                    ft.Container(ft.ElevatedButton(content = ft.Text('Использовать избранную тсратегию',size=12,),data={'page':'Использовать избранную стратегию','regime':'Дневная торговля'},bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                                ]),padding=ft.padding.only(left=72,top=10)
                                                ),
                                                width=709
                                                # height=100
                                            )
                                        ]
                                    )
                                ),
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.svoboda_freym_page


    def build(self):
        return self.print_page()
        