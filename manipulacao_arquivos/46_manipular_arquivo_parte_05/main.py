try:
    arquivo = input("Informe o nome do arquivo: ").strip().lower()
    with open(f"{arquivo}.txt", "r", encoding="utf-8") as f:
        texto = f.read()
    print(f"Texto gravado:\n{texto}")

    novoTexto = input("Digite o novo texto:\n")
    novaGravacao = f"{texto}\n{novoTexto}"

    with open(f"{arquivo}.txt", "w", encoding="utf-8") as f:
        f.write(novaGravacao)
    print("Gravação do novo texto conluída com sucesso!")

    with open(f"{arquivo}.txt", "r", encoding="utf-8") as f:
        textoFinal = f.read()
    print(f"Texto final: {textoFinal}")
except Exception as e:
    print(f"Não foi possível atualizar o conteúdo. {e}")