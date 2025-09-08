from django.shortcuts import render

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


# Create your views here.
def display_sub_actividades(request):
    return render(request, "sub_actividades/lista_sub-actividades.html", { "actividades": actividades, "subactividades": subactividades })