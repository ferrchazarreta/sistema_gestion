from typing import (
  List,
  Optional,
)

from vehiculos.models import (
  Model,
)

#logger = logging.getLogger(__name__)

class ModelsRepository:

  def create(self,
    name: str,
    ) -> Model.objects:
      
    return Model.objects.create(
      name = name,
    )
  
  def get_all(self) -> List[Model]:
    return Model.objects.all()
  
  def delete(self, model: Model):
    model.delete()

  def get_by_id(self, id: int) -> Model.objects:
    return Model.objects.get(id=id)
  
  def update(self,
            model: Model,
            nombre: str,) -> Model.objects:
    model.name = nombre
    model.save()