from django.http import JsonResponse
from rest_framework import viewsets
from .models import Direccion
from .serializers import DireccionSerializer

def vista_hola_mundo(request):
    data = {
        "message": "Hola, Mundo !!!"
    }
    return JsonResponse(data)

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer