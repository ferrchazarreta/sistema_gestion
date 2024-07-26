from django.views import View
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from vehiculos.forms import CarForm
from vehiculos.repositories.vehiculosRepository import CarRepository
from vehiculos.repositories.brandsRepository import BrandsRepository
from vehiculos.repositories.fuelRepository import FuelRepository
from vehiculos.repositories.countriesRepository import CountriesRepository
from vehiculos.repositories.modelsRepository import ModelsRepository

class CarView(View):
  def get(self, request):
    repo = CarRepository()
    vehiculos = repo.get_all()

    return render(
      request,
      'vehiculos/list.html',
      {
        'cars': vehiculos
      }
      )

class CarCreate(View):
  def get(self, request):
    if request.user.is_staff:
      form = CarForm()
      brandsRepo = BrandsRepository()
      fuelRepo = FuelRepository()
      countryRepo = CountriesRepository()
      modelRepo = ModelsRepository()

      marcas = brandsRepo.get_all()
      combustibles = fuelRepo.get_all()
      paises = countryRepo.get_all()
      modelos = modelRepo.get_all()

      return render(
        request,
        'vehiculos/create.html',
        {
          'form': form,
          'brands': marcas,
          'fuels': combustibles,
          'countries': paises,
          'models': modelos,
        }
      )
    else:
      return redirect('vehiculo_list')
    
  def post(self, request):
    if request.user.is_staff:
      carRepo = CarRepository()
      brandsRepo = BrandsRepository()
      fuelRepo = FuelRepository()
      countryRepo = CountriesRepository()
      modelRepo = ModelsRepository()
      data = request.POST

      brandId = data.get('brand')
      brand = brandsRepo.get_by_id(id=brandId)
      fuelId = data.get('fuel_type')
      fuel = fuelRepo.get_by_id(id=fuelId)
      countryId = data.get('country')
      country = countryRepo.get_by_id(id=countryId)
      modelId = data.get('model_car')
      model = modelRepo.get_by_id(id=modelId)
      door_quatity = data.get('door_quatity'),
      year_production = data.get('year_production'),
      cilindrada = data.get('cilindrada'),
      image = data.get('image'),
      price = data.get('price')


      newCar = carRepo.create(
        brand=brand,
        model_car=model,
        year_production=year_production,
        door_quatity=door_quatity,
        cilindrada=cilindrada,
        fuel_type=fuel,
        country_production=country,
        image=image,
        price=price
      )
      
      return redirect('vehiculo_list')
    else:
      return redirect('vehiculo_list')

# class ProductDetail(View):
#     def get(self, request, id):
#         repo = ProductosRepository()
#         producto = repo.get_by_id(id=id)
#         try:
#             imagen = ProductImage.objects.get(product=producto)
#         except:
#             imagen = None

#         return render(
#             request,
#             'product/detail.html',
#             {
#                 'product': producto,
#                 'image': imagen,
#             }
#         )

class CarDelete(View):
    def get(self, request, id):
        if request.user.is_staff:
            repo = CarRepository()
            vehiculo = repo.get_by_id(id=id)
            repo.delete(vehiculo=vehiculo)
        return redirect('vehiculo_list')

class CarUpdate(View):
  def get(self, request, id):
    if request.user.is_staff:
      carRepo = CarRepository()
      brandsRepo = BrandsRepository()
      fuelRepo = FuelRepository()
      countryRepo = CountriesRepository()
      modelRepo = ModelsRepository()


      vehiculo = carRepo.get_by_id(id)
      marcas = brandsRepo.get_all()
      combustibles = fuelRepo.get_all()
      paises = countryRepo.get_all()
      modelos = modelRepo.get_all()

      return render(
        request,
        'vehiculos/update.html',
        {
          'car': vehiculo,
          'brands': marcas,
          'fuels': combustibles,
          'countries': paises,
          'models': modelos,
        }
      )
    else:
      return redirect('vehiculo_list')
  
  def post(self, request, id):
    if request.user.is_staff:
      carRepo = CarRepository()
      brandsRepo = BrandsRepository()
      fuelRepo = FuelRepository()
      countryRepo = CountriesRepository()
      modelRepo = ModelsRepository()

      car = carRepo.get_by_id(id)
      brand = brandsRepo.get_by_id(request.POST.get('brand'))
      fuel = fuelRepo.get_by_id(request.POST.get('fuel_type'))
      country = countryRepo.get_by_id(request.POST.get('country'))
      model = modelRepo.get_by_id(request.POST.get('model_car'))
      data = request.POST
      
    

      carRepo.update(
        car,
        brand = brand,
        model_car = model,
        fuel_type = fuel,
        country_production = country,
        price= data.get('price'),
        year_production=data.get('year_production'),
        door_quatity= data.get('door_quatity'),
        cilindrada=data.get('cilindrada'),
        image=data.get('image')

      )

      return redirect('vehiculo_list')
    else:
      return redirect('vehiculos_list')