from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return  self.name

class Modelo(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return  self.name

class Brand(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return  self.name

class Fuel(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return  self.name

class Transmission(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return  self.name

class Gama(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return  self.name

class Condition(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return  self.name

class BodyWork(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return  self.name


# Create your models here.
class Car(models.Model):

  brand = models.ForeignKey(
    Brand,
    on_delete=models.CASCADE,
    related_name='brands',
  )

  model_car = models.ForeignKey(
    Modelo,
    on_delete=models.CASCADE,
    related_name='model_car',
  )

  year_production = models.CharField(max_length=4)

  door_quatity = models.IntegerField()

  cilindrada = models.IntegerField()

  fuel_type = models.ForeignKey(
    Fuel,
    on_delete=models.CASCADE,
    related_name='fuels',
  )

  country_production = models.ForeignKey(
    Country,
    on_delete=models.CASCADE,
    related_name='countries',
  )

  image = models.ImageField(upload_to='vehiculos_images/', null=True, blank=True)

  price = models.IntegerField()

  km = models.CharField(max_length=200, default=0)

  transmission= models.ForeignKey(
    Transmission,
    on_delete=models.CASCADE,
    related_name='transmission',
  )

  gama = models.ForeignKey(
    Gama,
    on_delete=models.CASCADE,
    related_name='gama',
  )

  condition = models.ForeignKey(
    Condition,
    on_delete=models.CASCADE,
    related_name='condition',
  )

  bodyWork = models.ForeignKey(
    BodyWork,
    on_delete=models.CASCADE,
    related_name='bodyWork',
  )

  def __str__(self):
    return  self.brand.name

  def info_car(self):
    return f"{self.brand} {self.model_car}, Año {self.year_production}"

#TESTIMONIOS
class VehiculoReview(models.Model):
  vehiculo = models.ForeignKey(
      Car,
      on_delete=models.CASCADE,
      related_name='reviews',
  )
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  text = models.TextField()
  date = models.DateField(auto_now_add=True)
  rating = models.IntegerField()
  def __str__(self):
      return f'Review by {self.author.username} for {self.vehiculo.brand.name}'
