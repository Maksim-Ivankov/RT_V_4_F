import flet as ft

def main(page: ft.Page):
    page.title = "GridView Example"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50
    page.update()
    images = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )
    page.add(images)
    for i in range(0, 60):
        images.controls.append(
            ft.Text('qwfqwfqw')
        )
    page.update()
ft.app(target=main)