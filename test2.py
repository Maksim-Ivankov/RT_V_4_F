import flet as ft



class Main:
    def __init__(self):
        None

    def run(self, page):
        self.page: ft.Page = page
        self.page.title = "RoboTrade"
        self.page.window_height, self.page.window_width = 1000, 400
        self.page.theme_mode = "dark" 
        
        
        
        
        self.page.add(ft.Text('123123'))




if __name__ == '__main__':
    main = Main()
    ft.app(target=Main().run, assets_dir="assets")