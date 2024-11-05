# close — цены закрытия; 2
# timeperiod — количество значений (по умолчанию — 5); 2
# nbdevup — плавающее значение стандартного отклонения для установки верхней полосы (по умолчанию — 2); 2
# nbdevdn — плавающее значение стандартного отклонения для установки нижней полосы (по умолчанию — 2); 2
# matype — тип движущейся средней (по умолчанию — 0, простая движущаяся средняя); 2
# verbose — показ логов (по умолчанию — False). 2


# Inputs:
# price: (any ndarray)

# Parameters:
# timeperiod: 5 nbdevup: 2 nbdevdn: 2 matype: 0 (Simple Moving Average)

# Outputs:
# upperband middleband lowerband

# Lines:
# upperband
# middleband
# lowerband
# Params:
# timeperiod (5)
# nbdevup (2)
# nbdevdn (2)
# matype (0)



# компонент - настройки стратегии BBANDS
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config
from src.trade_window.trade_windows_pages.components.content.UI.input import Input

class BBANDS(ft.UserControl):
    def __init__(self):
        super().__init__()

    def input_BBANDS_timeperiod(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_BBANDS_timeperiod':str(e.control.value)})
    def input_BBANDS_nbdevup(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_BBANDS_nbdevup':str(e.control.value)})
    def input_BBANDS_nbdevdn(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_BBANDS_nbdevdn':str(e.control.value)})
    def input_BBANDS_matype(self,e):
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_BBANDS_matype':str(e.control.value)})


    def print_component(self):
        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.BBANDS_timeperiod = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_BBANDS_timeperiod')
        self.BBANDS_nbdevup = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_BBANDS_nbdevup')
        self.BBANDS_nbdevdn = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_BBANDS_nbdevdn')
        self.BBANDS_matype = config.get('param_trade_historical_trade_svobodniy_freym', 'strat_BBANDS_matype')
        

        self.MA = ft.Container(
            ft.Container(
                
                    ft.Column(
                        controls=[
                            ft.Container(
                                ft.Container(ft.Text('Полосы Боллинджера',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))
                            ),
                            ft.Container(
                                ft.Row(controls=[
                                    ft.Container(
                                        ft.Column(controls=[
                                        ft.Container(ft.Text('Отклонение для установки верхней полосы',size=12,color=c_white,text_align='center'),width=170),
                                        Input(self.input_BBANDS_nbdevup,self.BBANDS_nbdevup,170),
                                        ft.Container(ft.Text('Временной промежуток',size=12,color=c_white,text_align='center'),width=170),
                                        Input(self.input_BBANDS_timeperiod,self.BBANDS_timeperiod,170),
                                    ]),
                                    # padding=ft.padding.only(bottom=50)
                                    ),
                                    ft.Column(controls=[
                                        ft.Container(ft.Text('Отклонение для установки нижней полосы',size=12,color=c_white,text_align='center'),width=170),
                                        Input(self.input_BBANDS_nbdevdn,self.BBANDS_nbdevdn,170),
                                        ft.Container(ft.Text('Тип движущейся средней',size=12,color=c_white,text_align='center'),width=170),
                                        Input(self.input_BBANDS_matype,self.BBANDS_matype,170),
                                    ])
                                ]),
                                width=396,
                                border = ft.border.all(1, c_white),
                                padding=ft.padding.only(top=14,bottom=14,left=20), 
                            )
                        ]
                    ),     
                alignment=ft.alignment.center
            ),
            width=860,
        )
        
        return self.MA

    def build(self):
        return self.print_component()
        