from django.urls import path
from solicitud_materiales.views import display_solicitud_materiales
urlpatterns = [
    path('', display_solicitud_materiales)
]