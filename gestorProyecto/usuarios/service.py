from .validations import validate_nombre, validate_apellido, validate_email, validate_rol
from .repositorio.repository import UsersRepository
from django.db.models import Q


class UserService:

    def __init__(self, repository):
        self.repository = repository

    def get_users(self):
        return self.repository.get_users()

    def create_user(self, nombre, apellido, email, rol='Usuario'):
        validate_nombre(nombre)
        validate_apellido(apellido)
        validate_email(email)
        validate_rol(rol)
        return self.repository.create_users(nombre, apellido, email, rol)

    def update_user(self, id, nombre, apellido, email, rol):
        validate_nombre(nombre)
        validate_apellido(apellido)
        validate_email(email)
        validate_rol(rol)
        return self.repository.update_users(id, nombre, apellido, email, rol)

    def delete_user(self, id):
        return self.repository.delete_users(id)
    
    def get_by_filter(self, search_query):
        q_filters = Q(nombre__icontains=search_query)
        return self.repository.get_by_filter(q_filters)

user_service = UserService(UsersRepository())
