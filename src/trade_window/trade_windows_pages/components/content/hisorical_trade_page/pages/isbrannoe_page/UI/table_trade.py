
import flet as ft
from variable import *
from imports import *

class Table_trade(ft.UserControl):
    def __init__(self,change_page,number_favorite):
        super().__init__()
        self.number_favorite = number_favorite
        self.change_page = change_page
        self.mas_trade = []


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
        self.update()


    def build(self):
        mas_max_trade = {}
        self.mas_trade[:] = []
        self.palka_table = ft.Container(width=1,height=15,bgcolor=c_white,margin=0,padding=0)
        self.path_folder_favorites = f'{path_favorites}\\{self.number_favorite}\\folder_trade'
        for i in range((len(os.listdir(f'{self.path_folder_favorites}'))),0,-1):
            self.path_save_trade_log = f'{self.path_folder_favorites}\\{i}\\trade.txt' # по очереди проходимся по каждой папке
            if os.path.isfile(self.path_save_trade_log):
                with open(self.path_save_trade_log) as file:
                    self.array_data_row = [row.strip() for row in file] # сюда сохраняем, что в ней лежит
                    count_trade_plus = 0
                    count_trade_minus = 0
                    money_trade_plus = 0
                    money_trade_minus = 0
                    comission = 0
                    
                    if len(self.array_data_row)!=0:
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
                                ],spacing=0,run_spacing=0),on_hover=self.hover_str,bgcolor=c_blue,margin=ft.margin.only(top=-5,bottom=-5),data={'page':'Избранные стратегии | Трейд','number_favorite':self.number_favorite,'number_trade':i},height=20,on_click=self.change_page
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
                            ],spacing=0,run_spacing=0),on_hover=self.hover_str,bgcolor=c_blue,margin=ft.margin.only(top=-5,bottom=-5),data={'page':'Избранные стратегии | Трейд','number_favorite':self.number_favorite,'number_trade':i},height=20,on_click=self.change_page
                            # margin=ft.margin.only(top=-10,bottom=-10)
                        )
                    )
        if len(os.listdir(f'{self.path_folder_favorites}'))<15:
            height_table = len(os.listdir(f'{self.path_folder_favorites}'))*15
            table_print_height = ft.Container(ft.Column(controls=self.mas_trade,height=height_table))
        else:
            table_print_height = ft.Container(ft.Column(controls=self.mas_trade,scroll=ft.ScrollMode.ALWAYS,height=300))
        
        self.ferst_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(#11
                                    ft.Column(controls=[
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
                                                ],spacing=0,run_spacing=0,),bgcolor=c_yelow,height=34
                                            ),
                                        
                                            table_print_height,
                                        ]),
                                    width=574,
                                ),
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.ferst_page