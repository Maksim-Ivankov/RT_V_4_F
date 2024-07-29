
import matplotlib.pyplot as plt
import squarify
import flet as ft
from flet.matplotlib_chart import MatplotlibChart
from binance.um_futures import UMFutures

    # Получаем активные монеты на бирже
key_1 = 'QIT80MTFskjHSr82dtsteA6bG01CUeODQCg65KoYaQ5LmPcSpYDzyv1Oa7fugW3m'
secret_1 = 'uMLo0WdaCv5FHBauV8QI4LZoDgmmVFf5Jd8TboKYRxHnHx6pmNrhg5bmdBgO54xI'

def main(page: ft.Page):

    fig, ax = plt.subplots()
    # plt.rcParams ['figure.figsize'] = [10, 15]
    # fig.set_figwidth(50) 
    # fig.set_figheight(20) 
    # for item in [fig, ax]:
    #     item.patch.set_visible(False)
    plt.box(False)
    # fig.set_size_inches(60, 10, forward=True)
    number_of_views = [205, 82, 467, 450, 300]
    news = ['BTCUSDT\n+12%', 'ETHUSDT\n+5%', 'DOGEUSDT\n-2%', 'SRPUSDT\n+1%', 'MATICUSDT\n-3%']
    clrs=['green','green','red','green','red']
    squarify.plot(number_of_views, label=news, pad=0,ec = 'black', color=clrs)
    plt.axis('off')
 
    page.add(
        ft.Container(
            MatplotlibChart(fig, expand=True,original_size=True,),bgcolor='red',height=500

            
        )
    )
    

ft.app(target=main)








