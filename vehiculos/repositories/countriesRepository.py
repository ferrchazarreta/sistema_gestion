from typing import (
  List,
  Optional,
)

from vehiculos.models import (
  Country,
)

#logger = logging.getLogger(__name__)

class CountriesRepository:

  def create(self,
    name: str,
    ) -> Country.objects:
      
    return Country.objects.create(
      name = name,
    )
  
  def get_all(self) -> List[Country]:
    return Country.objects.all()
  
  def delete(self, country: Country):
    country.delete()

  def get_by_id(self, id: int) -> Country.objects:
    return Country.objects.get(id=id)
  
  def update(self,
            country: Country,
            nombre: str,) -> Country.objects:
    country.name = nombre
    country.save()