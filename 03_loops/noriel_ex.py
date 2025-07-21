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

print('\n Ejercicio 2 de chatgpt.')
numeros = [5, 10, 3, 8]
suma = 0

for t in numeros:
    
  suma += t
  print(suma)

print('\n Ejercicio de chatgpt.')

nombres = ["Ana", "Luis", "Carlos", "Sara"]
roles = ["admin", "user", "admin", "user"]

for t in range(len(nombres)):
  if roles[t] == 'admin':
    print(nombres[t])

print('\n Ejercicio 7: Mostrar nombre de estudiantes que pasaron la materia.')
print(f'\n Los estudiantes que obtuvieron 70 o mas puntos fueron: ')
nombres = ["Camila", "José", "Valeria", "Luis", "Andrea"]
notas = [85, 60, 72, 45, 90]

for t in range(len(nombres)):
  if notas[t] >= 70:
    print(nombres[t])

print('\n Ejercicio 8: mostrar los numeros pares')
print('\n Los numeros pares son: ')
numeros = [3, 10, 15, 22, 8, 5, 12]

for t in numeros:
  if t % 2 == 0:
    print(t)

print('\n Ejercicio 9: Los numeros naturales del 1 al 15.')

age = [t for t in range(1, 16) if t > 0 ]
print(age)
    


print('\n Ejercicio 10: Dada una lista con edades, imprimir cuántas personas tienen más de 18 años.')
edades = [16, 21, 19, 14, 25, 30, 17]
contador = 0
for t in edades:
  if t > 18:
    contador += 1
print(f'La cantidad de personas con mas de 18 de edad son: {contador}')

print('\n Ejercicio 11: Dada una lista de palabras, imprimir solo las que tienen más de 4 letras.')
palabras = ["sol", "mar", "playa", "arena", "piedra", "cielo"]

for t in palabras:
  if len(t) > 4:
    print(t)
  

print('\n Ejercicio 12: Dada una lista con números, imprimir el cuadrado de cada número.')
numeros = [2, 4, 6, 8]


for t in numeros:
  cuadrado = t**2
  print(cuadrado)


print('\n Ejercicio 13: Dada una lista con temperaturas en Celsius, imprimir solo las temperaturas que estén por debajo de 0.')

temperaturas = [3, -5, 0, -2, 7, -1]

for t in temperaturas:
  if t < 0:
    print(t)



   
       




