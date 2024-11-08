

import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.istoriya_treyd_page.UI.trade_page.trade_page import Trade_page
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.istoriya_treyd_page.UI.trade_page.trade_page_set import Trade_page_set
#11
class Table_trade(ft.UserControl):
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page
        self.settings_print_graph = {}
        self.mas_trade = []
        self.strategys = {
            'one':'Канал,тренд,локаль,объём',
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
        self.state_number_str = {}
        self.str_comopoent = []
        
        
        len_td_our = len(os.listdir(path_save_trade))
        self.how_td_in_one_str = 20 # сколько делаем строк на однйо тсранице
        count_str = int(len_td_our/self.how_td_in_one_str)
        # print(count_str)
        self.number_td_start = 0+count_str*self.how_td_in_one_str
        self.number_td_end = 20+count_str*self.how_td_in_one_str
        
        for i in range(0,count_str):
            self.state_number_str[str(i)] = False
        self.state_number_str[str(count_str)] = True
        
    def open_page_trade(self,e):
        if e.control.key != 'Сет настроек':
            self.controls[:] = []
            self.controls.append(Trade_page(e.control.data))
        elif e.control.key == 'Сет настроек':
            self.controls[:] = []
            self.controls.append(Trade_page_set(e.control.data,self.change_page))
        self.update()
    
    def hover_str(self,e):
        if e.data == "true":
            e.control.bgcolor = c_yelow
            e.control.content.controls[1].content.color= c_blue
            e.control.content.controls[3].content.color= c_blue
            e.control.content.controls[5].content.color= c_blue
            e.control.content.controls[7].content.color= c_blue
            e.control.content.controls[9].content.color= c_blue
            e.control.content.controls[11].content.color=c_blue
            e.control.content.controls[13].content.color=c_blue
            e.control.content.controls[15].content.color=c_blue
            e.control.content.controls[17].content.color=c_blue
            e.control.content.controls[19].content.color=c_blue
            e.control.content.controls[21].content.color=c_blue
        else:
            e.control.bgcolor = c_blue
            e.control.content.controls[1].content.color= c_white
            e.control.content.controls[3].content.color= c_white
            e.control.content.controls[5].content.color= c_white
            e.control.content.controls[7].content.color= c_white
            e.control.content.controls[9].content.color= c_white
            e.control.content.controls[11].content.color=c_white
            e.control.content.controls[13].content.color=c_white
            e.control.content.controls[15].content.color=c_white
            e.control.content.controls[17].content.color=c_white
            e.control.content.controls[19].content.color=c_white
            e.control.content.controls[21].content.color=c_white
        self.update()

    def change_number_pages(self,e):
        # print(e.control.data)
        for key in self.state_number_str:
            if key == e.control.data:self.state_number_str[key]=True
            else:self.state_number_str[key]=False
        self.number_td_start = 0+int(e.control.data)*self.how_td_in_one_str
        self.number_td_end = 20+int(e.control.data)*self.how_td_in_one_str
        self.controls.pop()
        self.controls.append(self.print_page())
        self.update()

    def print_page(self):
        self.str_comopoent[:] = []
        self.mas_trade[:] = []
        mas_max_trade = {}
        
        self.palka_table = ft.Container(width=1,height=15,bgcolor=c_white,margin=0,padding=0)
        self.palka_horizont_table = ft.Container(width=850,height=1,bgcolor=c_white,margin=0)
        for i in range((len(os.listdir(path_save_trade))),0,-1):
            strategy_trade = ''
            strat_mas=[]
            strat_mas[:] = []

            # вытаскиваем название стратегии
            folder_strat = os.listdir(f'{path_save_trade}\\{i}')
            # print(folder_strat)
            for file in folder_strat:
                if file!='log_trade.txt' and file!='settings_our.txt' and file!='trade.txt':
                    strat_mas.append(file.rstrip('.txt'))
                if file == 'folder_trade':
                    strategy_trade = 'Сет настроек'
                    # print(f'{i} - Сет настроек')
            if strategy_trade == '':
                # print(f'{i} - одна настройка')
                if len(strat_mas) == 1: strategy_trade = self.strategys[strat_mas[0]]
                else: strategy_trade = 'Несколько'
            # print(strategy_trade)

            # добываем монеты
            path_settings = f'{path_save_trade}\\{i}\\settings_our.txt'
            if os.path.isfile(path_settings):
                with open(path_settings) as file:
                    self.array_data_row = [row.strip() for row in file]
                    count_coin = len(self.array_data_row[0].split('&')[5].split('|'))

            self.path_save_trade_log = f'{path_save_trade}\\{i}\\trade.txt' # по очереди проходимся по каждой папке
            if strategy_trade != 'Сет настроек':
                if os.path.isfile(self.path_save_trade_log):
                    with open(self.path_save_trade_log) as file:
                        self.array_data_row = [row.strip() for row in file] # сюда сохраняем, что в ней лежит
                        # long|100|86.0|-14.0|6.0|-8.0|RIFUSDT|0.08438508|0.08288712000000001|0.08322|1727936100000|1727936700000|C:\Users\МИН\AppData\Roaming\RoboTrade\svoboda_freym\23\work\RIFUSDT.csv|42|43
                        count_trade_plus = 0
                        count_trade_minus = 0
                        money_trade_plus = 0
                        money_trade_minus = 0
                        comission = 0

                        for data in self.array_data_row:
                            result_trade = float(data.split('|')[2])
                            depo_trade = float(data.split('|')[1])
                            if float(data.split('|')[3])>0:
                                count_trade_plus+=1
                                money_trade_plus+=float(data.split('|')[5])
                            else: 
                                count_trade_minus+=1
                                money_trade_minus+=float(data.split('|')[5])
                            comission+=float(data.split('|')[4])
                        count_trade = len(self.array_data_row)

                        self.mas_trade.append(
                            ft.Container(
                                ft.Row(controls=[self.palka_table,
                                    ft.Container(ft.Text(i,text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                    ft.Container(ft.Text('Дата',text_align='CENTER',color=c_white),width=50,),self.palka_table,
                                    ft.Container(ft.Text(f'{round(result_trade,2)}$  {round(((result_trade-depo_trade)/depo_trade)*100,2)}%',text_align='CENTER',color=c_white),width=160,),self.palka_table,
                                    ft.Container(ft.Text(count_trade,text_align='CENTER',color=c_white),width=56,),self.palka_table,
                                    ft.Container(ft.Text(f'{count_trade_plus}',text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                    ft.Container(ft.Text(f'{round(money_trade_plus,2)}$',text_align='CENTER',color=c_white),width=60,),self.palka_table,
                                    ft.Container(ft.Text(f'{count_trade_minus}',text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                    ft.Container(ft.Text(f'{round(money_trade_minus,2)}$',text_align='CENTER',color=c_white),width=60,),self.palka_table,
                                    ft.Container(ft.Text(f'{round(comission,2)}$',text_align='CENTER',color=c_white),width=68,),self.palka_table,
                                    ft.Container(ft.Text(strategy_trade,text_align='CENTER',color=c_white),width=220,),self.palka_table,
                                    ft.Container(ft.Text(count_coin,text_align='CENTER',color=c_white),width=56,),self.palka_table,
                                ],spacing=0,run_spacing=0),on_hover=self.hover_str,bgcolor=c_blue,margin=ft.margin.only(top=-5,bottom=-5),height=20,on_click=self.open_page_trade,data=i,key=strategy_trade,
                                # margin=ft.margin.only(top=-10,bottom=-10)
                            )
                        )
                        # self.mas_trade.append(self.palka_horizont_table)
                else:
                    self.mas_trade.append(
                            ft.Container(
                                ft.Row(controls=[self.palka_table,
                                    ft.Container(ft.Text(i,text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                    ft.Container(ft.Text('Дата',text_align='CENTER',color=c_white),width=50,),self.palka_table,
                                    ft.Container(ft.Text(f'0$  0%',text_align='CENTER',color=c_white),width=160,),self.palka_table,
                                    ft.Container(ft.Text('0',text_align='CENTER',color=c_white),width=56,),self.palka_table,
                                    ft.Container(ft.Text(f'0',text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                    ft.Container(ft.Text(f'0$',text_align='CENTER',color=c_white),width=60,),self.palka_table,
                                    ft.Container(ft.Text(f'0',text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                    ft.Container(ft.Text(f'0$',text_align='CENTER',color=c_white),width=60,),self.palka_table,
                                    ft.Container(ft.Text(f'0$',text_align='CENTER',color=c_white),width=68,),self.palka_table,
                                    ft.Container(ft.Text(strategy_trade,text_align='CENTER',color=c_white),width=220,),self.palka_table,
                                    ft.Container(ft.Text(count_coin,text_align='CENTER',color=c_white),width=56,),self.palka_table,
                                ],spacing=0,run_spacing=0),on_hover=self.hover_str,bgcolor=c_blue,margin=ft.margin.only(top=-5,bottom=-5),height=20,on_click=self.open_page_trade,data=i,key=strategy_trade
                                # margin=ft.margin.only(top=-10,bottom=-10)
                            )
                        )
            if strategy_trade == 'Сет настроек':
                mas_max_trade.clear()
                folder_strat = os.listdir(f'{path_save_trade}\\{i}\\folder_trade')
                # print(f'{i} - {len(folder_strat)}')
                for file_trade in folder_strat:
                    self.path_trade_set = f'{path_save_trade}\\{i}\\folder_trade\\{file_trade}\\trade.txt' # по очереди проходимся по каждой папке
                    if os.path.isfile(self.path_trade_set):
                        with open(self.path_trade_set) as file:
                            self.array_data_row_set = [row.strip() for row in file] # сюда сохраняем, что в ней лежит
                            # mas_max_trade.append(float(self.array_data_row_set[-1].split('|')[2]))
                            mas_max_trade[file_trade] = float(self.array_data_row_set[-1].split('|')[2])
                    else:
                        # mas_max_trade.append(0)
                        mas_max_trade[file_trade] = 0
                if len(mas_max_trade)!=0:
                    # max_index, max_value = max(enumerate(mas_max_trade), key=lambda pair: pair[1])
                    max_index = int((max(mas_max_trade, key=(mas_max_trade.get))))
                    self.path_trade_set = f'{path_save_trade}\\{i}\\folder_trade\\{max_index}\\trade.txt' # по очереди проходимся по каждой папке
                    # print('!!!!!!!!!!!!!!!!')
                    # print(self.path_trade_set)
                    if os.path.isfile(self.path_trade_set):
                        with open(self.path_trade_set) as file:
                            self.array_data_row = [row.strip() for row in file] # сюда сохраняем, что в ней лежит
                            count_trade_plus = 0
                            count_trade_minus = 0
                            money_trade_plus = 0
                            money_trade_minus = 0
                            comission = 0

                            for data in self.array_data_row:
                                result_trade = float(data.split('|')[2])
                                depo_trade = float(data.split('|')[1])
                                if float(data.split('|')[3])>0:
                                    count_trade_plus+=1
                                    money_trade_plus+=float(data.split('|')[5])
                                else: 
                                    count_trade_minus+=1
                                    money_trade_minus+=float(data.split('|')[5])
                                comission+=float(data.split('|')[4])
                            count_trade = len(self.array_data_row)

                            self.mas_trade.append(
                                ft.Container(
                                    ft.Row(controls=[self.palka_table,
                                        ft.Container(ft.Text(i,text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                        ft.Container(ft.Text('Дата',text_align='CENTER',color=c_white),width=50,),self.palka_table,
                                        ft.Container(ft.Text(f'{round(result_trade,2)}$  {round(((result_trade-depo_trade)/depo_trade)*100,2)}%',text_align='CENTER',color=c_white),width=160,),self.palka_table,
                                        ft.Container(ft.Text(count_trade,text_align='CENTER',color=c_white),width=56,),self.palka_table,
                                        ft.Container(ft.Text(f'{count_trade_plus}',text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                        ft.Container(ft.Text(f'{round(money_trade_plus,2)}$',text_align='CENTER',color=c_white),width=60,),self.palka_table,
                                        ft.Container(ft.Text(f'{count_trade_minus}',text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                        ft.Container(ft.Text(f'{round(money_trade_minus,2)}$',text_align='CENTER',color=c_white),width=60,),self.palka_table,
                                        ft.Container(ft.Text(f'{round(comission,2)}$',text_align='CENTER',color=c_white),width=68,),self.palka_table,
                                        ft.Container(ft.Text(strategy_trade,text_align='CENTER',color=c_white),width=220,),self.palka_table,
                                        ft.Container(ft.Text(count_coin,text_align='CENTER',color=c_white),width=56,),self.palka_table,
                                    ],spacing=0,run_spacing=0),on_hover=self.hover_str,bgcolor=c_blue,margin=ft.margin.only(top=-5,bottom=-5),height=20,on_click=self.open_page_trade,data=i,key=strategy_trade
                                    # margin=ft.margin.only(top=-10,bottom=-10)
                                )
                            )
                    else:
                        self.mas_trade.append(
                        ft.Container(
                            ft.Row(controls=[self.palka_table,
                                ft.Container(ft.Text(i,text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                ft.Container(ft.Text('Дата',text_align='CENTER',color=c_white),width=50,),self.palka_table,
                                ft.Container(ft.Text(f'0$  0%',text_align='CENTER',color=c_white),width=160,),self.palka_table,
                                ft.Container(ft.Text('0',text_align='CENTER',color=c_white),width=56,),self.palka_table,
                                ft.Container(ft.Text(f'0',text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                ft.Container(ft.Text(f'0$',text_align='CENTER',color=c_white),width=60,),self.palka_table,
                                ft.Container(ft.Text(f'0',text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                ft.Container(ft.Text(f'0$',text_align='CENTER',color=c_white),width=60,),self.palka_table,
                                ft.Container(ft.Text(f'0$',text_align='CENTER',color=c_white),width=68,),self.palka_table,
                                ft.Container(ft.Text(strategy_trade,text_align='CENTER',color=c_white),width=220,),self.palka_table,
                                ft.Container(ft.Text(count_coin,text_align='CENTER',color=c_white),width=56,),self.palka_table,
                            ],spacing=0,run_spacing=0),on_hover=self.hover_str,bgcolor=c_blue,margin=ft.margin.only(top=-5,bottom=-5),height=20,on_click=self.open_page_trade,data=i,key=strategy_trade
                            # margin=ft.margin.only(top=-10,bottom=-10)
                        )
                    )
                else:
                    self.mas_trade.append(
                        ft.Container(
                            ft.Row(controls=[self.palka_table,
                                ft.Container(ft.Text(i,text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                ft.Container(ft.Text('Дата',text_align='CENTER',color=c_white),width=50,),self.palka_table,
                                ft.Container(ft.Text(f'0$  0%',text_align='CENTER',color=c_white),width=160,),self.palka_table,
                                ft.Container(ft.Text('0',text_align='CENTER',color=c_white),width=56,),self.palka_table,
                                ft.Container(ft.Text(f'0',text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                ft.Container(ft.Text(f'0$',text_align='CENTER',color=c_white),width=60,),self.palka_table,
                                ft.Container(ft.Text(f'0',text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                ft.Container(ft.Text(f'0$',text_align='CENTER',color=c_white),width=60,),self.palka_table,
                                ft.Container(ft.Text(f'0$',text_align='CENTER',color=c_white),width=68,),self.palka_table,
                                ft.Container(ft.Text(strategy_trade,text_align='CENTER',color=c_white),width=220,),self.palka_table,
                                ft.Container(ft.Text(count_coin,text_align='CENTER',color=c_white),width=56,),self.palka_table,
                            ],spacing=0,run_spacing=0),on_hover=self.hover_str,bgcolor=c_blue,margin=ft.margin.only(top=-5,bottom=-5),height=20,on_click=self.open_page_trade,data=i,key=strategy_trade
                            # margin=ft.margin.only(top=-10,bottom=-10)
                        )
                    )
                            
            
        
        
        # print(self.mas_trade)
        self.mas_trade = sorted(self.mas_trade,key=lambda i:int(i.data))
        # print(self.mas_trade)
        # делаем нижние цирф для выбора страниц
        
        for key in self.state_number_str:
            if self.state_number_str[key] == False:
                self.str_comopoent.append(ft.Container(ft.Text(str(int(key)+1),text_align='CENTER',color=c_white),bgcolor=c_blue,width=20,height=24,border=ft.border.all(1,c_white),data=key,on_click=self.change_number_pages))
            else:
                self.str_comopoent.append(ft.Container(ft.Text(str(int(key)+1),text_align='CENTER',color=c_blue),bgcolor=c_yelow,width=20,height=24,border=ft.border.all(1,c_white),data=key,on_click=self.change_number_pages))
            
            
        self.ferst_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                # ft.Text('Таблица',size=12,color=c_white,text_align='CENTER',color=c_blue),
                                ft.Container(#11
                                    ft.Column(controls=[
                                            # ft.Container(ft.Row(controls=str_comopoent),bgcolor='red'),
                                            ft.Container(
                                                ft.Row(controls=[self.palka_table,
                                                    ft.Container(ft.Text('№',text_align='CENTER',color=c_blue),width=36,),self.palka_table,
                                                    ft.Container(ft.Text('Дата',text_align='CENTER',color=c_blue),width=50,),self.palka_table,
                                                    ft.Container(ft.Text('Результат',text_align='CENTER',color=c_blue),width=160,),self.palka_table,
                                                    ft.Container(ft.Text('Сделок',text_align='CENTER',color=c_blue),width=56,),self.palka_table,
                                                    ft.Container(ft.Text('в +',text_align='CENTER',color=c_blue),width=36,),self.palka_table,
                                                    ft.Container(ft.Text('В + $',text_align='CENTER',color=c_blue),width=60,),self.palka_table,
                                                    ft.Container(ft.Text('в -',text_align='CENTER',color=c_blue),width=36,),self.palka_table,
                                                    ft.Container(ft.Text('В - $',text_align='CENTER',color=c_blue),width=60,),self.palka_table,
                                                    ft.Container(ft.Text('Комиссия',text_align='CENTER',color=c_blue),width=68,),self.palka_table,
                                                    ft.Container(ft.Text('Стратегия',text_align='CENTER',color=c_blue),width=220,),self.palka_table,
                                                    ft.Container(ft.Text('Монет',text_align='CENTER',color=c_blue),width=56,),self.palka_table,
                                                ],spacing=0,run_spacing=0,),bgcolor=c_yelow,height=34
                                                # margin=ft.margin.only(top=-10,bottom=-10)
                                            ),
                                        
                                            ft.Container(ft.Column(controls=self.mas_trade[self.number_td_start:self.number_td_end],scroll=ft.ScrollMode.ALWAYS,height=410)),
                                            ft.Container(ft.Row(controls=self.str_comopoent),margin=ft.margin.only(left=250)),
                                        ]),
                                    width=850,
                                    # height=80,
                                    # margin=ft.margin.only(left=90),
                                ),
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.ferst_page
    
    def build(self):
        return self.print_page()
