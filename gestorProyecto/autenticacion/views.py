from django.shortcuts import render, redirect

# Lista de usuarios simulada
usuarios = [
    {'nombre': 'sebas', 'contrasena': '1234', 'role': 'user'},
    {'nombre': 'pepe', 'contrasena': '123', 'role': 'admin'}
]

# Login
def display(request):
    mensaje = ""
    if request.method == "POST":
        user = request.POST.get("nombre")
        pwd = request.POST.get("contrasena")
        encontrado = next((u for u in usuarios if u['nombre'] == user and u['contrasena'] == pwd), None)
        if encontrado:
            request.session["user"] = encontrado
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

# Ruta protegida
@login_required_simulado
def acciones(request):
    user = request.session["user"]
    return render(request, "acciones/lista_acciones.html", {"usuario": user})
