from django.contrib import admin
from django.urls import path
from  autenticacion.views import display
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', display)
]