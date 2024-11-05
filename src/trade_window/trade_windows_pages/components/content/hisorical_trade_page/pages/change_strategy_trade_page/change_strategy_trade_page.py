# страница выбора стратегии торговли
import flet as ft
from variable import *
from imports import *
#1
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_strategy_trade_page.UI.component_info_strat import Component_info_strat
from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config

class Change_strategy_trade_page(ft.UserControl):
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page
        self.strategy_translate = {
            'MIN':'Канал, тренд, локаль, объём',
            'MA':'Скользящие средние',
            'BBANDS':'Полосы Боллинджера',
            'EMA':'Эксп скользящая средняя',
            'DEMA':'Двойная эксп скользящая средняя',
            'KAMA':'Адаптивная скользящая Кауфмана',
            'AMA':'Адаптивная скользящая средняя',
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
            'CDLBREAKAWAY':'Отколовшийся',
            'CDLCLOSINGMARUBOZU':'закрытие Marubozu',
            'CDLCOUNTERATTACK':'Контратака',
            'CDLDARKCLOUDCOVER':'Темный облачный покров',
            'CDLDOJI':'Доджи',
            'CDLDOJISTAR':'Звезда доджи',
            'CDLENGULFING':'шаблон поглощения',
            'CDLEVENINGDOJISTAR':'Вечерняя звезда Доджи',
            'CDLEVENINGSTAR':'Вечерняя звезда',
            'CDLGAPSIDESIDEWHITE':'линии с промежутками вверх/вниз',
            'CDLGRAVESTONEDOJI':'Надгробный камень Доджи',
            'CDLHAMMER':'Молоток',
            'CDLHANGINGMAN':'Висельник',
            'CDLHARAMI':'шаблон Харами',
            'CDLHARAMICROSS':'Шаблон пересечения Харами',
            'CDLHIGHWAVE':'Свеча с высокой волной',
            'CDLHOMINGPIGEON':'Почтовый голубь',
            'CDLINVERTEDHAMMER':'Перевернутый молоток',
            'CDLKICKING':'Пинать ногами',
            'CDLLADDERBOTTOM':'Основание лестницы',
            'CDLLONGLEGGEDDOJI':'Длинноногий доджи',
            'CDLLONGLINE':'Свеча длинной строки',
            'CDLMATCHINGLOW':'низкий уровень соответствия',
            'CDLMORNINGSTAR':'Утренняя звезда',
            'CDLRICKSHAWMAN':'рикша',
            'CDLSPINNINGTOP':'Волчок',
            'CDLSTALLEDPATTERN':'остановленный шаблон',
            'CDLTASUKIGAP':'разрыв Тасуки',
            'CDLTHRUSTING':'шаблон перемещения',
            'CDLUPSIDEGAP2CROWS':'Две вороны',
            
        }
        self.flags_this = {
            'MIN':False,
            'MA':False,
            'BBANDS':False,
            'EMA':False,
            'DEMA':False,
            'KAMA':False,
            'AMA':False,
            'MAVP':False,
            'SAR':False,
            'TEMA':False,
            'TRIMA':False,
            'WMA':False,
            'CDL2CROWS':False,
            'CDL3BLACKCROWS':False,
            'CDL3INSIDE':False,
            'CDL3LINESTRIKE':False,
            'CDL3OUTSIDE':False,
            'CDL3STARSINSOUTH':False,
            'CDL3WHITESOLDIERS':False,
            'CDLABANDONEDBABY':False,
            'CDLADVANCEBLOCK':False,
            'CDLBELTHOLD':False,
            'CDLBREAKAWAY':False,
            'CDLCLOSINGMARUBOZU':False,
            'CDLCOUNTERATTACK':False,
            'CDLDARKCLOUDCOVER':False,
            'CDLDOJI':False,
            'CDLDOJISTAR':False,
            'CDLENGULFING':False,
            'CDLEVENINGDOJISTAR':False,
            'CDLEVENINGSTAR':False,
            'CDLGAPSIDESIDEWHITE':False,
            'CDLGRAVESTONEDOJI':False,
            'CDLHAMMER':False,
            'CDLHANGINGMAN':False,
            'CDLHARAMI':False,
            'CDLHARAMICROSS':False,
            'CDLHIGHWAVE':False,
            'CDLHOMINGPIGEON':False,
            'CDLINVERTEDHAMMER':False,
            'CDLKICKING':False,
            'CDLLADDERBOTTOM':False,
            'CDLLONGLEGGEDDOJI':False,
            'CDLLONGLINE':False,
            'CDLMATCHINGLOW':False,
            'CDLMORNINGSTAR':False,
            'CDLRICKSHAWMAN':False,
            'CDLSPINNINGTOP':False,
            'CDLSTALLEDPATTERN':False,
            'CDLTASUKIGAP':False,
            'CDLTHRUSTING':False,
            'CDLUPSIDEGAP2CROWS':False,
        }
        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        for i in literal_eval(config.get('param_trade_historical_trade_svobodniy_freym', 'strategys')):
            self.flags_this[i] = True
        self.ref_one = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_MA = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_BBANDS = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_DEMA = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_EMA = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_KAMA = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_AMA = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_MAVP = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_SAR = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_TEMA = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_TRIMA = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_WMA = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDL2CROWS = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDL3BLACKCROWS = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDL3INSIDE = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDL3LINESTRIKE = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDL3OUTSIDE = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDL3STARSINSOUTH = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDL3WHITESOLDIERS = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLABANDONEDBABY = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLADVANCEBLOCK = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLBELTHOLD = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLBREAKAWAY = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLCLOSINGMARUBOZU = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLCOUNTERATTACK = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLDARKCLOUDCOVER = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLDOJI = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLDOJISTAR = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLENGULFING = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLEVENINGDOJISTAR = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLEVENINGSTAR = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLGAPSIDESIDEWHITE = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLGRAVESTONEDOJI = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLHAMMER = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLHANGINGMAN = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLHARAMI = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLHARAMICROSS = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLHIGHWAVE = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLHOMINGPIGEON = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLINVERTEDHAMMER = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLKICKING = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLLADDERBOTTOM = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLLONGLEGGEDDOJI = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLLONGLINE = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLMATCHINGLOW = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLMORNINGSTAR = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLRICKSHAWMAN = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLSPINNINGTOP = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLSTALLEDPATTERN = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLTASUKIGAP = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLTHRUSTING = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLUPSIDEGAP2CROWS = ft.Ref[ft.CupertinoCheckbox]()
        self.refs_this = {
            'MIN':self.ref_one,
            'MA':self.ref_MA,
            'BBANDS':self.ref_BBANDS,
            'EMA':self.ref_EMA,
            'DEMA':self.ref_DEMA,
            'KAMA':self.ref_KAMA,
            'AMA':self.ref_AMA,
            'MAVP':self.ref_MAVP,
            'SAR':self.ref_SAR,
            'TEMA':self.ref_TEMA,
            'TRIMA':self.ref_TRIMA,
            'WMA':self.ref_WMA,
            'CDL2CROWS':self.ref_CDL2CROWS,
            'CDL3BLACKCROWS':self.ref_CDL3BLACKCROWS,
            'CDL3INSIDE':self.ref_CDL3INSIDE,
            'CDL3LINESTRIKE':self.ref_CDL3LINESTRIKE,
            'CDL3OUTSIDE':self.ref_CDL3OUTSIDE,
            'CDL3STARSINSOUTH':self.ref_CDL3STARSINSOUTH,
            'CDL3WHITESOLDIERS':self.ref_CDL3WHITESOLDIERS,
            'CDLABANDONEDBABY':self.ref_CDLABANDONEDBABY,
            'CDLADVANCEBLOCK':self.ref_CDLADVANCEBLOCK,
            'CDLBELTHOLD':self.ref_CDLBELTHOLD,
            'CDLBREAKAWAY':self.ref_CDLBREAKAWAY,
            'CDLCLOSINGMARUBOZU':self.ref_CDLCLOSINGMARUBOZU,
            'CDLCOUNTERATTACK':self.ref_CDLCOUNTERATTACK,
            'CDLDARKCLOUDCOVER':self.ref_CDLDARKCLOUDCOVER,
            'CDLDOJI':self.ref_CDLDOJI,
            'CDLDOJISTAR':self.ref_CDLDOJISTAR,
            'CDLENGULFING':self.ref_CDLENGULFING,
            'CDLEVENINGDOJISTAR':self.ref_CDLEVENINGDOJISTAR,
            'CDLEVENINGSTAR':self.ref_CDLEVENINGSTAR,
            'CDLGAPSIDESIDEWHITE':self.ref_CDLGAPSIDESIDEWHITE,
            'CDLGRAVESTONEDOJI':self.ref_CDLGRAVESTONEDOJI,
            'CDLHAMMER':self.ref_CDLHAMMER,
            'CDLHANGINGMAN':self.ref_CDLHANGINGMAN,
            'CDLHARAMI':self.ref_CDLHARAMI,
            'CDLHARAMICROSS':self.ref_CDLHARAMICROSS,
            'CDLHIGHWAVE':self.ref_CDLHIGHWAVE,
            'CDLHOMINGPIGEON':self.ref_CDLHOMINGPIGEON,
            'CDLINVERTEDHAMMER':self.ref_CDLINVERTEDHAMMER,
            'CDLKICKING':self.ref_CDLKICKING,
            'CDLLADDERBOTTOM':self.ref_CDLLADDERBOTTOM,
            'CDLLONGLEGGEDDOJI':self.ref_CDLLONGLEGGEDDOJI,
            'CDLLONGLINE':self.ref_CDLLONGLINE,
            'CDLMATCHINGLOW':self.ref_CDLMATCHINGLOW,
            'CDLMORNINGSTAR':self.ref_CDLMORNINGSTAR,
            'CDLRICKSHAWMAN':self.ref_CDLRICKSHAWMAN,
            'CDLSPINNINGTOP':self.ref_CDLSPINNINGTOP,
            'CDLSTALLEDPATTERN':self.ref_CDLSTALLEDPATTERN,
            'CDLTASUKIGAP':self.ref_CDLTASUKIGAP,
            'CDLTHRUSTING':self.ref_CDLTHRUSTING,
            'CDLUPSIDEGAP2CROWS':self.ref_CDLUPSIDEGAP2CROWS,
        }

    # выбор чекбокса
    def checed_var(self,e):
        # print(e.control.check_color)
        try:
            if e.control.check_color:
                self.change_coin = e.control.data
                if self.flags_this[self.change_coin] == False: # если сейчас 0
                #    e.control.content.controls[0].value=True 
                   self.flags_this[self.change_coin] = True
                else: 
                    # e.control.content.controls[0].value=False 
                    self.flags_this[self.change_coin] = False
            
        except:
            self.change_coin = e.control.content.controls[1].content.data # выбранная стратегия1
            if self.flags_this[e.control.content.controls[1].content.data] == False: # если сейчас 0
               e.control.content.controls[0].value=True 
               self.flags_this[e.control.content.controls[1].content.data] = True
            else: 
                e.control.content.controls[0].value=False 
                self.flags_this[e.control.content.controls[1].content.data] = False
        self.update()
        self.changed_strategys = []
        for i in self.flags_this.keys():
            if self.flags_this[i] == True:
                self.changed_strategys.append(i)
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strategys':str(self.changed_strategys)})
        self.print_info_strategy.update_component()

    # кнопка удаления стратегии в правом окне
    def delete_strat_btn(self,e):
        # print(self.controls[0].content.content.content.controls[1].content.content.controls[0].controls[1].content.controls[0].content.controls)
        for i in self.controls[0].content.content.content.controls[1].content.content.controls[0].controls[1].content.controls[0].content.controls:
            # print(i.data)
            if i.data == e.control.data:
                i.content.controls[0].value=False
        # print(e.control.data)
        self.flags_this[e.control.data] = False
        self.update()
        self.changed_strategys = []
        for i in self.flags_this.keys():
            if self.flags_this[i] == True:
                self.changed_strategys.append(i)
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strategys':str(self.changed_strategys)})
        self.print_info_strategy.update_component()

    def build(self):
        item_strategy = []
        for i in self.strategy_translate.keys():
            item_strategy.append(
                ft.Container(ft.Row(
                    controls=[
                        ft.CupertinoCheckbox(data=i,value=self.flags_this[i],check_color=c_blue,active_color=c_yelow,inactive_color=c_white,ref=self.refs_this[i],on_change=self.checed_var),
                        ft.Container(ft.Text(self.strategy_translate[i],color=c_white,data=i),margin = ft.margin.only(left=-15))
                    ]),on_click=self.checed_var,padding=ft.padding.only(bottom=-10,top=-10),width=300,data=i))

        self.print_info_strategy = Component_info_strat(self.delete_strat_btn)

        self.change_strategy_trade_page = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text('Выберите одну или несколько стратегий реальной тестовой торговли',
                                        size=12,color=c_white,text_align='center',),padding=ft.padding.only(left=230)),
                                ft.Container(
                                    ft.Container(
                                        ft.Column(controls=[
                                            ft.Column(
                                                controls=[
                                                    ft.Container(
                                                        ft.Container(ft.Text('Выбор стратегии',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white))),
                                                    ft.Container(
                                                        ft.Row(controls=[
                                                            ft.Container(
                                                                ft.Column(controls=item_strategy,scroll=ft.ScrollMode.ALWAYS,height=440),
                                                                width=300,
                                                                border = ft.border.all(1, c_white),
                                                                padding=ft.padding.only(left=10,top=20),
                                                            ),
                                                            ft.Container(
                                                                ft.Column(controls=[self.print_info_strategy,],scroll=ft.ScrollMode.ALWAYS),
                                                                width=560,
                                                                height = 460,
                                                                border = ft.border.all(1, c_white),
                                                                padding=ft.padding.only(left=10,top=20),
                                                                margin=ft.margin.only(left=-11)
                                                            ),
                                                        ]), 
                                                        width=860,
                                                        border = ft.border.all(1, c_white),
                                                        # padding=14,
                                                        height = 460,
                                                        padding=ft.padding.only(left=-1,top=-1,bottom=-1)
                                                        
                                            )]),     
                                    ])),
                                    width=860,
                                ),
                                ft.Container(
                                    ft.Container(
                                        ft.Row(controls=[
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Назад',size=12,),data='Настройки робота',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                        ft.Container(ft.ElevatedButton(content = ft.Text('Выбрать режим торговли',size=12,),data='Выбрать режим торговли',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30),
                                    ]),padding=ft.padding.only(left=290,top=10)
                                    ),
                                    width=860,
                                    # height=920
                                )
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.change_strategy_trade_page