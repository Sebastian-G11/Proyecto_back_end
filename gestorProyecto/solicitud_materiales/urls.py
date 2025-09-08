from django.contrib import admin
from django.urls import path
from solicitud_materiales.views import display_solicitud_materiales
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', display_solicitud_materiales)
]