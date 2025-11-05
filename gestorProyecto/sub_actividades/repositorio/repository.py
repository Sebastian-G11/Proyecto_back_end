from .repository_interface import SubActividadRepositoryI
from sub_actividades.models import SubActividad


class SubActividadRepository(SubActividadRepositoryI):
    sub_actividades_model = SubActividad

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


    def actualizar_sub_actividad(self, id, **data):
        return self.sub_actividades_model.objects.filter(sub_actividad_id=id).update(**data)
    
    def eliminar_sub_actividad(self, id):
        return self.sub_actividades_model.objects.filter(sub_actividad_id=id).delete()

    def get_by_filter(self, q_filters):
        return self.sub_actividades_model.objects.filter(q_filters)
    

