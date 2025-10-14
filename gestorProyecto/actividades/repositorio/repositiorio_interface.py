from abc import ABC, abstractmethod

class ActividadesRepositoryI(ABC):
    @abstractmethod
    def get_actividades(self):
        pass

    @abstractmethod
    def create_actividad(self, data):
        pass

    @abstractmethod
    def update_actividad(self, id, data) -> bool:
        pass

    @abstractmethod
    def delete_actividad(self, id) -> bool:
        pass

    @abstractmethod
    def get_by_filter(self, q_filters):
        pass

class VerificacionesRepositoryI(ABC):
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