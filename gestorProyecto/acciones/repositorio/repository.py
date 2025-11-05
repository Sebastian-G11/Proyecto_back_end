from .repository_interface import AccionesRepositoryI, VerificacionRepositoryI
from ..models import Accion, VerificacionAccion

class AccionesRepository(AccionesRepositoryI):
    acciones_model = Accion

    def get_acciones(self):
         return self.acciones_model.objects.select_related(
            'dimension', 
            'responsable', 
            'estado'
        ).prefetch_related(
            'verificaciones' 
        ).all()
    
    def create_accion(self, **data):
        return self.acciones_model.objects.create(**data)

    def update_accion(self, id, **data):
        return self.acciones_model.objects.filter(accion_id=id).update(**data)

    def delete_accion(self, id):
        return self.acciones_model.objects.filter(accion_id=id).delete()
    
    def get_by_filter(self, q_filter):
        return self.acciones_model.objects.select_related(
            'dimension', 
            'responsable', 
            'estado'
        ).prefetch_related(
            'verificaciones'  
        ).all().filter(q_filter)

class VerificacionRepository(VerificacionRepositoryI):
    verificaciones_model = VerificacionAccion

    def get_verificaciones(self):
        return self.verificaciones_model.objects.all()

    def create_verificacion(self, **data):
        return self.verificaciones_model.objects.create(**data)

    def update_verificacion(self, id, data):
        return self.verificaciones_model.objects.filter(verificacion_id=id).update(**data)

    def delete_verificacion(self, id):
        return self.verificaciones_model.objects.filter(verificacion_id=id).delete()