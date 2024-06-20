from django.http import JsonResponse
from rest_framework import viewsets
from .models import Direccion, User, Category, Product, Purchase
from .serializers import DireccionSerializer, UserSerializer, CategorySerializer, ProductSerializer, PurchaseSerializer

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

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer