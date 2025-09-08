from django.shortcuts import render,redirect

# Mock de usuarios para añadido dinámico, posteriormente vendrán desde la BDD
usuarios = [
    {"nombre": "Juan", "apellido": "Pérez", "email": "juan.perez@example.com", "rol": "Administrador"},
    {"nombre": "María", "apellido": "Gómez", "email": "maria.gomez@example.com", "rol": "Usuario"},
    {"nombre": "Carlos", "apellido": "López", "email": "carlos.lopez@example.com", "rol": "Invitado"},
    {"nombre": "Ana", "apellido": "Torres", "email": "ana.torres@example.com", "rol": "Usuario"},
  ]

# Create your views here.
def display(request):
    return render(request, "usuarios/lista_usuarios.html", {"usuarios": usuarios})