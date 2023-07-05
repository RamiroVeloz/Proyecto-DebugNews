"""
Realizar un programa en el cual se declaren dos valores enteros por teclado
utilizando el método __init__. Calcular después la suma, resta, multiplicación y
división. Utilizar un método para cada una e imprimir los resultados obtenidos.
Llamar a la clase Calculadora.
"""

class Calculadora:
    def __init__(self, v1 ,v2 ):
        self.v1 = int(v1)
        self.v2 = int(v2)

    def suma (self):
        return (self.v1 + self.v2)
    
    def resta (self):
        return(self.v1 - self.v2)
    
    def mult (self):
        return (self.v1 * self.v2)
    
    def divi (self):
        return (self.v1 / self.v2)
    
val1 = int(input('Ingrese un valor:'))
val2 = int(input('Ingrese un valor:'))

calc = Calculadora(val1,val2)
print(calc.suma())
print(calc.resta())
print(calc.mult())
print(calc.divi())