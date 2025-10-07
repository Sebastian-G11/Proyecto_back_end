from abc import ABC, abstractmethod

class DimensionRepositoryI(ABC):
    @abstractmethod
    def get_dimensions(self):
        pass
    
    @abstractmethod
    def create_dimensions(self):
        pass
    
    @abstractmethod
    def update_dimensions(self, id) -> bool:
        pass
    
    @abstractmethod
    def delete_dimensions(self, id) -> bool:
        pass