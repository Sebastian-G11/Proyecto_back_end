from django.shortcuts import render

# Create your views here.
def display_dimensiones(request):
    return render(request, "dimensiones/prueba1.html")