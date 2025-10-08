from abc import ABC, abstractmethod

class DimensionesRepositoryI(ABC):
    @abstractmethod
    def get_dimensiones(self):
        pass

    @abstractmethod
    def create_dimension(self, nombre):
        pass

    @abstractmethod
    def update_dimension(self, id, nombre) -> bool:
        pass

    @abstractmethod
    def delete_dimension(self, id) -> bool:
        pass
