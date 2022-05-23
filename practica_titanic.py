# Universidad Tecnológica de Durango
# Por: Paola Elizabeth Rosales Verdín
# Fecha: 29/03/2022
# Materia: Administración de Bases de Datos

import pandas as pd
import matplotlib.pyplot as plt

#Agregar el archivo para anáñlisis con pandas
df = pd.read_csv('titanic.csv')

#Dimensión del dataframe
print(df.shape)

#Conocer la cantidad de datos faltantes por cada columna
#print(df.count())

#Obtener los nombres de las columnas en una lista
#col_names = df.columns.tolist()

#Iterar sobre la lista
#for column in col_names:
#    print("Valores nulos en <" + column + ">" + str(df[column].isnull().sum()))

#Cambiar un diccionario con los valores originales por valores de reemplazo
d = {'male': 'M', 'female': 'F'}
#utilizamos una lambda para el reemplazo en una sola línea
df['Sex']= df['Sex'].apply(lambda x:d[x])

#Checar el cambio
#print(df['Sex'].head())

#Cruce de tabla
ct = pd.crosstab(df['Survived'], df['Sex']).plot(kind='bar')
plt.xlabel("Sobrevivió")
plt.ylabel("Cantidad de sobrevivientes por género")
for barra in ct.containers:
    ct.bar_label(barra, label_type='edge') 
    
#plt.show()

#Agrupar por clase y género la suma de los sobrevivientes
pclass_survived = df.groupby(['Pclass','Sex'])['Survived'].sum()
#print(pclass_survived)

#Crear una figura de 15x15
plt.figure(figsize=(15,15))
#Crear dos columnas para renderizar varias gráficas
plt.subplot2grid((2,3), (0,0))
# Count de sobrevivientes y renderizarlo en tipo bar
t = df['Survived'].value_counts().plot(kind='bar')
plt.title("Sobrevivieron - Cuenta total")
plt.xlabel("Sobrevivió")
plt.ylabel("Cantidad de sobrevivientes")
# Agregar valor a cada barra
for container in t.containers:
    t.bar_label(container, label_type='edge')
    
plt.show()
