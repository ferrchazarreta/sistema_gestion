from typing import (
  List,
  Optional,
)

from vehiculos.models import (
  Modelo,
)

#logger = logging.getLogger(__name__)

class ModelsRepository:

  def create(self,
    name: str,
    ) -> Modelo.objects:
      
    return Modelo.objects.create(
      name = name,
    )
  
  def get_all(self) -> List[Modelo]:
    return Modelo.objects.all()
  
  def delete(self, model: Modelo):
    model.delete()

  def get_by_id(self, id: int) -> Modelo.objects:
    return Modelo.objects.get(id=id)
  
  def update(self,
            model: Modelo,
            nombre: str,) -> Modelo.objects:
    model.name = nombre
    model.save()