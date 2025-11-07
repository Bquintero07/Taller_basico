#7. Mayor de edad.
print("Verificar de mayoria de edad")

age = int(input("ingrese su edad: "))

if age <= 17:
    print("Usted es menor de edad, vualva cuando tenga 18 años.")
else:
    print("Usted es mayor de edad, bienvenido.")


#8. Número positivo, negativo o cero.

print("verificador de numeros")

num = int(input("Ingrese el numero que desea verificar: "))

if num == 0:
    print("su numero es cero.")
elif num > 0:
    print("Su numero es positivo")
else:
    print("Su numero es negativo")

#9. Par o impar.

print("Verificador de pares o impares")

num1 = int(input("Ingrese el numero que desea verificar: "))
if num1 % 2 == 0:
    print("El numero ingresado es par")
else:
    print("El numero ingresado es impar")

#10. Calculadora básica con +, -, *, /.

print("Calculadora basica")

numA = int(input("Ingrese un numero "))
operacion = input("ingrese el simbolo de la opracion +, -, *, /: ")
numB = int(input("Ingrese un numero "))

if operacion == "+":
    suma = numA + numB
    print(f"la suma de los numeros es igual a {suma}")
elif operacion == "-":
    resta = numA - numB
    print(f"la suma de los numeros es igual a {resta}")
elif operacion == "*":
    mult = numA * numB
    print(f"la suma de los numeros es igual a {mult}")
elif operacion == "/":
    div = numA / numB
    print(f"la suma de los numeros es igual a {div}")

#11 Clasificador de notas (Excelente, Aprobado, Reprobado).

print("Clasificador de notas")

grade = float(input("Ingrese su nota con numero entre 0 y 100, puede usar decimales: "))

if grade <= 33.4:
    print("Tu nota es reprobado.")
elif grade > 33.4 and grade <= 66.7:
    print("Tu nota es Aprobado.")
elif grade > 66.7 and grade <= 100:
    print("Tu nota es excelente.")

#12. Comparador de tres números: mayor y menor.

print("Comparador de numeros")

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"El numero {numero1} es el mayor")
elif numero2 > numero1 and numero2 > numero3:
    print(f"El numero {numero2} es el mayor")
elif numero3 > numero1 and numero3 > numero2:
    print(f"El numero {numero3} es el mayor")
