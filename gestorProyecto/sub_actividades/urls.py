from django.contrib import admin
from django.urls import path
from sub_actividades.views import display

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', display)
]