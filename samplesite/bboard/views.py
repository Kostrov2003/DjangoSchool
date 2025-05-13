from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse

from .models import CarModel, CarBrand, Car
from .forms import CarForm, CarModelForm
from django.db.models import Q


def index(request):
    return render(request, 'bboard/index.html')

def add_car_model(request):
    if request.method == 'POST':
        form = CarModelForm(request.POST)
        if form.is_valid():
            car_model = form.save()  # Сохраняем модель
            messages.success(request, f'Модель "{car_model.name}" успешно добавлена!')
        else:
            messages.error(request, 'Ошибка при добавлении модели. Пожалуйста, проверьте введенные данные.')
    else:
        form = CarModelForm()

    return render(request, 'bboard/add_car_model.html', {'form': form})

@login_required
def manage_car_poster(request):
    brand_id = request.GET.get('brand')
    model_id = request.GET.get('model')
    year = request.GET.get('year')

    cars = Car.objects.all()

    if brand_id:
        cars = cars.filter(model__brand_id=brand_id)

    if model_id:
        cars = cars.filter(model_id=model_id)

    if year:
        cars = cars.filter(year=year)

    # Все бренды для списка
    brands = CarBrand.objects.all()

    # Только модели выбранного бренда
    car_models = CarModel.objects.filter(brand_id=brand_id) if brand_id else []

    return render(request, 'bboard/delete_car_poster.html', {
        'cars': cars,
        'brands': brands,
        'car_models': car_models,
        'selected_brand': brand_id,
        'selected_model': model_id,
        'selected_year': year
    })

@login_required
def delete_car_poster(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car.delete()
        return redirect('manage_car')

@login_required
def add_car_poster(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CarForm()
    return render(request,'bboard/add_car_poster.html', {'form': form})


def get_models(request):
    brand_id = request.GET.get('brand_id')
    models = CarModel.objects.filter(brand_id=brand_id).values('id', 'name')
    return JsonResponse(list(models), safe=False)


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

