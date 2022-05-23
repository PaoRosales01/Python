    
texto_completo = 'Administración de bases de datos'
lista_completa = ['Administracion', 'Bases', 'Datos',2,'unidad']
search = 'Administración'

"""def Buscar(info_completa,search):
    if search in info_completa:
        print('La palabra se encuentra en el texto')
    else:
        print('La palabra no se encuentra en el texto')
        
Buscar(lista_completa, search)"""

#lista_completa = ['Administracion', 'Bases', 'Datos',2,'unidad']

diccionarios = [{
    'nombre': 'Paola',
    'edad':'20'
    },
               {
    'nombre': 'Alejandra',
    'edad':'22' 
               }]
for elemento in diccionarios:
   print(elemento['nombre'])



#Crear una función para utilizar un for y que reaccione a una lista de diccionarios y otra de strings