from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

class Country(models.Model):
  name = models.CharField(max_length=10)
  
  def __str__(self):
    return  self.name

class Model(models.Model):
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
    on_delete=models.SET_NULL,
    related_name='brands',
  )

  model_car = models.ForeignKey(
    Model,
    on_delete=models.SET_NULL,
    related_name='models',
  )

  year_production = models.TextField(
    max_digits=4
  )

  door_quatity = models.IntegerField(
    max_digits=1
  )

  cilindrada = models.IntegerField(
    max_digits=2
  )

  fuel_type = models.ForeignKey(
    Fuel,
    on_delete=models.SET_NULL,
    related_name='products',
  )

  country_production = models.ForeignKey(
    Country,
    on_delete=models.SET_NULL,
    related_name='countries',
  )
  
  image = models.ImageField(upload_to='vehiculos_images/', null=True)

  price = models.IntegerField(
    max_digits=50
  )

  def __str__(self):
    return  self.brand