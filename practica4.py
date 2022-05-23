# Universidad Tecnológica de Durango
# Por: Paola Elizabeth Rosales Verdín
# Fecha: 23/03/2022
# Materia: Administración de Bases de Datos

import pandas as pd
import matplotlib.pyplot as plt

#Crear tablas sencillas con count
df = pd.read_csv('users_modify.csv')
#Seleccionar solamente las columnas department, active y favorite_app
df = df[['role']]
# df['department'].value_counts().plot(kind='barh')
# plt.show()
# df['active'].value_counts().plot(kind='pie')
# plt.show()
df['role'].value_counts().plot(kind='bar')
plt.show()
#CTRL K C
