"""
URL configuration for gestorProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import autenticacion.urls
import dimensiones.urls
import acciones.urls
import actividades.urls
import sub_actividades.urls
import solicitud_materiales.urls
import usuarios.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(autenticacion.urls)),
    path('dimensiones/', include(dimensiones.urls)),
    path('acciones/', include(acciones.urls)),
    path('actividades/', include(actividades.urls)),
    path('sub_actividades/', include(sub_actividades.urls)),
    path('solicitud_materiales/', include(solicitud_materiales.urls)),
    path('usuarios/', include(usuarios.urls)),
]
