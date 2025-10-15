from .repositorio.repository import DimensionesRepository
from .repositorio.repository_interface  import DimensionesRepositoryI
from django.db.models import Q


class DimensionesService:
    def __init__(self, repository: DimensionesRepositoryI):
        self.repository = repository

    def get_all_dimensiones(self):
        return self.repository.get_dimensiones()

    def create_dimension(self, nombre):
        return self.repository.create_dimension(nombre)

    def update_dimension(self, id, nombre):
        return self.repository.update_dimension(id, nombre)

    def delete_dimension(self, id):
        return self.repository.delete_dimension(id)
    
    def get_by_filter(self, search_query):
        q_filters = Q(nombre__icontains=search_query) | Q()
        return self.repository.get_by_filter(q_filters)

dimensiones_service = DimensionesService(DimensionesRepository())
