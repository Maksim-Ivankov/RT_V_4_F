
import flet as ft
from variable import *
from imports import *


class Card_default(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.treyd_polosa = []
    


    def print_page(self,number,regime='None',number_trade=0):
        self.treyd_polosa[:] = []
        if regime == 'None':
            self.trade_page = ft.Container(
                ft.Column(controls=[
                
                ft.Container(ft.Text(number,color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white)),
                ft.Container(ft.Container(ft.Text('В очереди',color=c_white,text_align='CENTER'),bgcolor=c_blue_binance,padding=ft.padding.only(top=90)),width=170,height=200,border=ft.border.all(1,c_white))
            ]),data=number,key=str(number))
    # Все что ниже запускается из истории торговли. При клике в таблице по строке с торговлей по сету настроек
        elif regime == 'istorija_trade':
            self.path_trade_set = f'{path_save_trade}\\{number_trade}\\folder_trade\\{number}\\trade.txt' # по очереди проходимся по каждой папке
            if os.path.isfile(self.path_trade_set):
                with open(self.path_trade_set) as file:
                    self.array_data_row_set = [row.strip() for row in file]
                    for data in self.array_data_row_set:
                        if float(data.split('|')[3]) > 0:
                            self.treyd_polosa.append(ft.Container(ft.Text(f'Депо: {float(data.split('|')[2])}| Рез: {float(data.split('|')[3])}',color=c_blue,text_align='CENTER',size=12),bgcolor=c_green,width=150,height=20))
                        else:
                            self.treyd_polosa.append(ft.Container(ft.Text(f'Депо: {float(data.split('|')[2])}| Рез: {float(data.split('|')[3])}',color=c_white,text_align='CENTER',size=12),bgcolor=c_red,width=150,height=20))
                    self.treyd_polosa = list(reversed(self.treyd_polosa))
                    self.trade_page = ft.Container(
                        ft.Column(controls=[
                        ft.Container(ft.Text(number,color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white)),
                        ft.Container(ft.Container(ft.Column(controls=self.treyd_polosa,scroll=ft.ScrollMode.ALWAYS),height=150,padding=10),width=170,height=200,border=ft.border.all(1,c_white))
                    ]),data=number,key=str(number))
            else:
                self.trade_page = ft.Container(
                    ft.Column(controls=[
                    
                    ft.Container(ft.Text(number,color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white)),
                    ft.Container(ft.Container(ft.Text('Нет сделок',color=c_white,text_align='CENTER'),bgcolor=c_blue_binance,padding=ft.padding.only(top=90)),width=170,height=200,border=ft.border.all(1,c_white))
                ]),data=number,key=str(number))
            
           
           
        return self.trade_page

   