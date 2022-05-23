from crud import *
from bson.objectid import ObjectId

stock = {'stock':50}

def Joins(tabla1, tabla2, id1, id2, busq):
    producto = {'nombre':'Aspirina'}
    tabla1 = FunctionSelect(tabla1, {'_id':ObjectId(id1)}, busq)
    tabla2 = FunctionSelect(tabla2, {'_id':ObjectId(id2)}, busq)
    tabla2.update({tabla1: {tabla1:tabla1}})
    print(tabla2)
    
Joins('productos', 'ofertas', '6217f241f254f608cc6dc299', '6217fcee136cafd01a86a57c', 'one')