# #25. Sistema de calificaciones.

# print("====== Sistema de calificaciones ======")
# lista_estudiantes = []
# opcion = 0
# calificaciones = {
#     "Nombre Alumno" : "",
#     "Calificaciones" : []
# }

# while True:
#     print("1. Registrar usuario y notas")
#     print("2. Consultar notas por usuario")
#     print("3. Salir ")
    
#     opcion = int(input("Ingrese la opcion deseada: "))

#     if opcion == 1:
#         name = input("Ingrese el nombre del alumno: ")
#         notas = []
#         for i in range(5):
#             nota = float(input(f"Ingrese la {i + 1} nota del alumno: "))
#             notas.append(nota)
#         calificaciones = {"Nombre Alumno" : name, "Calificaciones" : notas}
#         lista_estudiantes.append(calificaciones)
#     elif opcion == 2:
#         name1 = input("Ingrese el nombre del alumno que quiere ver la notas: ")
#         encontrado = False

#         for estudiante in lista_estudiantes:
#             if estudiante["Nombre Alumno"].lower() == name1.lower():
#                 print(f"Las notas del estudiante {estudiante['Nombre Alumno']} son: {estudiante["Calificaciones"]}")
#                 encontrado = True
#                 break
#         if not encontrado:
#             print(f"El alumno {name1} no se encuentra en la lista.\n")
#     elif opcion == 3:
#         break
#     else:
#         print("Opcion invalida, intente de nuevo.")

# #26. Carrito de compras.

# print("====== Carrito de Compras ======")
# carrito_compras = []
# opcion = 0
# contador = 0.0
# articulo = {
#     "Nombre Producto" : "",
#     "Precio producto" : 0.0
# }

# while True:
#     print("1. Añdir articulo")
#     print("2. Consultar articulos en el carrito")
#     print("3. Eliminar articulo")
#     print("4. Valor total de la compra")
#     print("5. Salir ")
    
#     opcion = int(input("Ingrese la opcion deseada: "))

#     if opcion == 1:
#         name = input("Ingrese el nombre del producto: ")
#         price = float(input("Ingrese el precio del producto: "))
#         articulo = {"Nombre Producto" : name, "Precio producto" : price}
#         carrito_compras.append(articulo)
#     elif opcion == 2:
#         print("Actualmente en el carrito estan los siguientes articulos: \n")
#         print(carrito_compras)
#     elif opcion == 3:
#         name1 = input("Ingrese el nombre del articulo que desea eliminar: ")
#         encontrado = False
#         for compra in carrito_compras:
#             if compra["Nombre Producto"].lower() == name1.lower():
#                 carrito_compras.remove(compra)
#                 print(f"El articulo {name1} ha sido removido del carrito.")
#                 encontrado = True
#                 break
#         if not encontrado:
#             print(f"El articulo {name1} no se pudo eliminar ya que no se encuentra en el carrito")

#     elif opcion == 4:
#         for compra in carrito_compras:
#             contador += compra["Precio producto"]
#         print(f"En el carrito hay {len(carrito_compras)} articulos con valor total de {contador} pesos")
#     elif opcion == 5:
#         break
#     else:
#         print("Opcion invalida, intente de nuevo.")

#27. Cajero automático.

print("Bienvenido al cajero de RIWI")
saldo = 1000000.0
opcion = 0
while True:
    print("1. Desea hacer un retiro de su cuenta")
    print("2. Desea hacer un deposito a su cuenta")
    print("3. Desea consultar su saldo actual")
    print("4. Salir del cajero")

    opcion = int(input("Ingrese el numero de la accion que desea realizar: "))

    if opcion == 1:
        monto = float(input("Ingrese el valor que desea retirar: "))
        if monto <= saldo:
            saldo = saldo - monto
            print(f"Se han retirado {monto} pesos de su cuenta.\n")
            print(f"El saldo restante en su cuenta es {saldo} $.")
        else:
            print(f"En su cuenta no hay dinero suficiente para retirar {monto} $.\n")
    elif opcion == 2:
        monto = float(input("Ingrese el valor que desea depositar: "))
        saldo = saldo + monto
        print(f"Su deposito fue exitoso, se han agregado {monto} $.\n")
        print(f"Su nuevo saldo es {saldo} $.")
    elif opcion == 3:
        print(f"Su saldo actual es {saldo} $.")
    elif opcion == 4:
        print("Gracias por usar el cajero RIWI")
        break
    else:
        print("opcion invalida, vuelva a intentarlo.")


#28. Gestión de estudiantes (mini base de datos).

#29. Calculadora avanzada (usar funciones).

#30. Agenda de contactos (lista de diccionarios).