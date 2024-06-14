from django.http import JsonResponse
from rest_framework import viewsets
from .models import Direccion, User
from .serializers import DireccionSerializer, UserSerializer

def vista_hola_mundo(request):
    data = {
        "message": "Hola, Mundo !!!"
    }
    return JsonResponse(data)

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer