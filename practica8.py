# Universidad Tecnológica de Durango
# Por: Paola Elizabeth Rosales Verdín
# Fecha: 31/03/2022
# Materia: Administración de Bases de Datos

import pandas as pd
import matplotlib.pyplot as plt

#Agregar el archivo para anáñlisis con pandas
df = pd.read_csv('movie_metadata.csv')

#Previsualizar el archivo
#print(df.head())

#Dimensión del dataframe
#print(df.shape)

#Conocer la cantidad de datos faltantes por cada columna
#print(df.count())

#Obtener los nombres de las columnas en una lista
# col_names = df.columns.tolist()

# # #Iterar sobre la lista
# for column in col_names:
#     print("Valores nulos en <" + column + ">" + str(df[column].isnull().sum()))

#df['color'] = df['color'].fillna('Color')
#Cambiar un diccionario con los valores originales por valores de reemplazo
# d = {'Color': 'Glow', 'Black and White': 'BN'}
# #Utilizamos una lambda para el reemplazo en una sola línea
# df['color']= df['color'].apply(lambda x:d[x])

# #Checar el cambio
# print(df['color'].head())

#Cruce de tabla
ct = pd.crosstab(df['color'], df['duration']).plot(kind='bar')
plt.xlabel("Nombre del director")
plt.ylabel("Presupuesto")
for barra in ct.containers:
    ct.bar_label(barra, label_type='edge') 
    
plt.show()

#Agrupar por clase y género la suma de los sobrevivientes
pclass_color = df.groupby(['budget','duration'])['color'].sum()
print(pclass_color)

#Crear una figura de 15x15
# plt.figure(figsize=(15,15))
# #Crear dos columnas para renderizar varias gráficas
# #plt.subplot2grid((2,3), (0,0))
# t = df['duration'].value_counts().plot(kind='bar')
# plt.title("Duración - Total")
# plt.xlabel("Duración")
# plt.ylabel("Cantidad total")
# # Agregar valor a cada barra
# for container in t.containers:
#     t.bar_label(container, label_type='edge')
    
#plt.show()
