import flet as ft

if __name__ == "__main__":

    def main(page: ft.Page):

        page.title = "Flet Trello clone"
        page.padding = 0
        page.bgcolor = colors.BLUE_GREY_200
        app = TrelloApp(page)
        page.add(app)
        page.update()

ft.app(main)

# criando as classes
class TrelloApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.appbar_items = [
            ft.PopupMenuItem(text="Login"),
            ft.PopupMenuItem(),  # divider
            ft.PopupMenuItem(text="Settings")
        ]
        self.appbar = ft.AppBar(
            leading=ft.Icon(ft.Icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=ft.Text("Trolli",size=32, text_align="start"),
            center_title=False,
            toolbar_height=75,
            bgcolor=ft.Colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                ft.Container(
                    content=ft.PopupMenuButton(
                        items=self.appbar_items
                    ),
                    margin=ft.margin.only(left=50, right=25)
                )
            ],
        )
        self.page.appbar = self.appbar
        self.page.update()