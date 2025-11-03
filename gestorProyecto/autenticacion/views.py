from django.shortcuts import render, redirect
from django.contrib import messages
from autenticacion.service import auth_service

# Lista de usuarios simulada
usuarios = [
    {'nombre': 'sebas', 'contrasena': '1234', 'role': 'Usuario', 'role_id' : 30}, 
    {'nombre': 'pepe', 'contrasena': '123', 'role': 'Administrador', 'role_id' : 10}
]

# Login
def display(request):
    mensaje = ""
    if request.method == "POST":
        email = request.POST.get("email")
        pwd = request.POST.get("contrasena")
        user_data = {'email': email, 'password': pwd}
        encontrado = auth_service.auth(user_data)
        if encontrado:
            request.session["user"] = encontrado
            request.session.set_expiry(600)
            return redirect("/acciones/")
        else:
            mensaje = "Usuario o contraseña incorrecta"
    return render(request, "autenticacion/login.html", {"mensaje": mensaje})

# Logout
def logout(request):
    request.session.flush()
    return redirect("/")

# Decorador para proteger rutas
def login_required_simulado(view_func):
    def wrapper(request, *args, **kwargs):
        if "user" not in request.session:
            return redirect("/")
        return view_func(request, *args, **kwargs)
    return wrapper


def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        user = request.session.get("user")
        if not user or user.get("role_id") != 10:
            messages.error(request, "No tienes permiso para acceder a esta sección.")
            return render(request, "error/error_acceso.html", {"mensaje": "Acceso no autorizado"})
        return view_func(request, *args, **kwargs)
    return wrapper