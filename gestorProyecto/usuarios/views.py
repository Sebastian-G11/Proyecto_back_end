from django.shortcuts import render, redirect
from django.contrib import messages
from .repositorio.repository import UsersRepository
from .forms import FormUsuario
from autenticacion.views import login_required_simulado
from .service import user_service
from .validations import validate_nombre, validate_apellido, validate_email, validate_rol

repo = UsersRepository()


@login_required_simulado
def display(request):

    usuarios = repo.get_users()
    user = request.session.get("user")

    return render(request, "usuarios/lista_usuarios.html", {
        "usuarios": usuarios,
        "user": user, 
    })
    
    
@login_required_simulado
def agregar_usuario(request):

    if request.method == 'POST':
        form = FormUsuario(request.POST)

        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            rol = form.cleaned_data['rol']

            try:
                validate_nombre(nombre)
                validate_apellido(apellido)
                validate_email(email)
                validate_rol(rol)
                user_service.create_user(nombre, apellido, email, rol)
                messages.success(request, "Usuario agregado correctamente.")
                return redirect('usuarios:listado_usuarios')
            except ValueError as e:
                messages.error(request, str(e))
                form.add_error(None, str(e))
            except Exception as e:
                messages.error(request, "Ocurrió un error al crear el usuario.")
                form.add_error(None, f"Error inesperado: {str(e)}")

        else:
            messages.error(request, "Error al agregar el usuario. Verifique los datos.")
            return render(request, 'usuarios/crear_usuario.html', {'form': form})
    else:
        form = FormUsuario()

    return render(request, 'usuarios/crear_usuario.html', {'form': form})



@login_required_simulado
def actualizar_usuario(request, id):
    usuario = repo.get_user_by_id(id)
    if not usuario:
        messages.error(request, "Usuario no encontrado")
        return redirect("usuarios:listado_usuarios")

    if request.method == "POST":
        form = FormUsuario(request.POST, instance=usuario)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            rol = form.cleaned_data['rol']

            try:
                validate_nombre(nombre)
                validate_apellido(apellido)
                validate_email(email)
                validate_rol(rol)
                user_service.update_user(id, nombre, apellido, email, rol)
                messages.success(request, "Usuario actualizado correctamente")
                return redirect("usuarios:listado_usuarios")
            except ValueError as e:
                messages.error(request, str(e))
                form.add_error(None, str(e))
            except Exception as e:
                messages.error(request, f"Error al actualizar el usuario: {str(e)}")
                form.add_error(None, str(e))
        else:
            messages.error(request, "Errores en el formulario")
    else:
        form = FormUsuario(instance=usuario)

    return render(request, "usuarios/editar_usuario.html", {"form": form, "usuario": usuario})


@login_required_simulado
def eliminar_usuario(request, id):
    try:
        eliminado = user_service.delete_user(id)
        if eliminado:
            messages.success(request, "Usuario eliminado correctamente")
        else:
            messages.error(request, "Usuario no encontrado")
    except Exception as e:
        messages.error(request, f"Error al eliminar el usuario: {str(e)}")

    return redirect("usuarios:listado_usuarios")
