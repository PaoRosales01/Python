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
# Fecha: 07/04/2022
# Materia: Administración de Bases de Datos

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Agregar el archivo para anáñlisis con pandas para previsualizarlo
df = pd.read_csv('banco.csv')

#Dimensión del csv
#print(df.shape)

#Datos faltantes
#print(df.isnull())
print(df.isna().sum())

#Tipos de datos del dataset en general
#print(df.dtypes)

#Obtener los tipos de datos por columna
#col_names = df.columns.tolist()

#Iterar sobre la lista
#for column in col_names:
# print(df[column].dtypes)
 
 #Info
#print(df.describe())
 
#Describre
#print(df.info())
 
 #Datos duplicados
#print(df.duplicated().sum())
 

