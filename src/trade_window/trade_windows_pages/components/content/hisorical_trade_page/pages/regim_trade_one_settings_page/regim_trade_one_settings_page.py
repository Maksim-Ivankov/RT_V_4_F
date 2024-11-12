# страница выбора стратегии торговли
import flet as ft
from variable import *
from imports import *
#122
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_strategy_trade_page.UI.component_info_strat import Component_info_strat
from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config

from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.MA import MA
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.one import One
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.BBANDS import BBANDS
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.EMA import EMA
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.DEMA import DEMA
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.KAMA import KAMA
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.MAVP import MAVP
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.SAR import SAR
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.TEMA import TEMA
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.TRIMA import TRIMA
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.WMA import WMA
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDL2CROWS import CDL2CROWS
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDL3BLACKCROWS import CDL3BLACKCROWS
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDL3INSIDE import CDL3INSIDE
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDL3LINESTRIKE import CDL3LINESTRIKE
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDL3OUTSIDE import CDL3OUTSIDE
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDL3STARSINSOUTH import CDL3STARSINSOUTH
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDL3WHITESOLDIERS import CDL3WHITESOLDIERS
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDLABANDONEDBABY import CDLABANDONEDBABY
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDLADVANCEBLOCK import CDLADVANCEBLOCK
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDLBELTHOLD import CDLBELTHOLD
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDLCLOSINGMARUBOZU import CDLCLOSINGMARUBOZU
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDLCOUNTERATTACK import CDLCOUNTERATTACK
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDLDARKCLOUDCOVER import CDLDARKCLOUDCOVER
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDLENGULFING import CDLENGULFING
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDLEVENINGDOJISTAR import CDLEVENINGDOJISTAR
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDLGRAVESTONEDOJI import CDLGRAVESTONEDOJI
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDLHAMMER import CDLHAMMER
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDLHANGINGMAN import CDLHANGINGMAN
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDLHARAMI import CDLHARAMI
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDLHARAMICROSS import CDLHARAMICROSS
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDLHOMINGPIGEON import CDLHOMINGPIGEON
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDLINVERTEDHAMMER import CDLINVERTEDHAMMER
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDLLADDERBOTTOM import CDLLADDERBOTTOM
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDLLONGLEGGEDDOJI import CDLLONGLEGGEDDOJI
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDLMATCHINGLOW import CDLMATCHINGLOW
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDLMORNINGSTAR import CDLMORNINGSTAR
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDLRICKSHAWMAN import CDLRICKSHAWMAN
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDLSPINNINGTOP import CDLSPINNINGTOP
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.regim_trade_one_settings_page.strategys_settings.CDLTASUKIGAP import CDLTASUKIGAP


#1

class Regim_trade_one_settings_page(ft.UserControl):
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page
        self.strategy_translate = strategys_our
        self.strategy_print = {
            'one':One(),
            'MA':MA(),
            'BBANDS':BBANDS(),
            'EMA':EMA(),
            'DEMA':DEMA(),
            'KAMA':KAMA(),
            'MAVP':MAVP(),
            'SAR':SAR(),
            'TEMA':TEMA(),
            'TRIMA':TRIMA(),
            'WMA':WMA(),
            'CDL2CROWS':CDL2CROWS(),
            'CDL3BLACKCROWS':CDL3BLACKCROWS(),
            'CDL3INSIDE':CDL3INSIDE(),
            'CDL3LINESTRIKE':CDL3LINESTRIKE(),
            'CDL3OUTSIDE':CDL3OUTSIDE(),
            'CDL3STARSINSOUTH':CDL3STARSINSOUTH(),
            'CDL3WHITESOLDIERS':CDL3WHITESOLDIERS(),
            'CDLABANDONEDBABY':CDLABANDONEDBABY(),
            'CDLADVANCEBLOCK':CDLADVANCEBLOCK(),
            'CDLBELTHOLD':CDLBELTHOLD(),
            'CDLCLOSINGMARUBOZU':CDLCLOSINGMARUBOZU(),
            'CDLCOUNTERATTACK':CDLCOUNTERATTACK(),
            'CDLDARKCLOUDCOVER':CDLDARKCLOUDCOVER(),
            'CDLENGULFING':CDLENGULFING(),
            'CDLEVENINGDOJISTAR':CDLEVENINGDOJISTAR(),
            'CDLGRAVESTONEDOJI':CDLGRAVESTONEDOJI(),
            'CDLHAMMER':CDLHAMMER(),
            'CDLHANGINGMAN':CDLHANGINGMAN(),
            'CDLHARAMI':CDLHARAMI(),
            'CDLHARAMICROSS':CDLHARAMICROSS(),
            'CDLHOMINGPIGEON':CDLHOMINGPIGEON(),
            'CDLINVERTEDHAMMER':CDLINVERTEDHAMMER(),
            'CDLLADDERBOTTOM':CDLLADDERBOTTOM(),
            'CDLLONGLEGGEDDOJI':CDLLONGLEGGEDDOJI(),
            'CDLMATCHINGLOW':CDLMATCHINGLOW(),
            'CDLMORNINGSTAR':CDLMORNINGSTAR(),
            'CDLRICKSHAWMAN':CDLRICKSHAWMAN(),
            'CDLSPINNINGTOP':CDLSPINNINGTOP(),
            'CDLTASUKIGAP':CDLTASUKIGAP(),
        }


    def build(self):

        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        self.strategys = literal_eval(config.get('param_trade_historical_trade_svobodniy_freym', 'strategys'))
        
        strat_mas = []
        for strat in self.strategys:
            strat_mas.append(self.strategy_print[strat])

        self.regim_trade_one_settings_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text('Настройте выбранные ранее стратегии',size=12,color=c_white,text_align='center',),padding=ft.padding.only(left=310,bottom=14)),
                                ft.Container(ft.Column(controls=strat_mas,scroll=ft.ScrollMode.ALWAYS),height=500),
                                ft.Container(
                                    ft.Container(
                                        ft.Row(controls=[
                                            ft.Container(ft.ElevatedButton(content = ft.Text('Назад',size=12,),data='Выбрать режим торговли',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('Запустить торговлю',size=12,),data='Запустить торговлю',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                    ]),padding=ft.padding.only(left=290,top=10)
                                    ),
                                    width=860,
                                    # height=920
                                )
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)
                    ),expand=2
        )
        
        return self.regim_trade_one_settings_page