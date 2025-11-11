#25. Sistema de calificaciones.

print("====== Sistema de calificaciones ======")
lista_estudiantes = []
opcion = 0
calificaciones = {
    "Nombre Alumno" : "",
    "Calificaciones" : []
}

while True:
    print("1. Registrar usuario y notas")
    print("2. Consultar notas por usuario")
    print("3. Salir ")
    
    opcion = int(input("Ingrese la opcion deseada: "))

    if opcion == 1:
        name = input("Ingrese el nombre del alumno: ")
        notas = []
        for i in range(5):
            nota = float(input(f"Ingrese la {i + 1} nota del alumno: "))
            notas.append(nota)
        calificaciones = {"Nombre Alumno" : name, "Calificaciones" : notas}
        lista_estudiantes.append(calificaciones)
    elif opcion == 2:
        name1 = input("Ingrese el nombre del alumno que quiere ver la notas: ")
        encontrado = False

        for estudiante in lista_estudiantes:
            if estudiante["Nombre Alumno"].lower() == name1.lower():
                print(f"Las notas del estudiante {estudiante['Nombre Alumno']} son: {estudiante["Calificaciones"]}")
                encontrado = True
                break
        if not encontrado:
            print(f"El alumno {name1} no se encuentra en la lista.\n")
    elif opcion == 3:
        break
    else:
        print("Opcion invalida, intente de nuevo.")

#26. Carrito de compras.

print("====== Carrito de Compras ======")
carrito_compras = []
opcion = 0
contador = 0.0
articulo = {
    "Nombre Producto" : "",
    "Precio producto" : 0.0
}

while True:
    print("1. Añdir articulo")
    print("2. Consultar articulos en el carrito")
    print("3. Eliminar articulo")
    print("4. Valor total de la compra")
    print("5. Salir ")
    
    opcion = int(input("Ingrese la opcion deseada: "))

    if opcion == 1:
        name = input("Ingrese el nombre del producto: ")
        price = float(input("Ingrese el precio del producto: "))
        articulo = {"Nombre Producto" : name, "Precio producto" : price}
        carrito_compras.append(articulo)
    elif opcion == 2:
        print("Actualmente en el carrito estan los siguientes articulos: \n")
        print(carrito_compras)
    elif opcion == 3:
        name1 = input("Ingrese el nombre del articulo que desea eliminar: ")
        encontrado = False
        for compra in carrito_compras:
            if compra["Nombre Producto"].lower() == name1.lower():
                carrito_compras.remove(compra)
                print(f"El articulo {name1} ha sido removido del carrito.")
                encontrado = True
                break
        if not encontrado:
            print(f"El articulo {name1} no se pudo eliminar ya que no se encuentra en el carrito")

    elif opcion == 4:
        for compra in carrito_compras:
            contador += compra["Precio producto"]
        print(f"En el carrito hay {len(carrito_compras)} articulos con valor total de {contador} pesos")
    elif opcion == 5:
        break
    else:
        print("Opcion invalida, intente de nuevo.")

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

print("Bienvenido al sistema de gestion de estudiantes de RIWI")

tabla_usuarios = {}
id_user = 0
opcion = 0
while True:
    print("1. Agregar un nuevo registro.")
    print("2. Eliminar un registro.")
    print("3. Mostrar Todos los Registros.")
    print("4. Buscar estudiante por ID.")
    print("5. Modificar informacion de estudiante.")
    print("6. Salir.")

    opcion = int(input("Ingrese la opcion deseada: "))

    if opcion == 1:
        id_user += 1
        name = input("Ingrese el nombre del alumno: ")
        email = input("Ingrese el email del alumno: ")
        clan = input("Ingrese el clan al que pertenece el alumno: ")

        tabla_usuarios[id_user] = {"name": name, "email" : email, "clan" : clan}

    elif opcion == 2:
        id1 = int(input("Ingrese el ID del usuario que quiere eliminar: "))
        if id1 in tabla_usuarios:
            print(f"Se eliminara el usuario con ID {id1} y con nombre: {tabla_usuarios[id1].get("name")}\n")
            tabla_usuarios.pop(id1)
        else:
            print("El usuario que desea eliminar no existe en la base de datos.")
    elif opcion == 3:
        if len(tabla_usuarios) != 0:
            print("Estos son los usuarios registrados en la base de datos:\n")
            for usuario in tabla_usuarios:
                print(f"ID: {usuario} - Nombre: {tabla_usuarios[usuario]['name']} - Email: {tabla_usuarios[usuario]['email']} - Clan: {tabla_usuarios[usuario]['clan']}\n")
        else:
            print("No hay registros en la base de datos.")
    elif opcion == 4:
        id2 = int(input("Ingrese el ID del usuario que quiere buscar: "))
        if id2 in tabla_usuarios:
            print("Usuarios encontrado: \n")
            print(f"ID: {id2} - Nombre: {tabla_usuarios[id2].get("name")} - Email: {tabla_usuarios[id2].get("email")} - Clan: {tabla_usuarios[id2].get("clan")}\n")
        else:
            print("El usuario no existe en la base datos.")
    elif opcion == 5:
        id3 = int(input("ingrese el ID del usuario que desea modificar: "))
        if id3 in tabla_usuarios:
            print("este es el usuario a modificar: \n")
            print(f"ID: {id3} - Nombre: {tabla_usuarios[id3].get("name")} - Email: {tabla_usuarios[id3].get("email")} - Clan: {tabla_usuarios[id3].get("clan")}\n")
            name1 = input("Ingrese el nombre del alumno que desea modificar si no desea modificar este campo ingrese el mismo nombre: ")
            email1 = input("Ingrese el email del alumno que desea modificar si no desea modificar este campo ingrese el mismo email: ")
            clan1 = input("Ingrese el clan del alumno que desea modificar si no desea modificar este campo ingrese el mismo clan: ")
            tabla_usuarios.update({id3: {"name": name1, "email" : email1, "clan" : clan1}})
        else:
            print("El usuario no exite en la base de datos.")
    elif opcion == 6:
        print("Gracias por usar el sistema.")
        break
    else:
        print("Opcion invalida, intentelo de nuevo.")

#29. Calculadora avanzada (usar funciones).

def calculadorapro(num1, num2, operador):
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/":
        if num1 and num2 != 0:
            return num1 / num2
        else:
            print("no se puede dividir a 0 o dividir por 0")
    elif operador == "**":
        return num1 ** num2
    elif operador == "%":
        if num1 and num2 != 0:
            return num1 % num2
        else:
            print("no se puede dividir a 0 o dividir por 0")
    elif operador == "//":
        if num1 and num2 != 0:
            return num1 // num2
        else:
            print("no se puede dividir a 0 o dividir por 0")
    elif operador == "raiz":
        if num2 != 0:
            return num1 ** 1/num2
        else:
            print("no se puede dividir a 0 o dividir por 0")

print("Calculadora pro\n")
opcion = 0
while True:
    print("1. Hacer un calculo.")
    print("2. salir")
    opcion = int(input("Ingrese la opcion deseada: "))

    if opcion == 1:
        numA = int(input("Ingrese el primer numero: "))
        numB = int(input("Ingrese el segundo numero: "))
        op = input("Ingrese el operado: ")

        print(f"Al usar el operador {op} el resultado es: ")
        print(calculadorapro(numA, numB, op))
    elif opcion == 2:
        break
    else:
        print("Opcion incorrecta, intentelo de nuevo.")


#30. Agenda de contactos (lista de diccionarios).

print("Contactos 👥")

contactos = []

contacto = {}

opcion = 0
while True:
    print("1. Agregar contacto.")
    print("2. Buscar contacto.")
    print("3. Editar contacto.")
    print("4. Eliminar contacto.")
    print("5. salir.\n")

    opcion = int(input("Ingrese la opcion que desea realizar: "))

    if opcion == 1:
        name = input("Nombre del contacto: ")
        lastname = input("Apellido del contacto: ")
        cellphone = input("Numero del contacto: ")
        contacto = {"name" : name, "lastname" : lastname, "cellphone" : cellphone}
        contactos.append(contacto)
        print("Contacto guardado correctamente.\n")
    elif opcion == 2:
        buscar = input ("Ingrese el nombre del contacto que desea buscar: ")
        bandera = False
        for contacto in contactos:
            if contacto["name"] == buscar:
                print(f"Contacto:\n Nombre: {contacto["name"]}\n Apellido: {contacto["lastname"]}\n Telefono: {contacto["cellphone"]}.\n")
                bandera = True
                break
        if not bandera:
            print("Este contacto no existe")
    elif opcion == 3:
        buscar = input ("Ingrese el nombre del contacto que desea editar: ")
        bandera = False
        for contacto in contactos:
            if contacto["name"] == buscar:
                print(f"Contacto:\n Nombre: {contacto["name"]}\n Apellido: {contacto["lastname"]}\n Telefono: {contacto["cellphone"]}.\n")
                name = input("Nombre del contacto: ")
                lastname = input("Apellido del contacto: ")
                cellphone = input("Numero del contacto: ")
                contacto.update({"name" : name, "lastname" : lastname, "cellphone" : cellphone})
                bandera = True
                break
        if not bandera:
            print("Este contacto no existe")
    elif opcion == 4:
        buscar = input ("Ingrese el nombre del contacto que desea elimnar: ")
        bandera = False
        for contacto in contactos:
            if contacto["name"] == buscar:
                print(f"Contacto:\n Nombre: {contacto["name"]}\n Apellido: {contacto["lastname"]}\n Telefono: {contacto["cellphone"]}.\n")
                contactos.remove(contacto)
                print("Contacto eliminado correctamente.")
                bandera = True
                break
        if not bandera:
            print("Este contacto no existe")
    elif opcion == 5:
        break
    else:
        print("Opcion invalida, intentelo de nuevo.")


# https://github.com/daveshb/riwipython/blob/main/modulo1/semana1/Taller1.md