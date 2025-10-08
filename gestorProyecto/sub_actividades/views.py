from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from .models import SubActividad
from .forms import SubActividadForm

def listar_subactividades(request):
    subactividades = SubActividad.objects.all()
    return render(request, "sub_actividades/lista_sub_actividades.html", {
        "subactividades": subactividades,
    })


def agregar_subactividad(request):
    if request.method == 'POST':
        form = SubActividadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "La sub-actividad se ha agregado correctamente.")  
            return redirect('subactividades:listar_subactividades')
        else:
            messages.error(request, "Hubo un error al agregar la sub-actividad. Verifica los datos ingresados.")  
    else:
        form = SubActividadForm()
    return render(request, 'sub_actividades/crear_sub_actividades.html', {'form': form})


def editar_subactividad(request, id):
    subactividad = get_object_or_404(SubActividad, id=id)
    if request.method == 'POST':
        form = SubActividadForm(request.POST, instance=subactividad)
        if form.is_valid():
            form.save()
            messages.success(request, "La sub-actividad se ha actualizado correctamente.")
            return redirect('subactividades:listar_subactividades')
        else:
            messages.error(request, "No se pudo actualizar la sub-actividad. Revisa los datos ingresados.")
    else:
        form = SubActividadForm(instance=subactividad)
    return render(request, 'sub_actividades/editar_sub_actividades.html', {'form': form, 'subactividad': subactividad})


def eliminar_subactividad(request, id):
    subactividad = get_object_or_404(SubActividad, id=id)
    if request.method == 'POST':
        subactividad.delete()
        messages.success(request, "La sub-actividad se eliminó correctamente.")  # ✅
        return redirect('subactividades:listar_subactividades')
    return render(request, 'sub_actividades/eliminar_sub_actividades.html', {'subactividad': subactividad})
