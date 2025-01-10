
# from src.trade_window.trade_windows_pages.components.content.controllers.save_config import Save_config
import configparser

# Работа с директорией
APPNAME = "RoboTrade"
import sys
import os
if sys.platform == 'darwin':
    # from AppKit import NSSearchPathForDirectoriesInDomains
    # # http://developer.apple.com/DOCUMENTATION/Cocoa/Reference/Foundation/Miscellaneous/Foundation_Functions/Reference/reference.html#//apple_ref/c/func/NSSearchPathForDirectoriesInDomains
    # # NSApplicationSupportDirectory = 14
    # # NSUserDomainMask = 1
    # # True for expanding the tilde into a fully qualified path
    # appdata = path.join(NSSearchPathForDirectoriesInDomains(14, 1, True)[0], APPNAME)
    print('СДЕЛАТЬ ПОЗЖЕ ЛОКАЛИЗАЦИЮ ПОД MACOS')
elif sys.platform == 'win32':
    appdata = os.path.join(os.environ['APPDATA'], APPNAME)

# если в системном пути нет папки проекта, то создаем ее
if os.path.isdir(appdata) == False:
    os.makedirs(appdata)
    os.mkdir(f'{appdata}\\trade')
    os.mkdir(f'{appdata}\\favorites')
    os.mkdir(f'{appdata}\\historical_freym')
    os.mkdir(f'{appdata}\\svoboda_freym')
    print('Папки созданы')
    # теперь создаём файлы конфигурации с дефолтными значениями
    # config.ini
    config = configparser.ConfigParser()
    config.add_section('user')
    config.add_section('Binance_key')
    config.add_section('OKX_key')
    config.add_section('BiBit_key')
    config.add_section('Telegram_key')
    config.add_section('Birga_trade')
    config.add_section('settings_program')
    config.add_section('Proxi')
    config.add_section('param_trade_historical_trade_svobodniy_freym')
    config.set('user', 'email', '')
    config.set('user', 'password', '')
    config.set('user', 'apikey', '')
    config.set('Binance_key', 'api_key', '')
    config.set('Binance_key', 'secret_key', '')
    config.set('OKX_key', 'api_key', '')
    config.set('OKX_key', 'secret_key', '')
    config.set('BiBit_key', 'api_key', '')
    config.set('BiBit_key', 'secret_key', '')
    config.set('Telegram_key', 'api_key', 'ergerg342ergrwewef2f3f2qw')
    config.set('Telegram_key', 'id_group', 'werg34g34gwefwefwefwefqw')
    config.set('Birga_trade', 'birga_trade', 'Binance')
    config.set('settings_program', 'thema', 'Dark')
    config.set('settings_program', 'count_coin', '30')
    config.set('settings_program', 'regime_tree_map', 'Trading_volume')
    config.set('Proxi', 'addres', '')
    config.set('Proxi', 'port', '')
    config.set('Proxi', 'status', 'off')
    config.set('param_trade_historical_trade_svobodniy_freym', 'regime_trade_page','historical')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strategi_coin','top_dvigeniya')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strategi_coin_historical','change_list')
    config.set('param_trade_historical_trade_svobodniy_freym', 'sledim_money','1m')
    config.set('param_trade_historical_trade_svobodniy_freym', 'work_tf','5m')
    config.set('param_trade_historical_trade_svobodniy_freym', 'dlitelnost','24h')
    config.set('param_trade_historical_trade_svobodniy_freym', 'how_mach_money','10')
    config.set('param_trade_historical_trade_svobodniy_freym', 'coins_trade','')
    config.set('param_trade_historical_trade_svobodniy_freym', 'number_trade','0')
    config.set('param_trade_historical_trade_svobodniy_freym', 'number_trade_historical','0')
    config.set('param_trade_historical_trade_svobodniy_freym', 'use_last_sost','False')
    config.set('param_trade_historical_trade_svobodniy_freym', 'use_last_number','')
    config.set('param_trade_historical_trade_svobodniy_freym', 'use_last_sost_historical','False')
    config.set('param_trade_historical_trade_svobodniy_freym', 'use_last_number_historical','')
    config.set('param_trade_historical_trade_svobodniy_freym', 'regim_tp','fiks')
    config.set('param_trade_historical_trade_svobodniy_freym', 'regim_sl','fiks')
    config.set('param_trade_historical_trade_svobodniy_freym', 'regim_volume_min','fiks')
    config.set('param_trade_historical_trade_svobodniy_freym', 'regim_volume_max','fiks')
    config.set('param_trade_historical_trade_svobodniy_freym', 'name_bot','V_1')
    config.set('param_trade_historical_trade_svobodniy_freym', 'komission_mayker','0.07')
    config.set('param_trade_historical_trade_svobodniy_freym', 'deposit','100')
    config.set('param_trade_historical_trade_svobodniy_freym', 'leverage','20')
    config.set('param_trade_historical_trade_svobodniy_freym', 'komission_taker','0.07')
    config.set('param_trade_historical_trade_svobodniy_freym', 'tp','0.9')
    config.set('param_trade_historical_trade_svobodniy_freym', 'sl','0.4')
    config.set('param_trade_historical_trade_svobodniy_freym', 'volume_min','2000')
    config.set('param_trade_historical_trade_svobodniy_freym', 'volume_max','50000000')
    config.set('param_trade_historical_trade_svobodniy_freym', 'change_time_settings','0')
    config.set('param_trade_historical_trade_svobodniy_freym', 'time_on_work','6')
    config.set('param_trade_historical_trade_svobodniy_freym', 'time_off_work','18')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strategys','[]')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_one_up_chanal','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_one_down_chanal','30')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_one_corner_long','30')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_one_corner_short','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_ma_koef_bistro','3')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_ma_koef_medleno','15')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_ma_sovpad_last','2')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_ma_up_chanal','0.75')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_ma_down_chanal','0.30')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_bbands_timeperiod','5.0')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_bbands_nbdevup','3.0')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_bbands_nbdevdn','2.0')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_bbands_matype','0.0')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlabandonedbaby_penetration','0.3')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdldarkcloudcover_penetration','0.5')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdleveningdojistar_penetration','0.3')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlmorningstar_penetration','0.3')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_dema_timeperiod','30')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_ema_timeperiod','30')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_kama_timeperiod','30')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_mavp_minperiod','2')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_mavp_maxperiod','30')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_mavp_matype','0')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_sar_acceleration','0.02')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_tema_timeperiod','30')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_trima_timeperiod','30')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_wma_timeperiod','30')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_sar_maximum','0.2')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdl2crows_long','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdl2crows_short','-70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdl3blackcrows_long','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdl3blackcrows_short','-70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdl3inside_long','90')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdl3inside_short','-90')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdl3linestrike_long','90')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdl3linestrike_short','-80')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdl3outside_long','65')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdl3outside_short','-60')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdl3starsinsouth_long','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdl3starsinsouth_short','-70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdl3whitesoldiers_long','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdl3whitesoldiers_short','-70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlabandonedbaby_long','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlabandonedbaby_short','-70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdladvanceblock_long','90')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdladvanceblock_short','-85')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlbelthold_long','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlbelthold_short','-70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlclosingmarubozu_long','80')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlclosingmarubozu_short','-70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlcounterattack_long','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlcounterattack_short','-70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdldarkcloudcover_long','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdldarkcloudcover_short','-70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlengulfing_long','75')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlengulfing_short','-80')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdleveningdojistar_long','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdleveningdojistar_short','-70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlgravestonedoji_long','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlgravestonedoji_short','-70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlhammer_long','70.0')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlhammer_short','-70.0')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlhangingman_long','70.0')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlhangingman_short','-70.0')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlharami_long','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlharami_short','-70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlharamicross_long','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlharamicross_short','-70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlhomingpigeon_long','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlhomingpigeon_short','-70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlinvertedhammer_long','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlinvertedhammer_short','-70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlladderbottom_long','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlladderbottom_short','-70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdllongleggeddoji_long','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdllongleggeddoji_short','-70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlmatchinglow_long','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlmatchinglow_short','-70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlmorningstar_long','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlmorningstar_short','-70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlrickshawman_long','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlrickshawman_short','-70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlspinningtop_long','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdlspinningtop_short','-70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdltasukigap_long','70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'strat_cdltasukigap_short','-70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_general_regim_sl','fiks')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_general_regim_tp','fiks')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_general_regim_volume_max','fiks')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_general_regim_volume_min','fiks')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_general_input_start_time','0,1,2,3,4,5,6,7,8,9,10,11,12')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_general_input_stop_time','16,17,18,19,20,21,22,23,24')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_general_input_depo','100')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_general_input_leveradg','1,5,10,15,20')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_general_input_tp','0.7,0.9,1.2,1.5,2,4')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_general_input_sl','0.2,0.3,0.4')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_general_input_volume_min','50000,70000,120000,200000,500000,1000000')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_general_input_volume_max','1500000,3000000,5000000,10000000')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_general_input_how_mach_settings','5')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_ma_input_koef_bistro','3,4,5,6,7,8,9')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_ma_input_koef_medleno','11,12,13,14,15,16,17')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_ma_input_sovpad_last','1,2,3,4,5,6')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_ma_input_up_chanal','0.6,0.65,0.70,0.75,0.80,0.85,0.90')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_ma_input_down_chanal','0.05,0.10,0.15,0.20,0.25,0.30')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_one_input_up_chanal','60,65,70,75,80,85,90')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_one_input_down_chanal','10,15,20,25,30,35,40')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_one_input_corner_long','10,15,20,25,30')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_one_input_corner_short','90,85,80,75,70')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_bbands_timeperiod','4,5,6,7,8,9,10')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_bbands_nbdevup','1,2,3')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_bbands_nbdevdn','1,2,3')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_bbands_matype','0')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdl2crows_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdl2crows_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdl3blackcrows_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdl3blackcrows_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdl3inside_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdl3inside_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdl3linestrike_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdl3linestrike_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdl3outside_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdl3outside_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdl3starsinsouth_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdl3starsinsouth_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdl3whitesoldiers_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdl3whitesoldiers_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlabandonedbaby_penetration','0.2,0.25,0.3,0.35,0.4')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlabandonedbaby_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlabandonedbaby_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdladvanceblock_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdladvanceblock_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlbelthold_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlbelthold_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlclosingmarubozu_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlclosingmarubozu_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlcounterattack_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlcounterattack_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdldarkcloudcover_penetration','0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdldarkcloudcover_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdldarkcloudcover_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlengulfing_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlengulfing_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdleveningdojistar_penetration','0.2,0.25,0.3,0.35,0.4')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdleveningdojistar_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdleveningdojistar_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlgravestonedoji_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlgravestonedoji_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlhammer_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlhammer_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlhangingman_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlhangingman_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlharami_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlharami_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlharamicross_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlharamicross_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlhomingpigeon_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlhomingpigeon_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlinvertedhammer_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlinvertedhammer_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlladderbottom_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlladderbottom_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdllongleggeddoji_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdllongleggeddoji_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlmatchinglow_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlmatchinglow_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlmorningstar_penetration','0.2,0.25,0.3,0.35,0.4')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlmorningstar_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlmorningstar_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlrickshawman_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlrickshawman_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlspinningtop_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdlspinningtop_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdltasukigap_long','60,65,70,75,80,85,90,95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_cdltasukigap_short','-60,-65,-70,-75,-80,-85,-90,-95')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_dema_timeperiod','20,22,24,26,28,30,32,34,36,38,40')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_ema_timeperiod','20,22,24,26,28,30,32,34,36,38,40')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_kama_timeperiod','20,22,24,26,28,30,32,34,36,38,40')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_mavp_minperiod','2,3,4,5,6,7,8')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_mavp_maxperiod','25,26,27,28,29,30,31,32,33,34,35')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_mavp_matype','0')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_sar_acceleration','0.015,0.017,0.02,0.023,0.025')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_sar_maximum','0.15,0.17,0.2,0.22,0.25')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_tema_timeperiod','25,26,27,28,29,30,31,32,33,34,35')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_trima_timeperiod','25,26,27,28,29,30,31,32,33,34,35')
    config.set('param_trade_historical_trade_svobodniy_freym', 'set_wma_timeperiod','25,26,27,28,29,30,31,32,33,34,35')
    config.set('param_trade_historical_trade_svobodniy_freym', 'now_trade','[]')
    with open(f'{appdata}\\config.ini', 'w') as config_file:
        config.write(config_file)
    
# путь к файлу конфигурации для авторизации (запомнить меня)
path_imports_config = appdata + '\\config.ini' # основной файл инициализации, всех настроек
path_ini_svoboda_freym = appdata + '\\svoboda_freym.ini' # файл настроек для данных историческая торговля/свободный фрейм
path_ini_historical_freym = appdata + '\\historical_freym.ini' # файл настроек для данных историческая торговля/историческая торговля
path_ini_general_set = appdata + '\\general_set.ini' # файл общего сета настроек
path_ini_one_set = appdata + '\\one_set.ini' # файл сета настроек one
path_ini_MA_set = appdata + '\\MA_set.ini' # файл сета настроек MA
path_ini_BBANDS_set = appdata + '\\BBANDS_set.ini'
path_ini_EMA_set = appdata + '\\EMA_set.ini'
path_ini_DEMA_set = appdata + '\\DEMA_set.ini'
path_ini_KAMA_set = appdata + '\\KAMA_set.ini'
path_ini_MAVP_set = appdata + '\\MAVP_set.ini'
path_ini_SAR_set = appdata + '\\SAR_set.ini'
path_ini_TEMA_set = appdata + '\\TEMA_set.ini'
path_ini_TRIMA_set = appdata + '\\TRIMA_set.ini'
path_ini_WMA_set = appdata + '\\WMA_set.ini'
path_ini_CDL2CROWS_set = appdata + '\\CDL2CROWS_set.ini'
path_ini_CDL3BLACKCROWS_set = appdata + '\\CDL3BLACKCROWS_set.ini'
path_ini_CDL3INSIDE_set = appdata + '\\CDL3INSIDE_set.ini'
path_ini_CDL3LINESTRIKE_set = appdata + '\\CDL3LINESTRIKE_set.ini'
path_ini_CDL3OUTSIDE_set = appdata + '\\CDL3OUTSIDE_set.ini'
path_ini_CDL3STARSINSOUTH_set = appdata + '\\CDL3STARSINSOUTH_set.ini'
path_ini_CDL3WHITESOLDIERS_set = appdata + '\\CDL3WHITESOLDIERS_set.ini'
path_ini_CDLABANDONEDBABY_set = appdata + '\\CDLABANDONEDBABY_set.ini'
path_ini_CDLADVANCEBLOCK_set = appdata + '\\CDLADVANCEBLOCK_set.ini'
path_ini_CDLBELTHOLD_set = appdata + '\\CDLBELTHOLD_set.ini'
path_ini_CDLCLOSINGMARUBOZU_set = appdata + '\\CDLCLOSINGMARUBOZU_set.ini'
path_ini_CDLCOUNTERATTACK_set = appdata + '\\CDLCOUNTERATTACK_set.ini'
path_ini_CDLDARKCLOUDCOVER_set = appdata + '\\CDLDARKCLOUDCOVER_set.ini'
path_ini_CDLENGULFING_set = appdata + '\\CDLENGULFING_set.ini'
path_ini_CDLEVENINGDOJISTAR_set = appdata + '\\CDLEVENINGDOJISTAR_set.ini'
path_ini_CDLGRAVESTONEDOJI_set = appdata + '\\CDLGRAVESTONEDOJI_set.ini'
path_ini_CDLHAMMER_set = appdata + '\\CDLHAMMER_set.ini'
path_ini_CDLHANGINGMAN_set = appdata + '\\CDLHANGINGMAN_set.ini'
path_ini_CDLHARAMI_set = appdata + '\\CDLHARAMI_set.ini'
path_ini_CDLHARAMICROSS_set = appdata + '\\CDLHARAMICROSS_set.ini'
path_ini_CDLHOMINGPIGEON_set = appdata + '\\CDLHOMINGPIGEON_set.ini'
path_ini_CDLINVERTEDHAMMER_set = appdata + '\\CDLINVERTEDHAMMER_set.ini'
path_ini_CDLLADDERBOTTOM_set = appdata + '\\CDLLADDERBOTTOM_set.ini'
path_ini_CDLLONGLEGGEDDOJI_set = appdata + '\\CDLLONGLEGGEDDOJI_set.ini'
path_ini_CDLMATCHINGLOW_set = appdata + '\\CDLMATCHINGLOW_set.ini'
path_ini_CDLMORNINGSTAR_set = appdata + '\\CDLMORNINGSTAR_set.ini'
path_ini_CDLRICKSHAWMAN_set = appdata + '\\CDLRICKSHAWMAN_set.ini'
path_ini_CDLSPINNINGTOP_set = appdata + '\\CDLSPINNINGTOP_set.ini'
path_ini_CDLTASUKIGAP_set = appdata + '\\CDLTASUKIGAP_set.ini'
path_data_map_coin = appdata + '\\map_coin.json' # должен обновляться каждые n минут. С него рисуется тепловая карта и берутся монеты для получения датафреймов
path_data_user_tg_chat = appdata + '\\channel_users_tg.json' 
path_data_message_tg_chat = appdata + '\\channel_messages_tg.json'
path_JSON_coins_info_our = appdata + '\\coins_info_our.json'
path_svoboda_freym = appdata + '\\svoboda_freym' # начало пути для сохранения датафреймов - историческая торговля/свободный фрейм
path_historical_freym = appdata + '\\historical_freym' # начало пути для сохранения датафреймов - историческая торговля/историческая торговля
path_appdata = appdata
#--------------------------------------------------
# проверяем есть ли папка в директории для трейдов
if os.path.isdir(f'{appdata}\\trade'): 
    path_save_trade = appdata+'\\trade' # сюда будем сохранять трейды
else:
    os.mkdir(f'{appdata}\\trade') # если папки нет, создаем её
    path_save_trade = appdata+'\\trade' # сюда будем сохранять трейды
    
# проверяем есть ли папка в директории для избранных стратегий
if os.path.isdir(f'{appdata}\\favorites'): 
    path_favorites = appdata+'\\favorites' # сюда будем сохранять избранное
else:
    os.mkdir(f'{appdata}\\favorites') # если папки нет, создаем её
    path_favorites = appdata+'\\favorites' # сюда будем сохранять избранное
    
# проверяем есть ли папка в директории для сохраненеия датафреймов исторической торговли (дней сетов)
if os.path.isdir(f'{appdata}\\historical_freym'): 
    path_historical_freym = appdata+'\\historical_freym' # сюда будем сохранять избранное
else:
    os.mkdir(f'{appdata}\\historical_freym') # если папки нет, создаем её
    path_historical_freym = appdata+'\\historical_freym' # сюда будем сохранять избранное


#--------------------------------------------------

c_blue = '#222831'
c_white = '#FFFFFF'
c_yelow = '#FBD46D'
c_green = '#0AFF89'
c_red = '#FF0A0A'

c_blue_binance = '#161A1E'
c_green_binance = '#0ECB81'
c_red_binance = '#F6465D'
c_gray_binance = '#363A45'

server_ip = 'http://127.0.0.1:5000'

width_window_platforma = 1186
height_window_platforma = 760

version_desctop = 'v1.25.11'

key_bin = 'QIT80MTFskjHSr82dtsteA6bG01CUeODQCg65KoYaQ5LmPcSpYDzyv1Oa7fugW3m'
secret_bin = 'uMLo0WdaCv5FHBauV8QI4LZoDgmmVFf5Jd8TboKYRxHnHx6pmNrhg5bmdBgO54xI'

api_id_tg = '29054097'
api_hash_id_tg = 'ed0af3e9cb2fb29e47631254716cae92'
username_tg = 'maksimivankov'
data1 = {'sledim_money':'1m'}




strategys_our = {
    'one':'Канал, тренд, локаль, объём',
    'MA':'Скользящие средние',
    'BBANDS':'Полосы Боллинджера',
    'EMA':'Эксп скользящая средняя',                  # ноль показывают
    'DEMA':'Двойная эксп скользящая средняя',                 # ноль показывают
    'KAMA':'Адаптивная скользящая Кауфмана',                  # ноль показывают
    'MAVP':'Сколь средняя с пер периодом',                    # ноль показывают
    'SAR':'Параболический SAR',                   # ноль показывают
    'TEMA':'Тройная эксп сколь средняя',                  # ноль показывают
    'TRIMA':'Треугольная скользящая средняя',                 # ноль показывают
    'WMA':'Взвешенная скользящая средняя',                    # ноль показывают
    'CDL2CROWS':'Две вороны',                 # ноль показывают
    'CDL3BLACKCROWS':'Три черных ворона',                 # ноль показывают
    'CDL3INSIDE':'Три внутри Вверх / вниз',
    'CDL3LINESTRIKE':'Трехстрочный удар',
    'CDL3OUTSIDE':'Три внешних элемента Вверх / вниз',
    'CDL3STARSINSOUTH':'Три звезды на юге',                   # ноль показывают
    'CDL3WHITESOLDIERS':'Трое наступающих белых солдат',                  # ноль показывают
    'CDLABANDONEDBABY':'Брошенный ребенок',                   # ноль показывают
    'CDLADVANCEBLOCK':'Предварительный блок',
    'CDLBELTHOLD':'Удержание за ремень',
    'CDLCLOSINGMARUBOZU':'Marubozu',
    'CDLCOUNTERATTACK':'Контратака',                  # ноль показывают
    'CDLDARKCLOUDCOVER':'Темный облачный покров',                 # ноль показывают
    'CDLENGULFING':'шаблон поглощения',
    'CDLEVENINGDOJISTAR':'Вечерняя звезда Доджи',
    'CDLGRAVESTONEDOJI':'Надгробный камень Доджи',
    'CDLHAMMER':'Молоток',
    'CDLHANGINGMAN':'Висельник',
    'CDLHARAMI':'шаблон Харами',
    'CDLHARAMICROSS':'Шаблон пересечения Харами',
    'CDLHOMINGPIGEON':'Почтовый голубь',                  # ноль показывают
    'CDLINVERTEDHAMMER':'Перевернутый молоток',
    'CDLLADDERBOTTOM':'Основание лестницы',                   # ноль показывают
    'CDLLONGLEGGEDDOJI':'Длинноногий доджи',
    'CDLMATCHINGLOW':'низкий уровень соответствия',
    'CDLMORNINGSTAR':'Утренняя звезда',
    'CDLRICKSHAWMAN':'рикша',
    'CDLSPINNINGTOP':'Волчок',
    'CDLTASUKIGAP':'разрыв Тасуки',                       # ноль показывают
}
mas_name_strategys = ['one','MA','BBANDS','EMA','DEMA','KAMA','MAVP','SAR','TEMA','TRIMA','WMA','CDL2CROWS','CDL3BLACKCROWS','CDL3INSIDE','CDL3LINESTRIKE','CDL3OUTSIDE','CDL3STARSINSOUTH','CDL3WHITESOLDIERS','CDLABANDONEDBABY','CDLADVANCEBLOCK','CDLBELTHOLD','CDLCLOSINGMARUBOZU','CDLCOUNTERATTACK','CDLDARKCLOUDCOVER','CDLENGULFING','CDLEVENINGDOJISTAR','CDLGRAVESTONEDOJI','CDLHAMMER','CDLHANGINGMAN','CDLHARAMI','CDLHARAMICROSS','CDLHOMINGPIGEON','CDLINVERTEDHAMMER','CDLLADDERBOTTOM','CDLLONGLEGGEDDOJI','CDLMATCHINGLOW','CDLMORNINGSTAR','CDLRICKSHAWMAN','CDLSPINNINGTOP','CDLTASUKIGAP'
]

strategys_parametry_rus = {
    'one':['Верх канала','Низ канала','Угол тренда лонг','Угол тренда шорт'],
    'MA':['Коэф. быстрой скольз. средней','Коэф. медленной скольз. средней','Кол-во совпадений в прошлом','Прижатие к верху коридора','Прижатие к низу коридора'],
    'BBANDS':['Отклонение для установки верхней полосы','Временной промежуток','Отклонение для установки нижней полосы','Тип движущейся средней'],
    'EMA':['Временной промежуток'],                   # ноль показывают
    'DEMA':['Временной промежуток'],                  # ноль показывают
    'KAMA':['Временной промежуток'],                  # ноль показывают
    'MAVP':['Минимальный период','Максимальный период','Тип скользящей средней'],                 # ноль показывают
    'SAR':['Ускорение','Максимум'],                   # ноль показывают
    'TEMA':['Временной промежуток'],                  # ноль показывают
    'TRIMA':['Временной промежуток'],                 # ноль показывают
    'WMA':['Временной промежуток'],                   # ноль показывают
    'CDL2CROWS':['Временной промежуток','Временной промежуток'],                  # ноль показывают
    'CDL3BLACKCROWS':['Временной промежуток','Временной промежуток'],                 # ноль показывают
    'CDL3INSIDE':['Временной промежуток','Временной промежуток'],
    'CDL3LINESTRIKE':['Временной промежуток','Временной промежуток'],
    'CDL3OUTSIDE':['Временной промежуток','Временной промежуток'],
    'CDL3STARSINSOUTH':['Временной промежуток','Временной промежуток'],                   # ноль показывают
    'CDL3WHITESOLDIERS':['Временной промежуток','Временной промежуток'],                  # ноль показывают
    'CDLABANDONEDBABY':['Процент проникновения одной свечи внутри другой свечи','Процент сигнала в лонг','Процент сигнала в шорт'],                   # ноль показывают
    'CDLADVANCEBLOCK':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLBELTHOLD':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLCLOSINGMARUBOZU':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLCOUNTERATTACK':['Процент сигнала в лонг','Процент сигнала в шорт'],                   # ноль показывают
    'CDLDARKCLOUDCOVER':['Процент проникновения одной свечи внутри другой свечи','Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLENGULFING':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLEVENINGDOJISTAR':['Процент проникновения одной свечи внутри другой свечи','Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLGRAVESTONEDOJI':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLHAMMER':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLHANGINGMAN':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLHARAMI':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLHARAMICROSS':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLHOMINGPIGEON':['Процент сигнала в лонг','Процент сигнала в шорт'],                    # ноль показывают
    'CDLINVERTEDHAMMER':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLLADDERBOTTOM':['Процент сигнала в лонг','Процент сигнала в шорт'],                    # ноль показывают
    'CDLLONGLEGGEDDOJI':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLMATCHINGLOW':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLMORNINGSTAR':['Процент проникновения одной свечи внутри другой свечи','Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLRICKSHAWMAN':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLSPINNINGTOP':['Процент сигнала в лонг','Процент сигнала в шорт'],
    'CDLTASUKIGAP':['Процент сигнала в лонг','Процент сигнала в шорт'],                   # ноль показывают
}

strategys_parametry_for_section = {
    'one':['up_chanal','down_chanal','corner_long','corner_short'],
    'MA':['koef_bistro','koef_medleno','sovpad_last','up_chanal','down_chanal'],
    'BBANDS':['timeperiod','nbdevup','nbdevdn','matype'],
    'EMA':['timeperiod'],                 # ноль показывают
    'DEMA':['timeperiod'],                    # ноль показывают
    'KAMA':['timeperiod'],                    # ноль показывают
    'MAVP':['minperiod','maxperiod','matype'],                    # ноль показывают
    'SAR':['acceleration','maximum'],                 # ноль показывают
    'TEMA':['timeperiod'],                    # ноль показывают
    'TRIMA':['timeperiod'],                   # ноль показывают
    'WMA':['timeperiod'],                 # ноль показывают
    'CDL2CROWS':['long','short'],                 # ноль показывают
    'CDL3BLACKCROWS':['long','short'],                    # ноль показывают
    'CDL3INSIDE':['long','short'],
    'CDL3LINESTRIKE':['long','short'],
    'CDL3OUTSIDE':['long','short'],
    'CDL3STARSINSOUTH':['long','short'],                  # ноль показывают
    'CDL3WHITESOLDIERS':['long','short'],                 # ноль показывают
    'CDLABANDONEDBABY':['penetration','long','short'],                    # ноль показывают
    'CDLADVANCEBLOCK':['long','short'],
    'CDLBELTHOLD':['long','short'],
    'CDLCLOSINGMARUBOZU':['long','short'],
    'CDLCOUNTERATTACK':['long','short'],                  # ноль показывают
    'CDLDARKCLOUDCOVER':['penetration','long','short'],                   # ноль показывают
    'CDLENGULFING':['long','short'],
    'CDLEVENINGDOJISTAR':['penetration','long','short'],
    'CDLGRAVESTONEDOJI':['long','short'],
    'CDLHAMMER':['long','short'],
    'CDLHANGINGMAN':['long','short'],
    'CDLHARAMI':['long','short'],
    'CDLHARAMICROSS':['long','short'],
    'CDLHOMINGPIGEON':['long','short'],                   # ноль показывают
    'CDLINVERTEDHAMMER':['long','short'],
    'CDLLADDERBOTTOM':['long','short'],                   # ноль показывают
    'CDLLONGLEGGEDDOJI':['long','short'],
    'CDLMATCHINGLOW':['long','short'],
    'CDLMORNINGSTAR':['penetration','long','short'],
    'CDLRICKSHAWMAN':['long','short'],
    'CDLSPINNINGTOP':['long','short'],
    'CDLTASUKIGAP':['long','short'],                  # ноль показывают
}


