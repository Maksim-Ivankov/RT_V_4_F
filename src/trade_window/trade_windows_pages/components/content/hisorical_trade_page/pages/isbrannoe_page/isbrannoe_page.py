
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config

class Isbrannoe_page(ft.UserControl):
    def __init__(self,change_page,regime='see'):
        super().__init__()
        self.change_page = change_page
        self.mas_print_card = []
        self.regime = regime
        self.strat_mas = []

    def print_name_card(self,name):
        if len(name)>30:
            return ft.Container(ft.Row(controls=[ft.Text(name,text_align='center',color=c_yelow,height=30)],scroll=ft.ScrollMode.ALWAYS),width=200,margin=ft.margin.only(top=10))
        else:
            return ft.Container(ft.Text(name,text_align='center',color=c_yelow,height=30),width=200,margin=ft.margin.only(top=10))
    
    # если дневная торговля - значит н ажали из исторической торговли/дневная торговля при выборе монет и загрузке датафреймов
    def change_favorites_day_trade(self,e):
        # здесь нужно доастать данные избранной стратегии и засунуть везде, где нужно для дневной торговли
        
        # сохраняем общие данные избранной стратегии в конфигруацию, чтобы торгануть ими
        if os.path.isfile(f'{path_favorites}\\{e.control.data['number_favorite']}\\settings_our.txt'):
            with open(f'{path_favorites}\\{e.control.data['number_favorite']}\\settings_our.txt') as file: # открываем настройки стратегии, которую хотим сохранить
                settings_our_mas = ([row.strip() for row in file])[0].split('&')
        # Save_config('param_trade_historical_trade_svobodniy_freym',{
        Save_config('param_trade_historical_trade_svobodniy_freym',{'regim_tp':settings_our_mas[9]})
        Save_config('param_trade_historical_trade_svobodniy_freym',{'regim_sl':settings_our_mas[10]})
        Save_config('param_trade_historical_trade_svobodniy_freym',{'regim_volume_min':settings_our_mas[11]})
        Save_config('param_trade_historical_trade_svobodniy_freym',{'regim_volume_max':settings_our_mas[12]})
        Save_config('param_trade_historical_trade_svobodniy_freym',{'name_bot':settings_our_mas[13]})
        Save_config('param_trade_historical_trade_svobodniy_freym',{'komission_mayker':settings_our_mas[14]})
        Save_config('param_trade_historical_trade_svobodniy_freym',{'deposit':settings_our_mas[15]})
        Save_config('param_trade_historical_trade_svobodniy_freym',{'leverage':settings_our_mas[16]})
        Save_config('param_trade_historical_trade_svobodniy_freym',{'komission_taker':settings_our_mas[17]})
        Save_config('param_trade_historical_trade_svobodniy_freym',{'tp':settings_our_mas[18]})
        Save_config('param_trade_historical_trade_svobodniy_freym',{'sl':settings_our_mas[19]})
        Save_config('param_trade_historical_trade_svobodniy_freym',{'volume_min':settings_our_mas[20]})
        Save_config('param_trade_historical_trade_svobodniy_freym',{'volume_max':settings_our_mas[21]})
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strategys':settings_our_mas[22]})
        Save_config('param_trade_historical_trade_svobodniy_freym',{'change_time_settings':settings_our_mas[23]})
        Save_config('param_trade_historical_trade_svobodniy_freym',{'time_on_work':settings_our_mas[24]})
        Save_config('param_trade_historical_trade_svobodniy_freym',{'time_off_work':settings_our_mas[25]})
        # })
        # сохраняем данные настоек стратегии в конфигурацию, чтобы торгануть ими
        # вытаскиваем название стратегии
        folder_strat = os.listdir(f'{path_favorites}\\{e.control.data['number_favorite']}')
        for file in folder_strat:
            if file!='folder_trade' and file!='settings_our.txt' and file!='property.txt':
                self.strat_mas.append(file.rstrip('.txt'))
        for strat in self.strat_mas:
            if os.path.isfile(f'{path_favorites}\\{e.control.data['number_favorite']}\\{strat}.txt'):
                with open(f'{path_favorites}\\{e.control.data['number_favorite']}\\{strat}.txt') as file: # открываем настройки стратегии, которую хотим сохранить
                    settings_strategy = ([row.strip() for row in file])[0].split('&')
                if strat == 'BBANDS':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_BBANDS_timeperiod':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_BBANDS_nbdevup':str(settings_strategy[1])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_BBANDS_nbdevdn':str(settings_strategy[2])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_BBANDS_matype':str(settings_strategy[3])})
                if strat == 'CDL2CROWS':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDL2CROWS_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDL2CROWS_short':str(settings_strategy[1])})
                if strat == 'CDL3BLACKCROWS':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDL3BLACKCROWS_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDL3BLACKCROWS_short':str(settings_strategy[1])})
                if strat == 'CDL3INSIDE':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDL3INSIDE_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDL3INSIDE_short':str(settings_strategy[1])})
                if strat == 'CDL3LINESTRIKE':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDL3LINESTRIKE_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDL3LINESTRIKE_short':str(settings_strategy[1])})
                if strat == 'CDL3OUTSIDE':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDL3OUTSIDE_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDL3OUTSIDE_short':str(settings_strategy[1])})
                if strat == 'CDL3STARSINSOUTH':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDL3STARSINSOUTH_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDL3STARSINSOUTH_short':str(settings_strategy[1])})
                if strat == 'CDL3WHITESOLDIERS':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDL3WHITESOLDIERS_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDL3WHITESOLDIERS_short':str(settings_strategy[1])})
                if strat == 'CDLABANDONEDBABY':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLABANDONEDBABY_penetration':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLABANDONEDBABY_long':str(settings_strategy[1])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLABANDONEDBABY_short':str(settings_strategy[2])})
                if strat == 'CDLADVANCEBLOCK':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLADVANCEBLOCK_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLADVANCEBLOCK_short':str(settings_strategy[1])})
                if strat == 'CDLBELTHOLD':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLBELTHOLD_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLBELTHOLD_short':str(settings_strategy[1])})
                if strat == 'CDLCLOSINGMARUBOZU':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLCLOSINGMARUBOZU_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLCLOSINGMARUBOZU_short':str(settings_strategy[1])})
                if strat == 'CDLCOUNTERATTACK':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLCOUNTERATTACK_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLCOUNTERATTACK_short':str(settings_strategy[1])})
                if strat == 'CDLDARKCLOUDCOVER':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLDARKCLOUDCOVER_penetration':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLDARKCLOUDCOVER_long':str(settings_strategy[1])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLDARKCLOUDCOVER_short':str(settings_strategy[2])})
                if strat == 'CDLENGULFING':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLENGULFING_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLENGULFING_short':str(settings_strategy[1])})
                if strat == 'CDLEVENINGDOJISTAR':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLEVENINGDOJISTAR_penetration':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLEVENINGDOJISTAR_long':str(settings_strategy[1])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLEVENINGDOJISTAR_short':str(settings_strategy[2])})
                if strat == 'CDLGRAVESTONEDOJI':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLGRAVESTONEDOJI_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLGRAVESTONEDOJI_short':str(settings_strategy[1])})
                if strat == 'CDLHAMMER':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLHAMMER_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLHAMMER_short':str(settings_strategy[1])})
                if strat == 'CDLHANGINGMAN':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLHANGINGMAN_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLHANGINGMAN_short':str(settings_strategy[1])})
                if strat == 'CDLHARAMI':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLHARAMI_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLHARAMI_short':str(settings_strategy[1])})
                if strat == 'CDLHARAMICROSS':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLHARAMICROSS_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLHARAMICROSS_short':str(settings_strategy[1])})
                if strat == 'CDLHOMINGPIGEON':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLHOMINGPIGEON_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLHOMINGPIGEON_short':str(settings_strategy[1])})
                if strat == 'CDLINVERTEDHAMMER':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLINVERTEDHAMMER_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLINVERTEDHAMMER_short':str(settings_strategy[1])})
                if strat == 'CDLLADDERBOTTOM':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLLADDERBOTTOM_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLLADDERBOTTOM_short':str(settings_strategy[1])})
                if strat == 'CDLLONGLEGGEDDOJI':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLLONGLEGGEDDOJI_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLLONGLEGGEDDOJI_short':str(settings_strategy[1])})
                if strat == 'CDLMATCHINGLOW':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLMATCHINGLOW_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLMATCHINGLOW_short':str(settings_strategy[1])})
                if strat == 'CDLMORNINGSTAR':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLMORNINGSTAR_penetration':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLMORNINGSTAR_long':str(settings_strategy[1])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLMORNINGSTAR_short':str(settings_strategy[2])})
                if strat == 'CDLRICKSHAWMAN':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLRICKSHAWMAN_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLRICKSHAWMAN_short':str(settings_strategy[1])})
                if strat == 'CDLSPINNINGTOP':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLSPINNINGTOP_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLSPINNINGTOP_short':str(settings_strategy[1])})
                if strat == 'CDLTASUKIGAP':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLTASUKIGAP_long':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_CDLTASUKIGAP_short':str(settings_strategy[1])})
                if strat == 'DEMA':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_DEMA_timeperiod':str(settings_strategy[0])})
                if strat == 'EMA':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_EMA_timeperiod':str(settings_strategy[0])})
                if strat == 'KAMA':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_KAMA_timeperiod':str(settings_strategy[0])})
                if strat == 'MA':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_MA_koef_bistro':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_MA_koef_medleno':str(settings_strategy[1])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_MA_sovpad_last':str(settings_strategy[2])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_MA_up_chanal':str(settings_strategy[3])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_MA_down_chanal':str(settings_strategy[4])})
                if strat == 'MAVP':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_MAVP_minperiod':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_MAVP_maxperiod':str(settings_strategy[1])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_MAVP_matype':str(settings_strategy[2])})
                if strat == 'one':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_one_up_chanal':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_one_down_chanal':str(settings_strategy[1])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_one_corner_long':str(settings_strategy[2])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_one_corner_short':str(settings_strategy[3])})
                if strat == 'SAR':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_SAR_acceleration':str(settings_strategy[0])})
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_MSAR_maximum':str(settings_strategy[1])})
                if strat == 'TEMA':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_TEMA_timeperiod':str(settings_strategy[0])})
                if strat == 'TRIMA':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_TRIMA_timeperiod':str(settings_strategy[0])})
                if strat == 'WMA':
                    Save_config('param_trade_historical_trade_svobodniy_freym',{'strat_WMA_timeperiod':str(settings_strategy[0])})
        
        self.change_page(e)

    def get_btn_use(self,number_favorite):
        if self.regime == 'see':
            # если режим просмотра, то после нажатия, нужно предложить, историческая торговля, тестовая торговля или торговый робот и так далее
            return ft.Container(ft.ElevatedButton(content = ft.Text('Использовать стратегию',size=12,),data='Использовать избранную стратегию изнутри',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30)
        if self.regime == 'Дневная торговля':
            # если дневная торговля - значит н ажали из исторической торговли/дневная торговля при выборе монет и загрузке датафреймов
            return ft.Container(ft.ElevatedButton(content = ft.Text('Использовать стратегию',size=12,),data={'page':'Запустить торговлю','number_favorite':number_favorite},bgcolor=c_yelow,on_click=self.change_favorites_day_trade,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30)


# name_bot
# strategi_coin
# how_mach_money
# komission_mayker
# komission_taker
# work_tf
# dlitelnost
# regim_tp
# regim_sl
# tp
# sl
# regim_volume_min
# regim_volume_max
# volume_min
# volume_max
# leverage
# strategys
# sledim_money
# deposit
# coins_trade
# change_time_settings
# time_on_work
# time_off_work
# use_last_sost
# use_last_number
# number_trade
# + там же сохранить настройки стратегии1

    def build(self):
        
        mas_count_favorites = os.listdir(path_favorites)
        mas_count_favorites = [int(item) for item in mas_count_favorites]
        mas_count_favorites = sorted(mas_count_favorites)
        
        if len(os.listdir(path_favorites))==0:
            data_print_favorites = ft.Container(ft.Text('Добавьте избранные стратегии для отображения',text_align='center'),padding=ft.padding.only(top=220),width=850)
        else:
            for i in mas_count_favorites: # итерируемся по папкам с сохранененными стратегиями
                if os.path.isfile(f'{path_favorites}\\{i}\\property.txt'):
                    with open(f'{path_favorites}\\{i}\\property.txt') as file: # открываем настройки стратегии, которую хотим сохранить
                        array_data_1 = [row.strip() for row in file]
                    # если режим по умолчанию - просто смотреть стратегии
                    self.mas_print_card.append(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(
                                    ft.Container(ft.Text(f'Стартегия {i}',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                    ft.Container(
                                        ft.Container(ft.Column(controls=[
                                                self.print_name_card(array_data_1[0]),
                                                # ft.Container(ft.Text(array_data_1[0],text_align='center',color=c_yelow),width=200),
                                                ft.Container(ft.Column(controls=[ft.Text(array_data_1[1],text_align='center')],scroll=ft.ScrollMode.ALWAYS,height=100),width=200),
                                                ft.Container(ft.Text('Трейдов: 15 | Сделок: 92',text_align='center'),width=200),
                                                ft.Container(ft.Text('Дневная доходность: 3.72%',text_align='center'),width=200,margin=ft.margin.only(bottom=8)),
                                                ft.Container(ft.Row(controls=[
                                                        ft.Container(ft.ElevatedButton(content = ft.Text('Смотреть трейды',size=12,),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),data={'page':'Избранные стратегии | Показать трейды','number_favorite':i,'name_favorite':array_data_1[0]},on_click=self.change_page),alignment=ft.alignment.center,height=30,width=150),
                                                        ft.Container(ft.Image(src='src/trade_window/trade_windows_pages/components/content/hisorical_trade_page/pages/isbrannoe_page/UI/img/pancil_blue.png'),bgcolor=c_yelow,width=30,height=30,padding=7,data={'page':'Избранные стратегии | Измеить данные стартегии','number_favorite':i},on_click=self.change_page),
                                                    ]),width=850,margin=ft.margin.only(left=5)),
                                                self.get_btn_use(i)
                                            ]),padding=5),
                                        width=210,
                                        height = 312,
                                        padding=ft.padding.only(left=-1,top=-1,bottom=-1),
                                        border=ft.border.all(1,c_white)
                                    )]
                        )
                    ))
                    
            data_print_favorites = ft.Row(
                controls=self.mas_print_card,
                wrap=True,
                spacing=10,
                run_spacing=10,
            )
                        
        
        self.ferst_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text('Избранные стратегии - стратегии с задаными настройками, которые были добавлены в избранное',size=12,color=c_white,text_align='center'),
                                             width=900,margin=ft.margin.only(bottom=15)),
                                ft.Container(
                                    data_print_favorites,
                                    width=900,
                                ),
                            ],scroll=ft.ScrollMode.ALWAYS,height=600),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.ferst_page