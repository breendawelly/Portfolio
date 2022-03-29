import csv

#1. abrir o arquivo
with open('', encoding='utf-8') as arquivo_referencia:

    #2. ler a tabela
    tabela = csv.reader(arquivo_referencia, delimiter=',')

