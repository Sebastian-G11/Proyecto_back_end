from .repository_interface import UsersRepositoryI
from ..models import Usuarios
from ..validations import validate_nombre, validate_apellido, validate_email, validate_rol

class UsersRepository(UsersRepositoryI):

    def create_users(self, nombre, apellido, email, rol='Usuario'):
        # Realiza las validaciones antes de crear el usuario
        validate_nombre(nombre)
        validate_apellido(apellido)
        validate_email(email)
        validate_rol(rol)
        usuario = Usuarios(nombre=nombre, apellido=apellido, email=email, rol=rol)
        usuario.save()
        return usuario

    def get_users(self):
        return Usuarios.objects.all()

    def get_user_by_id(self, id):
        try:
            return Usuarios.objects.get(id=id)
        except Usuarios.DoesNotExist:
            return None

    def update_users(self, id, nombre, apellido, email, rol):
        try:
            usuario = Usuarios.objects.get(id=id)
            usuario.nombre = nombre
            usuario.apellido = apellido
            usuario.email = email
            usuario.rol = rol
            usuario.save()
            return usuario
        except Usuarios.DoesNotExist:
            return None

    def delete_users(self, id):
        usuario = self.get_user_by_id(id)
        if not usuario:
            return False
        usuario.delete()
        return True
