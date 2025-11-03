from abc import ABC, abstractmethod

class UsersRepositoryI(ABC):
    @abstractmethod
    def get_users(self):
        pass

    @abstractmethod
    def get_user_by_email(self, email):
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

    @abstractmethod
    def get_by_filter(self, q_filters):
        pass   