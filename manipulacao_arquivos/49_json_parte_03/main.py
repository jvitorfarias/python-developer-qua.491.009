import json

try:
    arquivo = input("Informe o arquivo: ").lower().strip()

    with open(f"{arquivo}.json", "r", encoding = "utf-8") as f:
        lista = json.load(f)

    for dado in lista:
        dado['altura'] = dado['altura'].replace(",", ".")
        dado['altura'] = float(dado['altura'])
        dado['peso'] = float(dado['peso'])

    # serializa o dicionário em json e grava o arquivo
    with open(f"{arquivo}.json", "w", encoding = "utf-8") as f:
        json.dump(lista, f, ensure_ascii = False, indent = 4)

    # confirmacao
    print("Conversão gravada com sucesso.")
except Exception as e:
    print(f"Não foi possível converter. {e}.")