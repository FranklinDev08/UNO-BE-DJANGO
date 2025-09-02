from django.db import models

# TODO: Definir el modelo de auditoría según las necesidades del proyecto
class AuditoriaModel(models.Model):
    usuario_id = models.BigIntegerField()
    accion = models.CharField(max_length=255)
    tabla = models.CharField(max_length=50)
    registro_id = models.BigIntegerField(null=True, blank=True)
    detalles = models.TextField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    # Asignar el nombre de la tabla en la base de datos
    class Meta:
        db_table = 'auditoria'
        managed = True

    # Retornar una representación legible del registro de auditoría
    def __str__(self):
        return f"{self.usuario_id} - {self.accion} - {self.tabla}"