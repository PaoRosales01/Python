# Universidad Tecnológica de Durango
# Por: Paola Elizabeth Rosales Verdín
# Fecha: 01/03/2022
# Materia: Administración de Bases de Datos

import pandas as pd
from pymongo import MongoClient

con        = MongoClient('localhost', 27017)
db         = con['sta_clara']
collection = db['productos']

# Crear una función para automatizar el export
# Debe de exportar todas las colecciones según requiera el usuario
def ExportPandas(tabla):
    collection = db[tabla]
    datos = list(collection.find())
    df  = pd.DataFrame(datos)
    #Exportar csv y xlsx
    df.to_csv(tabla +'.csv',index=False)
    df.to_excel(tabla +'.xlsx',index=False)
    
def exportar_datos(formato):
    # Obtener todos los nombres de las colecciones
    lista_collect = db.list_collection_names()
    for name in lista_collect:
        collection = db[name]
        datos = list(collection.find())
        df = pd.DataFrame(datos)
        if formato == 'CSV':
            df.to_csv(name +'.csv',index=False)
        elif formato == 'XLSX':
            df.to_excel(name +'.xlsx',index=False)


# Obtener un dataframe de la búsqueda de la colección
#datos = list(collection.find())
#df    = pd.DataFrame(datos)

# Exportar a Excel o CSV
#df.to_csv('productos.csv',index=False)
#df.to_excel('productos.xlsx',index=False)

#exportar_datos('CSV')

dfx = pd.read_csv('productos.csv')
print(dfx.head())

#backup
#Exportar una BD
#mongodump --db sta_clara --out C:\Users\paola\Desktop\backupmongo
#Importar una BD
#mongorestore --db sta_clara_backup C:\Users\paola\Desktop\backupmongo\sta_clara

