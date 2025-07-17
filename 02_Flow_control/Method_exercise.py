
import os
os.system('cls')
###
print('EJERCICIOS')
# Usa siempre que puedas los métodos que has aprendido
###

print('\n Ejercicio 1: Añadir y modificar elementos')
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.
lista1 = [1, 2, 3, 4, 5]
print('\n Esta es nuestra lista:')
print(lista1)

print('\n Ahora le agregamos el numero 6 usando el metodo .append(): ')
lista1.append(6)
print(lista1)

print('\n Ahora le insertamos el numero 10 en el indice 2:')
lista1.insert(2, 10)
print(lista1)

print('\n Como ultimo paso cambiamos el primer indice para que su valor sea 0: ')
lista1[0] = 0
print(lista1)




#############################################################

print("\n ------------------------------------------------------------ \n")

print('Ejercicio 2: Combinar y limpiar listas')
# Crea dos listas:
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().
print('\n Esta es la lista a:')
print(lista_a)

print('\n Esta es la lista b: ')
print(lista_b)

print('\n Esta es la lista a con la lista b como nueva extension: ')
lista_a.extend(lista_b)
print(lista_a) 

print("\n Aqui le quitamos el numero 1 a la lista a: ")
lista_a.remove(1)
print(lista_a)

print('\n Aqui eliminamos el indice 3 de la lista a:')
deli = lista_a.pop(3)
print(deli)
print(lista_a)

print('\n Aqui limpiamos la lista b por completo: ')
lista_b.clear()
print(lista_b)


print("\n ------------------------------------------------------------ \n")


############################################################################3

print('Ejercicio 3: Slicing y eliminación con del')
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('\n Esta es la lista')
print(lista2)
del lista2[2:5]
print('\n Esta es la lista despues de eliminar los elementos desde el indice 2 hasta el 5 (sin contar el 5) ')
print(lista2)


print("\n ------------------------------------------------------------ \n")

################################################################################


print('Ejercicio 4: Ordenar y contar')
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.
print('\n Esta es la lista original:' )
lista3 = [5, 2, 8, 1, 9, 4, 2]
print(lista3)

print('\n Esta es la lista organizada de forma ascendente: ')
lista3.sort()
print(lista3)

print('\n Este es el conteo de cuantas veces aparece el numero 2 en la lista: ', lista3.count(2))
print('\n Esto es para comprobar si el numero 7 se encuentra en la lista: ', 7 in lista3)


print("\n ------------------------------------------------------------ \n")

print('Ejercicio 5: Copia vs. Referencia')
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

original = [1, 2, 3]
copia = original[::]
copia2 = original.copy()
referencia = original
referencia[0] = 10
print("Original: ", original)
print('Copia: ', copia)
print('Copia 2: ', copia2)
print('Referencia: ', referencia )


print("\n ------------------------------------------------------------ \n")

#############################################################################



print('Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.')
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.

print('\n Esta es nuestra lista: ')
fruta = ["Manzana", "pera", "BANANA", "naranja"]
print(fruta)
fruta.sort(key=str.lower)

print("\n Esta es la lista organizada sin diferencia de mayusculas ni minusculas: ")
print(fruta)