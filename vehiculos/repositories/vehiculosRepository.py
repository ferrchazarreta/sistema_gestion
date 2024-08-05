from typing import (
    List,
    Optional,
)

from vehiculos.models import (
  Car,
  Modelo,
  Brand,
  Fuel,
  Country,
  Transmission,
  Condition,
  Gama,
  BodyWork,
)

#logger = logging.getLogger(__name__)

class CarRepository:
  def create(
    self,
    brand: Brand,
    model_car: Modelo,
    year_production: str,
    door_quatity: int,
    cilindrada: int, 
    fuel_type: Fuel,
    country_production: Country,
    transmission:Transmission,
    condition:Condition,
    gama:Gama,
    bodyWork:BodyWork,
    image:  Optional[str] = None,
    price: Optional[int] = None,
    ) -> Car.objects:
    
    return Car.objects.create(
      brand = brand,
      model_car =  model_car,
      year_production = year_production,
      door_quatity = door_quatity,
      cilindrada = cilindrada,
      fuel_type = fuel_type,
      country_production = country_production,
      image = image,
      price = price,
      transmission = transmission,
      condition = condition,
      gama = gama,
      bodyWork = bodyWork,
    )
  
  def update(self,
            vehiculo: Car,
            brand: Brand,
            model_car: Modelo,
            year_production: str,
            door_quatity: int,
            cilindrada: int, 
            fuel_type: Fuel,
            country_production: Country,
            transmission:Transmission,
            condition:Condition,
            gama:Gama,
            bodyWork:BodyWork,
            image: Optional[str] = None,
            price: Optional[int] = None,
            ) -> None:
    if int(price) < 0:
      raise ValueError('El precio no puede ser menor a 0')
    if int(cilindrada) < 0 :
      raise ValueError('La cilindrada no puede ser menor a 0')
    if int(door_quatity) < 0 :
      raise ValueError('La cantidad de puertas no puede ser menor a 0')
    
    vehiculo.brand = brand
    vehiculo.model_car = model_car
    vehiculo.year_production = year_production
    vehiculo.door_quatity = door_quatity
    vehiculo.cilindrada = cilindrada
    vehiculo.fuel_type = fuel_type
    vehiculo.country_production = country_production
    vehiculo.price = price
    vehiculo.transmission =transmission
    vehiculo.condition = condition
    vehiculo.gama = gama
    vehiculo.bodyWork = bodyWork
    # Solo actualiza la imagen si se ha proporcionado una nueva
    if image:
        vehiculo.image = image
        
    vehiculo.save()

  def get_all(self) -> List[Car]:
    return Car.objects.all()
  
  def filter_by_id(self, vehiculo_id,) -> Optional[Car]:
    return Car.objects.filter(id=vehiculo_id).first()
  
  def get_by_id(self, id: int,) -> Optional[Car]:
    try:
      vehiculo = Car.objects.get(id=id)
    except:
      vehiculo = None
    return vehiculo
  
  def get_product_on_price_range(
      self,
      min_price = float,
      max_price = float,
    ) -> List[Car]:
    vehiculo = Car.objects.filter(
      price__range = (min_price, max_price)
    )
    return vehiculo
  
  def filter_by_brand(
    self,
    brand = Brand,
  ) -> List[Car]:
    return Car.objects.filter(brands = brand)

  def delete(self, vehiculo: Car):
      vehiculo.delete()
  