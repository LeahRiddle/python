###
# EJERCICIOS (for)
###

from os import system
if system("clear") != 0: system("cls")

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1: Imprimir numeros pares")
lit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for par in lit:
    if par % 2 == 0:
        print(par)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.

print("\nEjercicio 2: Calcular la media de una lista.")
numeros = [10, 20, 30, 40, 50]
suma = 0
for num in numeros:
    suma += num
media = suma / len(numeros)
print(f'\n la media es: {media}')



# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3: Buscar el maximo de una lista.")
numer = [15, 5, 25, 10, 20]
maxo = numer[0]
for  num in numer:
    if num > maxo:
        maxo = num
print(f'\n El numero maximo es: {maxo}')



# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4: filtar cadenas por longitud.")
palabras = [catn for catn in ["casa", "arbol", "sol", "elefante", "luna"] if len(catn) > 5]
print(palabras) 


# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5: Contar palanras que empiezan por una letra.")
palabrasn = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
contador = 0

letra = input('\n Por favor ingresar una letra. ').lower()
for l in palabrasn:
    if l.lower().startswith(letra):
        contador += 1
print(f'\n Esta es la cantidad de palabras que empiezan por la letra {letra}: {contador}')



  
