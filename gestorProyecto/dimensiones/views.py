from django.shortcuts import render, redirect
from django.db.models import Max
from django.contrib import messages
from .forms import FormDimensiones
from .service import dimensiones_service
from .repositorio.repository import DimensionesRepository
from .models import Dimensiones
from autenticacion.views import login_required_simulado

repo = DimensionesRepository()

@login_required_simulado
def lista_dimensiones(request):
    dimensiones = dimensiones_service.get_dimensiones()  
    return render(request, "dimensiones/lista_dimensiones.html", {
        "dimensiones": dimensiones
    })


@login_required_simulado
def agregar_dimension(request):
    if request.method == "POST":
        form = FormDimensiones(request.POST)
        if form.is_valid():
            try:
                nueva_dimension = dimensiones_service.create_dimension(form.cleaned_data['nombre'])  
                messages.success(request, f"Dimensión '{nueva_dimension.nombre}' creada exitosamente")
                return redirect("dimensiones:listado_dimensiones")
            except Exception as e:
                messages.error(request, f"Error al crear la dimensión: {str(e)}")
                form.add_error(None, str(e))
        else:
            messages.error(request, "Errores en el formulario.")
    else:
        form = FormDimensiones()


    dimension_id = Dimensiones.objects.aggregate(Max('id'))['id__max'] + 1 if Dimensiones.objects.exists() else 1

    return render(request, "dimensiones/crear_dimensiones.html", {
        "form": form,
        "dimension_id": dimension_id
    })


@login_required_simulado
def editar_dimension(request, id):
    try:
        dimension = repo.get_dimension_by_id(id)  
    except Dimensiones.DoesNotExist:
        messages.error(request, "Dimensión no encontrada.")
        return redirect('dimensiones:listado_dimensiones')

    if request.method == 'POST':
        form = FormDimensiones(request.POST, instance=dimension)
        if form.is_valid():
            try:
                updated_dimension = dimensiones_service.update_dimension(id, form.cleaned_data['nombre']) 
                messages.success(request, f"Dimensión '{updated_dimension.nombre}' actualizada correctamente.")
                return redirect('dimensiones:listado_dimensiones')
            except Exception as e:
                messages.error(request, f"Error al actualizar la dimensión: {str(e)}")
                form.add_error(None, str(e))
        else:
            messages.error(request, "Errores en el formulario.")
            return render(request, 'dimensiones/editar_dimensiones.html', {'form': form, 'dimension': dimension})
    else:
        form = FormDimensiones(instance=dimension)

    return render(request, 'dimensiones/editar_dimensiones.html', {'form': form, 'dimension': dimension})


@login_required_simulado
def eliminar_dimension(request, id):
    try:
        eliminado = dimensiones_service.delete_dimension(id)  
        if eliminado:
            messages.success(request, "Dimensión eliminada correctamente.")
        else:
            messages.error(request, "Dimensión no encontrada.")
    except Exception as e:
        messages.error(request, f"Error al eliminar la dimensión: {str(e)}")
    
    return redirect("dimensiones:listado_dimensiones")
