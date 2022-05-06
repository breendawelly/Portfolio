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