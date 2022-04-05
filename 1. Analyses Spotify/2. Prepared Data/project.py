import csv


#1. abrir o arquivo
with open('top50.csv', encoding='utf-8') as arquivo_referencia:

    #2. ler a tabela
    tabela = csv.reader(arquivo_referencia, delimiter=',')

    #3. Navegar pela tabela
    for l in tabela:
        id_autor = l[0]
        nome = l[1]

        print(id_autor, nome)

