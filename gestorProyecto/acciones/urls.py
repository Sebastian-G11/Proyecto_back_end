from django.urls import path
from acciones.views import display_acciones


urlpatterns = [
    path('', display_acciones)
]
