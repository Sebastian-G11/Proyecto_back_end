from django.shortcuts import render, redirect
from django.contrib import messages
from .repositorio.repository import UsersRepository
from .forms import FormUsuario
from autenticacion.views import login_required_simulado, admin_required
repo = UsersRepository()



@login_required_simulado
def display(request):
    usuarios = repo.get_users()
    user = request.session.get("user")

    return render(request, "usuarios/lista_usuarios.html", {
        "usuarios": usuarios,
        "user": user, 
    })
    
    
@admin_required
@login_required_simulado
def agregar_usuario(request):
    if request.method == 'POST':
        form = FormUsuario(request.POST)

        if form.is_valid():
            form.save() 
            messages.success(request, "Usuario agregado correctamente.")
            return redirect('usuarios:listado_usuarios') 
        else:
            messages.error(request, "Error al agregar el usuario. Verifique los datos.")
            return render(request, 'usuarios/crear_usuario.html', {'form': form})

    else:
        form = FormUsuario() 
    return render(request, 'usuarios/crear_usuario.html', {'form': form})


@admin_required
@login_required_simulado
def actualizar_usuario(request, id):
    usuario = repo.get_user_by_id(id)
    if not usuario:
        messages.error(request, "Usuario no encontrado")
        return redirect("usuarios:listado_usuarios")

    if request.method == "POST":
        form = FormUsuario(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario actualizado correctamente")
            return redirect("usuarios:listado_usuarios")
        else:
            messages.error(request, "Errores en el formulario")
    else:
        form = FormUsuario(instance=usuario)

    return render(request, "usuarios/editar_usuario.html", {"form": form, "usuario": usuario})


@admin_required
@login_required_simulado
def eliminar_usuario(request, id):
    eliminado = repo.delete_users(id)
    if eliminado:
        messages.success(request, "Usuario eliminado correctamente")
    else:
        messages.error(request, "Usuario no encontrado")
    return redirect("usuarios:listado_usuarios")
