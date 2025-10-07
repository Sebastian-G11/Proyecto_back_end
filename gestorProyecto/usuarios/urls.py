from django.urls import path
from usuarios.views import display
urlpatterns = [
    path('', display)
]