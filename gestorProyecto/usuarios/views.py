from django.shortcuts import render,redirect

# Create your views here.

usuarios = [
    {'nombre' : 'sebas',  'contrasena' : '1234'},
     {'nombre' : 'pepe', 'contrasena' : '123'}
]

def display(request):
    mensaje = ""
    if request.method == "POST":
        user = request.POST.get("nombre", "")
        pwd = request.POST.get("contrasena", "")


        encontrado = any(u['nombre'] == user and u['contrasena'] == pwd for u in usuarios)

        if encontrado:
            return redirect("/acciones/")  # redirige a la raíz que ya muestra renderTemplate
        else:
            mensaje = "Usuario o contraseña incorrecta"

    return render(request, "usuario/login.html", {"mensaje": mensaje})