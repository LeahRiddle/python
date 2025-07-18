###
# 02 - Bucles (For)
# Permiten ejecutar un bloque de codigo repetidamente mientras ITERA
###
from os import system
if system("clear") != 0: system("cls")

print('\n Bucle for:')

##Iterar una lista
frutas = ['Manzana', 'pera', 'limon']
for frutas in frutas:
    print(frutas)

# Iterar sobre cualquier cosa que sea iterable.
print('\n Iteraciones:')
cadena = 'Naruto'
for caracter in cadena:
    print(caracter)

# enumerate (), esto es para que se imprima el indice de cada vaina.indice y fruta son variables btw, se puede poner el nombre que quiera.

# indice = primera posicion indice.
# fruta = seguna posicion el valor.
frutas2 = ['Manzana', 'pera', 'limon']
for indice, fruta in enumerate(frutas2):
    print(f'El indice es {indice} y la fruta es {fruta}')

## Bucles anidados (esto ya lo sabia, hasta lo he aplicado en los ejercicios lol.)
print('\n Bucles anidados.')
letras = ['a', 'b', 'c']
num = [1, 2, 3]
for letra in letras:
    for nume in num:
        print(f'{letra}{nume}')


# usando el break
print('\n Break:')
animals = ['perro', 'gato', 'raton', 'loro', 'pez', 'canario']
for animal in animals:
    print(animal)
    if animal == 'loro':
        break
        

## lo mismo, pero lo vamos a convinar con el enumerate().

print('\n Enumarate: ')

animalss = ['perro', 'gato', 'loro', 'conejo', 'ballena', 'canario', 'tigre', 'pulpo']

for index, animal in enumerate(animalss):
    print(animal)
    if animal == 'canario':
        print(f'el {animal} esta en el indice {index}')
        break
## Ahora con el continue

print('\n Continue:')
animalsss = ['perro', 'gato', 'loro', 'conejo', 'ballena', 'canario', 'tigre', 'pulpo']

for index, animala in enumerate(animalsss):
    if animala == 'canario': continue
    print(animala)

## compresion de listas (list comprehension)
print('\n Comprension de listas:')
animalssss  = ['perro', 'gato', 'loro', 'conejo', 'ballena', 'canario', 'tigre', 'pulpo']

m = [a.upper() for a in animalssss]
print(m)

## compresion de listas con condicional, otra forma de hacerlo en una linea.
par = [num for num in [1, 2, 3, 4, 5, 6, 7, 8,] if num % 2 == 0]
print(par)

