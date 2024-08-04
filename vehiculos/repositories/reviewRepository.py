from typing import (
    List,
)

from vehiculos.models import (
    VehiculoReview,
)

from vehiculos.repositories.vehiculosRepository import CarRepository

from django.contrib.auth.models import User


class ReviewRepository:
    def get_all(self) -> List[VehiculoReview]:
        return VehiculoReview.objects.all()
    
    def get_by_id(self, id) -> VehiculoReview:
        return VehiculoReview.objects.get(id = id)

    def create(self,
               vehiculo_id: int,
               user: User,
               opinion: str,
               rating: int) -> None:
        repoVehiculos = CarRepository()
        vehiculo = repoVehiculos.get_by_id(id=vehiculo_id)
        review = VehiculoReview.objects.create(
            vehiculo = vehiculo,
            author = user,
            text = opinion,
            rating = rating
        )
        return review
    
    def delete(self, review: VehiculoReview):
            review.delete()