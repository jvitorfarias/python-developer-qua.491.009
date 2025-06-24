nomes = [
    'Sasuke',
    'Naruto',
    'Sakura',
    'Kakashi',
    'Sai',
    'Yamato'
]

# exibe a lista
for nome in nomes:
    print(nome)

# usuario informa nome a ser acrescentado na lista
novo_nome = input("Informe o novo nome: ").title().strip()

# novo nome
nomes.append(novo_nome)

# reexibe a lista
for nome in nomes:
    print(nome)