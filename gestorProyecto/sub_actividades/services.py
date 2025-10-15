from .repositorio.repository import SubActividadRepository
from .repositorio.repository_interface import SubActividadRepositoryI
from django.db.models import Q


class SubActividadService:

    def __init__(self, repository: SubActividadRepositoryI):
        self.repository = repository
        pass

    def crear_sub_actividad(self ,actividad, nombre, grado_aprobacion):
         
        return self.repository.crear_sub_actividad(actividad, nombre, grado_aprobacion)


    def obtener_sub_actividades(self):
        return self.repository.obtener_sub_actividades()
    @staticmethod
    def eliminar_sub_actividad(id):
        repository = SubActividadRepository()
        return repository.eliminar_sub_actividad(id)
    
    @staticmethod
    def get_by_filter(search_query):
        q_filters = Q(nombre__icontains=search_query) | Q()
        repository = SubActividadRepository()
        return repository.get_by_filter(q_filters)


    def obtener_sub_actividad_por_id(self, id):
        return self.repository.obtener_sub_actividad_por_id(id)


    def actualizar_sub_actividad(self, id, actividad, nombre, grado_aprobacion):
        return self.repository.actualizar_sub_actividad(id, actividad, nombre, grado_aprobacion)


    def eliminar_sub_actividad(self, id):
        return self.repository.eliminar_sub_actividad(id)

subactividad_service = SubActividadService(SubActividadRepository())
