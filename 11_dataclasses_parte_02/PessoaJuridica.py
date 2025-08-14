import Pessoa
from dataclasses import dataclass

@dataclass
class PessoaJuridica(Pessoa.Pessoa):
    razaoSocial: str
    nomeFantasia: str
    cnpj: str

    def __str__(self):
        return f"{'-'*20} Dados da empresa: {'-'*20}\n\nRazão Social: {self.razaoSocial}\nNome da Empresa: {self.nomeFantasia}\nCNPJ: {self.cnpj}\nEmail: {self.email}\nTelefone: {self.telefone}\nEndereço: {self.endereco}"