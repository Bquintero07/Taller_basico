#1. Hola usuario: pide al usuario su nombre y edad.
# Luego imprime un mensaje: "Hola [nombre], tienes [edad] años."
print("Hola Usuario\n")
name = input("Ingrese su edad: ")
age = int(input("Ingrese su edad: "))

print(f"Hola {name}, tienes {age} años.")

#2. Suma de dos números.
print("Suma de 2 numeros\n")

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))

result = num1 + num2

print(f"la suma de los numero es {result}")

#3. Área del triángulo.

print("Area del triangulo\n")

base = int(input("Ingrese la base del triangulo: "))
height = int(input("Ingrese la altura del triangulo: "))

area = (base * height)/2

print(f"El area de este triangulo es {area}")

#4. Conversor de grados Celsius a Fahrenheit.

print("Conversor de grados celsius a fahrentheit\n")

celsius = float(int("Ingrese los grados celsius: "))
fahrenheit = (celsius * (9/5)) + 32

print(f"este es el equivalente en grados fahrenheit {fahrenheit}")

#5. Tipo de dato: usar type() para mostrar el tipo de cada variable.
A = ""
B = 0
C = 1.1

print(type(A), type(B), type(C))

#6. Edad futura: pide la edad actual y muestra cuántos años tendrá el usuario dentro de 10 años.

print("Calculadora edad futura")

age1 = int(input("Ingrese su edad actual: "))
age_future = age1 + 10

print(f"En 10 años usted tendra {age_future} años")