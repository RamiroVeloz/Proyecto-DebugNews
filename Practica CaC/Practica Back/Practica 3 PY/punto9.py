"""
Realizar una clase que administre una agenda. Se debe almacenar para cada
contacto el nombre, el teléfono y el email. Además deberá mostrar un menú
con las siguientes opciones: Añadir contacto, Listar contactos, Buscar contacto,
Editar contacto, Cerrar agenda.
"""

class Agenda:

    def __init__(self,nom,tel,email):
        self.nom = nom
        self.tel = tel
        self.email = email
    
    def __str__(self):
        return (f'Nombre: {self.nom} Telefono: {self.tel} Email: {self.email}')
    
    