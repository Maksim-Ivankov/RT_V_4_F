# страница выбора стратегии торговли
import flet as ft
from variable import *
from imports import *
#121
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_strategy_trade_page.UI.component_info_strat import Component_info_strat
from src.trade_window.trade_windows_pages.components.content.hisorical_trade_page.pages.change_strategy_trade_page.UI.print_info_strategy_component import Print_info_strategy_component
from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config

class Change_strategy_trade_page(ft.UserControl):
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page
        self.strategy_translate = strategys_our
        self.flags_this = {}
        for i in mas_name_strategys:
            self.flags_this[i] = False
        config = configparser.ConfigParser()         
        config.read(path_imports_config)
        for i in literal_eval(config.get('param_trade_historical_trade_svobodniy_freym', 'strategys')):
            self.flags_this[i] = True
        self.regime_trade_page = config.get('param_trade_historical_trade_svobodniy_freym', 'regime_trade_page')
        self.ref_one = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_MA = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_BBANDS = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_DEMA = ft.Ref[ft.CupertinoCheckbox]()            # даёт ноль
        self.ref_EMA = ft.Ref[ft.CupertinoCheckbox]()         # даёт ноль
        self.ref_KAMA = ft.Ref[ft.CupertinoCheckbox]()            # даёт ноль
        self.ref_MAVP = ft.Ref[ft.CupertinoCheckbox]()            # даёт ноль
        self.ref_SAR = ft.Ref[ft.CupertinoCheckbox]()         # даёт ноль
        self.ref_TEMA = ft.Ref[ft.CupertinoCheckbox]()            # даёт ноль
        self.ref_TRIMA = ft.Ref[ft.CupertinoCheckbox]()           # даёт ноль
        self.ref_WMA = ft.Ref[ft.CupertinoCheckbox]()         # даёт ноль
        self.ref_CDL2CROWS = ft.Ref[ft.CupertinoCheckbox]()           # даёт ноль
        self.ref_CDL3BLACKCROWS = ft.Ref[ft.CupertinoCheckbox]()          # даёт ноль
        self.ref_CDL3INSIDE = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDL3LINESTRIKE = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDL3OUTSIDE = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDL3STARSINSOUTH = ft.Ref[ft.CupertinoCheckbox]()            # даёт ноль
        self.ref_CDL3WHITESOLDIERS = ft.Ref[ft.CupertinoCheckbox]()           # даёт ноль
        self.ref_CDLABANDONEDBABY = ft.Ref[ft.CupertinoCheckbox]()            # даёт ноль
        self.ref_CDLADVANCEBLOCK = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLBELTHOLD = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLCLOSINGMARUBOZU = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLCOUNTERATTACK = ft.Ref[ft.CupertinoCheckbox]()            # даёт ноль
        self.ref_CDLDARKCLOUDCOVER = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLENGULFING = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLEVENINGDOJISTAR = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLGRAVESTONEDOJI = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLHAMMER = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLHANGINGMAN = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLHARAMI = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLHARAMICROSS = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLHOMINGPIGEON = ft.Ref[ft.CupertinoCheckbox]()         # даёт ноль
        self.ref_CDLINVERTEDHAMMER = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLLADDERBOTTOM = ft.Ref[ft.CupertinoCheckbox]()         # даёт ноль
        self.ref_CDLLONGLEGGEDDOJI = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLMATCHINGLOW = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLMORNINGSTAR = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLRICKSHAWMAN = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLSPINNINGTOP = ft.Ref[ft.CupertinoCheckbox]()
        self.ref_CDLTASUKIGAP = ft.Ref[ft.CupertinoCheckbox]()            # даёт ноль
        self.refs_this = {
            'one':self.ref_one,
            'MA':self.ref_MA,
            'BBANDS':self.ref_BBANDS,
            'EMA':self.ref_EMA,           # даёт ноль
            'DEMA':self.ref_DEMA,         # даёт ноль
            'KAMA':self.ref_KAMA,         # даёт ноль
            'MAVP':self.ref_MAVP,         # даёт ноль
            'SAR':self.ref_SAR,           # даёт ноль
            'TEMA':self.ref_TEMA,         # даёт ноль
            'TRIMA':self.ref_TRIMA,           # даёт ноль
            'WMA':self.ref_WMA,           # даёт ноль
            'CDL2CROWS':self.ref_CDL2CROWS,           # даёт ноль
            'CDL3BLACKCROWS':self.ref_CDL3BLACKCROWS,         # даёт ноль
            'CDL3INSIDE':self.ref_CDL3INSIDE,
            'CDL3LINESTRIKE':self.ref_CDL3LINESTRIKE,
            'CDL3OUTSIDE':self.ref_CDL3OUTSIDE,
            'CDL3STARSINSOUTH':self.ref_CDL3STARSINSOUTH,         # даёт ноль
            'CDL3WHITESOLDIERS':self.ref_CDL3WHITESOLDIERS,           # даёт ноль
            'CDLABANDONEDBABY':self.ref_CDLABANDONEDBABY,         # даёт ноль
            'CDLADVANCEBLOCK':self.ref_CDLADVANCEBLOCK,
            'CDLBELTHOLD':self.ref_CDLBELTHOLD,
            'CDLCLOSINGMARUBOZU':self.ref_CDLCLOSINGMARUBOZU,
            'CDLCOUNTERATTACK':self.ref_CDLCOUNTERATTACK,         # даёт ноль
            'CDLDARKCLOUDCOVER':self.ref_CDLDARKCLOUDCOVER,
            'CDLENGULFING':self.ref_CDLENGULFING,
            'CDLEVENINGDOJISTAR':self.ref_CDLEVENINGDOJISTAR,
            'CDLGRAVESTONEDOJI':self.ref_CDLGRAVESTONEDOJI,
            'CDLHAMMER':self.ref_CDLHAMMER,
            'CDLHANGINGMAN':self.ref_CDLHANGINGMAN,
            'CDLHARAMI':self.ref_CDLHARAMI,
            'CDLHARAMICROSS':self.ref_CDLHARAMICROSS,
            'CDLHOMINGPIGEON':self.ref_CDLHOMINGPIGEON,           # даёт ноль
            'CDLINVERTEDHAMMER':self.ref_CDLINVERTEDHAMMER,
            'CDLLADDERBOTTOM':self.ref_CDLLADDERBOTTOM,           # даёт ноль
            'CDLLONGLEGGEDDOJI':self.ref_CDLLONGLEGGEDDOJI,
            'CDLMATCHINGLOW':self.ref_CDLMATCHINGLOW,
            'CDLMORNINGSTAR':self.ref_CDLMORNINGSTAR,
            'CDLRICKSHAWMAN':self.ref_CDLRICKSHAWMAN,
            'CDLSPINNINGTOP':self.ref_CDLSPINNINGTOP,
            'CDLTASUKIGAP':self.ref_CDLTASUKIGAP,         # даёт ноль
        }
        self.print_info_strategy_component = Print_info_strategy_component()

    # выбор чекбокса
    def checed_var(self,e):
        # print(self.controls[0].content.content.content.controls[1].content.content.controls[0].controls[1].content.controls[1].content.controls)
        try:
            if e.control.check_color:
                self.change_coin = e.control.data
                if self.flags_this[self.change_coin] == False: # если сейчас 0
                   self.flags_this[self.change_coin] = True
                   self.controls[0].content.content.content.controls[1].content.content.controls[0].controls[1].content.controls[1].content.controls.pop()
                   self.controls[0].content.content.content.controls[1].content.content.controls[0].controls[1].content.controls[1].content.controls.append(self.print_info_strategy_component.print_component(self.change_coin))
                else: 
                    self.flags_this[self.change_coin] = False
                    self.controls[0].content.content.content.controls[1].content.content.controls[0].controls[1].content.controls[1].content.controls.pop()
                    self.controls[0].content.content.content.controls[1].content.content.controls[0].controls[1].content.controls[1].content.controls.append(self.print_info_strategy_component.print_component(self.changed_strategys[0]))
            
        except:
            self.change_coin = e.control.content.controls[1].content.data # выбранная стратегия1
            if self.flags_this[e.control.content.controls[1].content.data] == False: # если сейчас 0
                e.control.content.controls[0].value=True 
                self.flags_this[e.control.content.controls[1].content.data] = True
                self.controls[0].content.content.content.controls[1].content.content.controls[0].controls[1].content.controls[1].content.controls.pop()
                self.controls[0].content.content.content.controls[1].content.content.controls[0].controls[1].content.controls[1].content.controls.append(self.print_info_strategy_component.print_component(self.change_coin))
            else: 
                e.control.content.controls[0].value=False 
                self.flags_this[e.control.content.controls[1].content.data] = False
                self.controls[0].content.content.content.controls[1].content.content.controls[0].controls[1].content.controls[1].content.controls.pop()
                self.controls[0].content.content.content.controls[1].content.content.controls[0].controls[1].content.controls[1].content.controls.append(self.print_info_strategy_component.print_component(self.changed_strategys[0]))
        self.update()
        self.changed_strategys = []
        for i in self.flags_this.keys():
            if self.flags_this[i] == True:
                self.changed_strategys.append(i)
        Save_config('param_trade_historical_trade_svobodniy_freym',{'strategys':str(self.changed_strategys)})
        self.print_info_strategy.update_component()
        if len(self.changed_strategys) == 0:
            self.controls[0].content.content.content.controls[1].content.content.controls[0].controls[1].content.controls[1].content.controls.pop()
            self.controls[0].content.content.content.controls[1].content.content.controls[0].controls[1].content.controls[1].content.controls.append(self.print_info_strategy_component)
            self.update()

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
        if len(self.changed_strategys) == 0:
            self.controls[0].content.content.content.controls[1].content.content.controls[0].controls[1].content.controls[1].content.controls.pop()
            self.controls[0].content.content.content.controls[1].content.content.controls[0].controls[1].content.controls[1].content.controls.append(self.print_info_strategy_component)
            self.update()
        
    def open_strat_btn(self,e):
        self.controls[0].content.content.content.controls[1].content.content.controls[0].controls[1].content.controls[1].content.controls.pop()
        self.controls[0].content.content.content.controls[1].content.content.controls[0].controls[1].content.controls[1].content.controls.append(self.print_info_strategy_component.print_component(e.control.data))
        self.update()

    def build(self):
        self.changed_strategys = []
        for i in self.flags_this.keys():
            if i=='general': continue
            if self.flags_this[i] == True:
                self.changed_strategys.append(i)
        item_strategy = []
        for i in self.strategy_translate.keys():
            if i=='general': continue
            item_strategy.append(
                ft.Container(ft.Row(
                    controls=[
                        ft.CupertinoCheckbox(data=i,value=self.flags_this[i],check_color=c_blue,active_color=c_yelow,inactive_color=c_white,ref=self.refs_this[i],on_change=self.checed_var),
                        ft.Container(ft.Text(self.strategy_translate[i],color=c_white,data=i),margin = ft.margin.only(left=-15))
                    ]),on_click=self.checed_var,padding=ft.padding.only(bottom=-10,top=-10),width=300,data=i))

        self.print_info_strategy = Component_info_strat(self.delete_strat_btn,self.open_strat_btn)

        if self.regime_trade_page == 'svoboda':
            btn_continue = ft.Container(ft.ElevatedButton(content = ft.Text('Выбрать режим торговли',size=12,),data='Выбрать режим торговли',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30)
        elif self.regime_trade_page == 'historical':
            btn_continue = ft.Container(ft.ElevatedButton(content = ft.Text('Настроить стратгии',size=12,),data='Одна настройка',bgcolor=c_yelow,on_click=self.change_page,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30)

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
                                                                ft.Column(controls=[
                                                                    self.print_info_strategy,
                                                                    ft.Container(height=1,bgcolor=c_yelow),
                                                                    self.print_info_strategy_component,
                                                                    ]),
                                                                    # ],scroll=ft.ScrollMode.ALWAYS),
                                                                width=560,
                                                                height = 460,
                                                                border = ft.border.all(1, c_white),
                                                                padding=ft.padding.only(left=10,top=20,right=10,bottom=20),
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
                                        btn_continue,
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