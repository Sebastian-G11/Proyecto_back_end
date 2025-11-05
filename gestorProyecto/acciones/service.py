from .repositorio.repository_interface import AccionesRepositoryI, VerificacionRepositoryI
from .repositorio.repository import AccionesRepository, VerificacionRepository
from django.db.models import Q

class AccionesService:
    def __init__(self, repository: AccionesRepositoryI):
        self.repository = repository

    def get_all_acciones(self):
        return self.repository.get_acciones()

    def create_accion(self, request, data):
        user = request.session.get("user")
        if user: 
            data['responsable_id'] = user['usuario_id']
            return self.repository.create_accion(**data)

    def update_accion(self, id, data):
        return self.repository.update_accion(id, **data)

    def delete_accion(self, id):
        return self.repository.delete_accion(id)
    
    def get_by_filter(self, search_query):
        q_filter = Q(nombre__icontains=search_query) | Q(descripcion__icontains=search_query)
        return self.repository.get_by_filter(q_filter)


class VerificacionService:
    def __init__(self, repository: VerificacionRepositoryI):
        self.repository = repository

    def get_verificaciones(self):
        return self.repository.get_verificaciones()

    def create_verificacion(self, accion_id, **data):
        data['accion_id'] = accion_id
        return self.repository.create_verificacion(**data)

    def update_verificacion(self, id, data):
        return self.repository.update_verificacion(id, data)

    def delete_verificacion(self, id):
        return self.repository.delete_verificacion(id)


acciones_service = AccionesService(AccionesRepository())
verificacion_service = VerificacionService(VerificacionRepository())