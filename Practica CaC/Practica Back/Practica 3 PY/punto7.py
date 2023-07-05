"""
Desarrollar un programa que cargue los datos de un triángulo. Implementar una
clase con los métodos para inicializar los atributos, imprimir el valor del lado
con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o
escaleno).
"""

class Tri:
    def __init__(self,l1,l2,l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
    
    def __str__(self):
        return (f'El lado uno mide {self.l1}cm, el lado dos mide {self.l2}cm y el lado tres mide {self.l3}cm')

    def lado_mayor (self):
        if (self.l3 < self.l1 > self.l2):
            print (f'El lado uno {self.l1} es el lado mayor.')
        elif (self.l3 < self.l2 > self.l1):
            print(f'El lado dos {self.l2} es el mayor.')
        else:
            print(f'El lado tres {self.l3} es el mayor.')
    
    def tipo_tri (self):
        if (self.l1 == self.l2 == self.l3):
            print('El triangulo es equilatero.')
        elif (self.l1 == self.l2 or self.l2 == self.l3 or self.l1 == self.l3):
            print('El triangulo es isoceles.')
        elif (self.l1 != self.l2 != self.l3):
            print('El triangulo es escaleno.')


t1 = Tri(1,2,4)
print(t1)
t1.lado_mayor()
t1.tipo_tri()