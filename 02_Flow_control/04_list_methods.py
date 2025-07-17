##
# 04 - Listas de metodos.
# Los metodos mas importantes para trabajar con listas.
###

import os
os.system("cls")
"""
# Lo visto anteriormente solo concatenaba, ahora si es para anadir (mi teclado sigue en ingles.)

lista = [1, 2, 3]

#El .append() nos ayudara a hacerlo, adentro del parentesis va lo que le queremos agregar.

lista.append(4) # esto lo anade al final
print(lista)

#este es para insertarlo en una posicion en concreto. un ejemplo con letras. asi esta constituido: .insert(x, x) (la x es un ejemplo de como deberia ir los elementos) el primero es para elegir el indice de donde queremos insertar el elemento, y lo segundo el elemento a insertar

listaL = ["(*/ω＼*)", "b", "c",'d', 'e']
listaL.append('f')

listaL.insert(3, '༼ つ ◕_◕ ༽つ') # En el lugar 3, que seria la d, se va a insertar el signo de exclamacion, dejando a la 'd' en la siguiente posicion.

#print(listaL)

## Es casi basicamente concatear, este agrega nuevos elementos a la lista al final.

listaL.extend(["(❁´◡`❁)", ":-D","ಠ_ಠ"])
print(listaL)

## Ahora vamos a eliminar elementos de la lista.

listaL.remove("b") #este elimina la primera cadena de texto que contenga una b. Hay que tener cuidado con esta.

print(listaL)

# este es para eliminar el ultimo elemento de la lista, y que lo devuelve, y tambien lo modifica.

ultimo = listaL.pop() #viene por defecto el -1, se puede con numeros negativos, diablo, con cualquier indice y ya conio.
ultimito = listaL.pop(0)
print(ultimo)
print(ultimito)
print(listaL)

#Este es otra forma
print(listaL[3])
del listaL[3]
print(listaL)

# Este es para eliminar todos los elemntos de la lista.

listaL.clear()
print(listaL)

# Eliminar un rango de elementos.

listaO = ["(⌐■_■)", "😐", "🙄", "^_^"]


del listaO[1:3] # es similar al slicing, EL ULTIMO NO SE CUENTA, SIEMPRE SE ME OLVIDA ಥ_ಥ

print(listaO)

"""

# mas metodos

#esto a esta modificando, no se guarda, sela pa bola y ordenarla.
print('ordenar listas modificando la original')
num = [12, 3, 41, 35, 26, 22]
num.sort() #esto es para ordenarla.
print(num)

#Esto e diq pa crear una copia - nueva lista ya ordenada.
print('\n ordenar listas creando una nueva lista')
num2 = [12, 3, 41, 35, 26, 22]
sortedN = sorted(num2)
print(sortedN)

# ordenar una lista de cadenas de texto.
print('\n Ordenar cadenas de texto (todo en minusculas)')
cadenas = ["banana", "manzana", "pera", "kiwi"]
sortf = sorted(cadenas)  # Ordena la lista de cadenas en orden alfabético. 
print(sortf)

# Ordenar cadenas de texto sin importar mayúsculas o minúsculas.
print('\n Ordenar cadenas de texto (sin importar mayúsculas y minúsculas)')
cadenass = ["Banana", "manzana", "pera", "kiwi"]

cadenass.sort(key=str.lower) #esta es otra forma.

#sortfr = sorted(cadenass, key=str.lower)  # Ordena sin importar mayúsculas.
print(cadenass)


# cositas utiles (ESTOY HARTA DE METODOS (¬_¬ ) )

animals = ["perro", "gato", "elefante", "jirafa", "gato", "león"]
print('\n Longitud de la lista')    
print(len(animals))  # Imprime la longitud de la lista.
print(animals.count("gato"))  # Cuenta cuántas veces aparece "gato" en la lista.

print("ola" in animals)  # Verifica si "perro" está en la lista, e imprime True o False.
print("vampiro" not in animals)  # Verifica si "perro" no está en la lista, e imprime True o False.