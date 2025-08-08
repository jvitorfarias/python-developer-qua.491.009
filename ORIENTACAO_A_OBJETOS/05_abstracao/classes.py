from abc import ABC
from abc import abstractmethod 

# classe abstrata
class Conta:
    @abstractmethod
    def __init__(self, saldo):
        # atributos private
        self.__saldo = saldo

    # metodos get e set
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    # metodos de acao
    @abstractmethod
    def consultarDados(self):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

class ContaCorrente(Conta):
    def __init__(self, titular, cpf, agencia, conta, saldo):
        self.__titular = titular
        self.__cpf = cpf
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo
        super().__init__(saldo)

    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    # cpf
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    # agencia
    @property
    def agencia(self):
        return self.__agencia
    
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    # conta
    @property
    def conta(self):
        return self.__conta
    
    @conta.setter
    def conta(self, conta):
        self.__conta = conta

    # metodos da interface
    def consultarDados(self):
        print(f"{'-'*20} DADOS DA CONTA {'-'*20}")
        print(f"Titular: {self.__titular}")
        print(f"CPF: {self.__cpf}")
        print(f"Agência: {self.__agencia}")
        print(f"Conta: {self.__conta}")
        print(f"Saldo: R$ {self.__saldo:.2f}")

    def depositar(self, valor):
        self.__saldo += valor
        return self.__saldo
    
    def sacar(self, valor):
        self.__saldo -= valor
        return self.__saldo