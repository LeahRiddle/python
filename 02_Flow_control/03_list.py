###
# 03 - listas

# Secuencia mutables de elementos.
#Pueden contener elementos de diferentes tipos.
###

#este es un truco para limpiar la consola, se me olvidaba escribirlo, lol.
import os
os.system("cls")
 # Creacion de listas

lista1 = [1, 2, 3, 4, 5] #Lista de enteros
lista2 = ["manzana", "peras", "Platanos"] #lista de enteros.

# esta forma en que lo hice es opcional, debido a que python no se declara en si la variable, pero al yo tenerlo en estricto tengo que ponerlo asi.
lista3: list[int | str | float | bool] = [1, "hola", 3.14, True] #lista de tipo multiple

listaV = [] #lista vacioa
listaL = [[1, 2], [3, 4]]

# Tambien podemos tener matrices.
matrix = [[1, 2], [2, 3], [3, 4], [4, 5]]

print(lista1)
print(lista2)
print(lista3)
#print(listaV)
print(listaL)
print(matrix)

# Acessp a elementos por indice.
# El primero siempre es el 0.
print("\n Acceso a elementos por indice.")
print(lista3[1])

#Este es una forma de acceeder al ultimo si no sabes que numero es, porque estamos contando desde atras hacia adelante
print(lista3[-1])

#Este es para acceder a la lista de listas, primero elegimos la lista asi: [0][1], esto significa que queremos que imprima el primero de la lista 0.

print(listaL[1][0])

# Slicing (rebanado) de listas (no deberiamos acostumbrarnos a esto)

print(lista1[1:4]) #[2, 3, 4]
 # esto va a imprimir del 2 al 4, no imprime el numero 5 porque ese el el limite o algo asi, el ultimo no se incluye.

# tambien podemos hacerlo asi. SE VE SUPER LINDOO T.T
print(lista1[:3]) # [1, 2, 3]

#tambien se puede hacer asi para imprimir solo los ultimos.
print(lista1[3:]) # [3, 4, 5]

#esto es para que lo imprima todo, es una copia, para que? ni idea.
print(lista1[:])

# Hay mas cosas.
"""
print(lista1[desde:hasta:paso]) # [indice, hasta donde llega (sin incluirlo), paso]
"""
# esto es para imprimir cada 2 numeros, tambien se puede hacer con la cantidad que queramos.
print(lista1[::2]) # [1, 3, 5]

# Tambien podemos usar el slicing para invertir una lista.
print(lista1[::-1]) # [5, 4, 3, 2,


# Ahora vamos a modificar la lista, obviamente no podemos modificar partes que no hay, asi que abstenerse de eso.

lista1[2] = 33
print(lista1)

# Ahora vamos a anadir (mi teclado esta en ingles, btw)

ListaA = [1, 2, 3]

#esta es la forma mas larga y menos eficiente, yo quede mala yo juraba que estaba bn asi :(

ListaA = ListaA + [4, 5, 6, 7, 8, 9] #esto lo que va a hacer es concatenar la lista original y la que acabamos de agregar.
print(ListaA)

#Forma corta, mas eficiente y directa: + =

ListaA += [10, 11, 12]
print(ListaA)

## Recuperar longitud de una lista.

print("Longitud de una lista",len(ListaA))