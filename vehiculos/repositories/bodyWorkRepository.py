from typing import (
  List,
)

from vehiculos.models import (
  BodyWork,
)

#logger = logging.getLogger(__name__)

class BodyWorkRepository:

  def create(self,
    name: str,
    ) -> BodyWork.objects:
      
    return BodyWork.objects.create(
      name = name,
    )
  
  def get_all(self) -> List[BodyWork]:
    return BodyWork.objects.all()
  
  def delete(self, bodyWork: BodyWork):
    bodyWork.delete()

  def get_by_id(self, id: int) -> BodyWork.objects:
    return BodyWork.objects.get(id=id)
  
  def update(self,
            bodyWork: BodyWork,
            nombre: str,) -> BodyWork.objects:
    bodyWork.name = nombre
    bodyWork.save()