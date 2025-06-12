# tratamento de excecao
try:
    n = int(input("informe um número inteiro: ").replace(",", "."))
    print(f"Número informado: {n}")
except Exception as e:
    print(f"Não foi possível exibir o número. Error: {e}. Tente novamente.")
finally:
    print("Programa encerrado com sucesso.")