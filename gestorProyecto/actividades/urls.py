from django.urls import path
from .views import display_actividades, display_crear_actividad, display_editar_actividad, eliminar_actividad, display_crear_verificacion, display_editar_verificacion, eliminar_verificacion

urlpatterns = [
    path('', display_actividades, name='actividades'),
    path('crear-actividad/', display_crear_actividad, name='crear_actividad'),
    path('editar-actividad/<int:id>/', display_editar_actividad, name='editar_actividad'),  
    path('eliminar-actividad/<int:id>/', eliminar_actividad, name='eliminar_actividad'),
    path('crear-verificacion/<int:id>', display_crear_verificacion, name='crear_verificacion'),
    path('editar-verificacion/<int:id>/', display_editar_verificacion, name='editar_verificacion'),
    path('eliminar-verificacion/<int:id>/', eliminar_verificacion, name='eliminar_verificacion')
]