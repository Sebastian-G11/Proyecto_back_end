from django.shortcuts import redirect, render, get_object_or_404
from autenticacion.views import login_required_simulado
from .service import actividades_service, verificaciones_service
from .forms import ActividadForm, VerificacionForm
from django.contrib import messages
from .models import Actividad, VerificacionActividad
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

## Mock de actividades y acciones para hacer el añadido dinámico en la template, posteriormente vendrán directamente desde la base de datos

acciones = [
        {
          "nombre": "Capacitación Personal"
        },
        {
          "nombre": "Implementación CRM"
        }
    ]

@login_required_simulado
def display_actividades(request):
    user = request.session.get("user")
    actividades_list = actividades_service.get_actividades()
    verificaciones = verificaciones_service.get_verificaciones()

    paginator = Paginator(actividades_list, 3)
    page = request.GET.get('page')

    try:
        actividades = paginator.page(page)
    except PageNotAnInteger:
        actividades = paginator.page(1)
    except EmptyPage:
        actividades = paginator.page(paginator.num_pages)

    return render(request, 'actividades/lista_actividades.html', {"user": user,"actividades": actividades, "acciones": acciones, "verificaciones": verificaciones})

@login_required_simulado
def display_crear_actividad(request):
    user = request.session.get("user")
    if request.method == "POST":
        form = ActividadForm(request.POST)
        if form.is_valid():
            actividad = actividades_service.create_actividad(form.cleaned_data)
            messages.success(request, f'Acción "{actividad.nombre}" creada exitosamente')  

            return redirect("/actividades")
    else:
        form = ActividadForm()

    return render(request, 'actividades/crear_actividad.html', {"user": user, "form": form})

@login_required_simulado
def display_editar_actividad(request, id):
    user = request.session.get("user")
    actividad = get_object_or_404(Actividad, actividad_id=id)

    if request.method == "POST":
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            actividad = actividades_service.update_actividad(id, form.cleaned_data)
            messages.success(request, f'Actividad actualizada exitosamente')  
            return redirect("/actividades")
    else:
        form = ActividadForm(instance=actividad)

    return render(request, 'actividades/editar_actividad.html', {"user": user, "form": form, "actividad": actividad})

@login_required_simulado
def eliminar_actividad(request, id):
    actividad = get_object_or_404(Actividad, actividad_id=id)

    if request.method == "POST":
        actividades_service.delete_actividad(id)
        messages.success(request, f'Actividad "{actividad.nombre}" eliminada exitosamente')  
        return redirect("/actividades")

    return render(request, 'actividades/confirmar_eliminacion.html', {"actividad": actividad})

@login_required_simulado
def display_crear_verificacion(request):
    user = request.session.get("user")

    if request.method == "POST":
        form = VerificacionForm(request.POST)
        if form.is_valid():
            verificacion = verificaciones_service.create_verificacion(form.cleaned_data)
            messages.success(request, f'Medio de verificación "{verificacion.nombre}" creado exitosamente')  
            return redirect("/actividades")
    else:
        form = VerificacionForm()

    return render(request, "actividades/crear_verificacion.html", {"user": user, "form": form})

@login_required_simulado
def display_editar_verificacion(request, id):
    user = request.session.get("user")
    verificacion = get_object_or_404(VerificacionActividad, verificacion_id=id)

    if request.method == "POST":
        form = VerificacionForm(request.POST, instance=verificacion)
        if form.is_valid():
            verificacion = verificaciones_service.update_verificacion(id, form.cleaned_data)
            messages.success(request, f'Medio de verificación actualizado exitosamente')  
            return redirect("/actividades")
    else:
        form = VerificacionForm(instance=verificacion)

    return render(request, "actividades/editar_verificacion.html", {"user": user, "form": form, "verificacion": verificacion})

@login_required_simulado
def eliminar_verificacion(request, id):
    verificacion = get_object_or_404(VerificacionActividad, verificacion_id=id)

    if request.method == "POST":
        verificaciones_service.delete_verificacion(id)
        messages.success(request, f'Medio de verificación "{verificacion.nombre}" eliminado exitosamente')  
        return redirect("/actividades")

    return render(request, "actividades/confirmar_eliminacion_verificacion.html", {"verificacion": verificacion})