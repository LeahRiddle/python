import os
os.system("cls")

"""
print("\n Por favor ingresar la contraseña.")
con = input()
password = 'python123'
intentos = 1

while con != password:
    print('Por favor ingresar la contraseña correcta.')
    con = input()
    intentos += 1

print(f'Acceso concedido despues de {intentos} intentos.')

"""

print('\n Bienvenid@ al cajero automatico.')
saldo = 1000
print('\n Estas son las opciones que tenemos disponibles: ')
print('\n ' \
'1) Ver saldo. ' \
'2) Depositar dinero. ' \
'3) Retirar dinero. ' \
'4) Salir.')
print('\n Por favor ingresar la opcion que desee realizar.')
op = int(input())

while op != 4:
    
    if op == 1:
        print(f'\n Este es su saldo actual: {saldo}')
        break
    elif op == 2:
        print('\n Por favor ingresar el monto.')
        monto = int(input())
        while monto < 0:
            print('\n El monto debe ser mayor a 0.')
            monto = int(input('\n Por favor ingresar un monto valido. '))
        print(f'\n Este es el monto actual: {monto + saldo}')
        break
    elif op == 3:
        print('\n Por favor ingresar el monto.')
        monto = int(input())
        while monto < 0:
            print('\n El monto debe ser mayor a 0.')
            monto = int(input('\n Por favor ingresar un monto valido. '))

        while monto > saldo:
            print("\n Saldo insuficiente. Por favor, ingresar otro monto.")
            monto = int(input())
        if monto <= saldo:
            print(f'\n El monto actual ahora es: {saldo - monto}')
        break

print("\n Gracias por usar nuestro cajero automatico, ten un lindo dia. ( •̀ ω •́ )✧")