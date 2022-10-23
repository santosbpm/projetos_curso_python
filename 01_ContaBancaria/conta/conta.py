from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, value):
        self._agencia = value

    
    @property
    def numero_conta(self):
        return self._numero_conta

    @numero_conta.setter
    def numero_conta(self, value):
        self._numero_conta = value

    @property
    def saldo(self):
        return self._saldo

    def detalhes(self):
        print(f'Agência: {self.agencia}\n'
              f'Conta: {self.numero_conta}\n'
              f'Saldo: {self.saldo}')

    def depositar(self, value):
        self._saldo += value
        self.detalhes()

    @abstractmethod
    def sacar(self, value):
        pass

