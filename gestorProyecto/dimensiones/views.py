from django.shortcuts import render
from autenticacion.views import login_required_simulado
# Mock de dimensiones para hacer el añadido dinámico en el template, posteriormente esta estructurá vendrá directamente de la BDD
dimensiones = [
    {
        "dimension_id": 1,
        "nombre": "Gestión de Capacitaciones"
    },
    {
        "dimension_id": 2,
        "nombre": "Interacción con el Cliente"
    }
]
@login_required_simulado
# Create your views here.
def display_dimensiones(request):
    user = request.session.get("user")
    return render(request, "dimensiones/lista_dimensiones.html", {"usuario":user, "dimensiones": dimensiones })