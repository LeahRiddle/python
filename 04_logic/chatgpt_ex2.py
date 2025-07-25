import os
os.system('cls')

## Ejercicios de diccionarios de chat gpt.

## PRIMER EJERCICIO.
print('\n Ejercicio 1: Acceder a un valor por clave.')
# Dado este diccionario:
persona = {"nombre": "Laura", "edad": 20, "ciudad": "Santiago"}
# Imprime el valor de la clave "edad"

print(f' El valor de la clave "edad" es: {persona["edad"]}')

## SEGUNDO EJERCICIO.
print('Ejercicio 2: Agregar un nuevo elemento.')
# Dado este diccionario:
animal = {"tipo": "perro", "edad": 5}
# Agrega una nueva clave "nombre" con el valor "Toby"
animal["nombre"] = "Toby"
print(animal)

## TERCER EJERCICIO.

print('Ejercicio 3: Verificar si una clave existe.')
# Dado este diccionario:
colores = {"rojo": "#FF0000", "verde": "#00FF00"}
# Verifica si la clave "azul" existe y muestra un mensaje si no está

"""for a in colores:"""
if "azul" not in colores.keys():
        print('La clave "azul" no existe en este diccionario.')

## CUARTO EJERCICIO.
print('Ejercicio 4: Crear un diccionario desde dos listas')
# Dadas estas dos listas:
nombres = ["Ana", "Luis", "Pedro"]
edades = [20, 21, 19]
dic = {}
# Crea un diccionario que relacione cada nombre con su edad
# Resultado esperado: {'Ana': 20, 'Luis': 21, 'Pedro': 19}

'''dic.keys(nombres) 
dic.values(edades)
print(dic)'''

# Esta es la version de chatgpt.
'''dic = dict(zip(nombres, edades))
print(dic)'''

for a in range(len(nombres)):
        dic[nombres[a]] = edades[a]    
print(dic)

## QUINTO EJERCICIO.
print('Ejercicio 5: Recorrer un diccionario e imprimir claves y valores.')
# Dado este diccionario:
productos = {"pan": 15, "leche": 20, "café": 40}
# Imprime cada producto con su precio en una línea
# Ejemplo de salida: pan cuesta 15 pesos

for k, v in productos.items():
        print(f"El producto {k} cuesta {v}")


## SEXTO EJERCICIO.

print('\n Ejercicio 6: Contar cuántas veces aparece cada letra en una palabra.')

palabra = "banana"
dicts = {}

for o in palabra:
        if o in dicts:
                dicts[o] += 1
        else:
                dicts[o] = 1
print(dicts)

## SEPTIMO EJERCICIO.
print('\n Ejercicio 7: Encontrar el valor máximo en un diccionario.')
calificaciones = {"Ana": 85, "Luis": 95, "Carlos": 78, "Sara": 92}
mai = 0
best = ""
for k, n in calificaciones.items():
        if n > mai:
            mai = n
            best = k

print(f"{best} tiene la nota más alta: {mai}")

## OCTAVO EJERCICIO.
print("Ejercicio 8: Sumar todos los valores del diccionario.")

# Objetivo: Sumar todas las ventas y mostrar el total.
ventas = {"lunes": 150, "martes": 200, "miércoles": 180}
t = 0

for l in ventas.values():
        t += l
print(f'El total es: {t}')

## NOVENO EJERCICIO.

print('Ejercicio 9: Invertir claves y valores de un diccionario.')

paises = {"RD": "República Dominicana", "US": "Estados Unidos", "MX": "México"}
## 📌 Objetivo: Crear un nuevo diccionario donde las claves sean los nombres de los países y los valores sus códigos.
country = {}

for k,v in paises.items(): country[v] = k
print(country)

## DECIMO EJERCICIO.
print('\n Ejercicio 10: Contar cuántas veces aparece cada palabra en una frase.')
palabra = "hola mundo hola hola"
contador = {}

for c in palabra.split():
        if c in contador:
                contador[c] += 1
        else:
                contador[c] = 1
print(contador)

## EJERCICIO 11.
print('\n Ejercicio 11: Sumar los valores comunes entre dos diccionarios.')
tienda_a = {"pan": 10, "leche": 5, "huevos": 8}
tienda_b = {"leche": 7, "pan": 3, "café": 4}
tt = {}
## 📌 Objetivo: Crear un nuevo diccionario solo con los productos que están en ambas tiendas, y sumar sus cantidades.

for k,v  in tienda_a.items():
        if k in tienda_b:
            suma = tienda_a[k] + tienda_b[k]
            tt[k] = suma 

print(tt)

## EJERCICIO 12.

print('\n Ejercicio 12: Invertir un diccionario con listas.')
materias = {
    "Juan": ["Mate", "Historia"],
    "Ana": ["Historia", "Biología"],
    "Luis": ["Biología", "Mate"]
}
new_dic = {}
#Objetivo: Crear un nuevo diccionario donde las materias sean claves, y los valores sean listas con los nombres de los estudiantes que las tienen.

for k, v in materias.items():
   for materia in v:
        if materia not in new_dic:
            new_dic[materia] = []
        new_dic[materia].append(k)     
print(new_dic)
