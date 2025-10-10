from .repositorio.repositiorio_interface import ActividadesRepositoryI, VerificacionesRepositoryI
from .repositorio.repositorio import ActividadesRepository, VerificacionesRepository

class ActividadesService:
    def __init__(self, repository: ActividadesRepositoryI):
        self.repository = repository

    def get_actividades(self):
        return self.repository.get_actividades()

    def create_actividad(self, data):
        return self.repository.create_actividad(data)

    def update_actividad(self, id, data) -> bool:
        return self.repository.update_actividad(id, data)

    def delete_actividad(self, id) -> bool:
        return self.repository.delete_actividad(id)
    
class VerificacionesService:
    def __init__(self, repository: VerificacionesRepositoryI):
        self.repository = repository

    def get_verificaciones(self):
        return self.repository.get_verificaciones()

    def create_verificacion(self, data):
        return self.repository.create_verificacion(data)

    def update_verificacion(self, id, data) -> bool:
        return self.repository.update_verificacion(id, data)

    def delete_verificacion(self, id) -> bool:
        return self.repository.delete_verificacion(id)

actividades_service = ActividadesService(ActividadesRepository())
verificaciones_service = VerificacionesService(VerificacionesRepository())