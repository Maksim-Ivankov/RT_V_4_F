
import flet as ft
from variable import *
from imports import *

class Dinamic_dohodnost(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu


    def build(self):

        day = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
        dohod = [0,-2,-5,-7,-10,6,8,11,15,14,16,20,22,21,26,32,33,33,35,34,35,38,37,62,64,68,82,81,75,84,96,105,101,112,113,110,115,125,130]
        x = np.array(day)
        y = np.array(dohod)
        fig = plt.figure(figsize=(9,4))
        ax = fig.add_subplot(111)
        ax.spines[['left', 'top']].set_visible(False)
        ax.yaxis.tick_right()
        plt.fill_between(day, dohod, 0, color=c_green)
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_position('zero')
        ax.spines['bottom'].set_color(c_white)
        ax.spines['right'].set_color(c_white)
        ax.tick_params(axis='x', colors=c_white)
        ax.tick_params(axis='y', colors=c_white)
        ax.set_yticks(np.arange(0, max(dohod), 20))
        plt.grid(axis='y',color = c_white,linestyle = "-.")
        plt.fill_between(x, y, where=(y < 0), color=c_red)
        plt.fill_between(x, y, where=(y > 0), color=c_green)
        plt.xticks(size = 15)
        plt.yticks(size = 15)
        plt.plot(day,dohod)

        self.dinamic_dohodnost = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(ft.Text('Динамика доходности',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white),
                    )),
                    ft.Container(
                        ft.Container(MatplotlibChart(fig,transparent=True),
                                    margin=ft.margin.only(top=-10,left=-30,bottom=-10,right=-10)
                                     ),
                        width=290,
                        height=133,
                        border = ft.border.all(1, c_white),
                        padding=0,
                    ), 
                ]
            )
        )
        
        return self.dinamic_dohodnost