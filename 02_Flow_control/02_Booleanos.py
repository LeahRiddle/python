###
# 02 - Booleanos
# Valores logicos: True y False
# Operadores logicos: and, or, not  (Esto ni idea de porque se puso.)
# Fundamentos para el control de flujo y la logica de programación.
###

import os
os.system("cls")

# Los booleanos representan valores de verdad: True o False.
print(True)  # Imprime: True
print(False)  # Imprime: False

# Operadores de comparación que devuelven booleanos.

print("5 > 3", 5 > 3)  # Imprime: True
print("5 < 3", 5 < 3)  # Imprime: False  
print("5 == 5", 5 == 5)  # Imprime: True
#print("5 != 3", 5 != 3)  # Imprime: True
print("5 >= 5", 5 >= 5)  # Imprime: True
print("5 <= 3", 5 <= 3)  # Imprime: False

## Comparaciones con cadenas de texto
print("manzana < pera:", "manzana" < "pera")  # Imprime: True, esto debido a que es por orden alfabetico, tambien es sensible a mayusculas y minusculas.
print("manzana > pera:", "manzana" > "pera")  # Imprime: False

## Operadores lógicos: and, or, not

#AND: Devuelve True si ambas condiciones son verdaderas.
print("True and False:", True and False)  # Imprime: False.
print("False and False:", False and False)  # Imprime: False.

#OR: Devuelve True si al menos una de las condiciones es verdadera.
print("True or False:", True or False)  # Imprime: True.
print("True or True:", True or True)  # Imprime: True.

#NOT: Invierte el valor booleano.
print("not True:", not True)  # Imprime: False.
print("not False:", not False)  # Imprime: True.

# Tablas de verdad, para referencias:

# AND
print("\nTabla de verdad AND:")
print("A     B | A and B")  
print("True  True |", True and True)
print("True  False |", True and False)
print("False True |", False and True)
print("False and False:", False and False) 

# OR
print("\nTabla de verdad OR:")
print("A     B | A or B")
print("True  True |", True or True) 
print("True  False |", True or False)
print("False True |", False or True)
print("False and False:", False or False)

# NOT
print("\nTabla de verdad NOT:") 
print("A     | not A")
print("True  |", not True)  
print("False |", not False)