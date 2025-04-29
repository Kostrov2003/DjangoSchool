from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import CarModel, CarBrand, Car



def index(request):
    return render(request, 'bboard/index.html')


def page_bmw(request):
    try:
        bmw_brand = CarBrand.objects.get(name__iexact='BMW')
        selected_model_id = request.GET.get('model')  # ID выбранной модели

        # Получаем все модели марки BMW (для фильтра)
        bmw_models = CarModel.objects.filter(brand=bmw_brand)

        # Если выбрана конкретная модель — фильтруем по ней
        if selected_model_id:
            bmw_cars = Car.objects.filter(brand=bmw_brand, model_id=selected_model_id)
        else:
            bmw_cars = Car.objects.filter(brand=bmw_brand)

    except CarBrand.DoesNotExist:
        bmw_cars = []
        bmw_models = []

    context = {
        'bmw_cars': bmw_cars,
        'bmw_models': bmw_models,
        'selected_model_id': selected_model_id,
    }

    return render(request, 'bboard/page_bmw.html', context)

