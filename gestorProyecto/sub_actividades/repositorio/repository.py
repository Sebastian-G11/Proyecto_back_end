from .repository_interface import SubActividadRepositoryInterface
from sub_actividades.models import SubActividad

class SubActividadRepository(SubActividadRepositoryInterface):
    def crear_sub_actividad(self, actividad, nombre, grado_aprobacion):
        sub_actividad = SubActividad(
            actividad=actividad,
            nombre=nombre,
            grado_aprobacion=grado_aprobacion
        )
        sub_actividad.save()
        return sub_actividad

    def obtener_sub_actividades(self):
        return SubActividad.objects.all()

    def obtener_sub_actividad_por_id(self, id):
        return SubActividad.objects.get(id=id)

    def actualizar_sub_actividad(self, id, actividad, nombre, grado_aprobacion):
        sub_actividad = self.obtener_sub_actividad_por_id(id)
        sub_actividad.actividad = actividad
        sub_actividad.nombre = nombre
        sub_actividad.grado_aprobacion = grado_aprobacion
        sub_actividad.save()
        return sub_actividad

    def eliminar_sub_actividad(self, id):
        sub_actividad = self.obtener_sub_actividad_por_id(id)
        sub_actividad.delete()