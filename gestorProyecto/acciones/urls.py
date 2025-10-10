from django.urls import path
from acciones.views import delete_accion, display_acciones, display_create_accion, display_edit_accion, display_create_verificacion, display_edit_verificacion, eliminar_verificacion


urlpatterns = [
    path('', display_acciones),
    path('crear-accion/', display_create_accion, name='crear_accion'),
    path('editar-accion/<int:id>/', display_edit_accion, name='editar_accion'),
    path('eliminar-accion/<int:id>/', delete_accion, name='eliminar_accion'),
    path('crear-verificacion/', display_create_verificacion, name='crear_verificacion'),
    path('editar-verificacion/<int:id>/', display_edit_verificacion, name='editar_verificacion'),
    path('eliminar-verificacion/<int:id>/', eliminar_verificacion, name='eliminar_verificacion'),
]
