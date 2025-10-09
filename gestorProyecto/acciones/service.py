from .repositorio.repository_interface import AccionesRepositoryI
from .repositorio.repository import AccionesRepository

class AccionesService:
    def __init__(self, repository: AccionesRepositoryI):
        self.repository = repository

    def get_all_acciones(self):
        return self.repository.get_acciones()

    def create_accion(self, nombre):
        # Validaciones antes de crear la acción
        return self.repository.create_accion(nombre)

    def update_accion(self, id, data):
        return self.repository.update_accion(id, data)

    def delete_accion(self, id):
        return self.repository.delete_accion(id)
    
acciones_service = AccionesService(AccionesRepository())