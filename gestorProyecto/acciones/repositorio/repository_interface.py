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

    @abstractmethod
    def get_by_filter(self, q_filters):
        pass


class VerificacionRepositoryI(ABC):
    @abstractmethod
    def get_verificaciones(self):
        pass

    @abstractmethod
    def create_verificacion(self, data):
        pass

    @abstractmethod
    def update_verificacion(self, id, data) -> bool:
        pass

    @abstractmethod
    def delete_verificacion(self, id) -> bool:
        pass