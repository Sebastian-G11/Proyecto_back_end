from abc import ABC, abstractmethod

class SubActividadRepositoryI(ABC):
    @abstractmethod
    def crear_sub_actividad(self, actividad, nombre, grado_aprobacion):
        pass
    
    @abstractmethod
    def obtener_sub_actividades(self):
        pass

    @abstractmethod
    def obtener_sub_actividad_por_id(self, id):
        pass

    @abstractmethod
    def actualizar_sub_actividad(self, id, actividad, nombre, grado_aprobacion):
        pass

    @abstractmethod
    def eliminar_sub_actividad(self, id):
        pass

    @abstractmethod
    def get_by_filter(self, q_filters):
        pass