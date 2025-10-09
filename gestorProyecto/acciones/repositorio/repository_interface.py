from abc import ABC, abstractmethod

class AccionesRepositoryI(ABC):
    @abstractmethod
    def get_acciones(self):
        pass

    @abstractmethod
    def create_accion(self, data):
        pass

    @abstractmethod
    def update_accion(self, id, data) -> bool:
        pass

    @abstractmethod
    def delete_accion(self, id) -> bool:
        pass
