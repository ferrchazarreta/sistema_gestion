from typing import (
  List,
)

from noticias.models import (
  Category,
)

#logger = logging.getLogger(__name__)

class CategoryRepository:

  def create(self,
    name: str,
    ) -> Category.objects:
      
    return Category.objects.create(
      name = name,
    )
  
  def get_all(self) -> List[Category]:
    return Category.objects.all()
  
  def delete(self, category: Category):
    category.delete()

  def get_by_id(self, id: int) -> Category.objects:
    return Category.objects.get(id=id)
  
  def update(self,
            category: Category,
            nombre: str,) -> Category.objects:
    category.name = nombre
    category.save()