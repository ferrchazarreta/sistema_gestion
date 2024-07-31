from django.db import models

class Country(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return  self.name

class Modelo(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return  self.name

class Brand(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return  self.name

class Fuel(models.Model):
  name = models.CharField(max_length=10)
  
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
    related_name='products',
  )

  country_production = models.ForeignKey(
    Country,
    on_delete=models.CASCADE,
    related_name='countries',
  )
  
  image = models.ImageField(upload_to='vehiculos_images/', null=True, blank=True)

  price = models.IntegerField()

  def __str__(self):
    return  self.brand.name