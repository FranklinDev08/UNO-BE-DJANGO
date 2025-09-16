class RoleEntity:
    def __init__(self, nombre, descripcion=None, id=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion