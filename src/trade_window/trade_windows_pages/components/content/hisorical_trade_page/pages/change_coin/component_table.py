
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_coin.component_stroka_chang_coin import Component_stroka_chang_coin

class Component_table(ft.UserControl):
    def __init__(self,close_modal,coin_save):
        super().__init__()
        self.coin_save = coin_save
        self.close_modal = close_modal
        self.changed_sorted = 'По изменению' 
        self.mas_result_coin = []

    # получить монеты с биржи
    def get_coin(self):
        client = UMFutures(key=key_bin, secret=secret_bin)
        data = client.ticker_24hr_price_change()
        with open(path_JSON_coins_info_our, 'w', encoding="utf-8") as outfile:
            json.dump(data, outfile, ensure_ascii=False)


    # преобразует число к виду - 15M, 1K
    def num_format(self,num):
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num /= 1000.0
        # add more suffixes if you need them
        return '%.2f%s' % (num, ['', 'K', 'KK', 'M', 'T', 'P'][magnitude])

    # получить данные для таблицы из файла
    def get_data_coin_from_json(self):
        with open(path_data_map_coin, encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data

    # выбор сортировки
    def changed_sort_def(self,e):
        self.changed_sorted = e.control.content.value
        # self.controls[0].open = False
        self.controls = []
        self.controls.append(self.print_component())
        self.update()

    # нажатие на строку
    def checked_coin_table(self,e):
        if e.control.cells[0].content.value not in self.mas_result_coin:
            self.mas_result_coin.append(e.control.cells[0].content.value)
            e.control.color=c_yelow
            self.update()
        else: 
            self.mas_result_coin.remove(e.control.cells[0].content.value)
            e.control.color=c_white
            self.update()
        self.component_stroka_chang_coin.reprint_stroka(self.mas_result_coin)
        

    # кнопка сохранить монеты
    def save_coin_def(self,e):
        self.close_modal()
        self.coin_save()

    # данные для отрисовки таблицы
    def print_component(self):
        sort_mas_slovar = {
            'По цене': 'lastPrice',
            'По объёму': 'quoteVolume',
            'По изменению': 'priceChangePercent',
        }
        data_celka = self.get_data_coin_from_json()
        data_celka = sorted(data_celka, reverse=True,key=lambda d: float(d[sort_mas_slovar[self.changed_sorted]]))

        self.component_stroka_chang_coin = Component_stroka_chang_coin()
        datas_print = []
        for coins_info in data_celka:
            datas_print.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(coins_info['symbol'],text_align='center',color=c_blue,size=12)),
                    ft.DataCell(ft.Text(coins_info['priceChangePercent'],text_align='center',color=c_blue,size=12)),
                    ft.DataCell(ft.Text(coins_info['lastPrice'],text_align='center',color=c_blue,size=12)),
                    ft.DataCell(ft.Text(self.num_format(float(coins_info['volume'])*float(coins_info['lastPrice'])),text_align='center',color=c_blue,size=12)),
                ],on_select_changed=self.checked_coin_table,color=c_white
                )
            )

        sort_label_mas = ['По изменению','По цене','По объёму']
        data_print_sorted = []
        for sort in sort_label_mas:
            if sort == self.changed_sorted:
                data_print_sorted.append(ft.Container(ft.Text(sort,color=c_yelow),padding=5,margin=ft.margin.only(bottom=-10,left=0,top=10),on_click=self.changed_sort_def))
            else:
                data_print_sorted.append(ft.Container(ft.Text(sort,color=c_white),padding=5,margin=ft.margin.only(bottom=-10,left=0,top=10),on_click=self.changed_sort_def))

        self.component_table = ft.Container(
                    ft.Container(ft.Column(controls=[
                        ft.Container(ft.Text('Выбор монет',color=c_blue,size=14,text_align='center'),width=444,height=28,bgcolor=c_yelow,padding=ft.padding.only(top=5)),
                        ft.Container(ft.Text('Выберите монеты, которыми дальше будет торговать стратегия',color=c_white,size=12,text_align='center'),width=444),
                                ft.Column(
                                    controls=[
                                        ft.Container(
                                            ft.Row(controls=[
                                                ft.Container(ft.Text('Выбор монет',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10,left=15,top=10),border=ft.border.all(1,c_white),),
                                                ft.Row(controls=data_print_sorted)
                                            ])
                                            ),
                                        ft.Container(
                                            ft.Column(controls=[
                                                ft.Container(
                                                    ft.Column(controls=[
                                                        ft.DataTable(columns=[
                                                            ft.DataColumn(ft.Text('Символ',text_align='center',color=c_blue,size=12)),
                                                            ft.DataColumn(ft.Text('Изменение\nза 24ч, %',text_align='center',color=c_blue,size=12)),
                                                            ft.DataColumn(ft.Text('Цена',text_align='center',color=c_blue,size=12)),
                                                            ft.DataColumn(ft.Text('Объём',text_align='center',color=c_blue,size=12)),
                                                        ],rows = datas_print,
                                                        column_spacing = 18,
                                                        data_row_max_height = 30,
                                                        data_row_min_height = 30,
                                                        show_checkbox_column = False,

                                                    )
                                                    ],scroll=ft.ScrollMode.ALWAYS,),
                                                    width=400,
                                                    height=200,
                                                    bgcolor=c_white,
                                                    
                                                ),
                                                self.component_stroka_chang_coin,
                                                ft.Container(ft.ElevatedButton(content = ft.Text('Сохранить монеты',size=12,text_align='center'),on_click=self.save_coin_def,data='Свободный фрейм',bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=ft.margin.only(top=-6)),
                                            ]),
                                            width=407,
                                            height=294,
                                            border = ft.border.all(1, c_white),
                                            padding=10,
                                            margin=ft.margin.only(left=15)
                                                ),             
                                            
                                        ]
                                    )
                            ])),
                    width=444,
                    height=430,
                    bgcolor=c_blue,
                    border=ft.border.all(1,c_white),

                    margin=ft.margin.only(bottom=60,top=-70)
                    ) 
        return self.component_table


    def build(self):
        return self.print_component()