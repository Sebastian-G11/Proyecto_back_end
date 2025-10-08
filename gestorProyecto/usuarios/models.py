from django.db import models

# Create your models here.
class Usuarios(models.Model):
    ROLES = [
        ('Administrador', 'Administrador'),
        ('Usuario', 'Usuario'),
        ('Invitado', 'Invitado'),
    ]

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    rol = models.CharField(max_length=20, choices=ROLES, default='Usuario')

