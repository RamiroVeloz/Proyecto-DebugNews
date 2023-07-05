"""
10) Escribir un programa que escriba en pantalla los divisores de un número dado
11) Escribir un programa que nos diga si un número dado es primo (no es divisible
por ninguno otro número que no sea él mismo o la unidad)
12) Pide una nota (número). Muestra la calificación según la nota:
 0-3: Muy deficiente
 3-5: Insuficiente
 5-6: Suficiente
 6-7: Bien
 7-9: Notable
 9-10: Sobresaliente
13) Realiza un programa que escriba una pirámide del 1 al 30 de la siguiente
forma:
1
22
333
4444
55555
666666
……….
14) Haz un programa que escriba una pirámide inversa de los números del 1 al
número que indique el usuario de la siguiente forma (suponiendo que indica 6):
666666
55555
4444
333
22
1
15) Crear un programa que escriba los números del 1 al 500, y que indique cuales
son múltiplos de 4 y de 9 y que cada 5 líneas muestre una línea horizontal. Por
ejemplo:
1 2 3
4 (Múltiplo de 4)
5
------------------------------------------------------------
6 7
8 (Múltiplo de 4)
9 (Múltiplo de 9)
10
"""



def diez ():
    num = int(input('Ingrese un numero: '))
    for n in range (1,num):
        if ((num % n) == 0):
            print(f'El numero es divisible por {n}')

def once():
    ch = True
    num = int(input('Ingrese un numero: '))
    for n in range (2,num -1):
        if (num % n == 0):
            ch = False
            break
        else:
            ch = True
    if (ch == True):
        print (f'El numero {num} es primo.')
    else:
        print (f'El numero {num} no es primo.')

def doce():
    nota = float(input('Ingrese una nota: '))
    if (0 <= nota < 3):
        print('Muy deficiente.')
    elif (3 <= nota < 5):
        print('Insuficiente.')
    elif (5 <= nota < 6):
        print('Suficiente.')
    elif( 6 <= nota < 7):
        print('Bien')
    elif (8 <= nota < 9):
        print ('Notable.')
    elif (9 <= nota <= 10):
        print('Sobresaliente')

def trece ():
    for i in range (0,30):
        for j in range (0,i):
            print (i, end = ' ')
        print()

def catorce():
    for i in range ( 30, 0, -1):
        for j in range ( 0, i):
            print(i, end = ' ')
        print()

def quince():
    for i in range (1,500):
        if (i % 4 == 0 ):
            print(i, ' es multiplo de 4.')
        elif (i % 9 == 0):
            print (i, ' es multiplo de 9.')
        else:
            print(i)
        print()

#diez()
#once()
#doce()
#trece()
#catorce()
quince()
