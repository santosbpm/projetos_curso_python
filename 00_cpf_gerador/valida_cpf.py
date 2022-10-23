"""
Script baseado nessa ideia

CPF = 004.034.440-12
CPF_INVERTIDO = 21(044430400)
------------------------------------------------
2 * 0  = 0            #    2 * 1  = 2
3 * 4  = 12           #    3 * 0  = 0
4 * 4  = 16           #    4 * 4  = 16
5 * 4  = 20           #    5 * 4  = 20
6 * 3  = 18           #    6 * 4  = 24
7 * 0  = 0            #    7 * 3  = 21
8 * 4  = 32           #    8 * 0  = 0
9 * 0  = 0            #    9 * 4  = 36
10 * 0 = 0            #    10 * 0 = 0
        98            #    11 * 0 = 0
11 - (98 % 11) = 1    #             119
1 > 9 = 1             #     11 - (119 % 11) = 2
                      #
Digito 1 = 1          #   Digito 2 = 2
"""


def sequencia(cpf):  # Verifica se o CPF é uma sequência (Ex.: 111.111.111-11)
    seq = cpf[0] * len(cpf)

    if seq == cpf:
        return True
    else:
        return False


def calcula_digitos(cpf):
    cpf_reverso = reversed(cpf)  # O reverso do cpf para encaixar com o índice que será multiplicado
    dig1 = dig2 = 0

    for index, valor in enumerate(cpf_reverso):  # Enumerate irá encaixar o índice com valor
        if 1 < index < 11:  # O calculo vai iniciar a partir do índice 2 tirando os digitos
            dig1 += int(valor) * index

        if index > 0:  # O calculo vai iniciar a partir do índice 1 tirando o primeiro digito que não entra no calculo
            dig2 += int(valor) * (index + 1)

    dig1 = 11 - (dig1 % 11)
    if 11 - (dig1 % 11) > 9:
        dig1 = 0
    dig2 = 11 - (dig2 % 11)

    return str(dig1) + str(dig2)  # Concatena os dois digitos para formar um string


def validador(cpf):
    # Verifica se os digitos do cpf são iguais ao do calculo e se o cpf não é uma sequência
    if calcula_digitos(cpf) == cpf[9:] and not sequencia(cpf):
        return True
    return False
