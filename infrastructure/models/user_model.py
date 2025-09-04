
from django.db import models

class UserModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=100, unique=True)
    rol_id = models.BigIntegerField()  # Aquí podrías poner ForeignKey a Roles
    activo = models.BooleanField(default=True)
    ultimo_login = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'usuarios'
        managed = True

    def __str__(self):
        return self.username
