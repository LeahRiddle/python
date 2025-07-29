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

## EJERCICIO 5.
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

dicw = {}
for k, v in ventas.items():
    t = 0
    for q in v.values():
         t += q
    dicw[k] = t

print(dicw)


## EJERCICIO 6.
print('\n Ejercicio 6: Diccionario de listas ordenadas.')
#Objetivo:
#Ordenar las listas de números dentro de un diccionario.
datos = {
    "a": [5, 3, 9, 1],
    "b": [20, 11, 15],
    "c": [7, 6, 8]
}
orden = {"orden": []}

for k, v in datos.items():

    v.sort()
    orden["orden"].extend(v)
print(orden)

## EJERCICIO 7.
print('\n Ejercicio 7: Combinar dos listas en un diccionario.')
nombres = ["Ana", "Luis"]
edades = [20, 25]

r = dict(zip(nombres, edades))
print(r)

## EJERCICIO 8.
print('\n Ejercicio 8: Combinar dos diccionarios')

"""Objetivo:
Unir dos diccionarios sumando los valores de claves repetidas. Si una clave solo está en uno, se mantiene."""
dic1 = {"manzana": 2, "pera": 3, "mango": 1}
dic2 = {"manzana": 4, "uva": 1, "mango": 5}
dicR = {}
for k, v in dic1.items(): dicR[k] = v
    
for k2, v2, in dic2.items():
    if k2 in dicR:
        dicR[k2] += v2
    else:
        dicR[k2] = v2
print(dicR)


## EJERCICIO 9.
print('\n Ejercicio 9: ')