"""1) Escribe un programa muestre por pantalla “Hello World”.
2) Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5.
3) Escribe un programa que pida el nombre del usuario y escriba un texto que
diga “Hola nombreUsuario”
4) Escribe un programa que pida un número, pida otro número y escriba el
resultado de sumar estos dos números.
5) Escribe un programa que pida dos números y escriba en la pantalla cual es el
mayor.
6) Escribe un programa que pida 3 números y escriba en la pantalla el mayor de
los tres.
7) Escribe un programa que pida un número y diga si es divisible por 2
8) Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o
7 (sólo hay que comprobar si lo es por uno de los cuatro)
"""


def uno ():
    print ('Hello World')

def dos():
    print ('El resultado de la suma de 3 + 5 es ', 3 + 5)

def tres():
    texto = input('Ingrese un texto: ')
    print (f'Hola {texto}')

def cuatro():
    n1 = input('Ingrese un numero: ')
    n1 = int(n1)
    n2 = input('Ingrese otro numero: ')
    n2 = int(n2)
    res = n1 + n2
    print (f'El resultado de la suma de los numeros ingresados es: {res}')

def cinco():
    n1 = int(input('Ingrese un numero: '))
    n2 = int(input ('Ingrese otro numero: '))
    if (n1 > n2):
        print (f'{n1} es mayor que {n2}')
    else:
        print(f'{n2} es mayor que {n1}')

def seis():
    n1 = int(input('Ingrese un numero: '))
    n2 = int(input ('Ingrese otro numero: '))
    n3 = int(input ('Ingrese otro numero: '))
    if (n1 > n2) & (n1 > n3):
        print (f'El numero {n1} es el mayor de los tres.')
    elif (n2 > n1)  & (n2 > n3):
        print (f'El numero {n2} es el mayor de los tres.')
    else:
        print(f'El numero {n3} es el mayor de los tres.')

def siete ():
    n1 = int(input ('Ingrese un numero: '))
    if (n1 % 2 == 0):
        print ('El numero ingresado es divisible por dos.')
    else:
        print('El numero ingresado no es divisible por dos.')

def ocho():
    nums = [2,3,5,7]
    aux = int(input('Ingrese un numero: '))
    for n in nums:
        if( aux % n == 0):
            print ('El numero fue divisible por: ', n)
            break

uno()
dos()
tres()
cuatro()
cinco()
seis()
siete()
ocho()