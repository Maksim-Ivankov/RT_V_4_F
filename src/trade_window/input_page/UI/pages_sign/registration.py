
import flet as ft
from variable import *
from imports import *
import re

class Registration(ft.UserControl):


    def build(self):

        def registration(e):
            # response = requests.get(server_ip+'/test')
            # print(response.json())
            # if response.status_code == 200:
            #     print('Данные получены успешно!')
            
            success_validation = True
            # Валидация емаила
            if(re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', self.ref_email.current.value)):
                self.ref_email.current.border_color = c_white
                self.ref_email.current.label = 'Email'
                self.update()
                success_validation = True
            else:
                self.ref_email.current.border_color = c_red
                self.ref_email.current.label = 'Некорректный Email'
                self.update()
                success_validation = False
            # валидация паролей
            if self.ref_pass.current.value == self.ref_pass_two.current.value:
                self.ref_pass.current.border_color = c_white
                self.ref_pass.current.label = 'Пароль'
                self.update()
                success_validation = True
            else:
                self.ref_pass.current.border_color = c_red
                self.ref_pass.current.label = 'Пароли отличаются'
                self.update()
                success_validation = False
            if re.fullmatch(r'[A-Za-z0-9]{8,}', self.ref_pass.current.value):
                self.ref_pass.current.border_color = c_white
                self.ref_pass.current.label = 'Пароль'
                success_validation = True
                self.update()
            else:
                self.ref_pass.current.border_color = c_red
                self.ref_pass.current.label = 'A-Z + a-z + 0-9'
                self.update()
                success_validation = False
            data_reg = {
                'email':self.ref_email.current.value,
                'password':self.ref_pass.current.value
            }
            if success_validation == True:
                response = requests.post(server_ip+'/registration',data=data_reg)
                print(response)
           

        self.ref_email = ft.Ref[ft.TextField]()
        self.ref_pass = ft.Ref[ft.TextField]()
        self.ref_pass_two = ft.Ref[ft.TextField]()
        
        self.registration = ft.Container(
            ft.Column(
                controls=[
                    ft.TextField(ref=self.ref_email,label="Email",bgcolor=c_white,border_radius=0,border_color=c_white,height=30,color=c_blue,cursor_color=c_blue,cursor_height=22,text_align='center',content_padding= ft.padding.only(10),),
                    ft.TextField(ref=self.ref_pass,label="Пароль",password=True, can_reveal_password=True,bgcolor=c_white,border_radius=0,border_color=c_white,height=30,color=c_blue,cursor_color=c_blue,cursor_height=22,text_align='center',content_padding= ft.padding.only(10)),
                    ft.TextField(ref=self.ref_pass_two,label="Повторите пароль",password=True, can_reveal_password=True,bgcolor=c_white,border_radius=0,border_color=c_white,height=30,color=c_blue,cursor_color=c_blue,cursor_height=22,text_align='center',content_padding= ft.padding.only(10)),
                    ft.Container(ft.ElevatedButton(text="Зарегистрироваться",bgcolor=c_blue,color=c_white,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),),data="reg",on_click=registration),alignment=ft.alignment.center,),
                    ft.Text('Регистрируясь, вы соглашаетесь с Пользовательским соглашением и Политикой конфиденциальности',color=c_blue,size=10,text_align='center')
                    
                ],
                
            ),
            bgcolor=c_yelow,
            width=301,
            height=230,
            padding=20,
            margin=0,
            border = ft.border.all(1, c_white),
            
            
        )
        
        return self.registration