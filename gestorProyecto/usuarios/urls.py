from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.display, name='listado_usuarios'),  # Página principal que lista los usuarios
    path('agregar/', views.agregar_usuario, name='agregar_usuario'),  # Agregar usuario
    path('eliminar/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),  # Eliminar usuario
    path('actualizar/<int:id>/', views.actualizar_usuario, name='actualizar_usuario'),  # Editar usuario
]
