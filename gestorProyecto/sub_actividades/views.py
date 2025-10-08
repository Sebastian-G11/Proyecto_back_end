from django.shortcuts import render, redirect, get_object_or_404
from .models import SubActividad
from .forms import SubActividadForm
from django.contrib import messages
from .repositorio.repository import SubActividadRepository
from autenticacion.views import login_required_simulado



repo = SubActividadRepository()
@login_required_simulado
def listar_subactividades(request):
    """
    Muestra la lista de subactividades.
    """
    # Obtener todas las subactividades
    subactividades = SubActividad.objects.all()

    # Contexto a pasar a la plantilla
    return render(request, "sub_actividades/lista_sub_actividades.html", {
        "subactividades": subactividades,
    })


@login_required_simulado
def agregar_subactividad(request):
    if request.method == 'POST':
        form = SubActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subactividades:listar_subactividades')
    else:
        form = SubActividadForm()
    return render(request, 'sub_actividades/crear_sub_actividades.html', {'form': form})

@login_required_simulado
def editar_subactividad(request, id):
    subactividad = get_object_or_404(SubActividad, id=id)
    if request.method == 'POST':
        form = SubActividadForm(request.POST, instance=subactividad)
        if form.is_valid():
            form.save()
            return redirect('subactividades:listar_subactividades')
    else:
        form = SubActividadForm(instance=subactividad)
    return render(request, 'sub_actividades/editar_sub_actividades.html', {'form': form, 'subactividad': subactividad})

# Eliminar subactividad
@login_required_simulado
def eliminar_subactividad(request, id):
    """
    Elimina una sub-actividad directamente desde el modelo.
    """
    try:
        subactividad = SubActividad.objects.get(id=id)
        subactividad.delete()
        messages.success(request, "Sub-actividad eliminada correctamente.")
    except SubActividad.DoesNotExist:
        messages.error(request, "Sub-actividad no encontrada.")
    return redirect("subactividades:listar_subactividades")

