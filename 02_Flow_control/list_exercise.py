
###
print("EJERCICIOS")
###

import os
os.system("cls")

print("\n Ejercicio 1: El mensaje secreto \n")
# Dada la siguiente lista:
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

print(mensaje[7:])

print("\n Ejercicio 2: Intercambio de posiciones \n")
# Dada la siguiente lista:
numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

numeros[0] = 50
numeros[4] = 10
print(numeros)




print("\n Ejercicio 3: El sándwich de listas \n")
# Dadas las siguientes listas:
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

sandwich = pan + ingredientes + pan_abajo

print(sandwich)




print("\n Ejercicio 4: Duplicando la lista \n")
# Dada una lista:
lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

lista += [1, 2, 3]
print(lista)


print("Ejercicio 5: Extrayendo el centro")
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
lista = [10, 20, 30, 40, 50] # El centro es 30

print(lista[2])


print("Ejercicio 6: Reversa parcial")
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
lista = [1, 2, 3, 4, 5, 6] #-> Resultado: [3, 2, 1, 4, 5, 6]

mitad = len(lista) // 2
primera_mitad = lista[:mitad][::-1]
print(primera_mitad + lista[mitad:])