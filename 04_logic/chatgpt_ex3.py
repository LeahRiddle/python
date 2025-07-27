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