from .repositorio.repository import DimensionesRepository

class DimensionesService:

    def __init__(self, repository: DimensionesRepository):
        self.repository = repository

    def get_by_id(self, id):
        return self.repository.get_dimension_by_id(id)

    def get_dimensiones(self):
        return self.repository.get_dimensiones()

    def create_dimension(self, nombre):
        return self.repository.create_dimension(nombre)

    def update_dimension(self, id, nombre):
        return self.repository.update_dimension(id, nombre)

    def delete_dimension(self, id):
        return self.repository.delete_dimension(id)


dimensiones_service = DimensionesService(DimensionesRepository())
