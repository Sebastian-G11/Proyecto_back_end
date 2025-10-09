from .repository_interface import AccionesRepositoryI
from ..models import Accion

class AccionesRepository(AccionesRepositoryI):
    acciones_model = Accion
    def get_acciones(self):
        return self.acciones_model.objects.all()

    def create_accion(self, data):
        return self.acciones_model.objects.create(**data)

    def update_accion(self, id, data):
        return self.acciones_model.objects.filter(accion_id=id).update(**data)

    def delete_accion(self, id):
        return self.acciones_model.objects.filter(accion_id=id).delete()