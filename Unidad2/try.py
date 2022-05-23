import os


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
	lista_completa = ['Administracion', 'Bases', 'Datos', 2, 'unidad']
	for elemento in lista_completa:
		print(elemento)
        