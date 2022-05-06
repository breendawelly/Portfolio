import pandas as pd

tabela = pd.read_csv('Prepared/top50.csv', ';')
print(tabela)

#------------------------------------
05.05.22
import pandas as pd

tabela = pd.read_csv("Prepared/top50.csv", sep=',',encoding='latin-1')
print(tabela.loc['Popularity'])


#tabelaOrganizada = pd.DataFrame(tabela)
#print(tabelaOrganizada)
#tabelaOrganizada['Popularity']
#tabelaOrganizada.loc[[0]]


------------------------------------------
05.05.22
tabela = pd.read_csv("Prepared/top50.csv", sep=',',encoding='latin-1')
#print(tabela.loc['Popularity'])
#print(tabela)

#qtdArtistas = tabela['Artist.Name'].value_counts() #.values_counts() para contar total
qtdArtistas = tabela['Artist.Name'].nunique() #.nunique é usado para count distinct
print(qtdArtistas)

#qtdArtistas = tabela.value_counts['Artist.Name'].unique()
#qtdArtistas = count(tabela['Artist.Name'])
#qtdArtistas = tabela.count['Artist.Name']


----------------------------------------

#MEDIA
#dancabilidade = (tabela['Danceability'],numpy.mean('Danceability'))
#dancabilidade=numpy.mean('Danceability')
dancabilidade=tabela['Danceability'].mean()


print(dancabilidade)

#print ("The mean is =",numpy.mean(listnumbers)) Danceability

-----------------------------------------------------

O PROJETO PASSOU DISSO

import csv

with open('Prepared/top50.csv','r') as entrada:
    ler = csv.reader(entrada)
    for i,linha in enumerate(ler):
        print(linha)

PRA ISSO 

import numpy
import pandas as pd

tabela = pd.read_csv("Prepared/top50.csv", sep=',',encoding='latin-1')

#VALORES UNICOS
qtdArtistas = tabela['Artist.Name'].nunique() #.nunique é usado para count distinct
qtdMusicas = tabela['Track.Name'].nunique()

#MEDIA
dancabilidade=tabela['Danceability'].mean()
energia=tabela['Energy'].mean()
duracao=tabela['Beats.Per.Minute'].mean()
print(dancabilidade, energia,duracao)

#O TOP 5 FAREI NO DASH POIS HAVERÁ FILTROS E ESSE VALOR MUDARÁ 

TODO O ETL PRONTO, AGORA É SÓ JOGO NO TABLEAU. iMPORTANTE FAZER O MESMO COM O TOP100