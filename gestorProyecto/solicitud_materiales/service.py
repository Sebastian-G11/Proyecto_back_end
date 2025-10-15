from solicitud_materiales.repositorio.repository_interface import SolicitudRepositoryI
from solicitud_materiales.repositorio.repository import SolicitudRepository
from django.db.models import Q

class SolicitudService:
   def __init__(self, repository: SolicitudRepositoryI):
      self.repository = repository

   def get_by_id(self, id):
       return self.repository.get_by_id(id)

   def get_solicitudes(self):
       return self.repository.get_solicitudes()
   
   def create_solicitud(self, data):
       return self.repository.create_solicitud(data)
   
   def update_solicitud(self, id, data):
       return self.repository.update_solicitud(id, data)
   
   def delete_solicitud(self, id):
       return self.repository.delete_solicitud(id)
   
   def get_by_filter(self, search_query):
       q_filters = Q(materiales_solicitados__icontains=search_query) | Q(valor_esperado__icontains=search_query)
       return self.repository.get_by_filter(q_filters)


solicitud_service = SolicitudService(SolicitudRepository())