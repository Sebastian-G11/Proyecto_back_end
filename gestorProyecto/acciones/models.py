from django.db import models

# Create your models here.
class Accion(models.Model):
    accion_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    presupuesto_anual = models.IntegerField()
    presupuesto_reajustado = models.IntegerField(null=True, blank=True)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
