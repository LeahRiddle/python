###
# 01 - bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición.
###
import os
os.system("cls")

print('Hoy veremos el bucle while \n')

# Ejemplo de bucle while
    
print('\n Bucle While:')
contadora = 0

while contadora < 5:
    print(f"Contadora: {contadora}")
    contadora += 1  # Incrementa el contador en 1.   Tambien es super importante que se incremente el contador, porque si no, se quedaria en un bucle infinito y eso no es bueno.


# Este es un ejemplo de un bucle infinito. Usamos el break para romper el bucle infinito.

print('\n Bucle while infinito (obvio no se va a mostrar):')
"""
while True:
    print('hola')

"""

# asi se usa con break
contador = 0
print('\n Bucle While con break:')
while True:
    print(contador)
    contador += 1
    if contador == 5:
        break # se sale del bucle.

# este es otro ejemplo. en este se va a hacer el bucle hasta que encuentre el primer numero que sea divisible a 5, una vez que lo encunetre va a parar.

print('\n Otro bucle while con break: ')

contadoro = 0
while contadoro <= 100:
    contadoro += 1
    print(contadoro)
    if contadoro % 5 == 0:
        print("El numero es multiplo de 5")
        break
        

## Ahora vamos con el bucle continue.

## Continue, lo que hace es saltar esa iteracion en concreto y continuar con el bucle.

print('\n Bucle con continue:')
contadorc = 0
while contadorc < 10:
    contadorc += 1
    if contadorc % 2 == 0:
        continue # Si el contador es par, salta a la siguiente iteración.

    print(contadorc)

    # else en los bucles while, etsa es una forma de usar el else en los bucles while, se ejecuta cuando el bucle termina normalmente, sin un break.



print('\n Bucle while con else:')
contador_e = 0
while contador_e <= 5:
    print(f"Contador: {contador_e}")
    contador_e += 1
else:
    print("El bucle ha terminado sin interrupciones.") # Se ejecuta al finalizar el bucle sin un break.

"""
    print('\n Este es un ejemplo practico.')

    num = -1
    while num < 0:
        num = int(input('\n Escribe un numero positivo: '))

        if num < 0:
            print('\n El numero debe ser positivo. Intenta otra vez, plis (⌐■_■)')

print(f'\n El numero ingresado es {num}')

"""

## Ahora con el try catch (no se llama asi, pero asi le digo por culpa de c# hahahaha.)

print('\n Este es un ejemplo practico. Con try-catch')

num = -1
while num < 0:
    try:
        num = int(input('\n Escribe un numero positivo: '))
        if num < 0:
            print('\n El numero debe ser positivo. Intenta otra vez, plis (⌐■_■)')
    except:
        print('Lo que ingresaste no fue un numero, por favor esta vez ingresar un numero. ಠ_ಠ')

print(f'\n El numero ingresado es {num}')