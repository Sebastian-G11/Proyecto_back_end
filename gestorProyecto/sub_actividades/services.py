from .repositorio.repository import SubActividadRepository
from .validations import validar_grado_aprobacion, validar_nombre_unico

class SubActividadService:
    @staticmethod
    def crear_sub_actividad(actividad, nombre, grado_aprobacion):
        validar_grado_aprobacion(grado_aprobacion)
        validar_nombre_unico(nombre, actividad)
        
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
        validar_grado_aprobacion(grado_aprobacion)
        validar_nombre_unico(nombre, actividad)
        
        repository = SubActividadRepository()
        return repository.actualizar_sub_actividad(id, actividad, nombre, grado_aprobacion)

    @staticmethod
    def eliminar_sub_actividad(id):
        repository = SubActividadRepository()
        return repository.eliminar_sub_actividad(id)
