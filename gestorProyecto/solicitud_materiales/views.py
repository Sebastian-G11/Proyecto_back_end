from django.shortcuts import render
from autenticacion.views import login_required_simulado
## Mocks de actividades, solicitudes y usuarios para añadido dinámico, posteriormente vendrán de la misma BDD
actividades = [
    {"actividad_id": 1, "nombre": "Capacitación Inicial"},
    {"actividad_id": 2, "nombre": "Implementación CRM"},
    {"actividad_id": 3, "nombre": "Revisión de Inventario"}
]

solicitudes = [
    {
        "actividad_id": 1,
        "actividad_nombre": "Capacitación Inicial",
        "materiales_solicitados": "Laptop, Proyector",
        "numero_orden": "ORD001",
        "valor_esperado": 1200,
        "valor_final_compra": 1150,
        "codigo_factura": "FAC001",
        "fecha_creacion": "2025-09-08 10:00",
        "responsable": 101,
        "responsable_nombre": "Juan Pérez"
    },
    {
        "actividad_id": 2,
        "actividad_nombre": "Implementación CRM",
        "materiales_solicitados": "Servidor, Licencias Software",
        "numero_orden": "ORD002",
        "valor_esperado": 5000,
        "valor_final_compra": None,
        "codigo_factura": "FAC002",
        "fecha_creacion": "2025-09-08 12:00",
        "responsable": 102,
        "responsable_nombre": "María González"
    }
]

usuarios = [
    {"id": 101, "nombre": "Juan Pérez"},
    {"id": 102, "nombre": "María González"},
    {"id": 103, "nombre": "Carlos Ramírez"}
]


@login_required_simulado
# Create your views here.
def display_solicitud_materiales(request):
    user = request.session.get("user")
    return render(request, "solicitud_materiales/lista_materiales.html", {"usuario": user, "actividades": actividades, "solicitudes": solicitudes, "usuarios": usuarios})