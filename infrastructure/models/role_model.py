from django.db import models

class RoleModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'roles'
        managed = True

    def __str__(self):
        return self.nombre
