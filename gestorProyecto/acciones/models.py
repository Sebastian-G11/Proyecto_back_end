from django.db import models
from dimensiones.models import Dimensiones
from usuarios.models import Usuarios

class Estados(models.Model):
    estado_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.nombre

# Create your models here.
class Accion(models.Model):
    accion_id = models.AutoField(primary_key=True)
    dimension = models.ForeignKey(Dimensiones, related_name='acciones', on_delete=models.PROTECT, default=None)
    nombre = models.CharField(max_length=100)
    responsable = models.ForeignKey(Usuarios, related_name='acciones_responsable', on_delete=models.PROTECT, default=None)
    presupuesto_anual = models.IntegerField()
    presupuesto_reajustado = models.IntegerField(null=True, blank=True)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    estado = models.ForeignKey(Estados, related_name='acciones', on_delete=models.PROTECT, default=1)
    def __str__(self):
        return self.nombre

    
class VerificacionAccion(models.Model):
    verificacion_id = models.AutoField(primary_key=True)
    accion = models.ForeignKey(Accion, related_name='verificaciones', on_delete=models.CASCADE, default=None)
    nombre = models.CharField(max_length=40)
    url = models.URLField()

 
