from django.urls import path
from sub_actividades.views import display_sub_actividades

urlpatterns = [
    path('', display_sub_actividades)
]