try:
    arquivo = input("informe o nome do arquivo (sem extensão): ").strip().lower()
    with open(f"{arquivo}.txt", "r", encoding = "utf-8") as f:
        texto = f.read()
    print(texto)

    novoTexto = input("Digite o novo texto:\n")

    with open(f"{arquivo}.txt", "w", encoding = "utf-8") as f:
        f.write(novoTexto)
except Exception as e:
    print(f"Não foi possível atualizar o arquivo. {e}.")

