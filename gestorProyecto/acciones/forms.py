from django import forms
from acciones.models import Accion, VerificacionAccion
from dimensiones.models import Dimensiones
from .models import Estados

class AccionForm(forms.ModelForm):
    dimension = forms.ModelChoiceField(
        queryset=Dimensiones.objects.all(),
        empty_label="Seleccione una dimensión",
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Dimensión',
        help_text='Seleccione la dimensión a la que pertenece esta acción'
    )
    
    estado = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        empty_label="Seleccione un estado",
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Estado',
        help_text='Seleccione el estado actual de la acción',
        required=False
    )
    
    class Meta:
        model = Accion
        fields = ['dimension', 'nombre', 'presupuesto_anual', 'presupuesto_reajustado', 'descripcion', 'estado']
        
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
            'estado': 'Estado',
        }
        
        help_texts = {
            'nombre': 'Máximo 100 caracteres',
            'presupuesto_anual': 'Presupuesto inicial planificado',
            'presupuesto_reajustado': 'Presupuesto ajustado según necesidades',
            'descripcion': 'Detalle completo de la acción',
            'estado': 'Estado actual de la acción',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if not self.instance.pk:
            self.fields.pop('estado', None)
        

        if self.instance and self.instance.pk:
            self.fields.pop('dimension', None)
            self.fields.pop('presupuesto_anual', None)
    
    def clean_nombre(self):
        """Validar nombre de la acción"""
        nombre = self.cleaned_data.get('nombre')
        
        if not nombre or len(nombre.strip()) < 5:
            raise forms.ValidationError(
                "El nombre debe tener al menos 5 caracteres."
            )
        
        if nombre.strip().isdigit():
            raise forms.ValidationError("El nombre no puede ser solo números.")
        
        if len(nombre) > 100:
            raise forms.ValidationError("El nombre no puede exceder 100 caracteres.")
        
        return nombre.strip()
    
    def clean_presupuesto_anual(self):
        """Validar presupuesto anual (solo en creación)"""
        presupuesto = self.cleaned_data.get('presupuesto_anual')
        
        if presupuesto is None:
            raise forms.ValidationError("El presupuesto anual es requerido.")
        
        if presupuesto <= 0:
            raise forms.ValidationError("El presupuesto debe ser mayor a 0.")
        
        MINIMO = 100000
        if presupuesto < MINIMO:
            raise forms.ValidationError(f"El presupuesto debe ser al menos ${MINIMO:,.0f}.")
        
        MAXIMO = 1000000000
        if presupuesto > MAXIMO:
            raise forms.ValidationError(f"El presupuesto no puede exceder ${MAXIMO:,.0f}.")
        
        return presupuesto
    
    def clean_descripcion(self):
        """Validar descripción"""
        descripcion = self.cleaned_data.get('descripcion')
        
        if not descripcion or len(descripcion.strip()) == 0:
            raise forms.ValidationError("La descripción es requerida.")
        
        if len(descripcion.strip()) < 10:
            raise forms.ValidationError("La descripción debe tener al menos 10 caracteres.")
        
        if len(descripcion) > 1000:
            raise forms.ValidationError("La descripción no puede exceder 1000 caracteres.")
        
        return descripcion.strip()

    
class VerificacionForm(forms.ModelForm):
    class Meta:
        model = VerificacionAccion
        fields = ['nombre', 'url']
        
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Acta de reunión',
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
            'url': 'URL completa del documento',
        }
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        
        if not nombre or len(nombre.strip()) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        
        if nombre.strip().isdigit():
            raise forms.ValidationError("El nombre no puede ser solo números.")
        
        if len(nombre) > 40:
            raise forms.ValidationError(f"El nombre no puede exceder 40 caracteres.")
        
        return nombre.strip()
    
    def clean_url(self):
        url = self.cleaned_data.get('url')
        
        if not url:
            raise forms.ValidationError("La URL es requerida.")
        
        if not url.startswith(('http://', 'https://')):
            raise forms.ValidationError("La URL debe comenzar con 'http://' o 'https://'")
        
        if len(url) > 200:
            raise forms.ValidationError("La URL no puede exceder 200 caracteres.")
        
        if ' ' in url:
            raise forms.ValidationError("La URL no puede contener espacios.")
        
        return url