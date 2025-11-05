from django import forms
from .models import SubActividad
import re

class SubActividadForm(forms.ModelForm):
    class Meta:
        model = SubActividad
        fields = ['actividad', 'nombre', 'grado_aprobacion']
        widgets = {
            'actividad_id': forms.Select(attrs={'class': 'form-select'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la subactividad'}),
            'grado_aprobacion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0 - 100'}),
        }
        labels = {
            'actividad_id': 'Actividad Asociada',
            'nombre': 'Nombre de la Subactividad',
            'grado_aprobacion': 'Grado de Aprobación (%)',
        }


    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()

        if not nombre:
            raise forms.ValidationError("El nombre de la subactividad es obligatorio.")

        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        if len(nombre) > 80:
            raise forms.ValidationError("El nombre no puede exceder los 80 caracteres.")

        if not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9\s'-]+$", nombre):
            raise forms.ValidationError(
                "El nombre solo puede contener letras, números, espacios, guiones y tildes."
            )

        if nombre.isdigit():
            raise forms.ValidationError("El nombre no puede ser solo números.")

        if not self.instance.pk:
            if SubActividad.objects.filter(nombre__iexact=nombre).exists():
                raise forms.ValidationError(f"Ya existe una subactividad con el nombre '{nombre}'.")
        else:
            if SubActividad.objects.filter(nombre__iexact=nombre).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError(f"Ya existe otra subactividad con el nombre '{nombre}'.")

        return nombre.title()

    def clean_grado_aprobacion(self):
        grado_aprobacion = self.cleaned_data.get('grado_aprobacion')

        if grado_aprobacion is None:
            raise forms.ValidationError("El grado de aprobación es obligatorio.")

        if grado_aprobacion < 0 or grado_aprobacion > 100:
            raise forms.ValidationError("El grado de aprobación debe estar entre 0 y 100.")

        return grado_aprobacion
