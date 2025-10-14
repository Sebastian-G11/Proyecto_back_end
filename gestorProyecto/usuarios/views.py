from django.shortcuts import render, redirect
from django.contrib import messages
from .repositorio.repository import UsersRepository
from .forms import FormUsuario
from autenticacion.views import login_required_simulado
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

repo = UsersRepository()

@login_required_simulado
def display(request):
    """
    Muestra la lista de usuarios.
    """
    usuarios_list = repo.get_users()
    user = request.session.get("user")

    paginator = Paginator(usuarios_list, 3)
    page = request.GET.get('page')
    try:
        usuarios = paginator.page(page)
    except PageNotAnInteger:
        usuarios = paginator.page(1)
    except EmptyPage:
        usuarios = paginator.page(paginator.num_pages)

    return render(request, "usuarios/lista_usuarios.html", {
        "usuarios": usuarios,
        "user": user, 
    })
    
    
@login_required_simulado
def agregar_usuario(request):
    """
    Agregar un nuevo usuario.
    """
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


@login_required_simulado
def actualizar_usuario(request, id):
    """
    Actualiza un usuario existente.
    """
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


@login_required_simulado
def eliminar_usuario(request, id):
    """
    Elimina un usuario.
    """
    eliminado = repo.delete_users(id)
    if eliminado:
        messages.success(request, "Usuario eliminado correctamente")
    else:
        messages.error(request, "Usuario no encontrado")
    return redirect("usuarios:listado_usuarios")
