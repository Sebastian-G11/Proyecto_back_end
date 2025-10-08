from django import forms
from django.core.validators import RegexValidator
from .models import Usuarios
import re

class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'apellido', 'email', 'rol']
        widgets = {
            'nombre': forms.TextInput(attrs={'id': 'nombre', 'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'id': 'apellido', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'class': 'form-control'}),
            'rol': forms.Select(attrs={'id': 'rol', 'class': 'form-select'}),
        }
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo Electrónico',
            'rol': 'Rol del Usuario',
        }



    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()


        if not nombre:
            raise forms.ValidationError("El nombre es obligatorio.")


        if not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s'-]{2,30}$", nombre):
            raise forms.ValidationError(
                "El nombre solo puede contener letras, espacios, apóstrofes o guiones (2–30 caracteres)."
            )

        if len(nombre) < 2 or len(nombre) > 30:
            raise forms.ValidationError("El nombre debe tener entre 2 y 30 caracteres.")

        return nombre.title() 

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido', '').strip()

        if not apellido:
            raise forms.ValidationError("El apellido es obligatorio.")


        if not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s'-]{2,30}$", apellido):
            raise forms.ValidationError(
                "El apellido solo puede contener letras, espacios, apóstrofes o guiones (2–30 caracteres)."
            )

        if len(apellido) < 2 or len(apellido) > 30:
            raise forms.ValidationError("El apellido debe tener entre 2 y 30 caracteres.")

        return apellido.title()

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip()

        if not email:
            raise forms.ValidationError("El correo electrónico es obligatorio.")

        if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email):
            raise forms.ValidationError("Ingrese un correo electrónico válido.")


        email_lower = email.lower()
        if not self.instance.pk:
            if Usuarios.objects.filter(email__iexact=email_lower).exists():
                raise forms.ValidationError(f"El correo '{email}' ya está registrado.")
        else:
            if Usuarios.objects.filter(email__iexact=email_lower).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError(f"Ya existe otro usuario con el correo '{email}'.")

        return email_lower
