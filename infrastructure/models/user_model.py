from django.db import models

class UserModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    rol_id = models.BigIntegerField()
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'usuarios'
        managed = False

    def __str__(self):
        return self.username
