import json
import os 

usuarios = []

while True:
    usuario = {}
    print("1 - Cadastrar nova chave e novo dado.")
    print("2 - Cadastrar novo usuário.")
    print("3 - Salvar arquivo JSON.")
    print("4 - Sair do programa.")
    opcao = input("Informe a opção desejada:")
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            usuario['nome'] = input("Informe o nome: ").strip().title()
            usuario['idade'] = input("Informe a idade: ")
            usuario['email'] = input("Informe o email: ").strip().lower()

            usuarios.append(usuario)
            os.system("cls" if os.name == "nt" else "clear")

            print("Usuário cadastrado com sucesso.")
            continue
        case "2":
            with open(f"50_json_parte_04/{novo_arquivo}.json", "w", encoding = "utf-8") as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=4)

                os.system("cls" if os.name == "nt" else "clear")

                print("Arquivo salvo com sucesso.")
                continue
        case "3":
            if not novo_arquivo:
                novo_arquivo = input("Informe o nome do arquivo: ").strip().lower()
            with open(f"50_json_parte_04/{novo_arquivo}.json", "r", encoding = "utf-8") as f:
                dados = json.load(f)
            print(f"{'-'*20} USUÁRIOS {'-'*20}\n")
            for usuarios in dados:
                for chave in usuario:
                    print(f"{chave.capitalize()}: {usuario.get(chave)}")
                print(f"{'-'*40}")
            continue
        case "4":
            print("Programa encerrado.")
            break
        case _:
            print("Opção inválida.")
            continue
        