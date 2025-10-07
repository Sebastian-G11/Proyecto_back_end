from django.urls import path
from .views import display_actividades
from autenticacion.views import login_required_simulado
urlpatterns = [
    path('', display_actividades, name='actividades')
]