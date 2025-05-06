from django.urls import path
from .views import logo_view

urlpatterns = [
    path('', logo_view, name='logo'),
]
