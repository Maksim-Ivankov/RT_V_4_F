
import flet as ft
from variable import *
from imports import *


class Table_result(ft.UserControl):
    def __init__(self,reptint_table_result,print_page_one_trade_oura_set):
        super().__init__()
        self.reptint_table_result = reptint_table_result
        self.print_page_one_trade_oura_set = print_page_one_trade_oura_set
        self.mas_trade = []
        self.sort_list_arr = []
        self.sort_list = ['Результат','Сделок','В +','В -']
        self.sort_change = {
            'Результат':False,
            'Сделок':False,
            'В +':False,
            'В -':False

        }

    def hover_str(self,e):
        # print(e.control.content.controls)
        if e.data == "true":
            e.control.bgcolor = c_yelow
            e.control.content.controls[1].content.color= c_blue
            # e.control.content.controls[2].content.color= c_blue
            e.control.content.controls[3].content.color= c_blue
            e.control.content.controls[5].content.color= c_blue
            e.control.content.controls[7].content.color= c_blue
            e.control.content.controls[9].content.color= c_blue
            e.control.content.controls[11].content.color= c_blue
            e.control.content.controls[13].content.color= c_blue
            e.control.content.controls[15].content.color= c_blue
        #     print(e.control)
  
        else:
            e.control.bgcolor = c_blue
            e.control.content.controls[1].content.color= c_white
            e.control.content.controls[3].content.color= c_white
            e.control.content.controls[5].content.color= c_white
            e.control.content.controls[7].content.color= c_white
            e.control.content.controls[9].content.color= c_white
            e.control.content.controls[11].content.color= c_white
            e.control.content.controls[13].content.color= c_white
            e.control.content.controls[15].content.color= c_white
    
        # self.update()
        self.update_component()
    
    # открыть страницу торговли
    def open_page_trade(self,e):
        self.print_page_one_trade_oura_set(e.control.data)
    
    def clcik_sort(self,e):
        for key in self.sort_change:
            if key == e.control.data:self.sort_change[key] = True
            else:self.sort_change[key] = False
        self.reptint_table_result(e.control.data)


    def print_page(self,update_component,sort_result = 'basa',number_trade=(len(os.listdir(path_save_trade))+1)):
        self.mas_trade[:] = []
        self.update_component  = update_component
        self.palka_table = ft.Container(width=1,height=15,bgcolor=c_white,margin=0,padding=0)
        self.palka_horizont_table = ft.Container(width=850,height=1,bgcolor=c_white,margin=0)
        folder_strat = os.listdir(f'{path_save_trade}\\{number_trade}\\folder_trade')
        int_folder_strat = []
        for i in folder_strat:
            int_folder_strat.append(int(i))
        
        for file in sorted(int_folder_strat):
            # print(file)
            if os.path.isfile(f'{path_save_trade}\\{number_trade}\\folder_trade\\{str(file)}\\trade.txt'):
                with open(f'{path_save_trade}\\{number_trade}\\folder_trade\\{str(file)}\\trade.txt') as file2:
                    self.array_data_row = [row.strip() for row in file2] # сюда сохраняем, что в ней лежит
                    for data in self.array_data_row:
                        
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
                            ft.Row(controls=[ft.Container(),
                                ft.Container(ft.Text(str(file),text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                ft.Container(ft.Text(f'{round(result_trade,2)}$  {round(((result_trade-depo_trade)/depo_trade)*100,2)}%',text_align='CENTER',color=c_white),width=160,),self.palka_table,
                                ft.Container(ft.Text(count_trade,text_align='CENTER',color=c_white),width=56,),self.palka_table,
                                ft.Container(ft.Text(f'{count_trade_plus}',text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                ft.Container(ft.Text(f'{round(money_trade_plus,2)}$',text_align='CENTER',color=c_white),width=60,),self.palka_table,
                                ft.Container(ft.Text(f'{count_trade_minus}',text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                ft.Container(ft.Text(f'{round(money_trade_minus,2)}$',text_align='CENTER',color=c_white),width=60,),self.palka_table,
                                ft.Container(ft.Text(f'{round(comission,2)}$',text_align='CENTER',color=c_white),width=68,),
                            ],spacing=0,run_spacing=0),on_hover=self.hover_str,bgcolor=c_blue,margin=ft.margin.only(top=-5,bottom=-5),height=20,on_click=self.open_page_trade,data=str(file)
                        )
                    )
            else:
                self.mas_trade.append(
                        ft.Container(
                            ft.Row(controls=[ft.Container(),
                                ft.Container(ft.Text(str(file),text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                ft.Container(ft.Text(f'100$  0%',text_align='CENTER',color=c_white),width=160,),self.palka_table,
                                ft.Container(ft.Text('0',text_align='CENTER',color=c_white),width=56,),self.palka_table,
                                ft.Container(ft.Text(f'0',text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                ft.Container(ft.Text(f'0$',text_align='CENTER',color=c_white),width=60,),self.palka_table,
                                ft.Container(ft.Text(f'0',text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                ft.Container(ft.Text(f'0$',text_align='CENTER',color=c_white),width=60,),self.palka_table,
                                ft.Container(ft.Text(f'0$',text_align='CENTER',color=c_white),width=68,),
                            ],spacing=0,run_spacing=0),on_hover=self.hover_str,bgcolor=c_blue,margin=ft.margin.only(top=-5,bottom=-5),height=20,on_click=self.open_page_trade,data=str(file)
                        )
                    )
        
        self.sort_list_arr[:] = []
        for  i in self.sort_list:
            if self.sort_change[i]:
                self.sort_list_arr.append(ft.Container(ft.Text(i,color=c_blue,),data=i,bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white),on_click=self.clcik_sort))
            else:
                self.sort_list_arr.append(ft.Container(ft.Text(i,color=c_white,),data=i,bgcolor=c_blue,padding=5,margin=ft.margin.only(bottom=-10),on_click=self.clcik_sort))
        if sort_result == 'Результат':
            self.mas_trade = sorted(self.mas_trade, key=lambda res: float(res.content.controls[3].content.value.split(' ')[0][:-1]),reverse=True)      
        elif sort_result == 'Сделок':
            self.mas_trade = sorted(self.mas_trade, key=lambda res: int(res.content.controls[5].content.value),reverse=True)      
        elif sort_result == 'В +':
            self.mas_trade = sorted(self.mas_trade, key=lambda res: int(res.content.controls[7].content.value),reverse=True)      
        elif sort_result == 'В -':
            self.mas_trade = sorted(self.mas_trade, key=lambda res: int(res.content.controls[11].content.value),reverse=True)      
        
        self.table_result = ft.Container(
                                ft.Container(
                                    ft.Column(controls=[
                                        ft.Row(controls=[
                                                ft.Container(ft.Text('Результаты торговли по сету',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white)),
                                                ft.Row(controls=self.sort_list_arr)
                                            ]),
                                        ft.Container(
                                            ft.Column(controls=[
                                                ft.Container(#11
                                                             ft.Column(controls=[
                                                                 ft.Container(
                                                                    ft.Row(controls=[ft.Container(),
                                                                        ft.Container(ft.Text('№',text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                                                        ft.Container(ft.Text('Результат',text_align='CENTER',color=c_white),width=160,),self.palka_table,
                                                                        ft.Container(ft.Text('Сделок',text_align='CENTER',color=c_white),width=56,),self.palka_table,
                                                                        ft.Container(ft.Text('в +',text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                                                        ft.Container(ft.Text('В + $',text_align='CENTER',color=c_white),width=60,),self.palka_table,
                                                                        ft.Container(ft.Text('в -',text_align='CENTER',color=c_white),width=36,),self.palka_table,
                                                                        ft.Container(ft.Text('В - $',text_align='CENTER',color=c_white),width=60,),self.palka_table,
                                                                        ft.Container(ft.Text('Комиссия',text_align='CENTER',color=c_white),width=68,)
                                                                    ],spacing=0,run_spacing=0,),bgcolor=c_blue,height=34
                                                                ),
                                                                ft.Column(controls=self.mas_trade,scroll=ft.ScrollMode.ALWAYS,height=300),
                                                            ]),
                                                    # ft.Column(controls=self.mas_trade,scroll=ft.ScrollMode.ALWAYS,height=300),
                                                ),
                                            ]),
                                            border=ft.border.all(1,c_white)
                                        )
                                    ])),
                                width=524,margin=ft.margin.only(top=15,left=172),key="table_result")
        
        return self.table_result

                