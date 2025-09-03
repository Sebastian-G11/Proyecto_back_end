from django.contrib import admin
from django.urls import path
from acciones.views import display
urlpatterns = [
    path('admin/', admin.site.urls),
    path('prueba1/', display),
]