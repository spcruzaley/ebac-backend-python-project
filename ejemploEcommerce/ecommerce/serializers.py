# myapp/serializers.py
from rest_framework import serializers
from .models import Direccion, User, Category, Product

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'