import PessoaFisica
import PessoaJuridica
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = PessoaFisica.PessoaFisica(emai="", telefone="", endereco="", nome="", cpf="", idade=0)
    empresa = PessoaJuridica.PessoaJuridica(email="", telefone="", endereco="", razaoSocial="", nomeFantasia="", cnpj="")

    # input do usuario
    print("Informe os dados do usuário: \n")
    usuario.nome = input("Informe seu nome: ").strip().title()
    usuario.cpf = input("Informe seu CPF: ").strip()
    usuario.idade = int(input("Informe sua idade: ").strip())
    usuario.email = input("Informe seu email: ").strip()
    usuario.telefone = input("Informe seu telefone: ").strip()
    usuario.endereco = input("Informe seu endereço: ").strip()
    limpar()

    # input da empresa
    print("Informe os dados da empresa: \n")
    empresa.razaoSocial = input("Informe a razão social: ").strip().title()
    empresa.nomeFantasia = input("Informe o nome fantasia: ").strip().title()
    empresa.cnpj = input("Informe o CNPJ: ").strip()
    empresa.email = input("Informe o email da empresa: ").strip()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    empresa.endereco = input("Informe o endereço da empresa: ").strip()
    limpar()

    print(usuario)
    print(empresa)
if __name__ == "__main__":
    main()