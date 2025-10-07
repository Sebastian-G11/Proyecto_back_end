from abc import ABC, abstractmethod

class SolicitudRepositoryI(ABC):
    @abstractmethod
    def get_solicitudes(self):
        pass
    
    @abstractmethod
    def create_solicitud(self):
        pass
    
    @abstractmethod
    def update_solicitud(self, id) -> bool:
        pass
    
    @abstractmethod
    def delete_solicitud(self, id) -> bool:
        pass