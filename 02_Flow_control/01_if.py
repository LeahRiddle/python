###
# 01 - sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de codigo si se cumplen ciertas condiciones.
###

### Importar una biblioteca diq para ayudar a acceder al sistema y pode rponer un comando.

import os
os.system("cls")


## Sentencia simple condicional

"""
age = 18

if age >= 18:
    print("Eres mayor de edad");
"""
    ##Si o si tiene que tener tabulacion poruqe o si no no funcionaria, supuestamentte, se puede poner ;, pero no esta recomendadod

# Ahora vamos con  el else.

"""
age = 12
if age >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
"""

# Ahora vamos con el elif, no se puede poner el and, hazlo asi ombe y ya, que caga. el else no es obligatorio, pero obvio que lo usaria.

"""
print("Escribe tu nota")
nota = input()
nota = int(nota)


if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bien")
elif nota >= 5: 
    print("Diq Aprobado")
else:
    print("Reprobado")
"""

 ## Operaores logicos
 # Condiciones multiples

"""
age = 23
carnet = True

if age >= 18 and carnet:
    print("Puedes manejar")
else:
    print("No conduzcas")

"""
## otra condicion multiple, este es con OR


"""
if age >= 18 or carnet:
    print("Puedes manejar")
else:
    print("No conduzcas")

## en este utilizamos el not

vacaciones = False

if not vacaciones:
    print("Haz la tarea")
    """

## Ahora vamos a anidar condicionales ombe, toy hartica.
##### ESTO NO DEBERIAMOS HACERLO, se puedem pero no dberiamos aunque a veces se utiliza.

""" 
if edad >= 18:
    if money:
        print("Puedes fumar droga")
    else:
        print("No lo hagas mi pana")
else: 
    print("Ni eres suficiente para fumar droga, equide")
"""
##Esto es lo que recomienda hacer
 
"""
edad = 20
money = True

if edad < 18:
    print("Bro, no puedes, klk contigo")
elif money:
    print("Puedes solo porque tienes dinero")

elif not money:
    print("Ni siquiera tienes dinero ombe, lambon, veteme de ahi.")
"""

### Esto fue algo que hice, solo porque si, queria practicar.

"""
print("Por favor ingresar su edad")

edad = int(input())
print("Ahora, por favor escriba si tiene dinero o no, si tiene dinero escriba si, si no tiene no escriba nada.")

money = bool(input())

if edad >= 18 and money:
    print("Puedes fumar droga")
elif money:
    print("Tienes el dinero, pero no la edad.")
elif edad >= 18:
    print("Tienes la edad, pero no el dinero, baboso.")
else:
    print("No tienes ningun requisito, y esa loquera?")
"""

### Esto no recuerdo como lo llamo, pero era para ver los numeros y el booleano juntos.

num = 5
if num: #True
    print("El numero no es cero.")

numero = 0
if numero: #False
    print("El numero es cero.")

name = "Nani"
if name: #True
    print("El nombre no es vacio.")

nombre = ""
if nombre: #False
    print("El nombre es vacio.")


## Comparacion ==, asignacion =

number = 8 # Asignacion
number8 = number == 8  # Comparacion
if number8:  # Comparacion
    print("El numero es cinco.")


## La condicion ternaria, es una forma  conisa de escribir un if-else en una sola linea.

## [Codigo si cumple la condicion] if [condicion] else [codigo si no cumple la condicion]

print("Por favor ingresar su edad")
age = input()
age = int(age)

message = "Eres mayor de edad" if age >= 18 else "eres menor de edad."
print(message)

# tambien se puede hacer asi.
print("Eres mayor de edad" if age >= 18 else "Eres menor de edad.")



