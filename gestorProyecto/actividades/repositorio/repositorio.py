from .repositiorio_interface import ActividadesRepositoryI, VerificacionesRepositoryI
from ..models import Actividad, VerificacionActividad

class ActividadesRepository(ActividadesRepositoryI):
    actividades_model = Actividad

    def get_actividades(self):
        return self.actividades_model.objects.all()

    def create_actividad(self, data):
        return self.actividades_model.objects.create(**data)

    def update_actividad(self, id, data) -> bool:
        return self.actividades_model.objects.filter(actividad_id=id).update(**data)

    def delete_actividad(self, id) -> bool:
        return self.actividades_model.objects.filter(actividad_id=id).delete()
    
    def get_by_filter(self, q_filters):
        return self.actividades_model.objects.filter(q_filters)

class VerificacionesRepository(VerificacionesRepositoryI):
    verificaciones_model = VerificacionActividad

    def get_verificaciones(self):
        return self.verificaciones_model.objects.all()

    def create_verificacion(self, data):
        return self.verificaciones_model.objects.create(**data)

    def update_verificacion(self, id, data) -> bool:
        return self.verificaciones_model.objects.filter(verificacion_id=id).update(**data)

    def delete_verificacion(self, id) -> bool:
        return self.verificaciones_model.objects.filter(verificacion_id=id).delete()