from .repositorio.repository import SubActividadRepository
from .repositorio.repository_interface import SubActividadRepositoryInterface

class SubActividadService:
    def __init__(self, repository: SubActividadRepositoryInterface):
      self.repository = repository

    def crear_sub_actividad(self, actividad, nombre, grado_aprobacion):
        return self.repository.crear_sub_actividad(actividad, nombre, grado_aprobacion)


    def obtener_sub_actividades(self):
        return self.repository.obtener_sub_actividades()


    def obtener_sub_actividad_por_id(self, id):
        return self.repository.obtener_sub_actividad_por_id(id)

    def actualizar_sub_actividad(self, id, actividad, nombre, grado_aprobacion):
        return self.repository.actualizar_sub_actividad(id, actividad, nombre, grado_aprobacion)

    def eliminar_sub_actividad(self, id):
        return self.repository.eliminar_sub_actividad(id)

subactividad_service = SubActividadService(SubActividadRepository())
