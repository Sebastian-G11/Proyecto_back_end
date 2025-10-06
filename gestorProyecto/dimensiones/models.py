from django.db import models

# Create your models here.
class Dimensiones(models.Model):
    nombre = models.CharField(max_length=50)