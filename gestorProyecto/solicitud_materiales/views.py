from django.shortcuts import render

# Create your views here.
def display_solicitud_materiales(request):
    return render(request, "solicitud_materiales/prueba3.html")