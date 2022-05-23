from crud_clase import *
from bson.objectid import ObjectId


def join(tabla, tablajoin, id):
    producto = FunctionSelect(tabla, {'_id':id}, 'one')
    oferta = FunctionSelect(tablajoin, {'producto_id':id}, 'one')
    oferta.update({'producto':producto})
    #oferta.pop('producto_id')
    print(oferta)
#join('productos', 'ofertas', ObjectId('6217f241f254f608cc6dc299'))

def joinall(tabla, tablajoin, id):
    producto = FunctionSelect(tabla, {'_id':id}, 'all')
    oferta = FunctionSelect(tablajoin, {'producto_id':id}, 'all')
    for ofertas in oferta:
        ofertas.update({'producto':producto})
        ofertas.pop('producto_id')
        print(oferta)
    
#joinall('productos', 'ofertas', ObjectId('6217f241f254f608cc6dc298'))
#Trigger_ofertas({'nombre':'DICLOFENACO'}, 'productos', {'precio':108})

    
