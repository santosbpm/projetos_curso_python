import random
import string

def gerador(tamanho=12, numero=True, maiuscula=True, especial=False):
    senha = ''
    if numero:
        senha += string.digits

    if maiuscula:
        senha += string.ascii_letters
    else:
        senha += string.ascii_lowercase

    if especial:
        senha += string.punctuation

    senha = "".join(random.choices(senha, k=tamanho))

    return senha
    
