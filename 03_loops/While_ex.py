import os 
os.system("cls")
###
print('EJERCICIOS (while)')
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1: Cuenta atras")

num = 10
while num > 0:
    print(f'El valor del contador es {num}')
    num -= 1
print('El programa ha finalizado.')

print("\n ------------------------------------------------------- \n")

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.

print("\n Ejercicio 2: Suma de numeros pares.")
num2 = 0
suma = 0

while num2 <= 20:
   num2 += 1
   if num2 % 2 == 0:
     suma += num2
print(f'La suma de los numeros pares entre 1 y 20 es: {suma}')

print("\n ------------------------------------------------------- \n")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\n Ejercicio 3: Factorial de un numero.")

num3 = -1
fact = 1
try:
        num3 = int(input("Por favor ingresar un numero: "))
        while num3 > 0:
         fact *= num3
         num3 = num3 - 1
         print(fact)
       
except:
      print("Por favor ingresar un numero que sea entero Y positivo. (¬_¬ )")
#while num3 >0:
  
    
print("\n ------------------------------------------------------- \n")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\n Ejercicio 4: Validacion de contraseña.")

print('Por favor ingresar una contraseña (minimo 8 caracteres). \n')
password = input()

while len(password) <= 8:

    print('Por favor ingresar la contraseña con minimo 8 caracteres \n')
    password = input()
    if len(password) >= 8:
        print("Contraseña valida. (●'◡'●) \n")


print("\n ------------------------------------------------------- \n")
# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\n Ejercicio 5: Tabla de multiplicar.")

num4 = 1
"""
while num > 0:
    try:
        print("Por favor ingresar un numero.")
        num4 = int(input())
        if num4 > 0:
            print(f'Tabla de multiplicar del {num4}')
            a = 1
            while a <= 10:
                print(f'{num4} x {a} = {num4 * a}')
                a += 1
        else:
            print("Por favor, ingresa un numero positivo. (¬_¬ )")

    except:
        print('Por favor, ingresa un numero entero, no otro tipo de dato. ಠ_ಠ')
"""

try:
    num4 = int(input("Por favor ingresar un número: "))
    if num4 > 0:
        print(f'Tabla de multiplicar del {num4}')
        a = 1
        while a <= 10:
            print(f'{num4} x {a} = {num4 * a}')
            a += 1
    else:
        print("El número debe ser positivo.")
except:
    print('Por favor, ingresa un número entero, no otro tipo de dato. ಠ_ಠ')

print("\n ------------------------------------------------------- \n")
# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.

### REVISAAAAAR

print("\n Ejercicio 6:")
try:
    n = int(input("Por favor ingresar un numero entero positivo: "))
    
    num5 = 2
    while num5 <= n:
        primo = True
        div = 2
        while div * div <= num5:
            if num5 % div == 0:
                primo = False
                break   
            div += 1
            if primo:
                print(num5)
            else:
                print('Este numero no es primo.')


    num5 += 1



except:
    print("Por favor, ingresa un número entero positivo. (¬_¬ )")