from django.db import models
from actividades.models import Actividad

class SubActividad(models.Model):
    sub_actividad_id = models.AutoField(primary_key=True)
    actividad = models.ForeignKey(Actividad, related_name='sub_actividades', on_delete=models.PROTECT, default=None)
    nombre = models.CharField(max_length=80)
    fecha_creacion = models.DateTimeField(auto_now_add=True)  
    fecha_actualizacion = models.DateTimeField(auto_now=True) 
    grado_aprobacion = models.DecimalField(max_digits=5, decimal_places=2)
