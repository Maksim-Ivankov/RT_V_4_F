
import flet as ft
from variable import *
from imports import *
import re

class Sign_in(ft.UserControl):

    def build(self):

        # отрисовка регистрации после ошибки
        def open_reg_two(e):
            self.controls = []
            self.controls.append(
                ft.Container(
                    ft.Column(
                        controls=[
                            ft.TextField(value= self.ref_email.current.value ,ref = self.ref_email, label="Email",bgcolor=c_white,border_radius=0,border_color=c_white,height=30,color=c_blue,cursor_color=c_blue,cursor_height=22,text_align='center',content_padding= ft.padding.only(10),),
                            ft.TextField(value= self.ref_pass.current.value ,ref = self.ref_pass, label="Пароль",password=True, can_reveal_password=True,bgcolor=c_white,border_radius=0,border_color=c_white,height=30,color=c_blue,cursor_color=c_blue,cursor_height=22,text_align='center',content_padding= ft.padding.only(10)),
                            ft.TextField(value= self.ref_api_key.current.value ,ref = self.ref_api_key, label="Api-key",password=True, can_reveal_password=True,bgcolor=c_white,border_radius=0,border_color=c_white,height=30,color=c_blue,cursor_color=c_blue,cursor_height=22,text_align='center',content_padding= ft.padding.only(10)),
                            ft.Container(
                                ft.Row(
                                    controls=[
                                        ft.CupertinoCheckbox(value=False,check_color=c_blue,active_color=c_yelow,inactive_color=c_blue,ref=self.checkbox_vsisteme),
                                        ft.Container(ft.Text('Оставаться в системе',color=c_blue,),margin = ft.margin.only(left=-15),on_click=vsisteme)

                                    ]
                                ),margin = ft.margin.only(left=28,top=-12,bottom=-20)
                                # alignment=ft.alignment.center,
                            ),
                            ft.Container(ft.Text('Восстановить пароль',color=c_blue,size=12),margin = ft.margin.only(left=66,bottom=-2),on_click=vsisteme),
                            ft.Container(ft.ElevatedButton(text="Войти",bgcolor=c_blue,color=c_white,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),),data="reg",on_click=sign_input),alignment=ft.alignment.center,),

                        ],

                    ),
                    bgcolor=c_yelow,
                    width=301,
                    height=230,
                    padding=20,
                    margin=0,
                    border = ft.border.all(1, c_white)
                )
            )
            self.update()

        # функция авторизации - кнопка войти
        def sign_input(e):
            success_validation = {'1':0,'2':0,'3':0}
            # Валидация емаила
            if(re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', self.ref_email.current.value)):
                self.ref_email.current.border_color = c_white
                self.ref_email.current.label = 'Email'
                self.update()
                success_validation['1'] = 1
            else:
                self.ref_email.current.border_color = c_red
                self.ref_email.current.label = 'Некорректный Email'
                self.update()
                success_validation['1'] = 0
            # валидация паролей
            if re.fullmatch(r'[A-Za-z0-9]{8,}', self.ref_pass.current.value):
                self.ref_pass.current.border_color = c_white
                self.ref_pass.current.label = 'Пароль'
                success_validation['2'] = 1
                self.update()
            else:
                self.ref_pass.current.border_color = c_red
                self.ref_pass.current.label = 'A-Z + a-z + 0-9'
                self.update()
                success_validation['2'] = 0
            # валидация api-key
            if len(self.ref_api_key.current.value)>8:
                self.ref_api_key.current.border_color = c_white
                self.ref_api_key.current.label = 'Api-key'
                success_validation['3'] = 1
                self.update()
            else:
                self.ref_api_key.current.border_color = c_red
                self.ref_api_key.current.label = 'Некорректный Api-key'
                self.update()
                success_validation['3'] = 0
            # если валидация прошла успешно, отправляем запрос на вход в систему
            data_reg = {
                'email':self.ref_email.current.value,
                'password':self.ref_pass.current.value,
                'apikey':self.ref_api_key.current.value
            }
            if success_validation['1']==1 and success_validation['2']==1 and success_validation['3']==1:
                response = requests.post(server_ip+'/signinput',data=data_reg)
                # если получили ответ - успех, регистрация прошла успешно
                if response.json()['data']=='seccess':
                    print('Авторизация успешна')
                    # СЮДА ВСТАВЛЯЕМ ВХОД В ТЕРМИНАЛ!!!!!
                else: 
                    if response.json()['data']=='error':
                        self.controls = []
                        self.controls.append(
                            ft.Container(
                                ft.Container(
                                    ft.Column(
                                        controls=[
                                            ft.Text('Ошибка входа. Пароль или Api-key был введены неправильно. Проверьте правильность введённых данных и попробуйте еще раз',color=c_blue,text_align='center',),
                                            ft.Container(ft.ElevatedButton(text="Вернуться к регистрации",bgcolor=c_blue,color=c_white,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),),data="reg",on_click=open_reg_two),alignment=ft.alignment.center,),
                                        ]
                                    )
                                ),
                                bgcolor=c_yelow,
                                width=301,
                                height=230,
                                padding=ft.padding.only(top=60,left=20,right=20),
                                margin=0,
                                border = ft.border.all(1, c_white),
                            )
                        )
                        self.update()
                    if response.json()['data']=='user_not_found':
                        self.controls = []
                        self.controls.append(
                            ft.Container(
                                ft.Container(
                                    ft.Column(
                                        controls=[
                                            ft.Text('Пользователь с таким Email не найден. Вы можете зарегистрироваться на вкладке регистрация, либо проверьте правильность введённого email и попробуйте войти ещё раз.',color=c_blue,text_align='center',),
                                            ft.Container(ft.ElevatedButton(text="Вернуться к регистрации",bgcolor=c_blue,color=c_white,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),),data="reg",on_click=open_reg_two),alignment=ft.alignment.center,),
                                        ]
                                    )
                                ),
                                bgcolor=c_yelow,
                                width=301,
                                height=230,
                                padding=ft.padding.only(top=30,left=20,right=20),
                                margin=0,
                                border = ft.border.all(1, c_white),
                            )
                        )
                        self.update()
                
            

        # отработка клика по надписи оставаться в системе
        def vsisteme(e):
            if self.flag_ch == 0:
                self.checkbox_vsisteme.current.value=True
                self.flag_ch = 1
            else:
                self.checkbox_vsisteme.current.value=False
                self.flag_ch = 0
            self.update()

        self.ref_email = ft.Ref[ft.TextField]()
        self.ref_pass = ft.Ref[ft.TextField]()
        self.ref_api_key = ft.Ref[ft.TextField]()

        self.flag_ch=0
        self.checkbox_vsisteme = ft.Ref[ft.CupertinoCheckbox]()
        self.sign_in = ft.Container(
            ft.Column(
                controls=[
                    ft.TextField(ref = self.ref_email, label="Email",bgcolor=c_white,border_radius=0,border_color=c_white,height=30,color=c_blue,cursor_color=c_blue,cursor_height=22,text_align='center',content_padding= ft.padding.only(10),),
                    ft.TextField(ref = self.ref_pass, label="Пароль",password=True, can_reveal_password=True,bgcolor=c_white,border_radius=0,border_color=c_white,height=30,color=c_blue,cursor_color=c_blue,cursor_height=22,text_align='center',content_padding= ft.padding.only(10)),
                    ft.TextField(ref = self.ref_api_key, label="Api-key",password=True, can_reveal_password=True,bgcolor=c_white,border_radius=0,border_color=c_white,height=30,color=c_blue,cursor_color=c_blue,cursor_height=22,text_align='center',content_padding= ft.padding.only(10)),
                    ft.Container(
                        ft.Row(
                            controls=[
                                ft.CupertinoCheckbox(value=False,check_color=c_blue,active_color=c_yelow,inactive_color=c_blue,ref=self.checkbox_vsisteme),
                                ft.Container(ft.Text('Оставаться в системе',color=c_blue,),margin = ft.margin.only(left=-15),on_click=vsisteme)
                                
                            ]
                        ),margin = ft.margin.only(left=28,top=-12,bottom=-20)
                        # alignment=ft.alignment.center,
                    ),
                    ft.Container(ft.Text('Восстановить пароль',color=c_blue,size=12),margin = ft.margin.only(left=66,bottom=-2),on_click=vsisteme),
                    ft.Container(ft.ElevatedButton(text="Войти",bgcolor=c_blue,color=c_white,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),),data="reg",on_click=sign_input),alignment=ft.alignment.center,),
                    
                ],
                
            ),
            bgcolor=c_yelow,
            width=301,
            height=230,
            padding=20,
            margin=0,
            border = ft.border.all(1, c_white)
        )
        
        return self.sign_in