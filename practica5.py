# Universidad Tecnológica de Durango
# Por: Paola Elizabeth Rosales Verdín
# Fecha: 24/03/2022
# Materia: Administración de Bases de Datos

import pandas as pd
import matplotlib.pyplot as plt

#Group by
#Agregar el CSV al dataframe
df = pd.read_csv('usuarios_completo.csv')
#Seleccionar columnas para análisis
df = df[['is_admin', 'car']]
#print(df.head())
#Agrupar is_admin y car del dataframe
group = df.groupby(["is_admin", "car"])
print(group)
print(group.size().reset_index(name='counts'))
