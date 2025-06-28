""" Atividade: Crie um programa que faça as seguintes funções: 
- Cadastre um novo usuário
- Liste todos os usuários cadastrados
- Altere os dados de um usuário
- Fazer sorteio de usuário
- Exclua um usuário 
- Saia do programa
# NOTE - Dados do usuário:
- Nome completo
- Data de Nascimento
- E-mail
- CPF
- Telefone 
- Gênero
- Data do cadastro (pegar do sistema)
- Hora do cadastro (pegar do sistema)
- Lista começa
"""

import os
import datetime 
from datetime import date
data = ...
hora = ...

lista = []

while True:
    dicionario = {}
    print("Seja bem vindo!")
    print("1 - Cadastrar um novo usuário")
    print("2 - Listar usuários cadastrados")
    print("3 - Alterar os dados de um usuário")
    print("4 - Sortear um usuário")
    print("5 - Excluir um usuário")
    print("6 - Sair do programa")
    opcao = print("Digite o número da opção desejada: ").strip()
    
    match opcao:
        case "1":
            dicionario['nome'] = input("Qual o nome completo do novo usuário: ").title().strip()
            dicionario['dataNascimento'] = input("Qual a data de nascimento: ")
            dicionario['email'] = input("Qual o email do novo usuario: ")
            dicionario['cpf'] = input("Qual telefone do novo usuario: ")
            dicionario['telefone'] = input("Qual telefone do novo usuario: ")
            dicionario['Genero'] = input("Qual genero do novo usuario: ")
            dicionario['dataCadastro'] = data
            dicionario['horaCadastro'] = hora
            lista.append[dicionario]
        case "2":
            for user in lista:
                print(lista)
        case "3":
            ...
        case "4":
            ...
        case "5":
            ...
        case "6":
            ...
        case _:
            ...