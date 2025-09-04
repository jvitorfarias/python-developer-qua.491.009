import flet as ft
from dataclasses import dataclass

#classe Pessoa
@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    salario: float
    email: str

def main(page: ft.Page):
    # funcao do evento
    def mostrarDados(e):
        saidaTitulo.value = "Dados do Usuário:\n"
        nome.value = f"Nome: {usuario.nome.value}"
        idade.value = f"Idade: {usuario.idade.value} anos"
        peso.value = f"Peso: {usuario.peso.value} kg"
        salario.value = f"Salário: {usuario.salario.value}"
        email.value = f"Email: {usuario.email.value}"

        page.update()

    # instancia a classe
    usuario = Pessoa(nome="", idade="", peso="", salario="", email="")

    # propriedades da pagina
    page.title = "Dados do usuário"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # seta os valores informados pelo usuario
    usuario.nome = ft.TextField(label="Nome")
    usuario.idade = ft.TextField(label="Idade", suffix_text="anos")
    usuario.peso = ft.TextField(label="Peso", suffix_text="kg")
    usuario.salario = ft.TextField(label="Salário", prefix_text="R$ ")
    usuario.email = ft.TextField(label="Email", on_submit=mostrarDados)

    # variaveis de saida
    saidaTitulo = ft.Text(weight="bold")
    nome = ft.Text()
    idade = ft.Text()
    peso = ft.Text()
    salario = ft.Text()
    email = ft.Text()

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Dados do usuário", size=30, weight="bold"),
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
        usuario.nome,
        usuario.idade,
        usuario.peso,
        usuario.salario,
        usuario.email,
        ft.ElevatedButton("Enviar", on_click=mostrarDados, ),
        saidaTitulo,
        nome,
        idade,
        peso,
        salario,
        email
    )


ft.app(main)
