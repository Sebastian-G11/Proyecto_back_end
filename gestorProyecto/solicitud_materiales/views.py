from django.shortcuts import redirect, render
from autenticacion.views import login_required_simulado, admin_required
from solicitud_materiales.models import SolicitudMaterial
from solicitud_materiales.form import FormSolicitudMaterial
from solicitud_materiales.service import solicitud_service
from django import forms
from django.contrib import messages
from django.shortcuts import get_object_or_404

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
def display_solicitud_materiales(request):
    user = request.session.get("user")
    solicitudes = solicitud_service.get_solicitudes()
    return render(request, "solicitud_materiales/lista_materiales.html", {"user": user, "actividades": actividades, "solicitudes": solicitudes, "usuarios": usuarios})


@admin_required
@login_required_simulado
def crear_solicitud(request):
    user = request.session.get("user")
    
    if request.method == "POST":
        form = FormSolicitudMaterial(request.POST)
        if form.is_valid():
            try:
                solicitud = solicitud_service.create_solicitud(form.cleaned_data)
                messages.success(request, f'Solicitud "{solicitud.materiales_solicitados}" creada exitosamente')
                return redirect('/solicitud_materiales')
            except ValueError as e:
                messages.error(request, str(e))
                form.add_error(None, str(e))
            except Exception as e:
                messages.error(request, "Ocurrió un error al crear la solicitud")
                form.add_error(None, f"Error inesperado: {str(e)}")
    else:
        form = FormSolicitudMaterial()
    
    return render(request, "solicitud_materiales/crear_solicitud.html", {
        "usuario": user, 
        "form": form
    })


@admin_required
@login_required_simulado
def editar_solicitud(request, id):
    user = request.session.get("user")
    solicitud = get_object_or_404(SolicitudMaterial, solicitud_id=id)

    if request.method == "POST":
        form = FormSolicitudMaterial(request.POST, instance=solicitud)
        if form.is_valid():
            try:
                solicitud = solicitud_service.update_solicitud(id, form.cleaned_data)
                messages.success(request, f'Solicitud actualizada exitosamente')
                return redirect('/solicitud_materiales')
            except Exception as e:
                messages.error(request, f"Error al actualizar la solicitud: {str(e)}")
                form.add_error(None, str(e))
    else:
        form = FormSolicitudMaterial(instance=solicitud)
    
    return render(request, "solicitud_materiales/editar_solicitud.html", {
        "usuario": user, 
        "form": form, 
        "solicitud": solicitud
    })


@admin_required
@login_required_simulado
def eliminar_solicitud(request, id):
    if request.method == "POST":
        try:
            solicitud = get_object_or_404(SolicitudMaterial, solicitud_id=id)
            materiales = solicitud.materiales_solicitados
            solicitud_service.delete_solicitud(id)
            messages.success(request, f'Solicitud "{materiales}" eliminada exitosamente')
        except Exception as e:
            messages.error(request, f"Error al eliminar la solicitud: {str(e)}")
    
    return redirect('/solicitud_materiales')
