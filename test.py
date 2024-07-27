import flet as ft

def main(page: ft.Page):


    def row_with_vertical_alignment():
        return ft.Column(
            [
                # ft.Text(str(align), size=16),
                ft.Container(
                    # content=ft.Row(items(3), vertical_alignment=align),
                    bgcolor='blue',
                    height=150,
                ),
            ]
        )

    page.add(
        row_with_vertical_alignment(),
    )

ft.app(target=main)