from django.db import models
from acciones.models import Accion, Estados
from usuarios.models import Usuarios

# Create your models here.
class Actividad(models.Model):
    actividad_id = models.AutoField(primary_key=True)
    accion = models.ForeignKey(Accion, related_name='actividades', on_delete=models.CASCADE, default=None)
    nombre = models.CharField(max_length=40)
    responsable = models.ForeignKey(Usuarios, related_name='actividades_responsable', on_delete=models.CASCADE, default=None)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)
    estado = models.ForeignKey(Estados, related_name='actividades', on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'

    def __str__(self):
        return f"{self.nombre}"


class VerificacionActividad(models.Model):
    verificacion_id = models.AutoField(primary_key=True)
    actividad = models.ForeignKey(Actividad, related_name='verificaciones', on_delete=models.CASCADE, default=None)
    nombre = models.CharField(max_length=40)
    url = models.URLField()