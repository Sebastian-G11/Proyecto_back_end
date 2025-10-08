from django.urls import path
from .views import listar_subactividades,agregar_subactividad,editar_subactividad,eliminar_subactividad

app_name = 'subactividades'

urlpatterns = [
    path('', listar_subactividades, name='listar_subactividades'),
    path('agregar/', agregar_subactividad, name='agregar_subactividad'),
    path('editar/<int:id>/', editar_subactividad, name='editar_subactividad'),
    path('eliminar/<int:id>/', eliminar_subactividad, name='eliminar_subactividad'),
]