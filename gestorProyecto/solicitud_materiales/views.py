from django.shortcuts import redirect, render
from autenticacion.views import login_required_simulado
from solicitud_materiales.models import SolicitudMaterial
from solicitud_materiales.form import FormSolicitudMaterial
from solicitud_materiales.service import solicitud_service
from django import forms

## Mocks de actividades, solicitudes y usuarios para añadido dinámico, posteriormente vendrán de la misma BDD
actividades = [
    {"actividad_id": 1, "nombre": "Capacitación Inicial"},
    {"actividad_id": 2, "nombre": "Implementación CRM"},
    {"actividad_id": 3, "nombre": "Revisión de Inventario"}
]


usuarios = [
    {"id": 101, "nombre": "Juan Pérez"},
    {"id": 102, "nombre": "María González"},
    {"id": 103, "nombre": "Carlos Ramírez"}
]


@login_required_simulado
# Create your views here.
def display_solicitud_materiales(request):
    user = request.session.get("user")
    solicitudes = solicitud_service.get_solicitudes()
    return render(request, "solicitud_materiales/lista_materiales.html", {"usuario": user, "actividades": actividades, "solicitudes": solicitudes, "usuarios": usuarios})

def crear_solicitud(request):
    user = request.session.get("user")
    if request.method == "POST":
        # Procesar el formulario enviado
        form = FormSolicitudMaterial(request.POST)
        if form.is_valid():
          try:
                solicitud_service.create_solicitud(form.cleaned_data)
                return redirect('/solicitud_materiales')  # Redirigir a la lista de solicitudes
          except forms.ValidationError as e:
                form.add_error(None, str(e))  # Añadir error no relacionado con un campo específico
    else:
        form = FormSolicitudMaterial()
    
    return render(request, "solicitud_materiales/crear_solicitud.html", {"usuario": user, "form": form})

def editar_solicitud(request, id):
    user = request.session.get("user")
    solicitud = SolicitudMaterial.objects.get(id=id)

    if request.method == "POST":
        form = FormSolicitudMaterial(request.POST, instance=solicitud)
        if form.is_valid():
            form.save()
            return redirect('display_solicitud_materiales')
    else:
        form = FormSolicitudMaterial(instance=solicitud)
    
    return render(request, "solicitud_materiales/editar_solicitud.html", {"usuario": user, "form": form, "solicitud": solicitud})