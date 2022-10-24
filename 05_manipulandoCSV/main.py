import csv

with open('clientes.csv', 'r') as arquivo:
    dados = csv.reader(arquivo)
    # dados = csv.DictReader(arquivo)

    for dado in dados:
        print(dado)
        #print(dado['Nome'], dado['Sobrenome'])

