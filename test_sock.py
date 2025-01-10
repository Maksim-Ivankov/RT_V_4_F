import websockets
import json
import asyncio, time
import requests

import flet as ft

symbol = ['BTCUSDT']

# Класс, получающий стакан
class lol:
    def __init__(self, symbol):
        self.symbol = symbol
        # формируем ссылку для бодключения к вебсокетам 
        self._socket = "wss://fstream.binance.com/stream?streams="
        socet_symbol = ''
        for sym in symbol:
            socet_symbol += f'{sym.lower()}@depth@100ms/'
        self._socket = self._socket + socet_symbol
        self._socket = self._socket[:-1]

        self._bids = {}
        self._asks = {}
        self._last_update_id = 0
        self._prev_u = None
        self._lock = False
        self.bid_x = []
        self.bid_z = []
        self.ask_x = []
        self.ask_z = []
        self.y = [[0] * 100]
        self.data_socket = {}

    def _get_snapshot(self):
        """Сбросьте значения _bids и _asks на моментальный снимок текущей книги заказов и обновите last_update_id."""
        for sym in self.symbol:
            rest = f"https://fapi.binance.com/fapi/v1/depth?symbol={sym.lower()}&limit=1000"
            _bids,_asks = self._get_once_snapshot(rest)
            self.data_socket[sym] = [_bids,_asks]
            print(f'Получили снепшот {sym}')
            time.sleep(0.5)

    def _get_once_snapshot(self,_rest):
        r = requests.get(_rest)
        self._lock = True
        data = json.loads(r.text)
        self._last_update_id = data["lastUpdateId"]
        _bids = {float(price): float(qty) for price, qty in data["bids"]}
        _asks = {float(price): float(qty) for price, qty in data["asks"]}
        self._lock = False
        return _bids, _asks

    def connect(self):
        self._get_snapshot()
        # main = Main()
        # ft.app(target=Main().run, assets_dir="assets")
        loop22 = asyncio.new_event_loop()
        asyncio.set_event_loop(loop22)
        loop22 = asyncio.get_event_loop()
        loop22.run_until_complete(self.websocket_trade()) 

    def get_quotes(self) -> tuple[float, float]:
        """Return best bid and ask"""
        return max(self._bids.keys()), min(self._asks.keys())
    
    def get_bids(self,symbol):
        """Return bids"""
        return self.data_socket[symbol][0]
    
    def get_asks(self,symbol):
        """Return asks"""
        return self.data_socket[symbol][1]

        # запускаем вебсокеты, когда вошли в сделку, следим за монетой, рисуем график и данные в реальном времени    
    async def websocket_trade(self):
        i = 0
        try:
            async with websockets.connect(self._socket) as ws:
                while True:        
                    try:
                        message = json.loads(await ws.recv())['data']
                        for sym in self.symbol:
                            if message['s'] == sym:
                                if message["u"] >= self._last_update_id:
                                    for price_level, qty in message["b"]: # изменения, которые получаем с вебсокетов - два числа, уровень цены / объём
                                        if float(qty) == 0: # если объем по текущему уровню цены равен нулю
                                            self.data_socket[sym][0].pop(float(price_level), None) # то удаляем этот уровень цены
                                        else: 
                                            self.data_socket[sym][0][float(price_level)] = float(qty) # иначе добавляем  новый уровень цены
                                            # print(float(qty))
                                    for price_level, qty in message["a"]:
                                        if float(qty) == 0:
                                            self.data_socket[sym][1].pop(float(price_level), None)
                                        else:
                                            self.data_socket[sym][1][float(price_level)] = float(qty)
                                            # print(float(qty))
                                if self._prev_u != None and self._prev_u != message["pu"]:
                                    print("Рассинхронизация книги заказов приводит к появлению нового снимка")
                                    self._get_snapshot()
                                self._prev_u = message["u"]
                            else: print('НЕТ!!!!!!!!')
                        print(self.data_socket)
                        # file = open(f'set_websockets_5.txt', 'a')
                        # file.write(f'{self.data_socket}\n')
                        # # file.write(f'{message}\n')
                        # file.close()
                    except websockets.exceptions.ConnectionClosed:
                        break
        except Exception as e:
            print(f'Ошибка - {e}')

# Рисуем всё

class Main:
    def __init__(self):
        None

    def run(self, page):
        self.page: ft.Page = page
        self.page.title = "RoboTrade"
        self.page.window_height, self.page.window_width = 1000, 400
        self.page.theme_mode = "dark" 
        
        
        lolka = lol(symbol)
        lolka.connect()
        
        self.page.add(ft.Text('123123'))




if __name__ == '__main__':
    # lolka = lol(symbol)
    # lolka.connect()
    main = Main()
    ft.app(target=Main().run, assets_dir="assets")










