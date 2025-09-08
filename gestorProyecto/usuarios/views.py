from django.shortcuts import render,redirect

# Create your views here.
def display(request):
    usuarios = [
        {"nombre": "Juan", "apellido": "Pérez", "email": "juan.perez@example.com", "rol": "Administrador"},
        {"nombre": "María", "apellido": "Gómez", "email": "maria.gomez@example.com", "rol": "Usuario"},
        {"nombre": "Carlos", "apellido": "López", "email": "carlos.lopez@example.com", "rol": "Invitado"},
        {"nombre": "Ana", "apellido": "Torres", "email": "ana.torres@example.com", "rol": "Usuario"},
    ]
    return render(request, "usuarios/lista_usuarios.html", {"usuarios": usuarios})