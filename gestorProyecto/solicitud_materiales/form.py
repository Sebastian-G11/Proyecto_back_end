from django import forms
from solicitud_materiales.models import SolicitudMaterial
from actividades.models import Actividad  # ✅ Importa el modelo Actividad

class FormSolicitudMaterial(forms.ModelForm):
    actividad = forms.ModelChoiceField(
        queryset=Actividad.objects.select_related('accion').all(),
        empty_label="Seleccione una actividad",
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Actividad Asociada',
        help_text='Seleccione la actividad a la que pertenece esta solicitud'
    )
    
    class Meta:
        model = SolicitudMaterial
        fields = ["actividad", "materiales_solicitados", "numero_orden", "valor_esperado", "codigo_factura", "valor_final"]  

        widgets = {
            'materiales_solicitados': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Cemento, arena, ladrillos...',
                'maxlength': '50'
            }),
            'numero_orden': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: ORD-2024-001',
                'maxlength': '15'
            }),
            'valor_esperado': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
                'min': '0',
                'step': '0.01'
            }),
            'codigo_factura': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: FACT-2024-001',
                'maxlength': '25'
            }),
            'valor_final': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
                'min': '0',
                'step': '0.01'
            }),
        }

        labels = {
            'materiales_solicitados': 'Materiales Solicitados',
            'numero_orden': 'Número de Orden',
            'valor_esperado': 'Valor Esperado',
            'codigo_factura': 'Código de Factura',
            'valor_final': 'Valor Final',
        }

        help_texts = {
            'materiales_solicitados': 'Máximo 50 caracteres',
            'numero_orden': 'Código único de la orden (3-15 caracteres)',
            'valor_esperado': 'Valor estimado de la solicitud',
            'codigo_factura': 'Código único de la factura (3-25 caracteres)',
            'valor_final': 'Valor real de la solicitud',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.instance and self.instance.pk:
            self.fields.pop('actividad', None)
        

    def clean_materiales_solicitados(self):
        materiales = self.cleaned_data.get('materiales_solicitados')
        if not materiales or len(materiales) < 3:
            raise forms.ValidationError("El campo de materiales debe tener al menos 3 caracteres.")
        
        if materiales.isdigit():
            raise forms.ValidationError(
                "Los materiales no pueden ser solo números."
            )
        
        if len(materiales) > 50:
            raise forms.ValidationError(
                "Los materiales no pueden exceder 50 caracteres."
            )
        
        return materiales.strip()
    
    def clean_numero_orden(self):
        """Validar número de orden"""
        numero_orden = self.cleaned_data.get('numero_orden')
        
        # Validar que no esté vacío
        if not numero_orden:
            raise forms.ValidationError("El número de orden es requerido.")
        
        
        # Validar longitud
        if len(numero_orden) < 3:
            raise forms.ValidationError(
                "El número de orden debe tener al menos 3 caracteres."
            )
        
        if len(numero_orden) > 15:
            raise forms.ValidationError(
                "El número de orden no puede exceder 15 caracteres."
            )
        
        if not self.instance.pk:  
            if SolicitudMaterial.objects.filter(numero_orden=numero_orden).exists():
                raise forms.ValidationError(
                    f"Ya existe una solicitud con el número de orden '{numero_orden}'."
                )
        else:  # Al editar, excluir la instancia actual
            if SolicitudMaterial.objects.filter(numero_orden=numero_orden).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError(
                    f"Ya existe otra solicitud con el número de orden '{numero_orden}'."
                )
        
        return numero_orden.upper()
    
    def clean_valor_esperado(self):
        """Validar valor esperado"""
        valor = self.cleaned_data.get('valor_esperado')
        
        # Validar que no sea None
        if valor is None:
            raise forms.ValidationError("El valor esperado es requerido.")
        
        # Validar que sea mayor a 0
        if valor <= 0:
            raise forms.ValidationError(
                "El valor esperado debe ser mayor a 0."
            )
        
        # Validar valor mínimo
        VALOR_MINIMO = 1000
        if valor < VALOR_MINIMO:
            raise forms.ValidationError(
                f"El valor esperado debe ser al menos ${VALOR_MINIMO:,.0f}."
            )
        
        # Validar valor máximo
        VALOR_MAXIMO = 10000000
        if valor > VALOR_MAXIMO:
            raise forms.ValidationError(
                f"El valor esperado no puede exceder ${VALOR_MAXIMO:,.0f}."
            )
        
        return valor    
    
    def clean_codigo_factura(self):
        """Validar código de factura"""
        codigo = self.cleaned_data.get('codigo_factura')
        
        # Validar que no esté vacío
        if not codigo:
            raise forms.ValidationError("El código de factura es requerido.")
        
        # Validar longitud mínima
        if len(codigo) < 3:
            raise forms.ValidationError(
                "El código de factura debe tener al menos 3 caracteres."
            )
        
        # Validar longitud máxima
        if len(codigo) > 25:
            raise forms.ValidationError(
                "El código de factura no puede exceder 25 caracteres."
            )
        
        # Validar formato alfanumérico
        if not codigo.replace('-', '').replace('_', '').isalnum():
            raise forms.ValidationError(
                "El código de factura solo puede contener letras, números, guiones y guiones bajos."
            )
        
        # Validar que no exista duplicado (solo al crear)
        if not self.instance.pk:
            if SolicitudMaterial.objects.filter(codigo_factura=codigo.upper()).exists():
                raise forms.ValidationError(
                    f"Ya existe una solicitud con el código de factura '{codigo}'."
                )
        else:
            if SolicitudMaterial.objects.filter(codigo_factura=codigo.upper()).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError(
                    f"Ya existe otra solicitud con el código de factura '{codigo}'."
                )
        
        return codigo.upper()
    
    def clean_valor_final(self):
        """Validar valor final"""
        valor = self.cleaned_data.get('valor_final')
        
        # El valor final puede ser None o 0 inicialmente
        if valor is None:
            return valor
        
        # Si tiene valor, validar que sea positivo
        if valor < 0:
            raise forms.ValidationError("El valor final no puede ser negativo.")
        
        # Validar valor máximo
        VALOR_MAXIMO = 10000000
        if valor > VALOR_MAXIMO:
            raise forms.ValidationError(
                f"El valor final no puede exceder ${VALOR_MAXIMO:,.0f}."
            )
        
        return valor