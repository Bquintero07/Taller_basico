#13. Contar del 1 al 10.
print("Numeros del 1 al 10")
n = int(input("Ingrese el numero hasta el que quiera ver: "))
for i in range(1,n+1):
    print(i)

#14. Sumatoria del 1 al n.
print("Sumatoria de numeros")

num = int(input("Ingrese el numero hasta el que quiere sumar: "))
suma = 0
for i in range(1,num+1):
    suma += i
print(f"La suma de los numeros es igual a {suma}")

#15 Tabla de multiplicar.
print("Tabla de multiplicar hasta el 100")

numero = int(input("ingrese el numero del cual quiere conocer la tabla de multiplicar: "))

for i in range(1,101):
    print(i*numero)

#16. Contador regresivo con while.

print("Contador reguresivo usando while")

numA = int(input("Ingrese el numero desde el que inicia la cuenta: "))
while numA > 0:
    print(numA)
    numA -= 1

#17. Adivina el número (usar random).

print("Adivine el numero")

import random
num1 = int(input("Indique en el rango en el que quiere adiviar el numero desde 1 hasta: "))
num_random = random.randint(1, num1)
intentos = 0

print(f"El numero a adivinar esta entre 1 y {num1}")

while True:
    num2 = int(input("Ingrese el numero que crees correcto: "))
    if num2 > num_random:
        print("Tu numero es mayor")
    elif num2 < num_random:
        print("Tu numero es menor")
    else:
        print("Econtraste el numero correcto")
        break

#18. Sumar hasta que el usuario escriba 0.

print("Suma hasta agregar el 0")
contador = 0
numB = ""

while numB != 0:
    numB = int(input("Ingrese un numero si quiere sumar o ingrese 0 para parar: "))
    if numB == 0:
        print(f"La suma quedo en {contador}")
    else:
        contador += numB
        print(f"La suma va en {contador}")