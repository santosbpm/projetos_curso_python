from banco.banco import Banco
from cliente.cliente import Cliente
from conta.contacorrente import ContaCorrente
from conta.contapoupanca import ContaPoupanca

banco = Banco()

cliente1 = Cliente('Marcos', 25)
cliente2 = Cliente('Paulo', 26)
cliente3 = Cliente('Maria', 32)

conta1 = ContaPoupanca(1111, 254136, 0)
conta2 = ContaCorrente(2222, 254137, 0)
conta3 = ContaPoupanca(1212, 254138, 0)

cliente1.conta = conta1
cliente2.conta = conta2
cliente3.conta = conta3

banco.inserir_clientes(cliente1)
banco.inserir_conta(conta1)

banco.inserir_clientes(cliente2)
banco.inserir_conta(conta2)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(0)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado.')

print('####################')

if banco.autenticar(cliente2):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(20)
else:
    print('Cliente não autenticado.')
