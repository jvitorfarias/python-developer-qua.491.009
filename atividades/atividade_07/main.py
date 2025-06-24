"atividade - Crie um programa que faça as seguintes operações:"
"- Cadastre novo nome na lista"
"- Liste todos os nomes da lista"
"- Pesquise por um nome na lista"
"- Altere um nome na lista"
"- Exclua um nome na lista"
"- Sair do programa"

garagem = []


print("Seja bem vindo a sua garagem!")

while True:
    novoCarro = input("Qual carro deseja cadastrar? ")
    garagem.append(novoCarro)
    

    for carro in garagem:
        print(carro)

