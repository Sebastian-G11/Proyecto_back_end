from django.urls import path
from .views import display_dashboard

urlpatterns = [
  path('', display_dashboard, name='dashboard')
]
