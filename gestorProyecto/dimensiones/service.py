from .repositorio.repository import DimensionesRepository
from .repositorio.repository_interface import DimensionesRepositoryI
class DimensionesService:

    def __init__(self, repository:DimensionesRepositoryI):
        self.repository = repository

    def create_dimension(self, nombre):
        return self.repository.create_dimension(nombre)

    def update_dimension(self, id, nombre):
        return self.repository.update_dimension(id, nombre)

    def delete_dimension(self, id):
        return self.repository.delete_dimension(id)

dimensiones_service = DimensionesService(DimensionesRepository())
