from django.shortcuts import redirect, render
from autenticacion.views import login_required_simulado
from .service import acciones_service, verificacion_service
from .forms import AccionForm, VerificacionForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Accion, VerificacionAccion

## Mock de acciones y dimensiones para hacer el añadido dinámico en la template, posteriormente vendrán directamente desde la base de datos
dimensiones = [
    {
        "dimension_id": 1,
        "nombre": "Gestión de Capacitaciones"
    },
    {
        "dimension_id": 2,
        "nombre": "Interacción con el Cliente"
    }
    ]

verificaciones = [
    {
        "nombre": "Plan de capacitación",
        "url": "https://example.com/plan"
    }
]

@login_required_simulado
def display_acciones(request):
    user = request.session.get("user")
    acciones = acciones_service.get_all_acciones()
    verificaciones = verificacion_service.get_all_verificaciones()
    return render(request, "acciones/lista_acciones.html", {"user": user, "acciones": acciones, "dimensiones": dimensiones, "verificaciones": verificaciones})

@login_required_simulado
def display_create_accion(request):
    user = request.session.get("user")

    if request.method == "POST":
        form = AccionForm(request.POST)
        if form.is_valid():
            accion = acciones_service.create_accion(form.cleaned_data)
            messages.success(request, f'Acción "{accion.nombre}" creada exitosamente')  
            return redirect("/acciones")
    else:
        form = AccionForm()

    return render(request, "acciones/crear_accion.html", {"user": user, "dimensiones": dimensiones, "form": form})

@login_required_simulado
def display_edit_accion(request, id):
    user = request.session.get("user")
    accion = get_object_or_404(Accion, accion_id=id)

    if request.method == "POST":
        form = AccionForm(request.POST, instance=accion)
        if form.is_valid():
            accion = acciones_service.update_accion(id, form.cleaned_data)
            messages.success(request, f'Acción actualizada exitosamente')  
            return redirect("/acciones")
    else:
        form = AccionForm(instance=accion)

    return render(request, "acciones/editar_accion.html", {"user": user, "dimensiones": dimensiones, "form": form}) 

@login_required_simulado
def delete_accion(request, id):
    if request.method == "POST":
        try:
            accion = get_object_or_404(Accion, accion_id=id)
            nombre = accion.nombre
            acciones_service.delete_accion(id)
            messages.success(request, f'Acción "{nombre}" eliminada exitosamente')
        except Exception as e:
            messages.error(request, f'Error al eliminar la acción: {str(e)}')
    return redirect("/acciones")

@login_required_simulado
def display_create_verificacion(request):
    user = request.session.get("user")

    if request.method == "POST":
        form = VerificacionForm(request.POST)
        if form.is_valid():
            try:
                verificacion = verificacion_service.create_verificacion(form.cleaned_data)
                messages.success(request, f'Verificación "{verificacion.nombre}" creada exitosamente')
                return redirect("/acciones")
            except Exception as e:
                messages.error(request, f'Error al crear la verificación: {str(e)}')
    else:
        form = VerificacionForm()

    return render(request, "acciones/crear_verificacion.html", {"user": user, "dimensiones": dimensiones, "form": form})

@login_required_simulado
def display_edit_verificacion(request, id):
    user = request.session.get("user")
    verificacion = get_object_or_404(VerificacionAccion, verificacion_id=id)

    if request.method == "POST":
        form = VerificacionForm(request.POST, instance=verificacion)
        if form.is_valid():
            verificacion = verificacion_service.update_verificacion(id, form.cleaned_data)
            messages.success(request, f'Verificación actualizada exitosamente')
            return redirect("/acciones")
    else:
        form = VerificacionForm(instance=verificacion)

    return render(request, "acciones/editar_verificacion.html", {"user": user, "dimensiones": dimensiones, "form": form})

@login_required_simulado
def eliminar_verificacion(request, id):
    if request.method == "POST":
        try:
            verificacion = get_object_or_404(VerificacionAccion, verificacion_id=id)
            nombre = verificacion.nombre
            verificacion_service.delete_verificacion(id)
            messages.success(request, f'Verificación "{nombre}" eliminada exitosamente')
        except Exception as e:
            messages.error(request, f'Error al eliminar la verificación: {str(e)}')
    return redirect("/acciones")
    