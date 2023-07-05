"""
1) Desarrollar una función que reciba tres números positivos y devuelva el mayor
de los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor
estricto devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar
también un programa para ingresar los tres valores, invocar a la función y
mostrar el máximo hallado, o un mensaje informativo si éste no existe.
2) Desarrollar una función que reciba tres números enteros positivos y verifique si
corresponden a una fecha válida (día, mes, año). Devolver True o False según
la fecha sea correcta o no. Realizar también un programa para verificar el
comportamiento de la función.
4) Escribir dos funciones separadas para imprimir por pantalla los siguientes
patrones de asteriscos, donde la cantidad de filas se recibe como parámetro:
5) Crear una función lambda que devuelva el cuadrado de un valor recibido cómo
parámetro. Desarrollar además un programa para verificar el comportamiento
de la función.
6) Crear una función lambda para comprobar si un número es par o impar.
Desarrollar además un programa para verificar el comportamiento de la
función.
7) Crear una lista con los cuadrados de los números entre 1 y N (ambos
incluidos), donde N se ingresa desde el teclado. Luego se solicita imprimir los
últimos 10 valores de la lista.
8) Eliminar de una lista de palabras que se encuentren en una segunda lista.
Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.
"""
sq = lambda x:x ** 2
num = int(input('Ingrese un numero: '))
lista = [i for i in range (num)]
for i in range (1,num):
    print(lista[i],end =' - ')
cuadrados = list(map(sq,lista))
for i in range (1,num):
    print(cuadrados[i],end =' - ')
