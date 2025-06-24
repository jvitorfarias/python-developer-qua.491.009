# lista
cidades = [
    'Brasília',
    'São Paulo',
    'Rio de Janeiro',
    'Teresina',
    'Belo horizonte',
    'Palmas'
]


# exibe a lista e seus respectivos indices
for i in range(len(cidades)):
    print(f"Índice {i}: {cidades[i]}.")

# tratamento de exceção    
try:
    # usuario informa o nome da nova cidade
    novaCidade = input("Informe o nome da nova cidade: ").title().strip()
    i = int(input("Informe a posição da lista onde deseja inserir: "))

    if i >= 0 and i <= len(cidades):
        cidades.insert(i, novaCidade)
        print("Cidade inserida com sucesso!")
    else:
        print("Índice inválido.")
# tratamento de exceção
except Exception as e:
    print(f"Não foi possível inserir o item na lista. {e}.")
finally:
    for i in range(len(cidades)):
        print(f"Índice {i}: {cidades[i]}.")