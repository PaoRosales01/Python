# Universidad Tecnológica de Durango
# Por: Paola Elizabeth Rosales Verdín
# Fecha: 16/03/2022
# Materia: Administración de Bases de Datos

# Para el archivo usuarios incompletos, hacer lo siguiente:
# Company : agregar Other
# Car:  agregar Company
# App: agregar WhatsApp
# Avatar : agregar default
# Activo: agregar false *
# is_admin: agregar false *
# Department: agregar Other *
# Gender: agregar O *
# Nombre del archivo usuarios_completo
# Enviar código y archivo

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('usuarios_completo.csv')
df.plot(kind='scatter', x='gender', y='department')
plt.show()

#Empezar a leer el archivo csv
#df = pd.read_csv('users_modify.csv')


#Eliminar registros duplicados
#df.drop_duplicates(subset=['first_name', 'last_name', 'email'], keep='last', inplace=True)
#print(df.duplicated().sum())

#df.to_csv('usuariosmod.csv', index=False)

#Imprimir los nulos del dataframe
#print(df.isnull())

# Rellenar las filas nulas de la columna lenguaje
#df['company'] = df['company'].fillna('other')
#df['car'] = df['car'].fillna('company')
#df['favorite_app'] = df['favorite_app'].fillna('whatsApp')
#df['avatar'] = df['avatar'].fillna('https://robohash.org/default.png?size=50x50&set=set1')
#df['active'] = df['active'].fillna('false')
#df['is_admin'] = df['is_admin'].fillna('false')
#df['department'] = df['department'].fillna('other')
#df['gender'] = df['gender'].fillna('other')

#Rellenar las filas que contienen ese dato
#df['department'] = df['department'].replace('other','Other')
#df['gender'] = df['gender'].replace('other','O')
#df['active'] = df['active'].replace('false', False)
#df['is_admin'] = df['is_admin'].replace('false', False)
# df['company'] = df['company'].replace('other','Other')
# df['car'] = df['car'].replace('company', 'Company')
# df['favorite_app'] = df['favorite_app'].replace('whatsApp', 'WhatsApp')



#Guardar una copia con las columnas modificadas
#df.to_csv('usuarios_completo.csv', index=False)

