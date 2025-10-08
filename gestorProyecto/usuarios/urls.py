from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.display, name='listado_usuarios'),
    path('agregar/', views.agregar_usuario, name='agregar_usuario'),  
    path('eliminar/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'), 
    path('actualizar/<int:id>/', views.actualizar_usuario, name='actualizar_usuario'), 
]
