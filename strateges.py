# 'MIN' - готово
# 'MA' - готово 
# 'BBANDS'
# 'EMA'
# 'DEMA'
# 'KAMA'
# 'MAVP'
# 'SAR'
# 'TEMA'
# 'TRIMA'
# 'WMA'
# 'CDL2CROWS'
# 'CDL3BLACKCROWS'
# 'CDL3INSIDE'
# 'CDL3LINESTRIKE'
# 'CDL3OUTSIDE'
# 'CDL3STARSINSOUTH'
# 'CDL3WHITESOLDIERS'
# 'CDLABANDONEDBABY'
# 'CDLADVANCEBLOCK'
# 'CDLBELTHOLD'
# 'CDLCLOSINGMARUBOZU'
# 'CDLCOUNTERATTACK'
# 'CDLDARKCLOUDCOVER'
# 'CDLENGULFING'
# 'CDLEVENINGDOJISTAR'
# 'CDLGRAVESTONEDOJI'
# 'CDLHAMMER'
# 'CDLHANGINGMAN'
# 'CDLHARAMI'
# 'CDLHARAMICROSS'
# 'CDLHOMINGPIGEON'
# 'CDLINVERTEDHAMMER'
# 'CDLLADDERBOTTOM'
# 'CDLLONGLEGGEDDOJI'
# 'CDLMATCHINGLOW'
# 'CDLMORNINGSTAR'
# 'CDLRICKSHAWMAN'
# 'CDLSPINNINGTOP'
# 'CDLTASUKIGAP'

import talib as ta

# Группы индикаторов
# Исследования перекрытия
# Индикаторы импульса
# Индикаторы объема
# Индикаторы волатильности
# Преобразование цены
# Индикаторы цикла
# Распознавание образов


# ################################################################################################
# Исследования перекрытия
#   # BBANDS               Полосы Боллинджера                                   # upperband, middleband, lowerband = BBANDS(close, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)                                                                                         
# x # DEMA                 Двойная экспоненциальная скользящая средняя          # real = DEMA(close, timeperiod=30)                                                                                             
# x # EMA                  Экспоненциальная скользящая средняя                  # real = EMA(close, timeperiod=30)                                                                                     
# x # HT_TRENDLINE         Преобразование Гильберта - Мгновенная линия тренда   # real = HT_TRENDLINE(close)                                                                                                    
# x # KAMA                 Адаптивная скользящая средняя Кауфмана               # real = KAMA(close, timeperiod=30)                                                                                        
# х # MA                   Скользящая средняя                                   # real = MA(close, timeperiod=30, matype=0)                                                                     
#   # MAMA                 Адаптивная скользящая средняя МЕСА                   # mama, fama = MAMA(close, fastlimit=0, slowlimit=0)                                                                                    
#   # MAVP                 Скользящая средняя с переменным периодом             # real = MAVP(close, periods, minperiod=2, maxperiod=30, matype=0)                                                                                          
# х # MIDPOINT             Средняя точка за период                              # real = MIDPOINT(close, timeperiod=14)                                                                         
# х # MIDPRICE             Средняя цена за период                               # real = MIDPRICE(high, low, timeperiod=14)                                                                        
#   # SAR                  Параболический SAR                                   # real = SAR(high, low, acceleration=0, maximum=0)                                                                     
#   # SAREXT               Параболический SAR - расширенный                     # real = SAREXT(high, low, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0)                                                                                  
# х # SMA                  Простая скользящая средняя                           # real = SMA(close, timeperiod=30)                                                                            
#   # T3                   Тройная экспоненциальная скользящая средняя (T3)     # real = T3(close, timeperiod=5, vfactor=0)                                                                                                  
# х # TEMA                 Тройная экспоненциальная скользящая средняя          # real = TEMA(close, timeperiod=30)                                                                                             
# х # TRIMA                Треугольная скользящая средняя                       # real = TRIMA(close, timeperiod=30)                                                                                
# х # WMA                  Взвешенная скользящая средняя                        # real = WMA(close, timeperiod=30)                                                                                                                                         
#   # ################################################################################################
#   # Индикаторы импульса
# x # ADX                  Индекс Среднего направленного движения               # real = ADX(high, low, close, timeperiod=14)                                                                                       
# x # ADXR                 Рейтинг Индекса Среднего направленного движения      # real = ADXR(high, low, close, timeperiod=14)                                                                                                
# x # APO                  Абсолютный ценовой осциллятор                        # real = APO(close, fastperiod=12, slowperiod=26, matype=0)                                                                              
# x # AROON                Aroon                                                # aroondown, aroonup = AROON(high, low, timeperiod=14)                                                      
#   # AROONOSC             Осциллятор Aroon                                     # real = AROONOSC(high, low, timeperiod=14)                                                                 
# x # BOP                  Баланс сил                                           # real = BOP(open, high, low, close)                                                           
# x # CCI                  Индекс Товарного канала                              # real = CCI(high, low, close, timeperiod=14)                                                                        
# x # CMO                  Осциллятор импульса Чанда                            # real = CMO(close, timeperiod=14)                                                                          
# x # DX                   Индекс Направленного движения                        # real = DX(high, low, close, timeperiod=14)                                                                              
# х # MACD                 Конвергенция/Расхождение скользящих средних          # macd, macdsignal, macdhist = MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)                                                                                            
#   # MACDEXT              MACD с регулируемым типом скользящей средней         # macd, macdsignal, macdhist = MACDEXT(close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)                                                                                             
#   # MACDFIX              Фиксация конвергенции/расхождения скользящих         # macd, macdsignal, macdhist = MACDFIX(close, signalperiod=9)                                                                                              
#   #                      средних 12/26                                                                                                                                                                           
# x # MFI                  Индекс денежного потока                              # real = MFI(high, low, close, volume, timeperiod=14)                                                                        
# x # MINUS_DI             Индикатор отрицательного направления                 # real = MINUS_DI(high, low, close, timeperiod=14)                                                                                     
# x # MINUS_DM             Движение с отрицательным направлением                # real = MINUS_DM(high, low, timeperiod=14)                                                                                      
# x # MOM                  Импульс                                              # real = MOM(close, timeperiod=10)                                                        
# x # PLUS_DI              Плюс Индикатор направленности                        # real = PLUS_DI(high, low, close, timeperiod=14)                                                                              
#   # PLUS_DM              Плюс Индикатор направленности движения               # real = PLUS_DM(high, low, timeperiod=14)                                                                                       
#   # PPO                  Процентный ценовой осциллятор                        # real = PPO(close, fastperiod=12, slowperiod=26, matype=0)                                                                             
# x # ROC                  Скорость изменения :                                 # real = ROC(close, timeperiod=10)                                                                      
#   #                      ((цена/предварительная цена)-1)*100                                                                                                                                                                           
#   # ROCP                 Процентное соотношение темпов изменения:             # real = ROCP(close, timeperiod=10)                                                                                          
#   #                      (цена-цена выше нормы)/Цена выше нормы                                                                                                                                                                           
#   # ROCR                 Соотношение темпов изменения:                        # real = ROCR(close, timeperiod=10)                                                                               
#   #                      (цена/цена выше нормы)                                                                                                                                                                           
#   # ROCR100              Соотношение темпов изменения в масштабе 100:         # real = ROCR100(close, timeperiod=10)                                                                                              
#   #                      (цена/цена выше нормы)*100                                                                                                                                                                           
#   # RSI                  Индекс относительной силы                            # real = RSI(close, timeperiod=14)                                                                          
#   # STOCH                Стохастический                                       # slowk, slowd = STOCH(high, low, close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)                                                               
#   # STOCHF               Быстрый стохастик                                    # fastk, fastd = STOCHF(high, low, close, fastk_period=5, fastd_period=3, fastd_matype=0)                                                                  
#   # STOCHRSI             Индекс относительной силы Стохастика                 # fastk, fastd = STOCHRSI(close, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)                                                                                     
#   # TRIX                 1-дневная скорость изменения (ROC)                   # real = TRIX(close, timeperiod=30)                                                                                    
#   #                      Тройной плавной ЕМА                                                                                                                                                                           
#   # ULTOSC               Основной осциллятор                                  # real = ULTOSC(high, low, close, timeperiod1=7, timeperiod2=14, timeperiod3=28)                                                                    
#   # WILLR                %R Уильямса                                          # real = WILLR(high, low, close, timeperiod=14)                                                                                      
#   # ################################################################################################
#   # Индикаторы объема
#   # AD                   Индикаторная линия Чайкина                           # real = AD(high, low, close, volume)                                                                           
# x # ADOSC                Осциллятор Чайкина                                   # real = ADOSC(high, low, close, volume, fastperiod=3, slowperiod=10)                                                                   
#   # OBV                  На балансовом объеме                                 # real = OBV(close, volume)                                                               
#   # ################################################################################################
#   # Индикаторы цикла
#   # HT_DCPERIOD          Преобразование Гильберта - Доминирующий период цикла #  real = HT_DCPERIOD(close)                                                                                                    
#   # HT_DCPHASE           Преобразование Гильберта - Доминирующая фаза цикла   #  real = HT_DCPHASE(close)                                                                                                  
#   # HT_PHASOR            Преобразование Гильберта - Фазовые компоненты        #  inphase, quadrature = HT_PHASOR(close)                                                                                             
#   # HT_SINE              Преобразование Гильберта - синусоидальная волна      #  sine, leadsine = HT_SINE(close)                                                                                               
#   # HT_TRENDMODE         Преобразование Гильберта - режим тренда или цикла    #  integer = HT_TRENDMODE(close)                                                                                            
#   # ################################################################################################
#   # Преобразование цены
#   # AVGPRICE             Средняя цена                                        #  real = AVGPRICE(open, high, low, close                                                             
#   # MEDPRICE             Медианная цена                                      #  real = MEDPRICE(high, low)                                                               
#   # TYPPRICE             Типичная цена                                       #  real = TYPPRICE(high, low, close)                                                              
#   # WCLPRICE             Взвешенная цена закрытия                            #  real = WCLPRICE(high, low, close)                                                                        
#   # ################################################################################################
#   # Индикаторы волатильности
#   # ATR                  Средний истинный диапазон                           #  real = ATR(high, low, close, timeperiod=14)                                                                          
#   # NATR                 Нормализованный Средний истинный диапазон           #  real = NATR(high, low, close, timeperiod=14)                                                                                         
#   # TRANGE               Истинный диапазон                                   #  real = TRANGE(high, low, close)                                               
#   # ################################################################################################
#   # Распознавание образов
#   # CDL2CROWS            Две Вороны                                          #  integer = CDL2CROWS(open, high, low, close)                                                           
#   # CDL3BLACKCROWS       Три Черные Вороны                                   #  integer = CDL3BLACKCROWS(open, high, low, close)                                                                  
#   # CDL3INSIDE           Три Внутри, Вверх / Вниз                            #  integer = CDL3INSIDE(open, high, low, close)                                                                         
#   # CDL3LINESTRIKE       Удар в три линии                                    #  integer = CDL3LINESTRIKE(open, high, low, close)                                                                
#   # CDL3OUTSIDE          Три Снаружи, Вверх / Вниз                           #  integer = CDL3OUTSIDE(open, high, low, close)                                                                          
#   # CDL3STARSINSOUTH     Три Звезды На Юге                                   #  integer = CDL3STARSINSOUTH(open, high, low, close)                                                                  
#   # CDL3WHITESOLDIERS    Три Наступающих Белых Солдата                       #  integer = CDL3WHITESOLDIERS(open, high, low, close)                                                                              
#   # CDLABANDONEDBABY     Брошенный Ребенок                                   #  integer = CDLABANDONEDBABY(open, high, low, close, penetration=0)                                                                  
#   # CDLADVANCEBLOCK      Блокировка атаки                                    #  integer = CDLADVANCEBLOCK(open, high, low, close)                                                                 
#   # CDLBELTHOLD          Удержание за пояс                                   #  integer = CDLBELTHOLD(open, high, low, close)                                                                  
#   # CDLBREAKAWAY         Отступление                                         #  integer = CDLBREAKAWAY(open, high, low, close)                                                            
#   # CDLCLOSINGMARUBOZU   Закрывающий Марубозу                                #  integer = CDLCLOSINGMARUBOZU(open, high, low, close)                                                                     
#   # CDLCONCEALBABYSWALL  Скрывающий Ласточку                                 #  integer = CDLCONCEALBABYSWALL(open, high, low, close)                                                                    
#   # CDLCOUNTERATTACK     Контратака                                          #  integer = CDLCOUNTERATTACK(open, high, low, close)                                                           
#   # CDLDARKCLOUDCOVER    Темный облачный покров                              #  integer = CDLDARKCLOUDCOVER(open, high, low, close, penetration=0)                                                                       
#   # CDLDOJI              Доджи                                               #  integer = CDLDOJI(open, high, low, close)                                                      
#   # CDLDOJISTAR          Звезда Доджи                                        #  integer = CDLDOJISTAR(open, high, low, close)                                                             
#   # CDLDRAGONFLYDOJI     Стрекоза Доджи                                      #  integer = CDLDRAGONFLYDOJI(open, high, low, close)                                                               
#   # CDLENGULFING         Поглощающий узор                                    #  integer = CDLENGULFING(open, high, low, close)                                                                 
#   # CDLEVENINGDOJISTAR   Вечерняя звезда Доджи                               #  integer = CDLEVENINGDOJISTAR(open, high, low, close, penetration=0)                                                                      
#   # CDLEVENINGSTAR       Вечерняя звезда                                     #  integer = CDLEVENINGSTAR(open, high, low, close, penetration=0)                                                                
#   # CDLGAPSIDESIDEWHITE  Белые линии, проходящие                             #  integer = CDLGAPSIDESIDEWHITE(open, high, low, close)                                                                              
#   #                      рядом друг с другом вверх/вниз                                                                                                      
#   # CDLGRAVESTONEDOJI    Надгробный доджи                                    #  integer = CDLGRAVESTONEDOJI(open, high, low, close)                                                                
#   # CDLHAMMER            Молоток                                             #  integer = CDLHAMMER(open, high, low, close)                                                        
#   # CDLHANGINGMAN        Повешенный человек                                  #  integer = CDLHANGINGMAN(open, high, low, close)                                                                   
#   # CDLHARAMI            Узор Харами                                         #  integer = CDLHARAMI(open, high, low, close)                                                            
#   # CDLHARAMICROSS       Узор в виде креста Харами                           #  integer = CDLHARAMICROSS(open, high, low, close)                                                                          
#   # CDLHIGHWAVE          Свеча в форме высокой волны                         #  integer = CDLHIGHWAVE(open, high, low, close)                                                                            
#   # CDLHIKKAKE           Узор Хиккаке                                        #  integer = CDLHIKKAKE(open, high, low, close)                                                             
#   # CDLHIKKAKEMOD        Модифицированный узор Хиккаке                       #  integer = CDLHIKKAKEMOD(open, high, low, close)                                                                              
#   # CDLHOMINGPIGEON      Почтовый голубь                                     #  integer = CDLHOMINGPIGEON(open, high, low, close)                                                                
#   # CDLIDENTICAL3CROWS   Три одинаковые вороны                               #  integer = CDLIDENTICAL3CROWS(open, high, low, close)                                                                      
#   # CDLINNECK            Узор на шее                                         #  integer = CDLINNECK(open, high, low, close)                                                            
#   # CDLINVERTEDHAMMER    Перевернутый молот                                  #  integer = CDLINVERTEDHAMMER(open, high, low, close)                                                                  
#   # CDLKICKING           Пинающий                                            #  integer = CDLKICKING(open, high, low, close)                                                         
#   # CDLKICKINGBYLENGTH   Победитель определяется по длинному марубозу        #  integer = CDLKICKINGBYLENGTH(open, high, low, close)                                                                                             
#   # CDLLADDERBOTTOM      Подножие лестницы                                   #  integer = CDLLADDERBOTTOM(open, high, low, close)                                                                  
#   # CDLLONGLEGGEDDOJI    Длинноногий Доджи                                   #  integer = CDLLONGLEGGEDDOJI(open, high, low, close)                                                                  
#   # CDLLONGLINE          Длинная свеча в виде линии                          #  integer = CDLLONGLINE(open, high, low, close)                                                                           
#   # CDLMARUBOZU          Марубозу                                            #  integer = CDLMARUBOZU(open, high, low, close)                                                         
#   # CDLMATCHINGLOW       Соответствующий низкий                              #  integer = CDLMATCHINGLOW(open, high, low, close)                                                                       
#   # CDLMATHOLD           Удержание коврика                                   #  integer = CDLMATHOLD(open, high, low, close, penetration=0)                                                                  
#   # CDLMORNINGDOJISTAR   Утренняя звезда Доджи                               #  integer = CDLMORNINGDOJISTAR(open, high, low, close, penetration=0)                                                                      
#   # CDLMORNINGSTAR       Утренняя звезда                                     #  integer = CDLMORNINGSTAR(open, high, low, close, penetration=0)                                                                
#   # CDLONNECK            Узор на шее                                         #  integer = CDLONNECK(open, high, low, close)                                                            
#   # CDLPIERCING          Узор для пирсинга                                   #  integer = CDLPIERCING(open, high, low, close)                                                                  
#   # CDLRICKSHAWMAN       Мужчина-рикша                                       #  integer = CDLRICKSHAWMAN(open, high, low, close)                                                              
#   # CDLRISEFALL3METHODS  Рост/Падение тремя способами                        #  integer = CDLRISEFALL3METHODS(open, high, low, close)                                                                             
#   # CDLSEPARATINGLINES   Разделительные линии                                #  integer = CDLSEPARATINGLINES(open, high, low, close)                                                                     
#   # CDLSHOOTINGSTAR      падающая звезда                                     #  integer = CDLSHOOTINGSTAR(open, high, low, close)                                                                
#   # CDLSHORTLINE         Свеча в виде короткой линии                         #  integer = CDLSHORTLINE(open, high, low, close)                                                                            
#   # CDLSPINNINGTOP       Вращающийся волчок                                  #  integer = CDLSPINNINGTOP(open, high, low, close)                                                                   
#   # CDLSTALLEDPATTERN    Узор "Застопорившийся"                              #  integer = CDLSTALLEDPATTERN(open, high, low, close)                                                                       
#   # CDLSTICKSANDWICH     Сэндвич из палочек                                  #  integer = CDLSTICKSANDWICH(open, high, low, close)                                                                   
#   # CDLTAKURI            Такури (Доджи-стрекоза с очень длинной нижней тенью)#  integer = CDLTAKURI(open, high, low, close)                                                                                                     
#   # CDLTASUKIGAP         Тасуки Гэп                                          #  integer = CDLTASUKIGAP(open, high, low, close)                                                           
#   # CDLTHRUSTING         Узор "Выпад"                                        #  integer = CDLTHRUSTING(open, high, low, close)                                                             
#   # CDLTRISTAR           Узор "Тристар"                                      #  integer = CDLTRISTAR(open, high, low, close)                                                               
#   # CDLUNIQUE3RIVER      Уникальные 3 реки                                   #  integer = CDLUNIQUE3RIVER(open, high, low, close)                                                                  
#   # CDLUPSIDEGAP2CROWS   Перевернутый гэп "Две вороны"                       #  integer = CDLUPSIDEGAP2CROWS(open, high, low, close)                                                                              
#   # CDLXSIDEGAP3METHODS  Разрыв между повышением и понижением - три метода   #  integer = CDLXSIDEGAP3METHODS(open, high, low, close)                                                                        
#   # ################################################################################################
#   # Статистические функции
#   # BETA                 Бета                                                #  real = BETA(high, low, timeperiod=5)                                                     
#   # CORREL               Коэффициент корреляции Пирсона (r)                  #  real = CORREL(high, low, timeperiod=30)                                                                                   
#   # LINEARREG            Линейная регрессия                                  #  real = LINEARREG(close, timeperiod=14)                                                                   
#   # LINEARREG_ANGLE      Угол линейной регрессии                             #  real = LINEARREG_ANGLE(close, timeperiod=14)                                                                        
#   # LINEARREG_INTERCEPT  Пересечение линейной регрессии                      #  real = LINEARREG_INTERCEPT(close, timeperiod=14)                                                                               
#   # LINEARREG_SLOPE      Наклон линейной регрессии                           #  real = LINEARREG_SLOPE(close, timeperiod=14)                                                                          
#   # STDDEV               Стандартное отклонение                              #  real = STDDEV(close, timeperiod=5, nbdev=1)                                                                       
#   # TSF                  Прогноз временного ряда                             #  real = TSF(close, timeperiod=14)                                                                          
#   # VAR                  Различие                                            #  real = VAR(close, timeperiod=5, nbdev=1)                                 


















