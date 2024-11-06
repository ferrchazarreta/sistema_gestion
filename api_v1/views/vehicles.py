from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from vehiculos.models import (
    Country, Modelo, Brand, Fuel, Transmission, Gama, Condition, BodyWork, Car, VehiculoReview
)

from api_v1.serializers.vehicle_serializer import (
    CountrySerializer, ModeloSerializer, BrandSerializer, FuelSerializer,
    TransmissionSerializer, GamaSerializer, ConditionSerializer, BodyWorkSerializer,
    CarSerializer, VehiculoReviewSerializer
)

def get_or_create_related_model(Model, data):
    if data:
        instance, _ = Model.objects.get_or_create(name=data.get('name'))
        return instance
    return None

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAdminUser]

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
    permission_classes = [permissions.IsAdminUser]

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAdminUser]

class FuelViewSet(viewsets.ModelViewSet):
    queryset = Fuel.objects.all()
    serializer_class = FuelSerializer
    permission_classes = [permissions.IsAdminUser]

class TransmissionViewSet(viewsets.ModelViewSet):
    queryset = Transmission.objects.all()
    serializer_class = TransmissionSerializer
    permission_classes = [permissions.IsAdminUser]

class GamaViewSet(viewsets.ModelViewSet):
    queryset = Gama.objects.all()
    serializer_class = GamaSerializer
    permission_classes = [permissions.IsAdminUser]

class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    permission_classes = [permissions.IsAdminUser]

class BodyWorkViewSet(viewsets.ModelViewSet):
    queryset = BodyWork.objects.all()
    serializer_class = BodyWorkSerializer
    permission_classes = [permissions.IsAdminUser]

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAdminUser]

    def create(self, request, *args, **kwargs):
        data = request.data

        brand = get_or_create_related_model(Brand, data.get('brand'))
        model = get_or_create_related_model(Modelo, data.get('model_car'))
        country = get_or_create_related_model(Country, data.get('country_production'))
        fuel = get_or_create_related_model(Fuel, data.get('fuel_type'))
        transmission = get_or_create_related_model(Transmission, data.get('transmission'))
        gama = get_or_create_related_model(Gama, data.get('gama'))
        condition = get_or_create_related_model(Condition, data.get('condition'))
        bodyWork = get_or_create_related_model(BodyWork, data.get('bodyWork'))

        vehicle = Car.objects.create(
            brand=brand,
            model_car=model,
            country_production=country,
            fuel_type=fuel,
            transmission=transmission,
            gama=gama,
            condition=condition,
            bodyWork=bodyWork,
            year_production=data.get('year_production'),
            door_quatity=data.get('door_quatity'),
            cilindrada=data.get('cilindrada'),
            image=data.get('image'),
            price=data.get('price'),
            km=data.get('km')
        )

        serializer = self.serializer_class(vehicle)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class VehiculoReviewViewSet(viewsets.ModelViewSet):
    queryset = VehiculoReview.objects.all()
    serializer_class = VehiculoReviewSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        vehiculo_id = self.kwargs.get("vehiculo_id")
        return VehiculoReview.objects.filter(vehiculo_id=vehiculo_id)


