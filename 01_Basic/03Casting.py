###
# 03 - Casting types
# transformar tipos de un valor a otro (basicamente cambiar un tipo a otro, no me acuerdo como se le decia)

###############################################

# py no realiza conversiones automaticas entre tipos incompatibles. 

"""
# print("Conversion de tipos:") era asi que se llamaba, lol.

#   print(type(int("121")))
 """
# no se puede concatenar dos tipos distintos. por ej: str + int. no se puede, q caga. PRIMERO, hay que convertirlo para que se pueda concatenar, asi:
"""
# print(2 + int("231")) #Funciona
# print(2 + "23") # no funciona
"""
# otro ej pero al reves
"""
# print("100" + str(2)) #funciona
# print("100" + 2) #no funciona
"""
# otra weua, se puede convertir el flat a int, pero al hacerlo pierde presicion, debido a que ahora los decimales no van a valer, pura vrg.ej:

"""
# print(3.12) este dio 3.12
# print(int(3.12)) y este 3
"""
# convirtiendo booleanos
#el unico que se puede convertir a False es el 0, pero el 0 pelao, no 0.9, 0.4, SOLO 0
"""
# print(bool(3))
# print(bool(0))
# print(bool(-9))
"""
# bool con string

# la unica que puede ser false es la que no tiene na, "" = esta lit, ni space ni na
"""
# print(bool(""))
# print(bool("Ese huevo quiere sal"))
# print(bool("false"))
"""
# si no son numeros en str, no se puede convertir a int, dahhhhh
# print(int("ho"))

# hay una que redondea, pero ese se va al par mas cercano, por ej: 2.5 = 2, pero 3.5 = 4, pero 3.4 = 3, asi mas o menos se entienede.
"""
# print(round(7.4)) # = 7
# print(round(6.5)) # = 6
# print(round(5.5)) # = 6
"""