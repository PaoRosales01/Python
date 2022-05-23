# Universidad Tecnológica de Durango
# Por: Paola Elizabeth Rosales Verdín
# Fecha: 20/02/2022
# Materia: Administración de Bases de Datos

#Agrega la librería general de pymongo
import pymongo
#Agrega la función de MongoClient desde pymongo
from pymongo import MongoClient

#Se crea la conexión con Mongodb
con        = MongoClient('localhost', 27017)
db         = con['escolares']
collection = db['escuelas']

#Función para ver datos desde la base de datos
def FunctionSelect(tabla):
    #Esta variable crea un query de una lista para poder obtener la info
    resultados = list(tabla.find())
    #Print a variable resultados
    print(resultados)
    
#Función para insertar datos a la base de datos, recibe dos parametros de tabla y datos
def FunctionInsert(tabla, datos):
    
    #En el if detecta si el dato es una lista o un diccionario, si es una lista lo inserta en la base de datos
    if type(datos) == list:
        #con la instrudcción insert many
        tabla.insert_many(datos)
        #sino, inserta con la instrucción de insert one
    else:
        tabla.insert_one(datos)
    #Al insertarlo se muestra la información de la base de datos
    FunctionSelect(tabla)
    
#Función para eliminar datos de la base de datos, recibe dos parametros de tabla y dato
def FunctionDelete(tabla, dato):
    #Si el tipo de dato es lista eliminará todos los que coincidan con la lista
    if type(dato) == list:
        tabla.delete_many(dato)
    #Si no lo es, solo elimina un dato
    else:
        tabla.delete_one(dato)
    #Se hace un select de la tabla para ver los datos que quedaron
    FunctionSelect(tabla)
    
#La función de update recibe los parametros de tabla, find y values
def FunctionUpdate(tabla, find, values):
    #Se definen los nuevos valores con el set para no repetir la instrucción
    new_values = {'$set': new_values}
    #Si el tipo que se imprime al ejecutar el find es lista, se ejecuta el update_many
    if type(find) == list:
      tabla.update_many(find, new_values)
    #Si no, se ejecuta el update_one
    else:
      tabla.update_one(find, new_values)

   
    
FunctionUpdate(collection, find, values)