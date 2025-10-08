from django import forms
from .models import Dimensiones

class FormDimensiones(forms.ModelForm):
    class Meta:
        model = Dimensiones
        fields = ['nombre']  # Solo el nombre
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
