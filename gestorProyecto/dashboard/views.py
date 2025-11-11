from django.shortcuts import render

from autenticacion.views import admin_required, login_required_simulado
from .charts import evolucion_temporal_acciones, presupuesto_dimensiones, acciones_por_estado, progreso_actividades
from solicitud_materiales.models import SolicitudMaterial
from acciones.models import Accion
from dimensiones.models import Dimensiones
from actividades.models import Actividad

# Create your views here.
@admin_required
@login_required_simulado
def display_dashboard(request):
    user = request.session.get("user")

    grafico_presupuestos = presupuesto_dimensiones()
    grafico_acciones_estado = acciones_por_estado()
    grafico_progreso_actividades = progreso_actividades()
    grafico_evolucion_acciones = evolucion_temporal_acciones()

    total_solicitudes = SolicitudMaterial.objects.count()
    total_acciones = Accion.objects.count()
    total_dimensiones = Dimensiones.objects.count()
    total_actividades = Actividad.objects.count()

    context = {
        'user': user,
        'grafico_presupuestos': grafico_presupuestos,
        'grafico_acciones_estado': grafico_acciones_estado,
        'grafico_progreso_actividades': grafico_progreso_actividades,
        'grafico_evolucion_acciones': grafico_evolucion_acciones,
        'total_solicitudes': total_solicitudes,
        'total_acciones': total_acciones,
        'total_dimensiones': total_dimensiones,
        'total_actividades': total_actividades,
    }

    return render(request, 'dashboard/dashboard.html', context)