#Agrega la librería general de pymongo
import pymongo
#Agrega la función de MongoClient desde pymongo
from pymongo import MongoClient
import datetime
current_time=datetime.datetime.now()
#Se crea la conexión con Mongodb
con        = MongoClient('localhost', 27017)
#Selecciona la base de datos
db         = con['sta_clara']
#Función para ver datos desde la base de datos
def FunctionSelect(tabla,buscar,tipo):
    #Selecciona la colección
    collection = db[tabla]
    if tipo =='one':
        resultados = collection.find_one(buscar)
    elif tipo=='all':
        #Creando de un query una lista para poder obtener la info
        resultados=list(collection.find(buscar))
    #Print a variable resultados
    return resultados
    
#Función para insertar datos a la base de datos, recibe dos parametros de tabla y datos
def FunctionInsert(tabla, datos):
    #Selecciona la colección
    collection = db[tabla]
    #En el if detecta si el dato es una lista o un diccionario, si es una lista lo inserta en la base de datos
    if type(datos) == list:
        #con la instrudcción insert many
        collection.insert_many(datos)
        #sino, inserta con la instrucción de insert one
    else:
        collection.insert_one(datos)
    SaveLogs(tabla, 'insert')

    
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
def FunctionUpdate(tabla, find, new_values):
    #Selecciona la colección
    collection = db[tabla]
    #Se definen los nuevos valores con el set para no repetir la instrucción
    new_values = {'$set': new_values}
    #Si el tipo que se imprime al ejecutar el find es lista, se ejecuta el update_many
    if type(find) == list:
      collection.update_many(find, new_values)
    #Si no, se ejecuta el update_one
    else:
      collection.update_one(find, new_values)
    SaveLogs(tabla, 'update')

def FunctionSelectNombre(tabla, nombre, cantidad):
    #Selecciona la colección
    collection = db[tabla]
    #Esta variable crea un query de una lista para poder obtener la info
    resultados = list(collection.find({'nombre': nombre}))

    #Print a variable resultados
    for elementos in resultados:
    
        datos_carrito ={
            'nombre': elementos['nombre'],
            'producto_id':elementos['_id'],
            'cantidad':cantidad,
            'subtotal':elementos['precio'],
            'iva':16,
            'total':elementos['precio']*1.16*cantidad
        }
    FunctionInsert('carrito', datos_carrito)
    
def FunctionFind(tabla, dato):
    #Selecciona la colección
    collection = db[tabla]
    #Esta variable crea un query de una lista para poder obtener la info
    resultados = len(list(collection.find({'nombre': dato})))
    if resultados==1:
        documento=collection.find_one({'nombre': dato})
        print(documento)
        print('Solo se encontró un elemento que coincide con el nombre')
    elif resultados==0:
        print('No se encontró ningún elemento que coincida con el nombre')
    else:
        documento=list(collection.find({'nombre': dato}))
        for elementos in documento:
         print(documento)
        print('Se encontraron varios elementos que coincidieron con el nombre')
    
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

#Práctica 2        
def SaveLogs(table, action):
    data_log = {
        'accion:': action,
        'fecha': current_time,
        'tabla': table
    }
    FunctionInsert('log', data_log)

def Trigger_log(tabla,action,datos):
    #Actualizar el producto por nombre y cambiar precio
    #Seleccionamos la colección
    collection = db[tabla]
    #Busca en la colección por nombre para traer un elemento
    if action=='insert':
        FunctionInsert(tabla, datos)
        resultado = collection.find().limit(1)
        datos_log = {
        'action': action,
        'date': current_time,
        'table':tabla
        }
        FunctionInsert('logs', datos_log)
    elif action=='update':
        FunctionUpdate(tabla,buscar, nuevos)
        resultado=collection.find()
        datos_log2={
            'action': action,
            'date': current_time,
            'table':tabla
        }
        
        FunctionInsert('logs', datos_log2)

#Trigger_ofertas({'nombre:':'Aspirina'}, 'productos', '35')
       
       
       # for oferta in ofertas:
    #    ofertas.update({'producto':producto})
     #   ofertas.pop('producto_id')
      #  print(oferta)
        #print(oferta['producto']['nombre'])
   

