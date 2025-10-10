from django.db import models

# Create your models here.
class Actividad(models.Model):
    actividad_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)


class VerificacionActividad(models.Model):
    verificacion_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    url = models.URLField()