from rest_framework import serializers
from core.models import Stores
from core.models import Brands
from core.models import Deals

class HelloSerializer(serializers.Serializer):
    """Serializa un campo para probar nuetro APIView"""
    name = serializers.CharField(max_length=15)

class TiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stores
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = '__all__'

class DealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deals
        fields = '__all__'
