from os import system
if system("clear") != 0: system("cls")

'''
1.  Contar cuántas veces aparece un valor en una lista
2.  Eliminar elementos duplicados de una lista
3.  Buscar el valor máximo en una lista
4.  Contar cuántos elementos cumplen una condición
5.  Agrupar usuarios por rol
const usuarios = [
  { nombre: 'Ana', rol: 'admin' },
  { nombre: 'Luis', rol: 'user' },
  { nombre: 'Carlos', rol: 'admin' },
  { nombre: 'Sara', rol: 'user' }
];

for t in range(1,20):
    print(t)

    usuarios = [
    {"nombre": "Ana", "rol": "admin"},
    {"nombre": "Luis", "rol": "user"},
    {"nombre": "Carlos", "rol": "admin"},
    {"nombre": "Sara", "rol": "user"}

]
a =  'admin'
'''

usuarios = [
    {"nombre": "Ana", "rol": "admin"},
    {"nombre": "Luis", "rol": "user"},
    {"nombre": "Carlos", "rol": "admin"},
    {"nombre": "Sara", "rol": "user"}

]

## Primer ejercicio.

print('\n Ejercicio 1: contar cuantas veces "admin" sale en el diccionario.')

c = 0
for a in usuarios:
    if a["rol"] == "admin":
        c += 1
print(f'\n La cantidad de admin que hay son: {c}')

print('\n Ejercicio 2: Eliminar menajes duplicados en una lista.')

lista = [1, 2, 4, 7, 8,3, 1, 5, 5, 5, 2]
print(f'\n Esta es nuestra lista con numeros repetidos: {lista}')
v = []
for i in lista:
    if i not in v:
        v.append(i)

print(f'\n Esta es nuestra lista sin numeros repetidos: {v}')

# Ejercicio 3.

print('\n Ejercicio 3: Buscar el maximo de una lista.')
lista2 = [1, 2, 4, 7, 8,3, 1, 5, 5, 5, 2]
print(f'\n Esta es nuestra lista: {lista2}')
maxi = lista2[0]
for h in lista2:
    if h > maxi:
        maxi = h
print(f'\n El maximo de la lista es: {maxi}')


print('\n Ejercicio 4: contar cuantos elemntos cumplen una condicion.')
numeros = [4, 9, 12, 7, 15, 22, 18, 5, 3]
c = 0
print(f'\n Esta es nuestra lista {numeros}, tendremos que buscar cuantos son multiplos de 3.')

for l in numeros:
    if l % 3 == 0:
        c += 1
print(f'\n La cantidad de numeros que son multiplo de 3 son: {c}')

## Ejercicio 5.
print('\n Ejercicio 5: Agrupar usuarios por rol.')
usuarios = [
    {"nombre": "Ana", "rol": "admin"},
    {"nombre": "Luis", "rol": "user"},
    {"nombre": "Carlos", "rol": "admin"},
    {"nombre": "Sara", "rol": "user"}

]

user = []
admin = []

for w in usuarios:
    if w["rol"] == "admin":
        admin.append(w["nombre"])
    else:
        user.append(w["nombre"])
print(f'\n Esta es la lista de los que son administradores: {admin}')
print(f'Esta es la lista de los que son usuarios: {user}')