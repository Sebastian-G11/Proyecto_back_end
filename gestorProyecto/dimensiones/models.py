from django.db import models

# Create your models here.
class Dimensiones(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Dimensión"
        verbose_name_plural = "Dimensiones"
    
    def __str__(self):
        return self.nombre