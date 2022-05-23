# Universidad Tecnológica de Durango
# Por: Paola Elizabeth Rosales Verdín
# Fecha: 28/03/2022
# Materia: Administración de Bases de Datos

import pandas as pd
import matplotlib.pyplot as plt

#crosstab
#Agregar el archivo para análisis con pandas
df = pd.read_csv('users_modify.csv')
#Seleccionar las columnas a procesar
df = df[['gender', 'role']]
#Crear un cruce entre columnas y filas
ct = pd.crosstab(df['gender'], df['role']).plot(kind='bar')
plt.title('Gráfica para cruce de género y role')
plt.xlabel("Género")
plt.ylabel("Rol")
for barra in ct.containers:
    ct.bar_label(barra,label_type='edge')

plt.show()
