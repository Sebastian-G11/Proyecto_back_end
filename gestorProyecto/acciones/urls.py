from django.urls import path
from acciones.views import delete_accion, display_acciones, display_create_accion, display_edit_accion


urlpatterns = [
    path('', display_acciones),
    path('crear-accion/', display_create_accion, name='crear_accion'),
    path('editar-accion/<int:id>/', display_edit_accion, name='editar_accion'),
    path('eliminar-accion/<int:id>/', delete_accion, name='eliminar_accion'),
]
