from django.shortcuts import render,redirect
from autenticacion.views import login_required_simulado
# Mock de usuarios para añadido dinámico, posteriormente vendrán desde la BDD
usuarios = [
    {"nombre": "Juan", "apellido": "Pérez", "email": "juan.perez@example.com", "rol": "Administrador"},
    {"nombre": "María", "apellido": "Gómez", "email": "maria.gomez@example.com", "rol": "Usuario"},
    {"nombre": "Carlos", "apellido": "López", "email": "carlos.lopez@example.com", "rol": "Invitado"},
    {"nombre": "Ana", "apellido": "Torres", "email": "ana.torres@example.com", "rol": "Usuario"},
  ]
@login_required_simulado
# Create your views here.
def display(request):
  user = request.session.get("user")
  return render(request, "usuarios/lista_usuarios.html", {"user": user,"usuarios": usuarios})