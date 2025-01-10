
import flet as ft
from variable import *
from imports import *


client = UMFutures(key=key_bin, secret=secret_bin)

print(client.depth('BTCUSDT'))
# data = client.ticker_24hr_price_change()
# with open(path_data_map_coin, 'w', encoding="utf-8") as outfile:
#     json.dump(data, outfile, ensure_ascii=False)


