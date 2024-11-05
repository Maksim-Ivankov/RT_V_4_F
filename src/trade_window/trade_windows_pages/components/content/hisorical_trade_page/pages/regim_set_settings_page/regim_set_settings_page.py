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

class Regim_set_settings_page(ft.UserControl):
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page
        self.strategy_translate = {
            'one':'Канал, тренд, локаль, объём',
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
            'CDLENGULFING':'Шаблон поглощения',
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
            'CDLMATCHINGLOW':'Низкий уровень соответствия',
            'CDLMORNINGSTAR':'Утренняя звезда',
            'CDLRICKSHAWMAN':'Рикша',
            'CDLSPINNINGTOP':'Волчок',
            'CDLTASUKIGAP':'Разрыв Тасуки',
        }
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