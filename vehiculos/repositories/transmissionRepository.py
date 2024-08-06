from typing import (
  List,
)

from vehiculos.models import (
  Transmission,
)


class TransmissionRepository:

  def create(self,
    name: str,
    ) -> Transmission.objects:
      
    return Transmission.objects.create(
      name = name,
    )
  
  def get_all(self) -> List[Transmission]:
    return Transmission.objects.all()
  
  def delete(self, transmission: Transmission):
    transmission.delete()

  def get_by_id(self, id: int) -> Transmission.objects:
    return Transmission.objects.get(id=id)
  
  def update(self,
            transmission: Transmission,
            nombre: str,) -> Transmission.objects:
    transmission.name = nombre
    transmission.save()