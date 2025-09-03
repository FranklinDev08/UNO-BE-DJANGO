from django.db import models

# TODO:Modelo que representa los roles de usuario en el sistema
class RoleModel(models.Model):
    # Campo identificador único autoincremental
    id = models.BigAutoField(primary_key=True)

    # Nombre del rol (ej: Administrador, Usuario, etc.)
    nombre = models.CharField(max_length=50, unique=True)

    # Descripción opcional del rol
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # Nombre de la tabla en la base de datos
        db_table = 'roles'

        # Indica que Django no debe gestionar esta tabla (ya existe en la BD)
        managed = False

    # Representación legible del rol, usando su nombre
    def __str__(self):
        return self.nombre
