from conta.conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo, limite=100):
        super().__init__(agencia, numero_conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, value):
        if (self.saldo + self.limite) >= value:
            self._saldo -= value
            self.detalhes()
        else:
            print('Saldo Insuficiente!')
            
