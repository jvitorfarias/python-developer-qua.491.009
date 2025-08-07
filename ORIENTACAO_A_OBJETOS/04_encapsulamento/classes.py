# superClasse

class Pessoa:
    def __init__(self, telefone, endereco):
        self.__telefone = telefone # private
        self.__endereco = endereco # private

    # metodos de acesso


    # metodo get telefone
    @property #get
    def telefone(self):
        return self.__telefone

    # metodo set telefone
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property #get
    def endereco(self):
        return self.__endereco
    
    @telefone.setter
    def endereco(self, endereco):
        self.__endereco = endereco

class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        super().__init__(telefone, endereco)

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    
    @nome.setter
    def cpf(self, cpf):
        self.__nome = cpf

class PessoaJuridica(Pessoa):
    def __init__(self, nomeFantasia, cnpj, telefone, endereco):
        self.__nomeFantasia
        self.__cnpj
        super().__init__(telefone, endereco)

    @property
    def nomeFantasia(self):
        return self.__nomeFantasia
    
    @nomeFantasia.setter
    def nome(self, nomeFantasia):
        self.__nomeFantasia= nomeFantasia

    @property
    def cnpj(self):
        return self.__cnpj
    
    @cnpj.setter
    def nome(self, cnpj):
        self.__cnpj = cnpj
    