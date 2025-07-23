import os

# Para Windows
os.system('cls')

##
# 04 - Dictionaries.
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.
###

# Ejemplo tipico de diccionario.

print('\n Diccionarios.')


gente = {
    "nombre": "Miyamura",
    "edad": 16,
    "Es_estudiante": True,
    "Calificaciones": [6, 9, 8],
    "Redes": {
        "x": "ola",
        "face": "pola",
        "ig": "sola"
    }
}

## Apara acceder a los valores.
# gente = nombre del diccionario
# "nombre" = clave del diccionario
# op: [0] indice de la posicion de la lista a mostrar.
print(gente["nombre"])
print(gente["Calificaciones"][0])
print(gente["Redes"]["face"])

# cambiar los valores al acceder
gente["edad"] = 18
gente["Calificaciones"][0] = 7
gente["Redes"]["face"] = "azul" 

print(gente["edad"])
print(gente["Calificaciones"][0])
print(gente["Redes"]["face"])
print(gente)

# Eliminar completamente una propiedad.
'''del gente["edad"]
print(gente)'''

## Esto lo elimina y modifica el objeto, ni puta idea.
ola = gente.pop("Calificaciones")
print(f'\n Las calificaciones del estudiante son: {ola}')
print(gente)

# sobreescribir un diccionario con otro diccionario (update).

a = {"name": "nanami", "age": 17}
b = {"name": "tomoe", "es_estudiante": True}

a.update(b)
print(a)

# Comprobar si existe una propieda.
print("name" in gente) # False
print("nombre" in gente) # True

# Obtener todas las claves.
print('\n Keys:')
print(gente.keys())

# Obtener los valores.
print('\n Values:')
print(gente.values())

# Obtener tanto clave como valor.
print('\n Items:')
print(gente.items())
# este es bastante util para el for, ya que es iterable.
for key, value in gente.items():
    print(f"{key}: {value}")