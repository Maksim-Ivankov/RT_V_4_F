import flet as ft
from time import sleep
import time, threading

class Stakan_column(ft.UserControl):
    def __init__(self):
        super().__init__()


    def did_mount(self):
        self.running = True
        self.myThread = threading.Thread(target=self.update_data, args=(), daemon=True)
        self.myThread.start()

    def update_data(self):
        while self.running:
            print(time.strftime("%d.%m.%Y г. %H:%M:%S", time.localtime()))
            self.controls[0].value = time.strftime("%d.%m.%Y г. %H:%M:%S", time.localtime())
            time.sleep(1)
            self.update()

    
    

    def build(self):
        
        self.stakan_column = ft.Text('Здарова')

        return self.stakan_column
   






















