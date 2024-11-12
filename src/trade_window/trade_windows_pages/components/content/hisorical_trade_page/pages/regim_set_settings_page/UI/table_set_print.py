# страница выбора стратегии торговли1
import flet as ft
from variable import *
from imports import *

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.general_table import General_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.MA_table import MA_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.one_table import One_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.BBANDS_table import BBANDS_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.EMA_table import EMA_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.DEMA_table import DEMA_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.KAMA_table import KAMA_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.MAVP_table import MAVP_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.SAR_table import SAR_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.TEMA_table import TEMA_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.TRIMA_table import TRIMA_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.WMA_table import WMA_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDL2CROWS_table import CDL2CROWS_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDL3BLACKCROWS_table import CDL3BLACKCROWS_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDL3INSIDE_table import CDL3INSIDE_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDL3LINESTRIKE_table import CDL3LINESTRIKE_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDL3OUTSIDE_table import CDL3OUTSIDE_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDL3STARSINSOUTH_table import CDL3STARSINSOUTH_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDL3WHITESOLDIERS_table import CDL3WHITESOLDIERS_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDLABANDONEDBABY_table import CDLABANDONEDBABY_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDLADVANCEBLOCK_table import CDLADVANCEBLOCK_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDLBELTHOLD_table import CDLBELTHOLD_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDLCLOSINGMARUBOZU_table import CDLCLOSINGMARUBOZU_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDLCOUNTERATTACK_table import CDLCOUNTERATTACK_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDLDARKCLOUDCOVER_table import CDLDARKCLOUDCOVER_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDLENGULFING_table import CDLENGULFING_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDLEVENINGDOJISTAR_table import CDLEVENINGDOJISTAR_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDLGRAVESTONEDOJI_table import CDLGRAVESTONEDOJI_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDLHAMMER_table import CDLHAMMER_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDLHANGINGMAN_table import CDLHANGINGMAN_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDLHARAMI_table import CDLHARAMI_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDLHARAMICROSS_table import CDLHARAMICROSS_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDLHOMINGPIGEON_table import CDLHOMINGPIGEON_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDLINVERTEDHAMMER_table import CDLINVERTEDHAMMER_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDLLADDERBOTTOM_table import CDLLADDERBOTTOM_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDLLONGLEGGEDDOJI_table import CDLLONGLEGGEDDOJI_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDLMATCHINGLOW_table import CDLMATCHINGLOW_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDLMORNINGSTAR_table import CDLMORNINGSTAR_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDLRICKSHAWMAN_table import CDLRICKSHAWMAN_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDLSPINNINGTOP_table import CDLSPINNINGTOP_table
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_set_settings_page.table_data.CDLTASUKIGAP_table import CDLTASUKIGAP_table

class Table_set_print(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.strategy_translate = strategys_our
        self.strategy_component = {
            'general':General_table(),
            'one':MA_table(),
            'MA':One_table(),
            'BBANDS':BBANDS_table(),
            'EMA':EMA_table(),
            'DEMA':DEMA_table(),
            'KAMA':KAMA_table(),
            'MAVP':MAVP_table(),
            'SAR':SAR_table(),
            'TEMA':TEMA_table(),
            'TRIMA':TRIMA_table(),
            'WMA':WMA_table(),
            'CDL2CROWS':CDL2CROWS_table(),
            'CDL3BLACKCROWS':CDL3BLACKCROWS_table(),
            'CDL3INSIDE':CDL3INSIDE_table(),
            'CDL3LINESTRIKE':CDL3LINESTRIKE_table(),
            'CDL3OUTSIDE':CDL3OUTSIDE_table(),
            'CDL3STARSINSOUTH':CDL3STARSINSOUTH_table(),
            'CDL3WHITESOLDIERS':CDL3WHITESOLDIERS_table(),
            'CDLABANDONEDBABY':CDLABANDONEDBABY_table(),
            'CDLADVANCEBLOCK':CDLADVANCEBLOCK_table(),
            'CDLBELTHOLD':CDLBELTHOLD_table(),
            'CDLCLOSINGMARUBOZU':CDLCLOSINGMARUBOZU_table(),
            'CDLCOUNTERATTACK':CDLCOUNTERATTACK_table(),
            'CDLDARKCLOUDCOVER':CDLDARKCLOUDCOVER_table(),
            'CDLENGULFING':CDLENGULFING_table(),
            'CDLEVENINGDOJISTAR':CDLEVENINGDOJISTAR_table(),
            'CDLGRAVESTONEDOJI':CDLGRAVESTONEDOJI_table(),
            'CDLHAMMER':CDLHAMMER_table(),
            'CDLHANGINGMAN':CDLHANGINGMAN_table(),
            'CDLHARAMI':CDLHARAMI_table(),
            'CDLHARAMICROSS':CDLHARAMICROSS_table(),
            'CDLHOMINGPIGEON':CDLHOMINGPIGEON_table(),
            'CDLINVERTEDHAMMER':CDLINVERTEDHAMMER_table(),
            'CDLLADDERBOTTOM':CDLLADDERBOTTOM_table(),
            'CDLLONGLEGGEDDOJI':CDLLONGLEGGEDDOJI_table(),
            'CDLMATCHINGLOW':CDLMATCHINGLOW_table(),
            'CDLMORNINGSTAR':CDLMORNINGSTAR_table(),
            'CDLRICKSHAWMAN':CDLRICKSHAWMAN_table(),
            'CDLSPINNINGTOP':CDLSPINNINGTOP_table(),
            'CDLTASUKIGAP':CDLTASUKIGAP_table(),
        }
        self.strategy_translate_checked = 'general'
        self.strategy_translate['general'] = 'Общие настройки'
        

    def checked_menu_table(self,e):
        self.strategy_translate_checked = e.control.data
        self.controls = []
        self.controls.append(self.print_page())
        self.update()

    def print_page(self):

        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.strategys = literal_eval(config.get('param_trade_historical_trade_svobodniy_freym', 'strategys'))
        self.strategys.insert(0,'general')

        data_menu_mas = []
        data_menu_mas.append(ft.Container(ft.Container(ft.Text('Сет настроек',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))))
        for i in self.strategys:
            if i == self.strategy_translate_checked:
                data_menu_mas.append(ft.Container(ft.Container(ft.Text(self.strategy_translate[i],color=c_yelow,),bgcolor=c_blue,padding=5,margin=ft.margin.only(bottom=-10)),data=i,on_click=self.checked_menu_table))
                # data_menu_mas.append(ft.Container(ft.Container(ft.Text(self.strategy_translate[i],color=c_yelow,),bgcolor=c_blue,padding=5,margin=ft.margin.only(bottom=-10)),data=i,on_click=self.checked_menu_table))
            else:
                data_menu_mas.append(ft.Container(ft.Container(ft.Text(self.strategy_translate[i],color=c_white,),bgcolor=c_blue,padding=5,margin=ft.margin.only(bottom=-10)),data=i,on_click=self.checked_menu_table))


        self.table_set_print = ft.Container(
            ft.Container(
                ft.Column(controls=[
                    ft.Column(
                        controls=[
                            ft.Row(controls=data_menu_mas),
                            ft.Container(
                                self.strategy_component[self.strategy_translate_checked],
                                width=860,
                                border = ft.border.only(right=ft.border.BorderSide(1, c_white),left=ft.border.BorderSide(1, c_white),top=ft.border.BorderSide(1, c_white),bottom=ft.border.BorderSide(1, c_white)),
                                height = 210,
                                
                    )]),     
            ])),
            width=860,
        )
        
        return self.table_set_print

    def build(self):
        return self.print_page()