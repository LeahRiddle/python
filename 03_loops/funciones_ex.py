from os import system
if system("clear") != 0: system("cls")

# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora

print('\n Ejercicio de funciones.')

## Ejercicio 2.
print('\n Ejercicio 2: Doble del numero.')

def double(a):
    d = a*2
    print(f'\n El doble de {a} es: {d}')

double(5)

## Ejercicio 3.
print(f'\n Ejercicio 3: Verificar si es mayor de edad.')

def age(a):
    if a >= 18:
        print("Eres mayor de edad.")
    else:
        print('\n No eres mayor de edad.')
    
age(12)

## Ejercicio 4.
print('\n Ejercicio 4: Area de un cuadrado.')

def areas(lado):
    r = lado * lado
    print(f"\n Basado en el lado entregado ({lado}), el valor del area es {r}.")

areas(12)


## Ejercicio 5.
print('\n Ejercicio 5: Contar letras.')
def letra(l):
    o = len(l)
    print(f'\n La cantidad de letras que tiene la palabra "{l}" es: {o}')

letra("Banana_Fish")