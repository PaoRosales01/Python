# Universidad Tecnológica de Durango
# Por: Paola Elizabeth Rosales Verdín
# Fecha: 23/02/2022
# Materia: Administración de Bases de Datos


from crud import *

buscar = {'nombre': 'Amoxicilina'}
print(FunctionSelect('productos', buscar, 'all'))  

   


#Actualizaciones en productos
#Cambio de nombre y precio
#datos = {'nombre': 'Paracetamol', 'precio': 32 }
#nuevos = {'nombre':'Aspirina', 'precio':82 }


#Actualizaciones en usuarios
#Token de pago, Número interior, Código Postal
#datos = {'token_de_pago': '123456789'} 
#nuevos = {
#  'token_de_pago': '45452002',
#  'direccion.numero_int':'589ba',
#  'direccion.cp':'34620'
#   }

#datos = {
#    'nombre': 'Omeprazol',
#    'precio': 32
#}

#Trigger_log('productos', 'insert', datos)

buscar={'nombre':'Omeprazol'}
nuevos={'nombre':'Omeprazol','precio':32}

Trigger_log('productos', 'update', buscar)

#FunctionFind('productos', 'Aspirina')

#Hacer que FunctionSelect detecte si es find one o find

#Trigger_ofertas(buscar, tabla_productos,precio)
#FunctionSelect('ofertas')
#FunctionSelectNombre('productos', 'Aspirina',2)
#FunctionUpdate('usuarios', datos, nuevos)
#FunctionInsert('productos', datos_productos)
#FunctionSelect('productos')
