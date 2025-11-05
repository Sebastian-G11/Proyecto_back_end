from solicitud_materiales.repositorio.repository_interface import SolicitudRepositoryI
from solicitud_materiales.models import SolicitudMaterial

class SolicitudRepository(SolicitudRepositoryI):
    solicitudes_model = SolicitudMaterial

    def create_solicitud(self, data):
        return self.solicitudes_model.objects.create(**data)
    
    def get_solicitudes(self):
        return self.solicitudes_model.objects.select_related('actividad').all()

    def update_solicitud(self, id, data):
        return self.solicitudes_model.objects.filter(solicitud_id=id).update(**data)

    def delete_solicitud(self, id):
        return self.solicitudes_model.objects.filter(solicitud_id=id).delete()
    
    def get_by_filter(self, q_filters):
        return self.solicitudes_model.objects.select_related('actividad').all().filter(**q_filters)