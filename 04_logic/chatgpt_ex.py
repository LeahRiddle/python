import os
os.system('cls')

## Ejercicios de diccionarios de chat gpt.

print('\n Ejercicios de diccionarios.')

## PRIMER EJERCICIO
print('\n Ejercicio 1: Acceder a un valor por su clave.')

# Dado este diccionario
persona = {"nombre": "Laura", "edad": 20, "ciudad": "Santo Domingo"}
# Imprime la edad de la persona

print(persona["edad"])

## SEGUNDO EJERCICIO
print('\n Ejercicio 2: Agregar una nueva clave.')
# Dado este diccionario
carro = {"marca": "Toyota", "modelo": "Corolla"}
# Agrega una nueva clave llamada "año" con el valor 2020

carro.update({"year": 2020})
#otra manera
'''carro["year"] = 2020'''

print(carro)

## TERCER EJERCICIO.

print('\n Ejercicio 3: Contar cuántos elementos tiene un diccionario.')

# Dado este diccionario
colores = {"rojo": "#FF0000", "verde": "#00FF00", "azul": "#0000FF"}
# Imprime cuántos colores hay en el diccionario

"""for a in colores:
    a = len(colores)"""
a = len(colores)
print(f'\n El diccionario tiene {a} elementos.')

## CUARTO EJERCICIO

print('\n Ejercicio 4: Recorrer un diccionario e imprimir claves y valores')
# Dado este diccionario
paises = {"RD": "República Dominicana", "USA": "Estados Unidos", "MX": "México"}
# Imprime cada clave y su valor en formato: "Clave: RD, Valor: República Dominicana"

for k, v in paises.items():
    print(f'{k}: {v}')

## QUINTO EJERCICIO.

print('\n Ejercicio 5: Sumar valores numéricos de un diccionario.')
# Dado este diccionario
precios = {"manzana": 25, "banana": 15, "pera": 30}
# Calcula el total sumando todos los precios
r = 0
for p in precios.values():
    r += p
print(f'El total de todos los precios es: {r}')

## SEXTO EJERCICIO.
print('\n Ejercicio 6: Actualizar valores en un diccionario.')
productos = {"lápiz": 10, "cuaderno": 25, "borrador": 5}

for c in productos:
    productos[c] = productos[c] + 10
print(productos)

## SEPTIMO EJERCICIO.
print('\n Ejercicio 7: Buscar y mostrar un valor por clave.')

notas = {"Ana": 85, "Luis": 90, "Carlos": 78, "Sara": 92}
print('\n Por favor ingresar el nombre del estudiante.')
name = input().lower()
o = False

for n in notas.keys():
    if name in n.lower():
        print(f'Nota del estudiante: {notas[n]}')
        o = True
   
if not o:
    print("\n Estudiante no encontrado.")

'''notas.keys().lower()'''
'''if name != notas.key():
    print('hola')
else:
    print(False)
'''

## OCTAVO EJERCICIO.
print('\n Ejercicio 8: Eliminar elementos de un diccionario según condición')
inventario = {"manzanas": 10, "bananas": 0, "peras": 5, "naranjas": 0}
lita = []

for n in inventario:
    if inventario[n] == 0:
        lita.append(n)

for a in lita:
    if inventario[a] == 0: del inventario[a]

print(inventario)

## NOVENO EJERCICIO.

print('\n Ejercicio 9: Contar la frecuencia de palabras en una lista.')
palabras = ["manzana", "pera", "manzana", "banana", "pera", "manzana"]
a = {}
for w in palabras:
    if w in a:
        a[w] += 1
    else:
        a[w] = 1
print(a)

## DECIMO EJERCICIO. POR FIN DIOS MIO GRACIAS, ESCUCHASTE MIS PLEGARIAS \(￣︶￣*\))

print('\n Ejercicio 10: Combinar dos diccionarios sumando valores.')
tienda1 = {"manzana": 10, "banana": 5, "pera": 7}
tienda2 = {"banana": 3, "pera": 8, "naranja": 6}
rt = {}
for c, v in tienda1.items():
    rt[c] = v

for k2, v2 in tienda2.items():
    if k2 in rt:
        rt[k2] += v2
    else:
        rt[k2] = v2
print(rt)
        
