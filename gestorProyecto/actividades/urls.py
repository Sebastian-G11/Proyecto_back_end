from django.contrib import admin
from django.urls import path
from actividades.views import prueba2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', prueba2)
]