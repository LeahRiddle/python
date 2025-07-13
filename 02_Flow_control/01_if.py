###
# 01 - sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de codigo si se cumplen ciertas condiciones.
###

### Importar una biblioteca diq para ayudar a acceder al sistema y pode rponer un comando.

import os
os.system("cls")


## Sentencia simoke condicional

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

age = 23
carnet = True

if age >= 18 and carnet:
    print("Puedes manejar")
else:
    print("No conduzcas")


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

""""
if edad > 18:
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