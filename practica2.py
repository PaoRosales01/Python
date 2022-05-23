# Universidad Tecnológica de Durango
# Por: Paola Elizabeth Rosales Verdín
# Fecha: 15/03/2022
# Materia: Administración de Bases de Datos

import pandas as pd
import matplotlib.pyplot as plt

#Empezar a leer el archivo csv
df = pd.read_csv('users_data.csv')

#Informa datos estadísticos de un dataframe
#print(df.describe())

#Imprimir los nulos del dataframe
print(df.isnull())

# Rellenar las filas nulas de la columna lenguaje
df['lenguage'] = df['lenguage'].fillna('Other')

#Guardar una copia con las columnas modificadas
df.to_csv('users_modify.csv', index=False)