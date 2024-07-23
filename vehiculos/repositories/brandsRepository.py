from typing import (
  List,
  Optional,
)

from vehiculos.models import (
  Brand,
)

#logger = logging.getLogger(__name__)

class BrandsRepository:

  def create(self,
    name: str,
    ) -> Brand.objects:
      
    return Brand.objects.create(
      name = name,
    )
  
  def get_all(self) -> List[Brand]:
    return Brand.objects.all()
  
  def delete(self, brand: Brand):
    brand.delete()

  def get_by_id(self, id: int) -> Brand.objects:
    return Brand.objects.get(id=id)
  
  def update(self,
            brand: Brand,
            nombre: str,) -> Brand.objects:
    brand.name = nombre
    brand.save()