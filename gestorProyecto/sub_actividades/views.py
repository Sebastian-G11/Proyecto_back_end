from django.shortcuts import render

# Create your views here.
def display_sub_actividades(request):
    return render(request, "sub_actividades/prueba2.html")