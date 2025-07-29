"""
# TODO - Atividade: Faça um CRUD (Create, Read, Update, Delete) em um JSON.
Opções do menu:
- Criar novo arquivo JSON. (O usuário irá informar o diretório)
- Abrir o arquivo JSON. (O usuário irá informar o diretório)
- Cadastrar novo usuário.
- Listar todos os usuários de um arquivo JSON.
- Pesquisar por um usuário de um arquivo JSON.
- Alterar dados de um usuário em um arquivo JSON.
- Deletar usuário de um arquivo JSON.
- Sair do programa.
Dados do usuário:
- Nome
- Data de nascimento
- CPF
- Email
- Telefone
- Filme favorito do usuário
"""

import json
import os

usuarios = []

while True:
    usuario = {}
    print("1 - Criar novo arquivo JSON.")
    print("2 - Abrir o arquivo.")
    print("3 - Cadastrar novo usuário.")
    print("4 - Listar usuários cadastrados.")
    print("5 - Pesquisar por um usuário.")
    print("6 - Alterar dados de um usuário.")
    print("7 - Deletar um usuário.")
    print("8 - Sair do programa.")

    opcao = input("Informe a opção desejada: ")
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            ...
        case "2":
            ...
        case "3":
            ...
        case "4":
            ...
        case "5":
            ...
        case "6":
            ...
        case "7":
            ...
        case "8":
            print("Programa encerrado com sucesso. ")
            break
            