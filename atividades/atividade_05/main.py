"""atividade: Crie um programa que recebe do usuário o nome e aidade, e em seguida, mostre um menu de filmes com suas respectivas classificações indicativas e salas de exibição. Exemplo: 

- Sala 1: A Roda Quadrada - Livre 
- Sala 2: A Volta Dos Que Não Foram - 12 anos 
- Sala 3: Poeira em Alto Mar - 14 anos
- Sala 4: As Tranças do Rei Careca - 16 anos
- Sala 5: A Vingança do Peixe Frito - 18 anos

O usuário deve escolher a sala que está passando o filme que deseja assistir.
Se o usuário tiver idade mínima ou mais pra ver o filme, o programa imprime o ingresso com o nome do usuário, a sala, o nome do filme, a data e a hora da compra do ingresso, e deseje um bom filme, e em seguida encerra o programa.
Se o usuário não tiver a idade mínima pra ver o filme, o programa bloqueia a sua entrada, e re-exibe o menu de filmes para que ele escolha outro filme."""

# bibliotecas

import os
import datetime
from datetime import date

# setando hora e data
data = date.today().strftime("%d/%m/%y")
hora = datetime.datetime.now().strftime("%H:%M:%S")

#filmes das salas
sala1 = "A Roda Quadrada"
sala2 = "A Volta dos Que Não Foram"
sala3 = "Poeira em Alto Mar"
sala4 = "As Tranças do Rei Careca"
sala5 = "A Vingança do Peixe Frito"

# tratamento de exceção
try:
    nome = input("Informe o seu nome: ").title().strip()
    idade = int(input("Informe sua idade: "))

    while True:
        # menu
        print(f"{'-'*20} 🎞️ CINE COBRA 🎞️ {'-'*20}")
        print(f"Sala 1: {sala1} - Livre")
        print(f"Sala 2: {sala2} - 12 anos")
        print(f"Sala 3: {sala3} - 14 anos")
        print(f"Sala 4: {sala4} - 16 anos")
        print(f"Sala 5: {sala5} - 18 anos")
        sala = input("Informe a sala desejada: ").strip()
        os.system("cls" if os.name == "nt" else "clear")
        match sala:
            case "1":
                idadeMinima = 0
                filme = sala1
            case "2":
                idadeMinima = 12
                filme = sala2
            case "3":
                idadeMinima = 14
                filme = sala3
            case "4":
                idadeMinima = 16
                filme = sala4
            case "5":
                idadeMinima = 18
                filme = sala5
            case _:
                print("Sala inexistente, favor escolher outra sala")
                continue
        if idade >= idadeMinima:
            print(f"{'-'*20}🐍 INGRESSO CINE COBRA 🐍 {'-'*20}")
            print(f"{'-'*60}\n")
            print(f"🎦\nFilme: {filme} - {idadeMinima}")
            print(f"🎟️\nIngresso comprado por {nome} no dia {data} às {hora}")
            print("TENHA UM BOM FILME\n")
            print(f"{'-'*60}")
            break
        else:
            print(f"{nome} não possui idade mínima necessária para assistir {filme}.")
            print(f"Escolha outro filme.")
            continue
except Exception as e:
    print(f"Não foi possível compra ingresso. {e}")