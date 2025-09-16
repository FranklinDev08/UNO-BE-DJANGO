from django.db import models
from infrastructure.models.user_model import User

# TODO: Modelo para registrar acciones de auditoría en la base de datos
class Auditoria(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    accion = models.CharField(max_length=255)
    tabla = models.CharField(max_length=50)
    registro_id = models.BigIntegerField(null=True, blank=True)
    detalles = models.TextField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Auditoria"

    def __str__(self):
        return f"{self.accion} en {self.tabla} por {self.usuario}"
