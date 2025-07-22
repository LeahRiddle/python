import os
os.system('cls')

"""
¿Está en Equilibrio la Alianza entre Reed Richards y Johnny Storm?

En el universo de los 4 Fantásticos, la unión y el equilibrio entre los poderes es fundamental para enfrentar cualquier desafío. En este problema, nos centraremos en dos de sus miembros:

Reed Richards (Mr. Fantastic), representado por la letra R.
Johnny Storm (La Antorcha Humana), representado por la letra J.

Objetivo:

Crea una función en Python que reciba una cadena de texto. Esta función debe contar cuántas veces aparece la letra R (para Reed Richards) y cuántas veces aparece la letra J (para Johnny Storm) en la cadena.

- Si la cantidad de R y la cantidad de J son iguales, se considera que la alianza entre la mente y el fuego está en equilibrio y la función debe retornar True.
- Si las cantidades no son iguales, la función debe retornar False.
- En el caso de que no aparezca ninguna de las dos letras en la cadena, se entiende que el equilibrio se mantiene (0 = 0), por lo que la función debe retornar True.
"""

con = "RRJJJRJRJJRJJRJR"

def fanta(con):

    con = con.upper()
    countR = con.count("R")
    countJ = con.count("J")
    print(f'\n La cantidad de R son:{countR}, y la cantidad de J son:{countJ}')

    ## EL dice que se puede hacer asi, pero que mejor lo hagamos de la otra manera, que es mas sencilla.
    '''if countR == countR:
        return True
    else:
        return False'''
    
    ## Supuestamente deberiamos mejor hacerlo de esta forma.
    return countR == countJ
## Siempre tratar de evitar hacer codigo que no sirva.

print(fanta("RRRRJRJRJRJRJRJJRJRJ"))
print(fanta("RJRRJRJOSDOIDOI"))
print(fanta("hghghghla"))
