from typing import (
  List,
)

from vehiculos.models import (
  Condition,
)

class ConditionRepository:

  def create(self,
    name: str,
    ) -> Condition.objects:
      
    return Condition.objects.create(
      name = name,
    )
  
  def get_all(self) -> List[Condition]:
    return Condition.objects.all()
  
  def delete(self, condition: Condition):
    condition.delete()

  def get_by_id(self, id: int) -> Condition.objects:
    return Condition.objects.get(id=id)
  
  def update(self,
            condition: Condition,
            nombre: str,) -> Condition.objects:
    condition.name = nombre
    condition.save()