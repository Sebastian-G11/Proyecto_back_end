from solicitud_materiales.repositorio.repository_interface import SolicitudRepositoryI
from solicitud_materiales.repositorio.repository import SolicitudRepository
from solicitud_materiales.validations import validate_materiales

class SolicitudService:
   def __init__(self, repository: SolicitudRepositoryI):
      self.repository = repository

   def get_solicitudes(self):
       return self.repository.get_solicitudes()
   
   def create_solicitud(self, data):
       return self.repository.create_solicitud(data)


solicitud_service = SolicitudService(SolicitudRepository())