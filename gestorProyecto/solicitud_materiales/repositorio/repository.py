from solicitud_materiales.repositorio.repository_interface import SolicitudRepositoryI
from solicitud_materiales.models import SolicitudMaterial

class SolicitudRepository(SolicitudRepositoryI):
    solicitudes_model = SolicitudMaterial

    def create_solicitud(self, data):
        return self.solicitudes_model.objects.create(**data)
    
    def get_solicitudes(self):
        return self.solicitudes_model.objects.all()
    
    def update_solicitud(self, id):
        return super().update_solicitud(id)

    def delete_solicitud(self, id):
        return super().delete_solicitud(id)