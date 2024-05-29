from django.urls import path
from . import views

urlpatterns = [
    path('hola/', views.vista_hola_mundo, name='vista_hola_mundo'),
]
