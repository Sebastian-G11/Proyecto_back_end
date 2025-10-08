from django.urls import path
from .views import lista_dimensiones, agregar_dimension, eliminar_dimension, editar_dimension

app_name = 'dimensiones'

urlpatterns = [
    path('', lista_dimensiones, name='listado_dimensiones'),
    path('agregar/', agregar_dimension, name='agregar_dimension'),
    path('eliminar/<int:id>/', eliminar_dimension, name='eliminar_dimension'),
    path('editar/<int:id>/', editar_dimension, name='editar_dimension'),
]
