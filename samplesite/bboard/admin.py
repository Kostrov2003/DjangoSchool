from django.contrib import admin

from .models import CarModel
from .models import CarBrand
from .models import Car



admin.site.register(CarModel)
admin.site.register(CarBrand)
admin.site.register(Car)
