from abc import ABC, abstractmethod

class UsersRepositoryI(ABC):
    @abstractmethod
    def get_users(self):
        pass
    
    @abstractmethod
    def create_users(self, nombre, apellido, email, rol='Usuario'):
        pass
    
    @abstractmethod
    def update_users(self, id, nombre, apellido, email, rol) -> bool:
        pass
    
    @abstractmethod
    def delete_users(self, id) -> bool:
        pass
