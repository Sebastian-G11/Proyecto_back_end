from django import forms
from actividades.models import Actividad, VerificacionActividad
from acciones.models import Accion
from acciones.models import Estados


class ActividadForm(forms.ModelForm):
    accion = forms.ModelChoiceField(
        queryset=Accion.objects.select_related('dimension', 'responsable').all(),
        empty_label="Seleccione una acción",
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Acción',
        help_text='Seleccione la acción a la que pertenece esta actividad'
    )
    
    estado = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        empty_label="Seleccione un estado",
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Estado',
        help_text='Seleccione el estado actual de la actividad',
        required=False
    )
    
    class Meta:
        model = Actividad
        fields = ['accion', 'nombre', 'estado']
        
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Capacitación de personal',
                'maxlength': '40'
            }),
        }
        
        labels = {
            'nombre': 'Nombre de la Actividad',
            'estado': 'Estado',
        }
        
        help_texts = {
            'nombre': 'Máximo 40 caracteres',
            'estado': 'Estado actual de la actividad',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance.pk:
            self.fields.pop('estado', None)
        
        if self.instance and self.instance.pk:
            self.fields.pop('accion', None)
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        
        if not nombre or not nombre.strip():
            raise forms.ValidationError("El nombre es requerido.")
        
        nombre = nombre.strip()
        
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        
        if nombre.isdigit():
            raise forms.ValidationError("El nombre no puede ser solo números.")
        
        if len(nombre) > 40:
            raise forms.ValidationError(f"El nombre excede el máximo de 40 caracteres.")
        
        return nombre


class VerificacionForm(forms.ModelForm):
    class Meta:
        model = VerificacionActividad
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
        
        if not nombre or not nombre.strip():
            raise forms.ValidationError("El nombre es requerido.")
        
        nombre = nombre.strip()
        
        if len(nombre) < 3:
            raise forms.ValidationError("Debe tener al menos 3 caracteres.")
        
        if nombre.isdigit():
            raise forms.ValidationError("No puede ser solo números.")
        
        if len(nombre) > 40:
            raise forms.ValidationError("Excede el máximo de 40 caracteres.")
        
        return nombre
    
    def clean_url(self):
        url = self.cleaned_data.get('url')
        
        if not url:
            raise forms.ValidationError("La URL es requerida.")
        
        if not url.startswith(('http://', 'https://')):
            raise forms.ValidationError("Debe comenzar con http:// o https://")
        
        if len(url) > 200:
            raise forms.ValidationError("URL demasiado larga.")
        
        if ' ' in url:
            raise forms.ValidationError("No puede contener espacios.")
        
        return url