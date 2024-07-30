
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config

class Teplowaya_map(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.regime_tree_map_now = 'Changes_in_24_hours'

    # принимает данные с биржи и кол-во монет, которые нужно вернуть. Возвращает отсортированный словарь монета:процент движения
    def get_top_coin_changes_day(self,data,count):
        change={}
        change_istina = {}
        coin_max={}
        coin_min={}
        coin_mas1 = {}
        for i in data:
            change[i['symbol']] = abs(float(i['priceChangePercent']))
            change_istina[i['symbol']] = float(i['priceChangePercent'])
        coin_max = dict(sorted(change.items(), key=lambda item: item[1],reverse=True))
        i=0
        for key, value in coin_max.items():
            if i<count:
                coin_mas1[key] = value
                i=i+1
            else: break
        for i in coin_mas1:
            coin_mas1[i] = change_istina[i]
        return coin_mas1
    
    # принимает данные с биржи и кол-во монет, которые нужно вернуть. Возвращает отсортированный словарь монета:процент движения
    def get_top_coin_volume_trade(self,data,count):
        change={}
        change_istina = {}
        coin_max={}
        coin_min={}
        coin_mas1 = {}
        for i in data:
            change[i['symbol']] = round(float(i['openPrice'])*float(i['volume']))
        coin_max = dict(sorted(change.items(), key=lambda item: item[1],reverse=True))
        i=0
        for key, value in coin_max.items():
            if i<count:
                coin_mas1[key] = value
                i=i+1
            else: break
        return coin_mas1
    
    # отработка выбора режима тепловой карты
    def change_regime_tree_map(self,e):
        self.regime_tree_map_now = e.control.data
        data_save = {
            'regime_tree_map':e.control.data,
        }
        Save_config('settings_program',data_save)
        self.controls = []
        self.controls.append(self.print_tree_map(self.regime_tree_map_now))
        self.update()

    # преобразует число к виду - 15M, 1K
    def num_format(self,num):
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num /= 1000.0
        # add more suffixes if you need them
        return '%.2f%s' % (num, ['', 'K', 'KK', 'M', 'T', 'P'][magnitude])

    # отрисовка блока с тепловой картой
    def print_tree_map(self,regime):

        with open(path_data_map_coin) as data_file:
            data_loaded = json.load(data_file)

        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        if ('settings_program') in config.sections():
            count_coin = config.get('settings_program', 'count_coin')
            # если есть секция с настрйоками, проверяем есть ли в ней ключ - режим тепловой карты
            if config.has_option('settings_program', 'regime_tree_map'):
                self.regime_tree_map_now = config.get('settings_program', 'regime_tree_map')
            else: self.regime_tree_map_now = 'Changes_in_24_hours'
        else:
            count_coin = 10
            self.regime_tree_map_now = 'Changes_in_24_hours'
        
        if int(count_coin)>55:
            count_coin = 50
        if self.regime_tree_map_now == 'Trading_volume':
            if int(count_coin)>30:
                count_coin = 24

        translation_regime_tree_map_now = {
            'Changes_in_24_hours':'Изменения за 24 ч.',
            'Trading_volume':'Объём торгов',
            # 'Efficiency_in_1_hour':'Эффективность за 1 ч.',
        }

        # набираем массив вкладок режима
        # Отработка выбора режима тепловой карты
        regime_tree_map = ['Changes_in_24_hours','Trading_volume']
        item_birgas = []
        for i in regime_tree_map:
            if i == self.regime_tree_map_now:
                item_birgas.append(
                     ft.Container(ft.Text(translation_regime_tree_map_now[i],color=c_yelow,size=12),data = i,on_click=self.change_regime_tree_map)
                )
            else:
                 item_birgas.append(
                     ft.Container(ft.Text(translation_regime_tree_map_now[i],color=c_white,size=12),data = i,on_click=self.change_regime_tree_map)
                )
                 
        if self.regime_tree_map_now == 'Changes_in_24_hours':
            coin_mas = self.get_top_coin_changes_day(data_loaded,int(count_coin))
        elif self.regime_tree_map_now == 'Trading_volume':
            coin_mas = self.get_top_coin_volume_trade(data_loaded,int(count_coin))
         
# num_format
        data_graph = []
        weight_data_graph = []
        arr_coin_color = []
        for key, value in coin_mas.items():
            if self.regime_tree_map_now == 'Trading_volume':
                data_graph.append(f'{key}\n{self.num_format(value)}')
            else:
                data_graph.append(f'{key}\n{value}')
            weight_data_graph.append(abs(value))
            if value>0:
                arr_coin_color.append(c_green)
            else: 
                arr_coin_color.append(c_red)

        fig = plt.figure(figsize=(8,4))
        ax = fig.add_subplot(111)
        if int(count_coin) <31:
            if self.regime_tree_map_now == 'Trading_volume':
                squarify.plot(weight_data_graph, label=data_graph,ec = 'black', color=arr_coin_color,text_kwargs={'fontsize':6,'color':c_blue}, ax=ax)
            else:
                squarify.plot(weight_data_graph, label=data_graph,ec = 'black', color=arr_coin_color,text_kwargs={'fontsize':8,'color':c_blue}, ax=ax)
        elif int(count_coin) <55:
            squarify.plot(weight_data_graph, label=data_graph,ec = 'black', color=arr_coin_color,text_kwargs={'fontsize':6,'color':c_blue}, ax=ax)
        else: 
            squarify.plot(weight_data_graph, label=data_graph,ec = 'black', color=arr_coin_color,text_kwargs={'fontsize':6,'color':c_blue}, ax=ax)
        plt.axis('off')

        
        return ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(ft.Text('Тепловая карта',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))
                    ),
                    ft.Container(
                        
                        ft.Column(controls=[
                            ft.Container(
                                ft.Row(controls=item_birgas),padding=ft.padding.only(left=100,top=9)
                            ),
                            ft.Container(MatplotlibChart(fig,transparent=True),margin=ft.margin.only(top=-50,left=-22)),
                        ]),
                            
                        
                        width=668,
                        height=370,
                        border = ft.border.all(1, c_white),
                        padding=ft.padding.only(left=-85,top=0,bottom=0,right=-85),
                    ), 
                ]
            )
        )
        

    def build(self):

        # ниже запись json файл с монетами и данными по ним с биржи
        # client = UMFutures(key=key_bin, secret=secret_bin)
        # data = client.ticker_24hr_price_change()
        # with io.open(path_data_map_coin, 'w', encoding='utf8') as outfile:
        #     str_ = json.dumps(data,
        #                       indent=4, sort_keys=True,
        #                       separators=(',', ': '), ensure_ascii=False)
        #     outfile.write(str_)

        # Читаем json
        
        
        return self.print_tree_map(self.regime_tree_map_now)

# import flet as ft
# from variable import *
# from imports import *

# from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config

# class Teplowaya_map(ft.UserControl):
#     # def __init__(self,change_menu):
#     #     super().__init__()
#     #     self.change_menu = change_menu

#     # принимает данные с биржи и кол-во монет, которые нужно вернуть. Возвращает отсортированный словарь монета:процент движения
#     def get_top_coin_changes_day(self,data,count):
#         change={}
#         change_istina = {}
#         coin_max={}
#         coin_min={}
#         coin_mas1 = {}
#         for i in data:
#             change[i['symbol']] = abs(float(i['priceChangePercent']))
#             change_istina[i['symbol']] = float(i['priceChangePercent'])
#         coin_max = dict(sorted(change.items(), key=lambda item: item[1],reverse=True))
#         i=0
#         for key, value in coin_max.items():
#             if i<count:
#                 coin_mas1[key] = value
#                 i=i+1
#             else: break
#         for i in coin_mas1:
#             coin_mas1[i] = change_istina[i]
#         return coin_mas1
    
#     # отработка выбора режима тепловой карты
#     def change_regime_tree_map(self,e):
#         self.regime_tree_map_now = e.control.value
#         data_save = {
#             'regime_tree_map':e.control.value,
#         }
#         Save_config('settings_program',data_save)
#         self.controls = []
#         self.controls.append(self.print_tree_map(self.regime_tree_map_now))
#         self.update()

#     # отрисовка блока с тепловой картой
#     def print_tree_map(regime):

#         pass

#     def build(self):

#         # ниже запись json файл с монетами и данными по ним с биржи
#         # client = UMFutures(key=key_bin, secret=secret_bin)
#         # data = client.ticker_24hr_price_change()
#         # with io.open(path_data_map_coin, 'w', encoding='utf8') as outfile:
#         #     str_ = json.dumps(data,
#         #                       indent=4, sort_keys=True,
#         #                       separators=(',', ': '), ensure_ascii=False)
#         #     outfile.write(str_)

#         # Читаем json
#         with open(path_data_map_coin) as data_file:
#             data_loaded = json.load(data_file)

#         config = configparser.ConfigParser()         
#         config.read(path_imports_config)
#         if ('settings_program') in config.sections():
#             count_coin = config.get('settings_program', 'count_coin')
#         else:
#             api_key_tg = ''
#             id_group_tg = ''
        
#         if int(count_coin)>55:
#             count_coin = 50
        
#         coin_mas = self.get_top_coin_changes_day(data_loaded,int(count_coin))

#         data_graph = []
#         weight_data_graph = []
#         arr_coin_color = []
#         for key, value in coin_mas.items():
#             data_graph.append(f'{key}\n{value}')
#             weight_data_graph.append(abs(value))
#             if value>0:
#                 arr_coin_color.append(c_green)
#             else: 
#                 arr_coin_color.append(c_red)

#         fig = plt.figure(figsize=(8,4))
#         ax = fig.add_subplot(111)
#         if int(count_coin) <31:
#             squarify.plot(weight_data_graph, label=data_graph,ec = 'black', color=arr_coin_color,text_kwargs={'fontsize':8}, ax=ax)
#         elif int(count_coin) <55:
#             squarify.plot(weight_data_graph, label=data_graph,ec = 'black', color=arr_coin_color,text_kwargs={'fontsize':6}, ax=ax)
#         else: 
#             squarify.plot(weight_data_graph, label=data_graph,ec = 'black', color=arr_coin_color,text_kwargs={'fontsize':6}, ax=ax)
#         plt.axis('off')

#         # Отработка выбора режима тепловой карты
#         regime_tree_map = ['Изменения за 24 ч.','объём торгов','Эффективность за 1 ч.']
        
#         self.teplowaya_map = ft.Container(
#             ft.Column(
#                 controls=[
#                     ft.Container(
#                         ft.Container(ft.Text('Тепловая карта',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))
#                     ),
#                     ft.Container(
                        
#                         ft.Column(controls=[
#                             ft.Container(
#                                 ft.Row(controls=[
#                                 ft.Container(ft.Text('Изменения за 24 ч.'),on_click=self.change_regime_tree_map),
#                                 ft.Container(ft.Text('объём торгов'),on_click=self.change_regime_tree_map),
#                                 ft.Container(ft.Text('Эффективность за 1 ч.'),on_click=self.change_regime_tree_map),
#                             ]),padding=ft.padding.only(left=100,top=5)
#                             ),
#                             ft.Container(MatplotlibChart(fig,transparent=True),margin=ft.margin.only(top=-50,left=-22)),
#                         ]),
                            
                        
#                         width=668,
#                         height=370,
#                         border = ft.border.all(1, c_white),
#                         padding=ft.padding.only(left=-85,top=0,bottom=0,right=-85),
#                     ), 
#                 ]
#             )
#         )
        
#         return self.teplowaya_map