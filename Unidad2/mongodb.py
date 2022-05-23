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
prealumnos = db['prealumnos']
prealumnos.insert_one({
    'escuela_proc':
        {
            'clave':'10DGS2022',
            'nombre':'UTD',
            'direccion':'Durango-Mezquital 34308',
            'correo':'utd@edu.mx',
            'tel':'6181373050',
            'pais':'México',
            'estado':'Durango',
            'municipio':'Durango'
        }
   
    })

for alumno in list(prealumnos.find()):
    print(alumno)

 #Añadir un registro que tenga escuela_proc
