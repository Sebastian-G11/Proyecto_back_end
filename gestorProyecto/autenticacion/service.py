from usuarios.repositorio.repository_interface import UsersRepositoryI
from usuarios.repositorio.repository import UsersRepository

class AuthService:
    def __init__ (self, users_repository: UsersRepositoryI):
        self.users_repository = users_repository

    def auth(self, user_data):
        email = user_data.get('email')
        password = user_data.get('password')

        user = self.users_repository.get_user_by_email(email)
        if user and user.email == email:
            if user.password == password:
                user_data = {
                    'usuario_id': user.usuario_id,
                    'nombre': user.nombre,
                    'apellido': user.apellido,
                    'email': user.email,
                    'rol_name': user.rol.nombre,
                    'rol': user.rol.rol_id,
                }

                return user_data
        return None

auth_service = AuthService(UsersRepository())