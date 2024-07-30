
import flet as ft
from variable import *
from imports import *

class Telegram_chat(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu



    def build(self):

        print('----------------------123123123-------------------------')
        data_msg = requests.get(server_ip+'/get_tg_msg')
        data_msg = data_msg.json()

        # получаем последний key, чтобы потом с него начать
        for key,value in data_msg.items():
            now_message = key
        self.item_birgas = []
        # итерация по ключам с последнего до нулевого
        for i in range(int(now_message),-1,-1):
            for user,msg in data_msg[str(i)].items():
            # print(f'{key} - {value}')
                if len(msg)<22:
                    self.item_birgas.append(
                        ft.Container(ft.Row(controls=[
                            ft.Container(ft.Text(user[0],text_align='center',color=c_blue,size=12),width=25,height=25,border_radius=20,bgcolor=c_yelow,padding=ft.padding.only(top=3)),
                            ft.Container(ft.Text(msg,color=c_blue,size=11),bgcolor=c_white,padding=3,border_radius=ft.border_radius.only(top_left=5, top_right=5, bottom_right=5)),
                        ]))
                    )
                else:
                    self.item_birgas.append(
                        ft.Container(ft.Row(controls=[
                            ft.Container(ft.Text(user[0],text_align='center',color=c_blue,size=12),width=25,height=25,border_radius=20,bgcolor=c_yelow,padding=ft.padding.only(top=3)),
                            ft.Container(ft.Text(msg,color=c_blue,size=11,width=120),bgcolor=c_white,padding=3,border_radius=ft.border_radius.only(top_left=5, top_right=5, bottom_right=5)),
                        ]))
                    )
        
        self.telegram_chat = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(ft.Text('Telegram Chat',color=c_blue,),bgcolor=c_yelow,padding=5,margin=ft.margin.only(bottom=-10),border=ft.border.all(1,c_white),
                    )),
                    ft.Container(
                        ft.Column(controls=[
                            ft.Container(ft.Image(src=f"src/img/logo_2.png",width=140,height=28,),margin = ft.margin.only(bottom=-5,top=5),alignment=ft.alignment.center),
                            ft.Row(controls=[
                                ft.Text('RoboTrade Chat',size=12,color=c_white),
                                ft.Text('558 участников',size=12,color=c_white),
                            ]),
                            ft.Container(
                                ft.Container(
                                    ft.Column(controls=self.item_birgas),
                                    # width=189,
                                    # height=350,
                                    padding=5,
                                    # margin=ft.margin.only(bottom=-350)
                                ),
                                image_src='src/img/fon_tg.png',
                                image_fit=ft.ImageFit.COVER,
                                expand=True,
                                height=300,
                                margin=ft.margin.only(bottom=-50)
                                
                            ),
                            ft.Container(ft.ElevatedButton(content = ft.Text('Написать сообщение',size=12,),bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,height=30)
                        ]),
                        width=215,
                        height=370,
                        border = ft.border.all(1, c_white),
                        padding=10,
                    ), 
                ]
            )
        )
        
        return self.telegram_chat