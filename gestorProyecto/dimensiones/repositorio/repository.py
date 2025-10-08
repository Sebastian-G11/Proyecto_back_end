from .repository_interface import DimensionesRepositoryI
from ..models import Dimensiones

class DimensionesRepository(DimensionesRepositoryI):

    def get_dimensiones(self):
        return Dimensiones.objects.all()

    def get_dimension_by_id(self, id):
        try:
            return Dimensiones.objects.get(id=id)
        except Dimensiones.DoesNotExist:
            return None

    def create_dimension(self, nombre):
        dimension = Dimensiones(nombre=nombre)
        dimension.save()
        return dimension

    def update_dimension(self, id, nombre):
        dimension = self.get_dimension_by_id(id)
        if dimension:
            dimension.nombre = nombre
            dimension.save()
            return dimension
        return None

    def delete_dimension(self, id):
        dimension = self.get_dimension_by_id(id)
        if not dimension:
            return False
        dimension.delete()
        return True
