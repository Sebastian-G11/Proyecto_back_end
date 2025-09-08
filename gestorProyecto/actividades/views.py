from django.shortcuts import render
from datetime import datetime

## Mock de actividades y acciones para hacer el añadido dinámico en la template, posteriormente vendrán directamente desde la base de datos
actividades = [
        {
            "accion_id": "Capacitación Personal",
            "responsable": "Pedro Silva",  
            "nombre": "Clase de capacitación",
            "fecha_creacion": datetime(2025, 9, 4, 10, 0),
            "fecha_actualizacion": datetime(2025, 9, 5, 15, 30),
            "estado": 1,  # 1=Activo, 0=Inactivo
            "medios_verificacion": [
                {"nombre": "Plan de capacitación", "url": "https://example.com/plan"},
                {"nombre": "Registro asistencia", "url": "https://example.com/asistencia"},
            ],
        },
        {
            "accion_id": "Implementación CRM",
            "responsable": "Pedro Silva",
            "nombre": "Plan de uso de CRM",
            "fecha_creacion": datetime(2025, 9, 1, 11, 20),
            "fecha_actualizacion": datetime(2025, 9, 3, 9, 45),
            "estado": 0,
            "medios_verificacion": [
                {"nombre": "Manual usuario", "url": "https://example.com/manual"},
            ],
        },
    ]  
acciones = [
        {
          "nombre": "Capacitación Personal"
        },
        {
          "nombre": "Implementación CRM"
        }
    ]

# Create your views here.
def display_actividades(request):
    return render(request, 'actividades/lista_actividades.html', {"actividades": actividades, "acciones": acciones})