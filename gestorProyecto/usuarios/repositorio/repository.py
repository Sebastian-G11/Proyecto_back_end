from .repository_interface import UsersRepositoryI
from ..models import Usuarios


class UsersRepository(UsersRepositoryI):
    usuario_model = Usuarios

    def create_users(self, nombre, apellido, email, rol='Usuario'):
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
    
    def get_by_filter(self, q_filters):
        return self.usuario_model.objects.filter(q_filters)
