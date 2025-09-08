from django.contrib import admin
from django.urls import path
from dimensiones.views import display_dimensiones
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', display_dimensiones)
]