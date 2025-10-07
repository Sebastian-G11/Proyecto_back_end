from django.urls import path
from dimensiones.views import display_dimensiones
urlpatterns = [
    path('', display_dimensiones)
]