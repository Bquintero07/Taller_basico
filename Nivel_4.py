#19. Lista de frutas.
#20. Agregar y eliminar frutas.
print("Crear una lista")
fruta = ""
frutas = []
opcion = 0

print("Menu de las frutas")
while True:
    print("1. Agregar fruta")
    print("2. Mostrar lista")
    print("3. Eliminar fruta")
    print("4. Salir")
    opcion = int(input("Ingrese la opcion deseada: "))

    if opcion == 1:
        fruta = input("Ingrese la fruta que quiere añadir a la lista: ")
        frutas.append(fruta)
    elif opcion == 2:
        if len(frutas) != 0:
            print("Esta es la lista de las frutas\n")
            print(f"{frutas}\n")
        else:
            print("la lista esta vacia, no hay frutas prar mostrar")
    elif opcion == 3:
        fruta = input("Que fruta desea eliminar: ")
        if fruta in frutas:
            frutas.remove(fruta)
            print(F"La fruta {fruta} ha sido eliminada\n")
        else:
            print(f"La fruta {fruta} no se encuentra en la lista\n")
    elif opcion == 4:
        break
    else:
        print("Opcion no valida.\n")

#21. Buscar un elemento en la lista.

print("Busqueda de elementos en una lista")

elementos = []
elemento = ""
opcion = 0

print("Menu de lista")
while True:
    print("1. Agregar elemento a la lista")
    print("2. Buscar elemento en la lista")
    print("3. salir")

    opcion = int(input("Ingrese la opcion deseada: "))

    if opcion == 1:
        elemento = input("Ingrese el elemento: ")
        elementos.append(elemento)
    elif opcion == 2:
        elemento = input("Ingrese el elemento que desea buscar: ")
        if elemento in elementos:
            print(f"El elemento {elemento} se encuentra en la lista en pocision {elementos.index(elemento) + 1}")
        else:
            print(f"El elemento {elemento} no existe en la lista")
    elif opcion == 3:
        break
    else:
        print("Opcion invalida.")

#22. Lista de números y promedio.

print("Lista de numeros y promedio")

numeros = []
numero = 0
opcion = 0
contador = 0

print("Menu de lista")
while True:
    print("1. Agregar un numero a la lista")
    print("2. Obtener promedio de la lista")
    print("3. salir")

    opcion = int(input("Ingrese la opcion deseada: "))

    if opcion == 1:
        numero = int(input("Ingrese el numero: "))
        numeros.append(numero)
    elif opcion == 2:
        for numero in numeros:
            contador += numero
        print(f"El promedio de la lista es {contador/len(numeros)}")
    elif opcion == 3:
        break
    else:
        print("Opcion invalida.")

#23. Números pares: guardar solo los pares.

print("Lista de numeros pares")

numeros = []
numero = 0
opcion = 0

print("Menu de lista")
while True:
    print("1. Agregar un numero a la lista")
    print("2. Mostrar lista")
    print("3. salir")

    opcion = int(input("Ingrese la opcion deseada: "))

    if opcion == 1:
        numero = int(input("Ingrese el numero: "))
        if numero % 2 == 0:
            numeros.append(numero)
            print(f"El numero {numero} fue añadido a la lista ya que es par")
        else:
            print(f"El numero {numero} no fue añadido a la lista ya que es impar")
    elif opcion == 2:
        print(numeros)
    elif opcion == 3:
        break
    else:
        print("Opcion invalida.")

#24. Eliminar duplicados.

print("Eliminacion de duplicados")

elementos1 = []
lista_auxiliar = []
elemento1 = ""
opcion = 0

print("Menu de lista")
while True:
    print("1. Agregar un elemento a la lista")
    print("2. eliminar duplicados")
    print("3. salir")

    opcion = int(input("Ingrese la opcion deseada: "))

    if opcion == 1:
        elemento1 = (input("Ingrese el numero: "))
        elementos1.append(elemento1)
    elif opcion == 2:
        print("Esta es la lista original\n")
        print(elementos1)
        print("Esta es la lista sin duplicados\n")
        lista_auxiliar = set(elementos1)
        print(lista_auxiliar)
    elif opcion == 3:
        break
    else:
        print("Opcion invalida.")