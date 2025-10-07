from django import forms
from solicitud_materiales.models import SolicitudMaterial

class FormSolicitudMaterial(forms.ModelForm):
    class Meta:
        model = SolicitudMaterial
        fields = ["materiales_solicitados", "numero_orden", "valor_esperado", "codigo_factura", "valor_final"]

        widgets = {
            'materiales_solicitados': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_orden': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_esperado': forms.NumberInput(attrs={'class': 'form-control'}),
            'codigo_factura': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_final': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'materiales_solicitados': 'Materiales',
            'numero_orden': 'Número de Orden',
            'valor_esperado': 'Valor Esperado',
            'codigo_factura': 'Código de Factura',
        }

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
    

        
    

    

