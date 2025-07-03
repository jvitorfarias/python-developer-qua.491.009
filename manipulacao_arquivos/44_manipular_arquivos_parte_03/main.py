import os

while True:
    try:
        novoTexto = input("Digite o texto:\n")
        nomeArquivo = input("Dê o nome do arquivo (sem extensão): ").strip().lower()
        with open(f"44_manipular_arquivos_parte_03/{nomeArquivo}.txt", "w", encoding = "utf-8") as f:
            f.write(novoTexto)
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{nomeArquivo}.txt gravado com sucesso.")
        while True:
            prosseguir = input("Deseja gravar um novo arquivo? s/n").strip().lower()
            if prosseguir == "s" or prosseguir == "n":
                break
            else:
                print("Opção inválida.")
                continue
        match prosseguir:
            case "s":
                continue
            case "n":
                break
    except Exception as e:
        print(f"Não foi possível gravar arquivo. {e}.")
        continue