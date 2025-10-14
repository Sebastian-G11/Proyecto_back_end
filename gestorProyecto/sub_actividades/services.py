from .repositorio.repository import SubActividadRepository
from django.db.models import Q


class SubActividadService:
    @staticmethod
    def crear_sub_actividad(actividad, nombre, grado_aprobacion):
        repository = SubActividadRepository()
        return repository.crear_sub_actividad(actividad, nombre, grado_aprobacion)

    @staticmethod
    def obtener_sub_actividades():
        repository = SubActividadRepository()
        return repository.obtener_sub_actividades()

    @staticmethod
    def obtener_sub_actividad_por_id(id):
        repository = SubActividadRepository()
        return repository.obtener_sub_actividad_por_id(id)

    @staticmethod
    def actualizar_sub_actividad(id, actividad, nombre, grado_aprobacion):
        repository = SubActividadRepository()
        return repository.actualizar_sub_actividad(id, actividad, nombre, grado_aprobacion)

    @staticmethod
    def eliminar_sub_actividad(id):
        repository = SubActividadRepository()
        return repository.eliminar_sub_actividad(id)
    
    @staticmethod
    def get_by_filter(search_query):
        q_filters = Q(nombre__icontains=search_query) | Q()
        repository = SubActividadRepository()
        return repository.get_by_filter(q_filters)

subactividad_service = SubActividadService()
