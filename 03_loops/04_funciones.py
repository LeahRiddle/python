###
# 04 - Funciones
###
#### NO VER BANANA FISH, ESO ES DEL DIABLO. DESPUES SE DURA 4 DIAS EN DEPRESION.

# Bloques de codigo reutilizabes y parametrizables para tareas especificas.

from os import system
if system("clear") != 0: system("cls")

print('\n Funciones: ')

'''

def nombre_de_la_funcion(paranetro1, parametro2, ...):
 # docstring
 # cuerpo de la funcion
 return valor_de_retorno #opcional

'''

# Ejemplo de una funcion para imprimir algo en consola.

#Esta es la definicion de la funcion, para que se imprima tenemos que llamarla.
def saludo():
    print('Hola')

# ASi se llama una funcion. solo hay que poner el nombre y los parentesis.
saludo()

#Ejemplo de una funcion con parametro
'''def saludar_a(nombre): #nombre = parametro
    print(f'Sayonara, {nombre}')

saludar_a("Eiji")''' # Eiji 💔 = argumento.

# El parametro es lo que acepta la funcion.
# El argumento es lo que se le pasa a la funcion.
### Ash esta vivo y feliz mi gente (Ayuada💔, no es cierto.)

# Funciones con mas parametros.
'''def suma(a, e): #Ash y Eiji💔
    sumar = a + e
    return sumar'''
#Se puede hacer asi.
'''r = suma(17, 17)
print(r)'''

#o asi.
'''print(suma(17, 17))'''

# Documentar las funciones con docstring.

'''def resta(y, h): #Yoshiki y 'Hikaru' 💔
    """Resta dos numeros y devuelve el resultado."""
    return y - h'''
## Se puede acceder a los comentarios usando __doc__
'''print(resta.__doc__)'''

'''help(resta) ## esto era como para ver bn la funcion o algo asi.'''

## Parametro por defecto.
'''def mult(n, h = 2):
    return n * h
print(mult(2))'''
# el valor es opcional, pero se lo puedes especificar.

# Argumento por clave
def describir_gente(nombre, edad, sexo):
    print(f"Soy {nombre}, tengo {edad} de edad y me identifico como {sexo}")

#parametro son posicionales.
'''describir_gente("Ash", 17, "Hombre")

describir_gente(909, "Dino (ascco)", "una asquerosidad.")''' ## Maldito calvo asqueroso de mierda, tenias que morirte hijo de la gran puta pedofilo inservible.

#Argumento por clave.
# parametro nombrados
describir_gente(sexo="Hombre", nombre="Ash", edad= 17)