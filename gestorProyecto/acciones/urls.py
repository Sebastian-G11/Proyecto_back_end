from django.urls import path
from .views import display_acciones
from autenticacion.views import login_required_simulado

urlpatterns = [
    path('', login_required_simulado(display_acciones), name='acciones'),  # protegida
]
