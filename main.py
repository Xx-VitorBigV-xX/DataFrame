import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('AmesHousing.csv')

print(df.head())


#Calculando Media de colunas especificas comando(.mean())
#Calculando SalePrice
print("--- Medias ---")
print(df['SalePrice'].mean())
#Calculando GrLivArea
print(df['Gr Liv Area'].mean())
#Calculando Overall Qual
print(df['Overall Qual'].mean())

#Calculando eMediana de colunas especificas comando(.median())
#Calculando mediana de SalePrice
print("\n--- Mediana ---")
print(df['SalePrice'].median())
print(df['Gr Liv Area'].median())
print(df['Overall Qual'].median())

#simetricas medias e medinas são próximas
#Assimetrica possitiva media é maior
#assimetrica negativa media é menor
print("verificando assimetria")
print(df['SalePrice'].hist())
print(df['Gr Liv Area'].hist())
print(df['Overall Qual'].hist())

#Verificando a moda de year Built (.mode())
print("moda de YearBuilt:",df['Year Built'].mode())

#Amplitude de SalePrice
print("Amplitude :",df['SalePrice'].max() - df['SalePrice'].min( ))

#variancia e desvio padrao de GrLivArea e OverallQual.
print("variancia Gr Liv Area:",df['Gr Liv Area'].var())
print("variancia OverallQual:",df['Overall Qual'].var())
print("Desvio-Padrao Gr Liv Area:",df['Gr Liv Area'].std())
print("Desvio padrao OverallQual:",df['Overall Qual'].std())

#coeficiente de variacao
CV = df['SalePrice'].std()/df['SalePrice'].mean()
print(CV*100)
#Heterogênea


# Calcular o 90º percentil da coluna 'Preço'
percentil_90 = df['SalePrice'].quantile(0.9)

# Filtrar os 10% mais caros
top_10_percento = df[df['SalePrice'] >= percentil_90]['SalePrice']
#preco dos imoveis mais caros
print(top_10_percento)

#Distancia interquartilica é a diferença entre Q3 e Q1
quantil3 = df['SalePrice'].quantile(0.25)
quantil1 = df['SalePrice'].quantile(0.75)
distancia_interquantilica = quantil3 - quantil1
print("\ndistacia interquantilica: ",distancia_interquantilica)

#definicao de outlines Inferior e Superior
limite_inferior = quantil1 - 2.5 * distancia_interquantilica
limite_superior = quantil3 + 2.5 * distancia_interquantilica

# Filtrar os outliers
outliers = df[(df['SalePrice'] < limite_inferior) | (df['SalePrice'] > limite_superior)]['SalePrice']

# Mostrar os outliers
print("Outliers detectados:")
print(outliers)

quantidade_registro_outline = len(outliers)
print("quantidade de registros outliner: ",quantidade_registro_outline)
total = len(df['SalePrice'])

# Exibir o total de registros na coluna
total_registros = len(df['SalePrice'])
print("Total de registros na coluna:", total_registros)


media = df['Overall Qual'].mean()
desvio_padrao = df['Overall Qual'].std()
z_scores = [(x - media) / desvio_padrao for x in df['Overall Qual']]

print("Z-scores:", z_scores)


print (df['Gr Liv Area'].corr(df['SalePrice']))
print(df['Total Bsmt SF'].corr(df['SalePrice']))
print( df['Overall Qual'].corr(df['SalePrice']))

# Classificação da correlação de Pearson (r):
# Correlação muito forte: r entre 0.8 e 1.0 (ou -0.8 a -1.0)
# Correlação forte: r entre 0.6 e 0.8 (ou -0.6 a -0.8)
# Correlação moderada: r entre 0.4 e 0.6 (ou -0.4 a -0.6)
# Correlação fraca: r entre 0.2 e 0.4 (ou -0.2 a -0.4)
# Nenhuma correlação: r entre -0.2 e 0.2
