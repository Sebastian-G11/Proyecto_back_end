from .validations import validate_nombre, validate_apellido, validate_email, validate_rol
from .repositorio.repository_interface import UsersRepositoryI
from .repositorio.repository import UsersRepository


class UserService:
    def __init__(self, repository: UsersRepositoryI):
        self.repository = repository

    def create_user(self, nombre, apellido, email, rol='Usuario'):
        return self.repository.create_users(nombre, apellido, email, rol)

    def update_user(self, id, nombre, apellido, email, rol):
        return self.repository.update_users(id, nombre, apellido, email, rol)

    def delete_user(self, id):
        return self.repository.delete_users(id)

user_service = UserService(UsersRepository())
