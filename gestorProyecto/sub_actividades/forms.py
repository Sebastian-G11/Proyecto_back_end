# sub_actividades/forms.py

from django import forms
from .models import SubActividad

class SubActividadForm(forms.ModelForm):
    class Meta:
        model = SubActividad
        fields = ['actividad', 'nombre', 'grado_aprobacion']  # 

    # Opcionalmente, puedes agregar validaciones personalizadas aquí.
    def clean_grado_aprobacion(self):
        grado_aprobacion = self.cleaned_data.get('grado_aprobacion')
        if grado_aprobacion < 0 or grado_aprobacion > 100:
            raise forms.ValidationError("El grado de aprobación debe estar entre 0 y 100.")
        return grado_aprobacion
