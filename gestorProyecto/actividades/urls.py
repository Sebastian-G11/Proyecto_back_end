from django.contrib import admin
from django.urls import path
from actividades.views import display_actividades
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', display_actividades)
]