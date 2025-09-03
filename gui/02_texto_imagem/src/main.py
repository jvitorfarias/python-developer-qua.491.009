import flet as ft


def main(page: ft.Page):
    page.title = "Programinha maneiro"
    page.scroll = "adaptive"
    
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Column([ft.Text(
                        "Olá, mundo Flet Python!!!",
                        size=30,
                        weight="bold"
                    ),
                    ft.Text(
                        "🐍👌😁",
                        size=30
                    )])
            ),
            expand=True,
        ),
        ft.Image(
            src="/v627-aew-41-technologybackground.jpg",
            fit=ft.ImageFit.CONTAIN,
            error_content=ft.Text("Não foi possível abrir a imagem"),
            width=600
        )
    )


ft.app(target=main)
