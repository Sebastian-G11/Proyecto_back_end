from django import forms

def validate_materiales(materiales):
    if not materiales or len(materiales) < 3:
        raise forms.ValidationError("El campo de materiales debe tener al menos 3 caracteres.")
