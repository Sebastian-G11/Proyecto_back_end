from django.shortcuts import render

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

# Create your views here.
def display_dimensiones(request):
    return render(request, "dimensiones/lista_dimensiones.html", { "dimensiones": dimensiones })