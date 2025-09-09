from django.shortcuts import render
from autenticacion.views import login_required_simulado
# Mock de actividades y subactividades para añadido dinámico, posteriormente vendrán desde la BDD
actividades = [
    {
        "actividad_id": 1,
        "nombre": "Clase de capacitación"
    },
    {
        "actividad_id": 2,
        "nombre": "Plan de Uso de CRM"
    }
]

subactividades = [
    {
        "actividad": "Clase de Capacitación",
        "nombre": "Revisión de Materiales",
        "fecha_creacion": "2025-09-01",
        "fecha_actualizacion": "2025-09-02",
        "grado_aprobacion": "80%"
    },
    {
        "actividad": "Plan de Uso de CRM",
        "nombre": "Configuración de Usuarios",
        "fecha_creacion": "2025-09-03",
        "fecha_actualizacion": "2025-09-04",
        "grado_aprobacion": "90%"
    }
]

@login_required_simulado
# Create your views here.
def display_sub_actividades(request):
    user = request.session.get("user")
    return render(request, "sub_actividades/lista_sub-actividades.html", {"usuario":user, "actividades": actividades, "subactividades": subactividades })