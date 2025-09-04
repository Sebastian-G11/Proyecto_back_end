from django.shortcuts import render
from datetime import datetime

# Create your views here.
def prueba2(request):
    actividades = [
        {
            "accion_id": "Capacitación Personal",
            "responsable": "Pedro Silva",  
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
            "fecha_creacion": datetime(2025, 9, 1, 11, 20),
            "fecha_actualizacion": datetime(2025, 9, 3, 9, 45),
            "estado": 0,
            "medios_verificacion": [
                {"nombre": "Manual usuario", "url": "https://example.com/manual"},
            ],
        },
    ]  

    return render(request, 'actividades/lista_actividades.html', {"actividades": actividades})