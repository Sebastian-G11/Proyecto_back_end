from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import SubActividadForm
from .services import subactividad_service 
from .models import SubActividad

def listar_subactividades(request):
    user = request.session.get("user")
    subactividades = subactividad_service.obtener_sub_actividades()  
    return render(request, "sub_actividades/lista_sub_actividades.html", {
        "subactividades": subactividades,"user": user
    })


def agregar_subactividad(request):
    if request.method == 'POST':
        form = SubActividadForm(request.POST)
        if form.is_valid():
            actividad = form.cleaned_data['actividad']
            nombre = form.cleaned_data['nombre']
            grado_aprobacion = form.cleaned_data['grado_aprobacion']
            
            try:
                subactividad_service.crear_sub_actividad(actividad, nombre, grado_aprobacion)
                messages.success(request, "La sub-actividad se ha agregado correctamente.")  
                return redirect('subactividades:listar_subactividades')
            except Exception as e:
                messages.error(request, f"Hubo un error al agregar la sub-actividad. {str(e)}")
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
            actividad = form.cleaned_data['actividad']
            nombre = form.cleaned_data['nombre']
            grado_aprobacion = form.cleaned_data['grado_aprobacion']
            
            try:
                subactividad_service.actualizar_sub_actividad(id, actividad, nombre, grado_aprobacion)
                messages.success(request, "La sub-actividad se ha actualizado correctamente.")
                return redirect('subactividades:listar_subactividades')
            except Exception as e:
                messages.error(request, f"No se pudo actualizar la sub-actividad. {str(e)}")
        else:
            messages.error(request, "No se pudo actualizar la sub-actividad. Revisa los datos ingresados.")
    else:
        form = SubActividadForm(instance=subactividad)
    
    return render(request, 'sub_actividades/editar_sub_actividades.html', {'form': form, 'subactividad': subactividad})


def eliminar_subactividad(request, id):
    if request.method == 'POST':
        try:
            subactividad_service.eliminar_sub_actividad(id)
            messages.success(request, "La sub-actividad se eliminó correctamente.")
        except Exception as e:
            messages.error(request, f"Error al eliminar la sub-actividad. {str(e)}")
    
    return redirect('subactividades:listar_subactividades')
