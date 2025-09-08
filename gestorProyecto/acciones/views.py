from django.shortcuts import render
from autenticacion.views import login_required_simulado

@login_required_simulado
def display_acciones(request):
    user = request.session.get("user")
    acciones = [
        {
            "dimension": 1,
            "nombre": "Capacitación Personal",
            "responsable": "Juan Pérez",
            "presupuesto_anual": 5000000,
            "presupuesto_reajustado": 5500000,
            "estado": "Activo",
            "descripcion": "Capacitación anual del equipo de ventas.",
            "fecha_creacion": "01/01/2025 10:00",
            "fecha_actualizacion": "05/02/2025 15:30",
            "medios_verificacion": [
                {"nombre": "Plan de capacitación", "url": "https://example.com/plan"},
                {"nombre": "Registro asistencia", "url": "https://example.com/asistencia"},
            ],
        },
        {
            "dimension": 2,
            "nombre": "Implementación CRM",
            "responsable": "María López",
            "presupuesto_anual": 8000000,
            "presupuesto_reajustado": 8200000,
            "estado": "Inactivo",
            "descripcion": "Instalación y configuración del CRM de ventas.",
            "fecha_creacion": "15/01/2025 11:20",
            "fecha_actualizacion": "20/02/2025 09:45",
            "medios_verificacion": [
                {"nombre": "Manual usuario", "url": "https://example.com/manual"},
            ],
        },
    ]
    return render(request, "acciones/lista_acciones.html", {"usuario": user, "acciones": acciones})
