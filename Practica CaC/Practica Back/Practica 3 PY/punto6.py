"""
Realizar un programa que conste de una clase llamada Alumno que tenga
como atributos el nombre y la nota del alumno. Definir los métodos para
inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la
nota y si ha aprobado o no
"""
class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre;
        self.nota = nota
    
    def __str__(self):
        return (f'El alumno {self.nombre} tiene una nota de {self.nota}.')
    
    def esta_aprobado (self):
        if (self.nota > 6 ):
            print(f'El alumno {self.nombre} esta aprobado.')
        else:
            print(f'El alumno {self.nombre} esta desaprobado.')

a1 = Alumno('Carlos', 7)
a2 = Alumno('Jorge', 5)
print(a1)
print(a2)
ap1 = a1.esta_aprobado()
ap2 = a2.esta_aprobado()
