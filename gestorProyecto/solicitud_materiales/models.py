from django.db import models

# Create your models here.
class SolicitudMaterial(models.Model):
    materiales_solicitados = models.CharField(max_length=50)
    numero_orden = models.CharField(max_length=15)
    valor_esperado = models.IntegerField()
    valor_final = models.IntegerField(null=True, blank=True)
    codigo_factura = models.CharField(max_length=25)
    fecha_creacion = models.DateField(auto_now_add=True)
