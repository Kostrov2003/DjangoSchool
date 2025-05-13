from django.forms import ModelForm
from django import forms
from .models import Car, CarBrand, CarModel

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'year', 'mileage', 'content', 'price', 'image']

class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ['name', 'brand']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brand'].queryset = CarBrand.objects.all()  # Ограничим выбор брендов доступными
