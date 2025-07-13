###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí

print("Hola, por favor escribir tu nombre aqui debajo.")

name = input()

print("Aqui por favor la ciudad.")
city = input()

print(f"Gracias por la informacion, tu nombre es {name}, y vives en la ciudad de {city}")


print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))



print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí

a = "1235"
a = int(a)
a = float(a)
print(type(a))

b = 3.99
b = int(b)
print("Al momento de covertilo, el .99 desaparece y se vuelve un 3 solido, mira = {b}")


print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

a = "Leah"
b = 18
c = 1.58

print(f"Hola, mi nombre es {a}, tengo {b}, y mido {c}.")


print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

pi = 3.14
pi = round(pi)
print(pi/2)