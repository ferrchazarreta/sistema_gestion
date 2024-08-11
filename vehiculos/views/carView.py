from django.views import View
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from vehiculos.forms import CarForm
from vehiculos.repositories.vehiculosRepository import CarRepository
from vehiculos.repositories.brandsRepository import BrandsRepository
from vehiculos.repositories.fuelRepository import FuelRepository
from vehiculos.repositories.countriesRepository import CountriesRepository
from vehiculos.repositories.modelsRepository import ModelsRepository
from vehiculos.repositories.transmissionRepository import TransmissionRepository
from vehiculos.repositories.conditionRepository import ConditionRepository
from vehiculos.repositories.bodyWorkRepository import BodyWorkRepository
from vehiculos.repositories.gamaRepository import GamaRepository

class CarView(View):
  def get(self, request):
    repo = CarRepository()
    conditionRepo = ConditionRepository()
    bodyWorkRepo = BodyWorkRepository()
    gamaRepo = GamaRepository()
    transmissionRepo = TransmissionRepository()
    fuelRepo = FuelRepository()
    brandRepo = BrandsRepository()
    conditions = conditionRepo.get_all()
    bodyWorks = bodyWorkRepo.get_all()
    gamas = gamaRepo.get_all()
    transmissions = transmissionRepo.get_all()
    fuels = fuelRepo.get_all()
    brands = brandRepo.get_all()
    vehiculos = repo.get_all()

    return render(
      request,
      'vehiculos/list.html',
      {
        'cars': vehiculos,
        'conditions':conditions,
        'bodyWorks': bodyWorks,
        'gamas': gamas,
        'transmissions': transmissions,
        'fuels': fuels,
        'brands': brands,
      }
      )

class CarCreate(View):
  def get(self, request):
    if request.user.is_staff:
      form = CarForm()
      
      return render(
        request,
        'vehiculos/create.html',
        {
          'form': form,
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
      transmissionRepo = TransmissionRepository()
      conditionRepository = ConditionRepository()
      bodyWorkRepository = BodyWorkRepository()
      gamaRepository = GamaRepository()
      data = request.POST

      # codigo para guardar las imagenes dentro de los archivos
      if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
          form.save()
          return redirect('vehiculo_list') #redirigue a donde deseas
      else:
        form = CarForm()
        return render(request, 'vehiculo_list', {
      })

      

      brandId = data.get('brand')
      brand = brandsRepo.get_by_id(id=brandId)
      fuelId = data.get('fuel_type')
      fuel = fuelRepo.get_by_id(id=fuelId)
      countryId = data.get('country_production')
      country = countryRepo.get_by_id(id=countryId)
      modelId = data.get('model_car')
      model = modelRepo.get_by_id(id=modelId)  
      transmissionId = data.get('transmission')
      transmission = transmissionRepo.get_by_id(id=transmissionId)
      conditionId = data.get('condition')
      condition = conditionRepository.get_by_id(id=conditionId)
      gamaId = data.get('gama')
      gama = gamaRepository.get_by_id(id=gamaId)
      bodyWorkId = data.get('bodyWork')
      bodyWork = bodyWorkRepository.get_by_id(id=bodyWorkId)

      carRepo.create(
        brand=brand,
        model_car=model,
        year_production=data.get('year_production'),
        door_quatity=data.get('door_quatity'),
        cilindrada=data.get('cilindrada'),
        fuel_type=fuel,
        country_production=country,
        image= data.get('image'),
        price= data.get('price'),
        transmission=transmission,
        condition=condition,
        gama=gama,
        body_work=bodyWork,
      )
      
      return redirect('vehiculo_list')
    else:
      return redirect('vehiculo_list')

class CarDetail(View):
    def get(self, request, id):
        repo = CarRepository()
        vehiculo = repo.get_by_id(id=id)

        return render(
            request,
            'vehiculos/detail.html',
            {
              'car': vehiculo,
            }
        )

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
      transmissionRepo = TransmissionRepository()
      conditionRepository = ConditionRepository()
      bodyWorkRepository = BodyWorkRepository()
      gamaRepository = GamaRepository()


      vehiculo = carRepo.get_by_id(id)
      marcas = brandsRepo.get_all()
      combustibles = fuelRepo.get_all()
      paises = countryRepo.get_all()
      modelos = modelRepo.get_all()
      transmisiones = transmissionRepo.get_all()
      condicion = conditionRepository.get_all()
      carroceria = bodyWorkRepository.get_all()
      gama = gamaRepository.get_all()

      return render(
        request,
        'vehiculos/update.html',
        {
          'car': vehiculo,
          'brands': marcas,
          'fuels': combustibles,
          'countries': paises,
          'models': modelos,
          'transmissions':transmisiones,
          'conditions': condicion,
          'bodyWorks': carroceria,
          'gamas':gama,
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
      transmissionRepo = TransmissionRepository()
      conditionRepository = ConditionRepository()
      bodyWorkRepository = BodyWorkRepository()
      gamaRepository = GamaRepository()

      car = carRepo.get_by_id(id)
      brand = brandsRepo.get_by_id(request.POST.get('brand'))
      fuel = fuelRepo.get_by_id(request.POST.get('fuel_type'))
      country = countryRepo.get_by_id(request.POST.get('country'))
      model = modelRepo.get_by_id(request.POST.get('model_car'))
      transmission = transmissionRepo.get_by_id(request.POST.get('transmission'))
      condition = conditionRepository.get_by_id(request.POST.get('condition'))
      bodyWork = bodyWorkRepository.get_by_id(request.POST.get('bodyWork'))
      gama = gamaRepository.get_by_id(request.POST.get('gama'))
      data = request.POST
      
      # Verificar si se ha cargado una nueva imagen
      if 'image' in request.FILES:
        car.image = request.FILES['image']

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
        image=data.get('image'),
        transmission=transmission,
        condition=condition,
        bodyWork=bodyWork,
        gama=gama,
      )

      return redirect('vehiculo_list')
    else:
      return redirect('vehiculos_list')
    
class CarByBrand(View):
  def get(self, request, id):
    carRepo = CarRepository()
    conditionRepo = ConditionRepository()
    bodyWorkRepo = BodyWorkRepository()
    gamaRepo = GamaRepository()
    transmissionRepo = TransmissionRepository()
    fuelRepo = FuelRepository()
    brandRepo = BrandsRepository()
    conditions = conditionRepo.get_all()
    bodyWorks = bodyWorkRepo.get_all()
    gamas = gamaRepo.get_all()
    transmissions = transmissionRepo.get_all()
    fuels = fuelRepo.get_all()
    brands = brandRepo.get_all()
    brand = brandRepo.get_by_id(id=id)
    vehiculo = carRepo.filter_by_brand(brand=brand)
    return render(
      request,
      'vehiculos/list.html',
      {
        'cars': vehiculo,
        'conditions':conditions,
        'bodyWorks': bodyWorks,
        'gamas': gamas,
        'transmissions': transmissions,
        'fuels': fuels,
        'brands': brands,
      }
    )

class CarByCondition(View):
  def get(self, request, id):
    carRepo = CarRepository()
    conditionRepo = ConditionRepository()
    bodyWorkRepo = BodyWorkRepository()
    gamaRepo = GamaRepository()
    transmissionRepo = TransmissionRepository()
    fuelRepo = FuelRepository()
    brandRepo = BrandsRepository()
    conditions = conditionRepo.get_all()
    bodyWorks = bodyWorkRepo.get_all()
    gamas = gamaRepo.get_all()
    transmissions = transmissionRepo.get_all()
    fuels = fuelRepo.get_all()
    brands = brandRepo.get_all()
    condition = conditionRepo.get_by_id(id=id)
    vehiculo = carRepo.filter_by_condition(condition=condition)
    return render(
      request,
      'vehiculos/list.html',
      {
        'cars': vehiculo,
        'conditions':conditions,
        'bodyWorks': bodyWorks,
        'gamas': gamas,
        'transmissions': transmissions,
        'fuels': fuels,
        'brands': brands,
      }
    )

class CarByGama(View):
  def get(self, request, id):
    carRepo = CarRepository()
    conditionRepo = ConditionRepository()
    bodyWorkRepo = BodyWorkRepository()
    gamaRepo = GamaRepository()
    transmissionRepo = TransmissionRepository()
    fuelRepo = FuelRepository()
    brandRepo = BrandsRepository()
    conditions = conditionRepo.get_all()
    bodyWorks = bodyWorkRepo.get_all()
    gamas = gamaRepo.get_all()
    transmissions = transmissionRepo.get_all()
    fuels = fuelRepo.get_all()
    brands = brandRepo.get_all()
    gama = gamaRepo.get_by_id(id=id)
    vehiculo = carRepo.filter_by_gama(gama=gama)
    return render(
      request,
      'vehiculos/list.html',
      {
        'cars': vehiculo,
        'conditions':conditions,
        'bodyWorks': bodyWorks,
        'gamas': gamas,
        'transmissions': transmissions,
        'fuels': fuels,
        'brands': brands,
      }
    )

class CarByBodyWork(View):
  def get(self, request, id):
    carRepo = CarRepository()
    conditionRepo = ConditionRepository()
    bodyWorkRepo = BodyWorkRepository()
    gamaRepo = GamaRepository()
    transmissionRepo = TransmissionRepository()
    fuelRepo = FuelRepository()
    brandRepo = BrandsRepository()
    conditions = conditionRepo.get_all()
    bodyWorks = bodyWorkRepo.get_all()
    gamas = gamaRepo.get_all()
    transmissions = transmissionRepo.get_all()
    fuels = fuelRepo.get_all()
    brands = brandRepo.get_all()
    bodyWork = bodyWorkRepo.get_by_id(id=id)
    vehiculo = carRepo.filter_by_bodyWork(bodyWork=bodyWork)
    return render(
      request,
      'vehiculos/list.html',
      {
        'cars': vehiculo,
        'conditions':conditions,
        'bodyWorks': bodyWorks,
        'gamas': gamas,
        'transmissions': transmissions,
        'fuels': fuels,
        'brands': brands,
      }
    )
  
class CarByFuel(View):
  def get(self, request, id):
    carRepo = CarRepository()
    conditionRepo = ConditionRepository()
    bodyWorkRepo = BodyWorkRepository()
    gamaRepo = GamaRepository()
    transmissionRepo = TransmissionRepository()
    fuelRepo = FuelRepository()
    brandRepo = BrandsRepository()
    conditions = conditionRepo.get_all()
    bodyWorks = bodyWorkRepo.get_all()
    gamas = gamaRepo.get_all()
    transmissions = transmissionRepo.get_all()
    fuels = fuelRepo.get_all()
    brands = brandRepo.get_all()
    fuel = fuelRepo.get_by_id(id=id)
    vehiculo = carRepo.filter_by_fuel(fuel=fuel)
    return render(
      request,
      'vehiculos/list.html',
      {
        'cars': vehiculo,
        'conditions':conditions,
        'bodyWorks': bodyWorks,
        'gamas': gamas,
        'transmissions': transmissions,
        'fuels': fuels,
        'brands': brands,
      }
    )

class CarByTransmission(View):
  def get(self, request, id):
    carRepo = CarRepository()
    conditionRepo = ConditionRepository()
    bodyWorkRepo = BodyWorkRepository()
    gamaRepo = GamaRepository()
    transmissionRepo = TransmissionRepository()
    fuelRepo = FuelRepository()
    brandRepo = BrandsRepository()
    conditions = conditionRepo.get_all()
    bodyWorks = bodyWorkRepo.get_all()
    gamas = gamaRepo.get_all()
    transmissions = transmissionRepo.get_all()
    fuels = fuelRepo.get_all()
    brands = brandRepo.get_all()
    transmission = transmissionRepo.get_by_id(id=id)
    vehiculo = carRepo.filter_by_transmission(transmission=transmission)
    return render(
      request,
      'vehiculos/list.html',
      {
        'cars': vehiculo,
        'conditions':conditions,
        'bodyWorks': bodyWorks,
        'gamas': gamas,
        'transmissions': transmissions,
        'fuels': fuels,
        'brands': brands,
      }
    )