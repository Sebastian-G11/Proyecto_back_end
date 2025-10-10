from django import forms
from acciones.models import Accion, VerificacionAccion


class AccionForm(forms.ModelForm):
    class Meta:
        model = Accion
        fields = ['nombre', 'presupuesto_anual', 'presupuesto_reajustado', 'descripcion']
        
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Implementación de proyecto X',
                'maxlength': '100'
            }),
            'presupuesto_anual': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
                'min': '0'
            }),
            'presupuesto_reajustado': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
                'min': '0'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describa detalladamente la acción a realizar...',
                'rows': 5
            }),
        }
        
        labels = {
            'nombre': 'Nombre de la Acción',
            'presupuesto_anual': 'Presupuesto Anual',
            'presupuesto_reajustado': 'Presupuesto Reajustado',
            'descripcion': 'Descripción',
        }
        
        help_texts = {
            'nombre': 'Máximo 100 caracteres',
            'presupuesto_anual': 'Presupuesto inicial planificado',
            'presupuesto_reajustado': 'Presupuesto ajustado según necesidades',
            'descripcion': 'Detalle completo de la acción',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Si está editando, hacer presupuesto_anual solo lectura
        if self.instance.pk:
            self.fields['presupuesto_anual'].disabled = True
            self.fields['presupuesto_anual'].widget.attrs.update({
                'readonly': True,
                'class': 'form-control bg-light',
                'style': 'cursor: not-allowed;'
            })
            self.fields['presupuesto_anual'].help_text = 'Este campo no puede modificarse después de la creación'
    
    def clean_nombre(self):
        """Validar nombre de la acción"""
        nombre = self.cleaned_data.get('nombre')
        
        # Validar longitud mínima
        if not nombre or len(nombre.strip()) < 5:
            raise forms.ValidationError(
                "El nombre de la acción debe tener al menos 5 caracteres."
            )
        
        # Validar que no sea solo números
        if nombre.strip().isdigit():
            raise forms.ValidationError(
                "El nombre no puede ser solo números."
            )
        
        # Validar longitud máxima
        if len(nombre) > 100:
            raise forms.ValidationError(
                "El nombre no puede exceder 100 caracteres."
            )
        
        return nombre.strip()
    
    def clean_presupuesto_anual(self):
        """Validar presupuesto anual"""
        presupuesto = self.cleaned_data.get('presupuesto_anual')
        
        # Si está editando, retornar el valor original
        if self.instance.pk:
            return self.instance.presupuesto_anual
        
        # Validaciones solo para creación
        if presupuesto is None:
            raise forms.ValidationError("El presupuesto anual es requerido.")
        
        # Validar que sea mayor a 0
        if presupuesto <= 0:
            raise forms.ValidationError(
                "El presupuesto anual debe ser mayor a 0."
            )
        
        # Validar presupuesto mínimo
        PRESUPUESTO_MINIMO = 100000
        if presupuesto < PRESUPUESTO_MINIMO:
            raise forms.ValidationError(
                f"El presupuesto anual debe ser al menos ${PRESUPUESTO_MINIMO:,.0f}."
            )
        
        # Validar presupuesto máximo
        PRESUPUESTO_MAXIMO = 1000000000
        if presupuesto > PRESUPUESTO_MAXIMO:
            raise forms.ValidationError(
                f"El presupuesto anual no puede exceder ${PRESUPUESTO_MAXIMO:,.0f}."
            )
        
        return presupuesto

    
    def clean_descripcion(self):
        """Validar descripción"""
        descripcion = self.cleaned_data.get('descripcion')
        
        # Validar que no esté vacía
        if not descripcion or len(descripcion.strip()) == 0:
            raise forms.ValidationError("La descripción es requerida.")
        
        # Validar longitud mínima
        if len(descripcion.strip()) < 10:
            raise forms.ValidationError(
                "La descripción debe tener al menos 10 caracteres."
            )
        
        # Validar longitud máxima
        if len(descripcion) > 1000:
            raise forms.ValidationError(
                "La descripción no puede exceder 1000 caracteres."
            )
        
        return descripcion.strip()
    
class VerificacionForm(forms.ModelForm):
    class Meta:
        model = VerificacionAccion
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
    
