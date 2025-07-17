import os
os.system("cls")

"""
📝 Ejercicio: Verificador de Películas 🎬
Haz un programa que:

Le pida al usuario su nombre y edad.

Le pregunte si quiere ver una película con clasificación R (solo para mayores de 18).

Según su edad, usa condicionales para mostrar un mensaje:

Si tiene 18 años o más → “Puedes ver la película R.”

Si tiene entre 13 y 17 → “Necesitas permiso de un adulto.”

Si tiene menos de 13 → “No puedes ver esta película.”

Guarda el nombre, edad, deseo de ver la peli, y el mensaje final en una lista.

Imprime el tipo de cada dato (usa type()).

Muestra la lista con la información final al final.


"""

print('Bienvenido al programa verificador de peliculas.')
print('\n Por favor ingresar su nombre.')
name = input()
print('\n Ahora por favor ingresar su edad.')
age = int(input())

print('\n Para ver una pelicula clasificacion R por favor escribir algo, de no ser asi, no escriba nada.')
desicion = bool(input().strip())

message = ""
if age >= 18 and desicion:
    message = "Puedes ver la pelicula R."
    print(f"\n {message} ")
    
elif age >= 13 and desicion:
    message = "Necesitas permiso de un adulto."
    print(f"\n {message}")

elif age < 13 and desicion:
    message = 'No puedes ver la pelicula.'
    print(f"\n {message} ")

else:
    message = 'Puedes ver la pelicula sin problemas.'
    print(f"\n {message} ")

lista: list[str | int | bool ] = [name, age, desicion, message]

print("\n Estos son los tipos de datos de la informacion ingresada.")
print('\n Este es el tipo de dato del nombre: ', type(name))
print("De la edad: ", type(age))
print('De la desicion a tomar: ', type(desicion))
print("Del mensaje final mostrado: ", type(message))

print(f'\n Esta es la informacion ingresada guardada en una lista: {lista}')

print("\n Gracias por usar el programa verificador de peliculas (●'◡'●)")

