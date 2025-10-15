from .repository_interface import DimensionesRepositoryI
from ..models import Dimensiones

class DimensionesRepository(DimensionesRepositoryI):
    dimensiones_model = Dimensiones

    def get_dimensiones(self):
        return self.dimensiones_model.objects.all()

    def get_dimension_by_id(self, id):
        try:
            return self.dimensiones_model.objects.get(id=id)
        except Dimensiones.DoesNotExist:
            return None

    def create_dimension(self, nombre):
        dimension = Dimensiones(nombre=nombre)
        self.dimensiones_model.save()
        return dimension

    def update_dimension(self, id, nombre):
        dimension = self.dimensiones_model.get_dimension_by_id(id)
        if dimension:
            dimension.nombre = nombre
            dimension.save()
            return dimension
        return None

    def delete_dimension(self, id):
        dimension = self.dimensiones_model.get_dimension_by_id(id)
        if not dimension:
            return False
        dimension.delete()
        return True
    
    def get_by_filter(self, q_filters):
        return self.dimensiones_model.objects.filter(q_filters)
