# Previsualizar Datos
# dimensión
# datos faltantes
# valores nulos
# tipo de datos que tiene el dataset en general y por columna
# usar .info
# usar .describe
# y datos duplicados en suma

# Universidad Tecnológica de Durango
# Por: Paola Elizabeth Rosales Verdín
# Fecha: 01/04/2022
# Materia: Administración de Bases de Datos

import pandas as pd
import matplotlib.pyplot as plt

#Agregar el archivo para análisis con pandas
df = pd.read_csv('banco.csv')

#Cambiar un diccionario con los valores originales por valores de reemplazo
d = {'Female': 'F', 'Male': 'M'}
#Utilizamos una lambda para el reemplazo en una sola línea
df['gender']= df['gender'].apply(lambda x:d[x])

#Cambiar un diccionario con los valores originales por valores de reemplazo
f = {'<=50K': '49', '>50K': '51'}
#Utilizamos una lambda para el reemplazo en una sola línea
df['income']= df['income'].apply(lambda x:f[x])


#Cruce de tabla
ct = pd.crosstab(df['gender'], df['income']).plot(kind='bar')
plt.xlabel("Género")
plt.ylabel("Ingreso")
for barra in ct.containers:
    ct.bar_label(barra, label_type='center') 
    
plt.show()
