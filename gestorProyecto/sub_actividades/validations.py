from django.core.exceptions import ValidationError
from .models import SubActividad

def validar_grado_aprobacion(grado_aprobacion):
    """Valida que el grado de aprobación esté entre 0 y 100."""
    if grado_aprobacion < 0 or grado_aprobacion > 100:
        raise ValidationError("El grado de aprobación debe estar entre 0 y 100.")
    return grado_aprobacion

def validar_nombre_unico(nombre, actividad):
    """Valida que el nombre de la sub-actividad sea único dentro de la actividad."""
    if SubActividad.objects.filter(nombre=nombre, actividad=actividad).exists():
        raise ValidationError(f"Ya existe una sub-actividad con el nombre '{nombre}' para esta actividad.")
    return nombre
