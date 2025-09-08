from django.urls import path
from .views import display, logout

urlpatterns = [
    path('', display, name='login'),  # login principal
    path('logout/', logout, name='logout'),
]
