from .repositorio.repository_interface import AccionesRepositoryI, VerificacionRepositoryI
from .repositorio.repository import AccionesRepository, VerificacionRepository

class AccionesService:
    def __init__(self, repository: AccionesRepositoryI):
        self.repository = repository

    def get_all_acciones(self):
        return self.repository.get_acciones()

    def create_accion(self, nombre):
        return self.repository.create_accion(nombre)

    def update_accion(self, id, data):
        return self.repository.update_accion(id, data)

    def delete_accion(self, id):
        return self.repository.delete_accion(id)
    

class VerificacionService:
    def __init__(self, repository: VerificacionRepositoryI):
        self.repository = repository

    def get_all_verificaciones(self):
        return self.repository.get_verificaciones()

    def create_verificacion(self, data):
        return self.repository.create_verificacion(data)

    def update_verificacion(self, id, data):
        return self.repository.update_verificacion(id, data)

    def delete_verificacion(self, id):
        return self.repository.delete_verificacion(id)

acciones_service = AccionesService(AccionesRepository())
verificacion_service = VerificacionService(VerificacionRepository())