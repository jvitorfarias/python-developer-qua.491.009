import flet as ft


def main(page: ft.Page):
    #funcao do evento
    def exibirTexto(e):
        result.value = texto.value
        page.update()

    #propriedades da página
    page.title = "Eventos"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    #variaveis
    texto = ft.TextField(label="Digite aqui o seu texto")
    result = ft.Text()

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("App Evento", size=30, weight="bold"),
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
        texto,
        ft.ElevatedButton("Enviar", on_click=exibirTexto),
        result
    )


ft.app(main)
