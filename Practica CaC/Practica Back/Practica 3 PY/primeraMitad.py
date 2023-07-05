"""
1) Crear la clase Persona con los métodos “set_nombre”, “set_edad”,
“get_nombre”, “get_edad” y “print_persona”. Luego crear dos objetos del tipo
Persona e imprimirlos por consola.
2) Agregarle a la clase anterior un constructor que reciba nombre y edad.
3) Agregarle a la clase anterior un método “es_mayor_de_edad” que devuelva
True o False.
4) Agregarle un método “es_mayor_que” el cual recibe un objeto persona y
compara su edad con la del objeto actual.
5) Agregarle un método estático “get_mayor” que reciba dos objetos Persona y
devuelva el de edad mayor.
"""
class persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def set_nombre(self,nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre
        
    def set_edad(self,edad):
        self.edad = edad
        
    def get_edad(self):
        return self.edad
        
    def printPersona(self):
        print (f'Mi nombre es {self.nombre} y mi edad es {self.edad}')

    def es_mayor_que(self):
        if (self.edad >= 18):
            print(f'Es mayor de edad, tiene {self.edad}')
        else:
            print(f'Es menor de edad, tiene {self.edad}')

    @staticmethod
    def get_mayor (persona1,persona2 ):
        if (persona1.edad > persona2.edad):
            print(f'{persona1.nombre} es mayor que {persona2.nombre}')
        else:
            print(f'{persona2.nombre} es mayor que {persona1.nombre}')

persona1 = persona('Jorge', 15)
persona2 = persona('Carlos', 23)
mayor = persona.get_mayor(persona1,persona2)
persona1.printPersona()
persona1.es_mayor_que()
