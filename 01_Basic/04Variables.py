##

# 04 - Variables 
# Las Variables sirven para guardar datos en memoria.

# Py es un lenguaje de tipado dinamico y tipado fuerte.

###

# Asi se asignan las variables
"""
Jaruchan = "tamaki"
print(Jaruchan)

"""
#se pueden re asignar

# Tipado dinamico: el tipo de dato se determina en tiempo de ejecucion. Basicamente no es necesario declararlo explicitamente
"""
#Shino = "Mio"
   # print(type(Shino)) # = str

    # Shino = 1

    # print(type(Shino)) # = int
"""
    # Tipadp fuerte: py no realiza conversiones de tipado automatico.
"""
print(10 + "2") no funciona

print(f"Hola Shino es {Shino}") esta es una forma de usar la variable como en c#.
"""

# No lo recomienda (yo tampoco nmms)

"""
name, age, city = "Shino", 19, "La aldea de la hoja"
"""

#Se puede declarar las variables asi, pero no es recomendable (Quien diablos usaria eso nmms)

"""
print(f"Mi hombre se llama {name}, tiene {age} de edad, y vive en {city}")
"""

#Para el nombre las variables por lo general se utiliza el _ es el unico que es compatible de esos caracteres. ej:
"""
mi_nombre_es = "puta" #snake_case
"""

# Py no tiene variables constante, se puede simular, pero por lo general no tiene
"""
Mi_const = 1212 # UPPER_CASE  - constantes
"""

# la variables no pueden empezar por numeros, guiones o espacio

# Lista de palabras reservadas de py. hay una forma de recuperarla con un modulo, no se puede utilizar como nombre para una variable.

"""
['False', 'None', 'True', 'and', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
]
"""

# TIPOS DE VARIAbLES
"""
sepa_la_bola: bool = True

sepa_la_bola = 23
print(sepa_la_bola)
"""
#Esto es una anotacion, clickbait, pero al poner que al momento de ejecucion se ponga mas estrictos con el tema del tipo de variable esto nos va a dar error, porque ya verifico que la informacion no es compatible con su tipo. bueno, el editor nos dira que esta mal, pero como quiera se ejecuta.
