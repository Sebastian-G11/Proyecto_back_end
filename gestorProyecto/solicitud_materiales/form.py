from django import forms
from solicitud_materiales.models import SolicitudMaterial

class FormSolicitudMaterial(forms.ModelForm):
    class Meta:
        model = SolicitudMaterial
        fields = ["materiales_solicitados", "numero_orden", "valor_esperado", "codigo_factura"]

        widgets = {
            'materiales_solicitados': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_orden': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_esperado': forms.NumberInput(attrs={'class': 'form-control'}),
            'codigo_factura': forms.TextInput(attrs={'class': 'form-control'}),
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
        return materiales
