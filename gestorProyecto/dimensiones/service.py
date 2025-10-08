from .repositorio.repository import DimensionesRepository
from .validations import validate_nombre

class DimensionesService:

    def __init__(self, repository):
        self.repository = repository

    def create_dimension(self, nombre):
        # Validaciones antes de crear la dimensión
        validate_nombre(nombre)
        return self.repository.create_dimension(nombre)

    def update_dimension(self, id, nombre):
        # Validaciones antes de actualizar la dimensión
        validate_nombre(nombre)
        return self.repository.update_dimension(id, nombre)

    def delete_dimension(self, id):
        return self.repository.delete_dimension(id)

# Instanciamos el servicio con el repositorio
dimensiones_service = DimensionesService(DimensionesRepository())
