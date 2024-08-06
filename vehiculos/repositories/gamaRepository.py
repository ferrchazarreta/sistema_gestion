from typing import (
  List,
)

from vehiculos.models import (
  Gama,
)

class GamaRepository:

  def create(self,
    name: str,
    ) -> Gama.objects:
      
    return Gama.objects.create(
      name = name,
    )
  
  def get_all(self) -> List[Gama]:
    return Gama.objects.all()
  
  def delete(self, gama: Gama):
    gama.delete()

  def get_by_id(self, id: int) -> Gama.objects:
    return Gama.objects.get(id=id)
  
  def update(self,
            gama: Gama,
            nombre: str,) -> Gama.objects:
    gama.name = nombre
    gama.save()