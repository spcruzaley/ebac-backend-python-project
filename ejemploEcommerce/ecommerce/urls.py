from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import DireccionViewSet, UserViewSet, CategoryViewSet

router = DefaultRouter()
router.register('direcciones', DireccionViewSet)
router.register('users', UserViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('hola/', views.vista_hola_mundo, name='vista_hola_mundo'),
    path('', include(router.urls)),
]
