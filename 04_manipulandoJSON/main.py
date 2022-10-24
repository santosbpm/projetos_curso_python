import json
from dados import *

with open('clientes.json', 'w') as arquivo:
    json.dump(clientes_dicionario, arquivo, indent=4)

with open('clientes.json', 'r') as arquivo:
    data = json.load(arquivo)
    print(type(data))
    print(f'\n\n{data}')
