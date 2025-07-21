###
# 03 - range()
# Permite crear una secuencia de numeros. Puede ser util para el For, pero no solo para eso.
###

from os import system
if system("clear") != 0: system("cls")

print('\n range():')

'''
n = range(5) '''# Esto no crea listas, es un tipo de dato normal.
'''print(type(n))'''

## generando una secuencia de numeros del 0 al 9.
'''for t in range(10):
    print(t)'''
# por defecto su numero de inicio es 0, si queremos uno diferente hay que especificarlo. el ultimo no se cuenta.

# Range(inicio, fin)
'''for a in range(5, 10):
    print(a)'''

# Range(inicio, fin, paso)
'''for h in range(0,10, 2): # esto significa que los numeros van de dos en dos.
    print(h)'''

## Ahora con numeros negativos.
'''for o in range(-9, 0):
    print(o)'''

# cuenta regresiva.
'''for l in range(10, 0, -1):
    print(l)'''

## range() crea los numeros sobre la marcha, o sea que no se guarda na de eso, pq no es una pinche lista.

# Esto es para hacerlo una lista. no es recomendable, ni idea del pq.
'''n = list(range(5))
n = range(12)

list_of_n = list(n)
print(list_of_n)'''

## Esto se utiliza para hacer algo varias veces.

## Esta es una manera SIN el range. Este imprime 5.
print('\n Usando el while: ')
contador = 0
while contador < 5:
    print('hols')
    contador +=1

## Esta es CON el range. Este imprime 7.
print('\n Usando el Range():')
for _ in range(7):
    print('Tom R')