from django.contrib import admin
from django.urls import path
from sub_actividades.views import display_sub_actividades

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', display_sub_actividades)
]