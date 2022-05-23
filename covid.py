# Universidad Tecnológica de Durango
# Por: Paola Elizabeth Rosales Verdín
# Fecha: 20/04/2022
# Materia: Administración de Bases de Datos
# PROYECTO FINAL

import pandas as pd
import matplotlib.pyplot as plt

#Agregar el archivo para análisis con pandas para previsualizarlo
df = pd.read_csv('mexico_covid19.csv')
#df = pd.read_csv('covid_modify.csv')

#ANÁLISIS DEL DATASET

#Dimensión del csv
#print(df.shape)

#Datos de cada columna
#print(df.count())

#Datos faltantes por columna
# col_names = df.columns.tolist()

# #Iterar sobre la lista
# for column in col_names:
#   print("Valores nulos en <" + column + "> " + str(df[column].isnull().sum()))

#Obtener los tipos de datos por columna
col_types = df.columns.tolist()

#Iterar sobre la lista
for column in col_types:
    print("Tipo de dato en <" + column + "> " + str(df[column].dtypes))
 
#Datos duplicados
#print(df.duplicated().sum())


#LIMPIAR Y ESTANDARIZAR DATOS

#Reemplazar las filas que contienen el dato indicado por nuevos
# df['SEXO'] = df['SEXO'].map({1:'Hombre', 2:'Mujer'})
# df['INTUBADO'] = df['INTUBADO'].map({0:'No', 1:'Sí'})
# df['EMBARAZO'] = df['EMBARAZO'].map({1:'Negativo', 2:'Positivo'})
# df['DIABETES'] = df['DIABETES'].map({0:'Negativo', 1:'Positivo'})
# df['ASMA'] = df['ASMA'].map({0:'Negativo', 1:'Positivo'})
# df['HIPERTENSION'] = df['HIPERTENSION'].map({0:'Negativo', 1:'Positivo'})
# df['CARDIOVASCULAR'] = df['CARDIOVASCULAR'].map({1:'Negativo', 2:'Positivo'})
# df['OBESIDAD'] = df['OBESIDAD'].map({1:'Negativo', 2:'Positivo'})
# df['TABAQUISMO'] = df['TABAQUISMO'].map({1:'No', 2:'Sí'})
# df['PAIS_NACIONALIDAD'] = df['PAIS_NACIONALIDAD'].map({'MX':'México', '99':'Desconocido', 'EUA':'Estados Unidos de América', 'ESP':'España'})
# df['UCI'] = df['UCI'].map({97:'No ingresó', 2:'Ingresó'})

#Guardar una copia con las columnas modificadas 
# df.to_csv('covid_modify.csv', index=False, encoding='utf-8-sig')


#GRÁFICOS

#Gráfico de cantidad de pacientes asmáticos
# df['ASMA'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['#97F98F', '#F9A19D'])
# plt.title('Pacientes asmáticos',  
#                 fontdict={'family': 'Verdana', 
#                     'color' : '#1F2B6C',
#                     'weight': 'bold',
#                     'size': 18})	
# plt.show()


#CRUCE DE TABLA

#Crosstab de la influencia del tabaquismo e intubación
# ct = pd.crosstab(df['INTUBADO'], df['TABAQUISMO']).plot(kind='bar', color=['#FBC0ED', '#B2F5F7'])
# plt.title('¿Influye el tabaquismo en ser intubado?',
#            fontdict={'family': 'Verdana', 
#                      'color' : '#1F2B6C',
#                      'weight': 'bold',
#                      'size': 18})
# plt.xlabel("INTUBADO")
# plt.ylabel("TABAQUISMO")
# plt.show()

#Crosstab de la influencia de la obesidad e ingreso a UCI
# ct = pd.crosstab(df['UCI'], df['OBESIDAD']).plot(kind='barh', color=['#CEB2F7', '#B2D0F7'])
# plt.title('INGRESOS DE OBESIDAD A UCI',
#            fontdict={'family': 'Verdana', 
#                      'color' : '#1F2B6C',
#                      'weight': 'bold',
#                      'size': 18})
# plt.xlabel("OBESIDAD")
# plt.ylabel("UCI")
# plt.show()

#AGRUPAR POR FECHAS DE SÍNTOMAS E INGRESO
# pclass_covid = df.groupby(['FECHA_SINTOMAS','FECHA_INGRESO'])
# print(pclass_covid)
# print(pclass_covid.size().reset_index(name='counts'))
 
  
 
#INFORMACIÓN ADICIONAL DEL DATASET

#Describe
#print(df.describe())
 
#Info
#print(df.info())
 

