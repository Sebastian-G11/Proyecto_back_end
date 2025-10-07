from django.urls import path
from solicitud_materiales.views import crear_solicitud, display_solicitud_materiales, editar_solicitud

urlpatterns = [
    path('', display_solicitud_materiales),
    path('crear-solicitud/', crear_solicitud, name='crear_solicitud'),
    path('editar-solicitud/<int:id>', editar_solicitud, name='editar_solicitud'),
]