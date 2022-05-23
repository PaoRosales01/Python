# Universidad Tecnológica de Durango
# Por: Paola Elizabeth Rosales Verdín
# Fecha: 28/02/2022
# Materia: Administración de Bases de Datos

# Agrega la librería general de pymongo
import pymongo
# Agrega la Funciónde MongoClient desde pymongo
from pymongo import MongoClient
import datetime
current_time=datetime.datetime.now()
# Se crea la conexión con Mongodb
con = MongoClient('localhost', 27017)
db  = con['sta_clara']


#Práctica 2        
def SaveLogs(table, action):
    data_log = {
        'accion:': action,
        'fecha': current_time,
        'tabla': table
    }
    FunctionInsert('log', data_log)
    

# Función para traer datos desde la db
def FunctionSelect(tabla, buscar, tipo):
    collection = db[tabla]
    if tipo == 'one':
        resultados = collection.find_one(buscar)
    elif tipo == 'all':
        # Creando de un query una lista para poder obtener la info
        resultados = list(collection.find(buscar))
        # Print a variable resultados
    return resultados


def FunctionInsert(tabla, datos):
    collection = db[tabla]
    if type(datos) == list:
        collection.insert_many(datos)
    else:
        collection.insert_one(datos)
    #SaveLogs(tabla, 'insert')


def FunctionDelete(tabla, dato):
    if type(dato) == list:
        tabla.delete_many(dato)
    else:
        tabla.delete_one(dato)


def FunctionUpdate(tabla, find, values):
    collection = db[tabla]
    new_values = { "$set": values }
    if type(find) == list:
        collection.update_many(find, new_values)
    else:
        collection.update_one(find, new_values)
    SaveLogs(tabla, 'update')

    
def Trigger_ofertas(buscar, tabla_productos,precio):
    #Actualizar el producto por nombre y cambiar precio
    FunctionUpdate(tabla_productos,buscar, precio)
    #Seleccionamos la colección
    collection = db[tabla_productos]
    #Busca en la colección por nombre para traer un elemento
    resultado = collection.find_one(buscar)
    #declaramos el documento que se guarda en ofertas
    datos_oferta = {
        'producto_id': resultado['_id'],
        'precio': resultado['precio']
    }
    FunctionInsert('ofertas', datos_oferta)

#FunctionInsert('productos', datos_insert)
#print(FunctionSelect('logs', {}, 'all'))
#Trigger_ofertas({'nombre':'DICLOFENACO'}, 'productos', {'precio':100})
#print(oferta['producto']['nombre'])