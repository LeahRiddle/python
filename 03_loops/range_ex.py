###
print("EJERCICIOS (range)")
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1: Imprimir numeros del 1 al 10")

for j in range(1, 11):
    print(j)

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2: Imprimir numeros impares del 1 al 20.")

for u in range(1, 21):
    if u % 2 != 0:
        print(u)

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3: Imprimir numeros multiplos de 5.")
for l in range(5, 50, 5):
    print(l)


# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4: Imprimir numeros en orden inverso.")

for k in range(10, 0, -1):
    print(k)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5: Suma de numeros en un rango.")

l = 0

for s in range(1, 101):
    l += s
print(l)

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6: Tabla de Multiplicar.")

print('\n Por favor ingresar un numero natural entero.')
n = int(input())
m = 0
print(f'\n La tabla de multiplicar de {n} es: ')
for f in range(1,11):
    m = n*f
    print(f'{n} x {f} = {m}' )
    