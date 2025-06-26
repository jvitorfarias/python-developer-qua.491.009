# importacao
import os

# lista
nomes = ["Fulano", "Cicrano", "Beltrano", "João", "Maria", "José"]

# exibe a lista
for i in range(len(nomes)):
    print(f"{i}: {nomes[i]}")
print("=" * 60)

try:
    i = int(input("Informe o índice que deseja separar: "))
    if i >= 0 and i < len(nomes):
        nomeIsolado = nomes.pop(i)
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{nomeIsolado} separado com sucesso!")

        for i in range(len(nomes)):
            print(f"{i}: {nomes[i]}")
        print("=" * 60)

        print(f"Valor isolado da lista: {nomeIsolado}")
    else:
        print("Índice inválido")
except Exception as e:
    print(f"Não foi possível executar a operação. {e}.")