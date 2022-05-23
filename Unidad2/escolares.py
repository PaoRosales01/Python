#Agrega la librería general de pymongo
import pymongo
#Agrega la función de MongoClient desde pymongo
from pymongo import MongoClient
import datetime
current_time=datetime.datetime.now()
#Se crea la conexión con Mongodb
con        = MongoClient('localhost', 27017)
#Selecciona la base de datos
db         = con['sistema_escolares']

def FunctionSelect(tabla,buscar,tipo):
    collection = db[tabla]
    if tipo =='one':
        resultados = collection.find_one(buscar)
    elif tipo=='all':
        resultados=list(collection.find(buscar))
    return resultados
    
def FunctionInsert(tabla, datos):
    collection = db[tabla]
    if type(datos) == list:
        collection.insert_many(datos)
    else:
        collection.insert_one(datos)

def FunctionUpdate(tabla, find, alumno_id, new_values):
    collection = db[tabla]
    new_values = {'$set': new_values}
    if type(find) == list:
      collection.update_many(find, new_values)
    else:
      collection.update_one(find, new_values)
    FunctionProm(tabla, alumno_id)

def FunctionProm(tabla, alumno_id):
    collection = db[tabla]
    resultados = list(collection.find({'alumno_id': alumno_id}))
    cal = 0
    for elementos in resultados:
        cal = cal + elementos['calificacion']
        promfinal = cal/len(resultados)
        kardex = { 
                'alumno_id': alumno_id,
                'promedio': promfinal
    }
    FunctionInsert('kardex', kardex)

datos_alumno= {
    'nombre': 'Juan',
    'apellido': 'Perez',
    'carrera': 'Desarrollo y gestión de software'
}

materia = {
    'nombre': 'Desarrollo web'
}

calif = [{
    'alumno_id': '622675af649a667c23611d1c',
    'materia_id': '6226762e31a4b413d2286f21',
    'calificacion': 95
},
     {
    'alumno_id': '622675af649a667c23611d1c',
    'materia_id': '62267640ab07151cabd381a7',
    'calificacion': 90        
}]


#FunctionInsert('alumnos', datos_alumno)

#FunctionInsert('materias', materia)

updatealumno = {
    'calificacion': 97
}

FunctionUpdate('calificaciones', {'materia_id':'6226762e31a4b413d2286f21'},'622675af649a667c23611d1c' ,updatealumno)


