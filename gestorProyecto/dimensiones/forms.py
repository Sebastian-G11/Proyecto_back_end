from django import forms
from .models import Dimensiones
import re

class FormDimensiones(forms.ModelForm):
    class Meta:
        model = Dimensiones
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la dimensión'}),
        }
        labels = {
            'nombre': 'Nombre de la Dimensión',
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()


        if not nombre:
            raise forms.ValidationError("El nombre de la dimensión es obligatorio.")


        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        if len(nombre) > 50:
            raise forms.ValidationError("El nombre no puede exceder los 50 caracteres.")


        if not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9\s'-]+$", nombre):
            raise forms.ValidationError(
                "El nombre solo puede contener letras, números, espacios, guiones y tildes."
            )


        if nombre.isdigit():
            raise forms.ValidationError("El nombre no puede ser solo números.")
        if not self.instance.pk:
            if Dimensiones.objects.filter(nombre__iexact=nombre).exists():
                raise forms.ValidationError(f"Ya existe una dimensión con el nombre '{nombre}'.")
        else:
            if Dimensiones.objects.filter(nombre__iexact=nombre).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError(f"Ya existe otra dimensión con el nombre '{nombre}'.")

        return nombre.title()
