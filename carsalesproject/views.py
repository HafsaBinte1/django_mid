from django.shortcuts import render
from carModel.models import CarModel
from carBrand.models import CarBrand
def home(request, brand_slug = None):
    data = CarModel.objects.all()
    if brand_slug is not None:
        brand_name = CarBrand.objects.get(slug = brand_slug)
        data = CarModel.objects.filter(barnd_name = brand_name)
        print(data)
    brands = CarBrand.objects.all()
    return render(request, 'home.html',{'data': data , 'brands': brands})