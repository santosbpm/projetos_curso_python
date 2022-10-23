from conta.conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, value):
        if value <= self.saldo:
            self._saldo -= value
            self.detalhes()
        else:
            print('Saldo insuficiente!')
