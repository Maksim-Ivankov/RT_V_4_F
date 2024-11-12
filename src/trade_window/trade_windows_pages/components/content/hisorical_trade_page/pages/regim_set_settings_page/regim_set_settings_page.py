# страница выбора стратегии торговли1
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_strategy_trade_page.UI.component_info_strat import Component_info_strat
from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.table_set_print import Table_set_print
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.general_set import General_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.MA_set import MA_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.one_set import One_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.BBANDS_set import BBANDS_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.EMA_set import EMA_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.DEMA_set import DEMA_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.KAMA_set import KAMA_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.MAVP_set import MAVP_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.SAR_set import SAR_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.TEMA_set import TEMA_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.TRIMA_set import TRIMA_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.WMA_set import WMA_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDL2CROWS_set import CDL2CROWS_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDL3BLACKCROWS_set import CDL3BLACKCROWS_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDL3INSIDE_set import CDL3INSIDE_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDL3LINESTRIKE_set import CDL3LINESTRIKE_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDL3OUTSIDE_set import CDL3OUTSIDE_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDL3STARSINSOUTH_set import CDL3STARSINSOUTH_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDL3WHITESOLDIERS_set import CDL3WHITESOLDIERS_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDLABANDONEDBABY_set import CDLABANDONEDBABY_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDLADVANCEBLOCK_set import CDLADVANCEBLOCK_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDLBELTHOLD_set import CDLBELTHOLD_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDLCLOSINGMARUBOZU_set import CDLCLOSINGMARUBOZU_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDLCOUNTERATTACK_set import CDLCOUNTERATTACK_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDLDARKCLOUDCOVER_set import CDLDARKCLOUDCOVER_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDLENGULFING_set import CDLENGULFING_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDLEVENINGDOJISTAR_set import CDLEVENINGDOJISTAR_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDLGRAVESTONEDOJI_set import CDLGRAVESTONEDOJI_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDLHAMMER_set import CDLHAMMER_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDLHANGINGMAN_set import CDLHANGINGMAN_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDLHARAMI_set import CDLHARAMI_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDLHARAMICROSS_set import CDLHARAMICROSS_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDLHOMINGPIGEON_set import CDLHOMINGPIGEON_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDLINVERTEDHAMMER_set import CDLINVERTEDHAMMER_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDLLADDERBOTTOM_set import CDLLADDERBOTTOM_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDLLONGLEGGEDDOJI_set import CDLLONGLEGGEDDOJI_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDLMATCHINGLOW_set import CDLMATCHINGLOW_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDLMORNINGSTAR_set import CDLMORNINGSTAR_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDLRICKSHAWMAN_set import CDLRICKSHAWMAN_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDLSPINNINGTOP_set import CDLSPINNINGTOP_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.UI.card_set.CDLTASUKIGAP_set import CDLTASUKIGAP_set


from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_general_set import Generate_general_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_one_set import Generate_one_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_MA_set import Generate_MA_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_BBANDS_set import Generate_BBANDS_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_EMA_set import Generate_EMA_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_DEMA_set import Generate_DEMA_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_KAMA_set import Generate_KAMA_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_MAVP_set import Generate_MAVP_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_SAR_set import Generate_SAR_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_TEMA_set import Generate_TEMA_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_TRIMA_set import Generate_TRIMA_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_WMA_set import Generate_WMA_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDL2CROWS_set import Generate_CDL2CROWS_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDL3BLACKCROWS_set import Generate_CDL3BLACKCROWS_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDL3INSIDE_set import Generate_CDL3INSIDE_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDL3LINESTRIKE_set import Generate_CDL3LINESTRIKE_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDL3OUTSIDE_set import Generate_CDL3OUTSIDE_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDL3STARSINSOUTH_set import Generate_CDL3STARSINSOUTH_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDL3WHITESOLDIERS_set import Generate_CDL3WHITESOLDIERS_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDLABANDONEDBABY_set import Generate_CDLABANDONEDBABY_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDLADVANCEBLOCK_set import Generate_CDLADVANCEBLOCK_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDLBELTHOLD_set import Generate_CDLBELTHOLD_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDLCLOSINGMARUBOZU_set import Generate_CDLCLOSINGMARUBOZU_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDLCOUNTERATTACK_set import Generate_CDLCOUNTERATTACK_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDLDARKCLOUDCOVER_set import Generate_CDLDARKCLOUDCOVER_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDLENGULFING_set import Generate_CDLENGULFING_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDLEVENINGDOJISTAR_set import Generate_CDLEVENINGDOJISTAR_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDLGRAVESTONEDOJI_set import Generate_CDLGRAVESTONEDOJI_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDLHAMMER_set import Generate_CDLHAMMER_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDLHANGINGMAN_set import Generate_CDLHANGINGMAN_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDLHARAMI_set import Generate_CDLHARAMI_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDLHARAMICROSS_set import Generate_CDLHARAMICROSS_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDLHOMINGPIGEON_set import Generate_CDLHOMINGPIGEON_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDLINVERTEDHAMMER_set import Generate_CDLINVERTEDHAMMER_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDLLADDERBOTTOM_set import Generate_CDLLADDERBOTTOM_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDLLONGLEGGEDDOJI_set import Generate_CDLLONGLEGGEDDOJI_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDLMATCHINGLOW_set import Generate_CDLMATCHINGLOW_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDLMORNINGSTAR_set import Generate_CDLMORNINGSTAR_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDLRICKSHAWMAN_set import Generate_CDLRICKSHAWMAN_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDLSPINNINGTOP_set import Generate_CDLSPINNINGTOP_set
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.generate_set.generate_CDLTASUKIGAP_set import Generate_CDLTASUKIGAP_set

class Regim_set_settings_page(ft.UserControl):
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page
        self.strategy_translate = strategys_our
        self.card_set = {
            'one':One_set(self.click_neral_set),
            'MA':MA_set(self.click_neral_set),
            'BBANDS':BBANDS_set(self.click_neral_set),
            'EMA':EMA_set(self.click_neral_set),
            'DEMA':DEMA_set(self.click_neral_set),
            'KAMA':KAMA_set(self.click_neral_set),
            'MAVP':MAVP_set(self.click_neral_set),
            'SAR':SAR_set(self.click_neral_set),
            'TEMA':TEMA_set(self.click_neral_set),
            'TRIMA':TRIMA_set(self.click_neral_set),
            'WMA':WMA_set(self.click_neral_set),
            'CDL2CROWS':CDL2CROWS_set(self.click_neral_set),
            'CDL3BLACKCROWS':CDL3BLACKCROWS_set(self.click_neral_set),
            'CDL3INSIDE':CDL3INSIDE_set(self.click_neral_set),
            'CDL3LINESTRIKE':CDL3LINESTRIKE_set(self.click_neral_set),
            'CDL3OUTSIDE':CDL3OUTSIDE_set(self.click_neral_set),
            'CDL3STARSINSOUTH':CDL3STARSINSOUTH_set(self.click_neral_set),
            'CDL3WHITESOLDIERS':CDL3WHITESOLDIERS_set(self.click_neral_set),
            'CDLABANDONEDBABY':CDLABANDONEDBABY_set(self.click_neral_set),
            'CDLADVANCEBLOCK':CDLADVANCEBLOCK_set(self.click_neral_set),
            'CDLBELTHOLD':CDLBELTHOLD_set(self.click_neral_set),
            'CDLCLOSINGMARUBOZU':CDLCLOSINGMARUBOZU_set(self.click_neral_set),
            'CDLCOUNTERATTACK':CDLCOUNTERATTACK_set(self.click_neral_set),
            'CDLDARKCLOUDCOVER':CDLDARKCLOUDCOVER_set(self.click_neral_set),
            'CDLENGULFING':CDLENGULFING_set(self.click_neral_set),
            'CDLEVENINGDOJISTAR':CDLEVENINGDOJISTAR_set(self.click_neral_set),
            'CDLGRAVESTONEDOJI':CDLGRAVESTONEDOJI_set(self.click_neral_set),
            'CDLHAMMER':CDLHAMMER_set(self.click_neral_set),
            'CDLHANGINGMAN':CDLHANGINGMAN_set(self.click_neral_set),
            'CDLHARAMI':CDLHARAMI_set(self.click_neral_set),
            'CDLHARAMICROSS':CDLHARAMICROSS_set(self.click_neral_set),
            'CDLHOMINGPIGEON':CDLHOMINGPIGEON_set(self.click_neral_set),
            'CDLINVERTEDHAMMER':CDLINVERTEDHAMMER_set(self.click_neral_set),
            'CDLLADDERBOTTOM':CDLLADDERBOTTOM_set(self.click_neral_set),
            'CDLLONGLEGGEDDOJI':CDLLONGLEGGEDDOJI_set(self.click_neral_set),
            'CDLMATCHINGLOW':CDLMATCHINGLOW_set(self.click_neral_set),
            'CDLMORNINGSTAR':CDLMORNINGSTAR_set(self.click_neral_set),
            'CDLRICKSHAWMAN':CDLRICKSHAWMAN_set(self.click_neral_set),
            'CDLSPINNINGTOP':CDLSPINNINGTOP_set(self.click_neral_set),
            'CDLTASUKIGAP':CDLTASUKIGAP_set(self.click_neral_set),
            
            
        }
        self.open_page_get_set = {
            'Общие настройки':Generate_general_set(self.update_page),
            'MA':Generate_MA_set(self.update_page),
            'one':Generate_one_set(self.update_page),
            'BBANDS':Generate_BBANDS_set(self.update_page),
            'EMA':Generate_EMA_set(self.update_page),
            'DEMA':Generate_DEMA_set(self.update_page),
            'KAMA':Generate_KAMA_set(self.update_page),
            'MAVP':Generate_MAVP_set(self.update_page),
            'SAR':Generate_SAR_set(self.update_page),
            'TEMA':Generate_TEMA_set(self.update_page),
            'TRIMA':Generate_TRIMA_set(self.update_page),
            'WMA':Generate_WMA_set(self.update_page),
            'CDL2CROWS':Generate_CDL2CROWS_set(self.update_page),
            'CDL3BLACKCROWS':Generate_CDL3BLACKCROWS_set(self.update_page),
            'CDL3INSIDE':Generate_CDL3INSIDE_set(self.update_page),
            'CDL3LINESTRIKE':Generate_CDL3LINESTRIKE_set(self.update_page),
            'CDL3OUTSIDE':Generate_CDL3OUTSIDE_set(self.update_page),
            'CDL3STARSINSOUTH':Generate_CDL3STARSINSOUTH_set(self.update_page),
            'CDL3WHITESOLDIERS':Generate_CDL3WHITESOLDIERS_set(self.update_page),
            'CDLABANDONEDBABY':Generate_CDLABANDONEDBABY_set(self.update_page),
            'CDLADVANCEBLOCK':Generate_CDLADVANCEBLOCK_set(self.update_page),
            'CDLBELTHOLD':Generate_CDLBELTHOLD_set(self.update_page),
            'CDLCLOSINGMARUBOZU':Generate_CDLCLOSINGMARUBOZU_set(self.update_page),
            'CDLCOUNTERATTACK':Generate_CDLCOUNTERATTACK_set(self.update_page),
            'CDLDARKCLOUDCOVER':Generate_CDLDARKCLOUDCOVER_set(self.update_page),
            'CDLENGULFING':Generate_CDLENGULFING_set(self.update_page),
            'CDLEVENINGDOJISTAR':Generate_CDLEVENINGDOJISTAR_set(self.update_page),
            'CDLGRAVESTONEDOJI':Generate_CDLGRAVESTONEDOJI_set(self.update_page),
            'CDLHAMMER':Generate_CDLHAMMER_set(self.update_page),
            'CDLHANGINGMAN':Generate_CDLHANGINGMAN_set(self.update_page),
            'CDLHARAMI':Generate_CDLHARAMI_set(self.update_page),
            'CDLHARAMICROSS':Generate_CDLHARAMICROSS_set(self.update_page),
            'CDLHOMINGPIGEON':Generate_CDLHOMINGPIGEON_set(self.update_page),
            'CDLINVERTEDHAMMER':Generate_CDLINVERTEDHAMMER_set(self.update_page),
            'CDLLADDERBOTTOM':Generate_CDLLADDERBOTTOM_set(self.update_page),
            'CDLLONGLEGGEDDOJI':Generate_CDLLONGLEGGEDDOJI_set(self.update_page),
            'CDLMATCHINGLOW':Generate_CDLMATCHINGLOW_set(self.update_page),
            'CDLMORNINGSTAR':Generate_CDLMORNINGSTAR_set(self.update_page),
            'CDLRICKSHAWMAN':Generate_CDLRICKSHAWMAN_set(self.update_page),
            'CDLSPINNINGTOP':Generate_CDLSPINNINGTOP_set(self.update_page),
            'CDLTASUKIGAP':Generate_CDLTASUKIGAP_set(self.update_page),
        }

    def update_page(self):
        self.controls = []
        self.controls.append(self.print_page())
        self.update()

    # нажали на кнопку - получить сет в генеральных настройках
    def click_neral_set(self,e):
        self.controls = []
        self.controls.append(self.open_page_get_set[e.control.data])
        self.update()


    def print_page(self):

        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.strategys = literal_eval(config.get('param_trade_historical_trade_svobodniy_freym', 'strategys'))
        
        grid_component = []
        grid_component.append(General_set(self.click_neral_set))
        str_header = ''
        for strat in self.strategys:
            str_header = str_header + self.strategy_translate[strat] + ' | '
            grid_component.append(self.card_set[strat])

        self.regim_set_settings_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text(f'Установка сета настроек для стратегий:\n{str_header}',size=12,color=c_white,text_align='center',),padding=ft.padding.only(left=288,bottom=10)),
                                # ft.Row(controls=grid_component),
                                ft.Container(
                                    ft.GridView(
                                        controls = grid_component,
                                        runs_count=3,
                                        spacing=-140,
                                    ),
                                    width=860,
                                    height=240,
                                    padding = 10,
                                    border=ft.border.all(1,c_white)
                                ),
                                Table_set_print(),
                                ft.Container(
                                    ft.Container(
                                        ft.Row(controls=[
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Назад',size=12,),data='Выбрать режим торговли',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Запустить торговлю',size=12,),data='Запустить торговлю сет',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                    ]),padding=ft.padding.only(left=290,top=10)
                                    ),
                                    width=860,
                                    # height=920
                                )
                            ]),
                            # ],scroll=ft.ScrollMode.ALWAYS),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.regim_set_settings_page

    def build(self):
        return self.print_page()