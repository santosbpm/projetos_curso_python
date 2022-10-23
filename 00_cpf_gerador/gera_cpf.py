from valida_cpf import validador
from random import randint


def formata(cpf):
    formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'  # Formata a sequência de números para o padrão CPF
    return formatado


def gerador():  # Gera uma sequencia de numeros aleatórios
    while True:
        #  Cria uma sequência de números de 11 digitos e se não tiver o total é preenchido por zero com o zfill
        cpf = str(randint(00000000000, 99999999999)).zfill(11)
        if validador(cpf):  # Verifica a validade do cpf
            return formata(cpf)
