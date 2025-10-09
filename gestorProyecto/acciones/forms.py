from django import forms
from acciones.models import Accion


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