import os
os.system('cls')

## EJERCICIOS DE DICCIONARIOS (Sip, todavia tengo qur practicar eso.)

print('Ejercicios de diccionarios \n')
## PRIMER EJERCICIO.

print('Ejercicio 1: Crear un diccionario simple.')
#  Objetivo: Crear un diccionario con información de una persona (nombre, edad y país) y mostrarlo.
person = {"nombre": "Naruto", "edad": 19, "Pais": "Aldea de la hoja"}
print(person)

## SEGUNDO EJERCICIO.
print('\n Ejercicio 2: Acceder a un valor.')
notas = {"Ana": 85, "Luis": 60, "Pedro": 74, "Carlos": 50, "Laura": 92}
"""
Objetivo:
Dado un diccionario de estudiantes y sus notas, reemplaza cada nota con una categoría:

90 o más: "Excelente"

70 0 89: "Bueno"

Menos de 70: "Insuficiente
"""
for k, v in notas.items():
    if v >= 90:
        notas[k] = "Excelente"
    elif v <= 70:
        notas[k] = "Bueno"
    elif v > 70:
        notas[k] = "Insuficiente"

print(notas)

##EJERCICIO 3.
print('\n Ejercicio 3: Encontrar la palabra con más vocales.')
"""
Objetivo:
De una lista de palabras, identificar cuál tiene más vocales (a, e, i, o, u) y mostrarla.
"""
palabras = ["sol", "maravilla", "universo", "luz", "cielo", "estrella"]
vc = "aeiou"
pc = "" 
m = 0

for p in palabras:
    con =  sum(1 for l in p if l in vc)
    if con > m:
        m = con
        pc = p
print(f'La palabra con mas vocales es: {p}')

## EJERCICIO 4.
print('\n Ejercicio 4: Agrupar números por par o impar.')
"""
Objetivo:
Crear un diccionario con dos claves: "pares" y "impares", y agrupar los números según su tipo.
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dic = {"Par": [], "Impar": []}
for n in numeros:
    if n % 2 == 0:
        dic["Par"].append(n)
    else:
        dic["Impar"].append(n)

print(dic)

'''## EJERCICIO 5.
print('\n Ejercicio 5: Sumar valores por grupo.')
"""
]Objetivo:
Dado un diccionario con ventas por mes y por persona, sumar el total de cada persona.
"""
ventas = {
    "Juan": {"enero": 100, "febrero": 120, "marzo": 90},
    "Ana": {"enero": 150, "febrero": 80, "marzo": 110},
    "Pedro": {"enero": 200, "febrero": 50, "marzo": 70}
}

for k, v in ventas.items():'''

## EJERCICIO 6.
print('\n Ejercicio 6: Combinar dos listas en un diccionario.')
nombres = ["Ana", "Luis"]
edades = [20, 25]

r = dict(zip(nombres, edades))
print(r)
