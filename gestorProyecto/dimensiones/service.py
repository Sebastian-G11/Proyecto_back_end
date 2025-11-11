from .repositorio.repository import DimensionesRepository
from .repositorio.repository_interface  import DimensionesRepositoryI
from django.db.models import Q
from dimensiones.models import Dimensiones as Dimension

class DimensionesService:
    def __init__(self, repository: DimensionesRepositoryI):
        self.repository = repository

    def get_all_dimensiones(self) -> list[Dimension]:
        return self.repository.get_dimensiones()

    def create_dimension(self, nombre) -> Dimension:
        return self.repository.create_dimension(nombre)

    def update_dimension(self, id, nombre) -> Dimension:
        return self.repository.update_dimension(id, nombre)

    def delete_dimension(self, id):
        return self.repository.delete_dimension(id)
    
    def get_by_filter(self, search_query):
        q_filters = Q(nombre__icontains=search_query) | Q()
        return self.repository.get_by_filter(q_filters)
    
    def get_suma_presupuestos(self):
        return self.repository.get_suma_presupuestos()

dimensiones_service = DimensionesService(DimensionesRepository())
