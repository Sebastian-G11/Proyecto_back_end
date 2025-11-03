from django.db import models
from acciones.models import Accion, Estados
from usuarios.models import Usuarios

# Create your models here.
class Actividad(models.Model):
    actividad_id = models.AutoField(primary_key=True)
    accion_id = models.ForeignKey(Accion, related_name='actividades', on_delete=models.PROTECT, default=None)
    nombre = models.CharField(max_length=40)
    responsable = models.ForeignKey(Usuarios, related_name='actividades_responsable', on_delete=models.PROTECT, default=None)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)
    estado = models.ForeignKey(Estados, related_name='actividades', on_delete=models.PROTECT, default=1)


class VerificacionActividad(models.Model):
    verificacion_id = models.AutoField(primary_key=True)
    actividad_id = models.ForeignKey(Actividad, related_name='verificaciones', on_delete=models.PROTECT, default=None)
    nombre = models.CharField(max_length=40)
    url = models.URLField()