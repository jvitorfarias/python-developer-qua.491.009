# lista
cidades = [
    "Konohagakure",
    "Sunagakure",
    "Kirigakure",
    "Iwagakure",
    "Iwagakure",
    "Amegakure",
    "Takigakure",
    "Otogakure",
    "Uzushiogakure",
    "Iwagakure",
    "Vale do Fim",
    "País do Ferro",
    "Caverna Ryūchi",
    "Monte Myōboku",
    "Konohagakure"
]

# usuário informa o nome da cidade a ser pesquisada
cidadePesquisada = input("Informe o nome da cidade: ").title().strip()

# programa conta quantas vezes ocorre o item pesquisado
qtde = cidades.count(cidadePesquisada)

# programa indica quantas vezes o item foi encontrado
print(f"{cidadePesquisada} foi encontrado {qtde} vezes na lista.")