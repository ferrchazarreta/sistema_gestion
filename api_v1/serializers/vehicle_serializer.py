from rest_framework import serializers
from vehiculos.models import Country, Modelo, Brand, Fuel, Transmission, Gama, Condition, BodyWork, Car, VehiculoReview

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = ['id', 'name']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']

class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = ['id', 'name']

class TransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmission
        fields = ['id', 'name']

class GamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gama
        fields = ['id', 'name']

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ['id', 'name']

class BodyWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyWork
        fields = ['id', 'name']

class CarSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    model_car = ModeloSerializer()
    fuel_type = FuelSerializer()
    country_production = CountrySerializer()
    transmission = TransmissionSerializer()
    gama = GamaSerializer()
    condition = ConditionSerializer()
    bodyWork = BodyWorkSerializer()

    class Meta:
        model = Car
        fields = [
            'id', 'brand', 'model_car', 'fuel_type', 'country_production', 'transmission', 'gama',
            'condition', 'bodyWork', 'year_production', 'door_quatity', 'cilindrada', 'price',
            'km', 'image'
        ]

class VehiculoReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculoReview
        fields = ['id', 'vehiculo', 'author', 'text', 'date', 'rating']
        read_only_fields = ['id', 'vehiculo', 'author', 'date']
