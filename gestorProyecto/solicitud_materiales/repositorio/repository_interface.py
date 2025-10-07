from abc import ABC, abstractmethod

class SolicitudRepositoryI(ABC):
    
    @abstractmethod
    def get_solicitudes(self):
        pass
    
    @abstractmethod
    def create_solicitud(self, data):
        pass
    
    @abstractmethod
    def update_solicitud(self, id, data) -> bool:
        pass
    
    @abstractmethod
    def delete_solicitud(self, id) -> bool:
        pass