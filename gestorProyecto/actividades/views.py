from django.shortcuts import render

# Create your views here.
def prueba2(request):
    return render(request, 'actividades/lista_actividades.html')