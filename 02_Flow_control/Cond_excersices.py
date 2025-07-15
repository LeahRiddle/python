
###
# EJERCICIOS
###
import os
os.system("cls")

print("Ejercicio 1: Determinar el mayor de dos números \n")
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

print("Bienvenido al programa para determinar el mayor de dos números.")

print("\n Por favor, ingresar el primer numero.")
num1 = int(input())

print("\n Ahora, por favor, ingresar el seguno numero.")
num2 = int(input())

if num1 > num2:
    print(f"\n El numero mas grande es {num1}.")
elif num2 > num1:
    print(f"\n El numero mas grande es {num2}.")
elif num1 == num2:
    print("Los numeros son iguales.")

print("\n Gracias por usar el programa para determinar el mayor de dos números :)\n")


print("--------------------------------------------")

print("\n Ejercicio 2: Calculadora simple")
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

print("\n Bienvenido a la calculadora simple.")

print("\n Por favor, ingresar el primer numero (Tiene que ser un numero entero).")
num1 = int(input())

print("\n Ahora, por favor, ingresar el seguno numero (Tiene que ser un numero entero).")
num2 = int(input())

print("\n Ahora, por favor, ingresar la operacion que desea realizar (+, -, *, /).")
operation = input()

if operation == "+":
    print(f"\n El resultado de la suma es: {num1 + num2}.")
elif operation == "-":
    print(f"\n El resultado de la resta es:{num1 - num2}")
elif operation == "*":
    print(f"\n El resultado de la multiplicacion es {num1 * num2}")
elif operation == "/":
    print(f"\n El resultado de la division es: {num1 / num2}")
elif num1 or num2 == float:
    print("El numero que acaba de ingresar no es un numero entero.\n")

print("\n Gracias por usar el programa de calculadora simple :)")


print("\n Ejercicio 3: Año bisiesto")
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

print("--------------------------------------------")

print("\n Bienvenido al programa para determinar si el año es bisiesto.")

print("\n Por favor ingresar el año.")
year = int(input())

if year % 4 == 0:
    print("\n El año ingresado es bisiesto.")
else:
    print("\n El año ingresado no es bisiesto")

print("\n Gracias por usar el programa para saber si el año es bisiesto :)")

print("--------------------------------------------")

print("\n Ejercicio 4: Categorizar edades")
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

print("\nBienvenido al programa para catagorizar las edades.")
print("\n Por favor ingresar su edad.")
age = int(input())

if age <= 2:
    print("\n Perteneces a la categoria de Bebes.")
elif age <=  12:
    print("\n Perteneces a la categoria de Niños.")
elif age <= 17:
    print("\n Perteneces a la categoria de Adolescente.")
elif age <= 64:
    print("\n Perteneces a la categoria de Adulto.")
elif age >= 65: 
    print("\n Pertences a la categoria de Adulto mayor.")

print("\n Gracias por usar el programa para categorizar las edades :)")
