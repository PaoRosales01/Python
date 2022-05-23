# Universidad Tecnológica de Durango
# Por: Paola Elizabeth Rosales Verdín
# Fecha: 17/02/2022
# Materia: Administración de Bases de Datos

import os

def strs():
    lista_completa = ['Administracion', 'Bases', 'Datos', 2, 'unidad']
    for elemento in lista_completa:
        print(elemento)
    
def dicts():
    diccionarios = [{
                'nombre': 'Paola',
                'edad': '20'
            },
                {
                'nombre': 'Angelica',
                'edad': '22'
            },
                {
                'nombre': 'Arturo',
                'edad': '29'
            },
            ]

    for elemento in diccionarios:
        print(elemento)


def menu():
    os.system('cls')
    print("Selecciona una opción de lo que deseas visualizar")
    print("\t1 - Recorrer una lista de strings")
    print("\t2 - Recorrer una lista de diccionarios")
    print("\t3 - Salir")


while True:
    menu()
    opc = input("Inserta una opción del menú --> ")

    if opc == "1":
            print("\nLista de strings:")
            strs()
            input("Pulsa una tecla para continuar-->")
            
    elif opc == "2":
            print("\nLista de diccionarios:")
            dicts()
            input("Pulsa una tecla para continuar-->")
            
            
    elif opc == "3":
        exit()
    
    else:
        print("")
        input("No has pulsado ninguna opción correcta (1-3)...\npulsa una tecla para continuar")
