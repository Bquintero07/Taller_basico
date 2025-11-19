#0. FizzBuZZ

# for i in range(1, 101):
#     if (i % 3) == 0 and (i % 5) == 0:
#         print("FizzBuZZ")
#     elif (i % 3) == 0:
#         print("Fizz")
#     elif (i % 5) == 0:
#         print("BuZZ")
#     else:
#         print(i)

#1. Clasificador de números (listas + condicionales)

# lista = [0,1,2,0,3,4,5,6,-8,-7,-1,-100,0,0,3,4,-6]
# listapositiva = []
# listanegativa = []
# ceros = []
# for num in lista:
#     if num > 0:
#         listapositiva.append(num)
#     elif num < 0:
#         listanegativa.append(num)
#     else:
#         ceros.append(num)
# print(listapositiva)
# print(listanegativa)
# print(ceros)

#2. Contador de vocales (funciones)

# def contar_vocales(texto):
#     lower = texto.lower()
#     vocales = {"a":0,"e":0,"i":0,"o":0,"u":0 }
#     for letra in lower:
#         if letra in vocales.keys():
#             vocales[letra] += 1
#     return vocales

# print(contar_vocales("esternocleidomastoideo"))

#3. Lista de tareas (listas + diccionarios)

# lista_tareas = []

# while True:
#     try:
#         print("1. Agregar una nueva tarea.")
#         print("2. Marcar tarea como finalizada.")
#         print("3. Mostrar tareas.")
#         print("4. Salir")

#         opcion = int(input("Ingrese la opcion que deseada: "))

#         if opcion == 1:
#             tarea = input("Ingrese la tarea que desea realizar: ")
#             completada = False
#             tarea = {"Titulo" : tarea, "Completada": completada}
#             lista_tareas.append(tarea)
#             print("La tarea ha sido creada.\n")
#         elif opcion == 2:
#             if len(tarea) == 0:
#                 print("La lista de tareas esta vacia.\n")
#             else:
#                 buscar = input("Ingrese el nombre de la tarea que quiere marcar como finalizada: ")
#                 for tarea in lista_tareas:
#                     if buscar.lower() == tarea["Titulo"].lower():
#                         print(tarea["Titulo"])
#                         accion = input("\nDesea marcar esta tarea como completada (Si o No): ")
#                         if accion.lower() == "si":
#                             tarea["Completada"] = True
#                             print(f"\nLa tarea {tarea["Titulo"]} ha sido completada.\n")
#                         else:
#                             print(f"\nLa tarea {tarea["Titulo"]} sigue sin completarse\n.")
#                         break
#                 else:
#                     print("Esa tarea aun no se a agregado a la lista de tareas.\n")
#         elif opcion == 3:
#             if len(lista_tareas) != 0:
#                 for tarea in lista_tareas:
#                     if tarea["Completada"]:
#                         print("Tareas completadas: \n")
#                         print(f"Nombre tarea: {tarea["Titulo"]} | Status: Completada")
#                         break
#                 else:
#                     print("Tareas incompletas: \n")
#                     print(f"Nombre tarea: {tarea["Titulo"]} | Status: sin completar")
#             else:
#                 print("No hay ninguna tarea en la lista aun.\n")
#         elif opcion == 4:
#             break
#         else:
#             print("opcion ivalida seleccione una del menu(1-3).\n")
#     except ValueError:
#         print("Error: ingrese un valor valido.")

#4. Máquina de bebidas (condicionales + loops)

maquina = {"Agua" : 1, "Jugo" : 2, "Cafe" : 3 }
billetes = [1,5,10]

# El programa debe:

# mostrar el menú
# pedir al usuario que elija
# pedir el pago
# validar si el dinero es suficiente
# devolver cambio si aplica
# imprimir un mensaje de compra exitosa

while True:
    try:
        print("1. Elegir el producto")
        print("2. Pagar producto")
        print("3. Salir ")
        
    except ValueError:
        print("Error: ingrese un valor valido.")