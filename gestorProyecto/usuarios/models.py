from django.db import models

class Roles(models.Model):
    rol_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

# Create your models here.
class Usuarios(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    rol = models.ForeignKey(Roles, related_name='usuarios', on_delete=models.PROTECT, default=2)
    def __str__(self):
         return f"{self.nombre}"
