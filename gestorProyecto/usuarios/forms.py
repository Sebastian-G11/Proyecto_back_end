from django import forms
from .models import Usuarios

class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'apellido', 'email', 'rol']  # Especificar los campos que realmente necesitas
        widgets = {
            'nombre': forms.TextInput(attrs={'id': 'nombre', 'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'id': 'apellido', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'class': 'form-control'}),
            'rol': forms.Select(attrs={'id': 'rol', 'class': 'form-select'}),
        }
