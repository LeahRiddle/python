import os
os.system("cls")

"""
Ejercicio: Registro de Temperaturas
1) Pide al usuario que ingrese cuántos días quiere registrar (input, casting, variable).

2)Crea una lista vacía para guardar las temperaturas (list, variable).

3) Usa un ciclo para pedir al usuario la temperatura de cada día (input, casting, append).

4) Después de registrar, imprime la lista de temperaturas (print, list).

5) Pregunta al usuario si quiere ver las temperaturas en Fahrenheit o Celsius (input, variable, if/elif/else, booleans).

6) Si elige Fahrenheit, convierte todas las temperaturas de Celsius a Fahrenheit usando una lista nueva (casting, list method).

7) Imprime la lista convertida (print).

8) Usa un condicional para decir si la temperatura más alta es mayor a 30°C (o su equivalente en F) y muestra un mensaje especial (if, else, booleans, list method).

"""

print("Bienvenido al programa de registro de temperaturas.")
print("\n Por favor, ingresar la cantidad de dias que desea registrar.")
dias = int(input())

temperatura = []