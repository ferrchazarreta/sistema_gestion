from typing import (
  List,
  Optional,
)

from vehiculos.models import (
  Fuel,
)

#logger = logging.getLogger(__name__)

class FuelRepository:

  def create(self,
    name: str,
    ) -> Fuel.objects:
      
    return Fuel.objects.create(
      name = name,
    )
  
  def get_all(self) -> List[Fuel]:
    return Fuel.objects.all()
  
  def delete(self, fuel: Fuel):
    fuel.delete()

  def get_by_id(self, id: int) -> Fuel.objects:
    return Fuel.objects.get(id=id)
  
  def update(self,
            fuel: Fuel,
            nombre: str,) -> Fuel.objects:
    fuel.name = nombre
    fuel.save()