from django import forms
from actividades.models import Actividad, VerificacionActividad


class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['nombre']
        
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Capacitación de personal',
                'maxlength': '40'
            }),
        }
        
        labels = {
            'nombre': 'Nombre de la Actividad',
        }
        
        help_texts = {
            'nombre': 'Máximo 40 caracteres',
        }
    
    def clean_nombre(self):
        """Validar nombre de la actividad"""
        nombre = self.cleaned_data.get('nombre')
        
        # Validar que no esté vacío
        if not nombre or len(nombre.strip()) == 0:
            raise forms.ValidationError("El nombre es requerido.")
        
        # Validar longitud mínima
        if len(nombre.strip()) < 3:
            raise forms.ValidationError(
                "El nombre debe tener al menos 3 caracteres."
            )
        
        # Validar que no sea solo números
        if nombre.strip().isdigit():
            raise forms.ValidationError(
                "El nombre no puede ser solo números."
            )
        
        # Validar longitud máxima
        if len(nombre) > 40:
            raise forms.ValidationError(
                f"El nombre no puede exceder 40 caracteres. Actualmente tiene {len(nombre)}."
            )
        
        # Validar que no contenga caracteres especiales peligrosos
        caracteres_prohibidos = ['<', '>', '{', '}', '|', '\\', '^', '`', ';']
        for char in caracteres_prohibidos:
            if char in nombre:
                raise forms.ValidationError(
                    f"El nombre contiene caracteres no permitidos: {char}"
                )
        
        
        
        return nombre.strip()
    

class VerificacionForm(forms.ModelForm):
    class Meta:
        model = VerificacionActividad
        fields = ['nombre', 'url']
        
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Acta de reunión, Informe mensual',
                'maxlength': '40'
            }),
            'url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://ejemplo.com/documento'
            }),
        }
        
        labels = {
            'nombre': 'Nombre del Medio de Verificación',
            'url': 'URL del Documento',
        }
        
        help_texts = {
            'nombre': 'Máximo 40 caracteres',
            'url': 'URL completa del documento o recurso',
        }
    
    def clean_nombre(self):
        """Validar nombre del medio de verificación"""
        nombre = self.cleaned_data.get('nombre')
        
        # Validar que no esté vacío
        if not nombre or len(nombre.strip()) == 0:
            raise forms.ValidationError("El nombre es requerido.")
        
        # Validar longitud mínima
        if len(nombre.strip()) < 3:
            raise forms.ValidationError(
                "El nombre debe tener al menos 3 caracteres."
            )
        
        # Validar que no sea solo números
        if nombre.strip().isdigit():
            raise forms.ValidationError(
                "El nombre no puede ser solo números."
            )
        
        # Validar longitud máxima
        if len(nombre) > 40:
            raise forms.ValidationError(
                f"El nombre no puede exceder 40 caracteres. Actualmente tiene {len(nombre)}."
            )
        
        # Validar que no contenga caracteres especiales peligrosos
        caracteres_prohibidos = ['<', '>', '{', '}', '|', '\\', '^', '`']
        for char in caracteres_prohibidos:
            if char in nombre:
                raise forms.ValidationError(
                    f"El nombre contiene caracteres no permitidos: {char}"
                )
        
        return nombre.strip()
    
    def clean_url(self):
        """Validar URL del medio de verificación"""
        url = self.cleaned_data.get('url')
        
        # Validar que no esté vacío
        if not url:
            raise forms.ValidationError("La URL es requerida.")
        
        # Validar longitud mínima
        if len(url) < 10:
            raise forms.ValidationError(
                "La URL debe tener al menos 10 caracteres."
            )
        
        # Validar que comience con http:// o https://
        if not url.startswith(('http://', 'https://')):
            raise forms.ValidationError(
                "La URL debe comenzar con 'http://' o 'https://'"
            )
        
        # Validar longitud máxima (200 caracteres es estándar para URLField)
        if len(url) > 200:
            raise forms.ValidationError(
                "La URL no puede exceder 200 caracteres."
            )
        
        # Validar que no contenga espacios
        if ' ' in url:
            raise forms.ValidationError(
                "La URL no puede contener espacios."
            )
        
        # Validar formato básico de URL
        import re
        url_pattern = re.compile(
            r'^https?://'  # http:// o https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # dominio
            r'localhost|'  # localhost
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # o IP
            r'(?::\d+)?'  # puerto opcional
            r'(?:/?|[/?]\S+)$', re.IGNORECASE
        )
        
        if not url_pattern.match(url):
            raise forms.ValidationError(
                "La URL no tiene un formato válido."
            )
        
        # Validar dominios peligrosos o sospechosos (opcional)
        dominios_bloqueados = ['malware.com', 'phishing.com', 'spam.com']
        for dominio in dominios_bloqueados:
            if dominio in url.lower():
                raise forms.ValidationError(
                    f"El dominio '{dominio}' está bloqueado por seguridad."
                )
        
        return url
    
