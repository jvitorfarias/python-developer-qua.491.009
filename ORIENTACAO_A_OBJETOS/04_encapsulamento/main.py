import classes as c
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = c.PessoaFisica(nome="", cpf="", telefone="", endereco="")
    empresa = c.PessoaJuridica(nomeFantasia="", cnpj="", telefone="", endereco="")

    # setando os valores do usuario
    print("Insira os dados do usuario:\n")

    usuario.nome = input("Informe o nome: ").strip().title() #set
    usuario.cpf = input("Informe o cpf: ").strip() #set
    usuario.telefone = input("Informe o telefone: ").strip() #set
    usuario.endereco = input("Informe o endereco: ").strip().title() #set

    limpar()

    empresa.nomeFantasia = input("Informe o nome da empresa: ").strip().title()
    empresa.cnpj = input("Informe o CNPJ da empresa: ").strip().title()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    empresa.endereco = input("Informe o endereco da empresa: ").strip().title()

    limpar()

    # chamando os metodos get
    print("Dados do usuario:\n")
    print(f"Nome do usuário: {usuario.nome}")
    print(f"CPF do usuário: {usuario.cpf}")
    print(f"Telefone do usuário: {usuario.telefone}")
    print(f"Endereco do usuário: {usuario.endereco}")

    print("Dados da empresa:\n")
    print(f"Nome da empresa: {empresa.nomeFantasia}")
    print(f"CNPJ da empresa: {empresa.cnpj}")
    print(f"Telefone da empresa: {empresa.telefone}")
    print(f"Endereco da empresa: {empresa.endereco}")

if __name__ == "__main__":
    main()