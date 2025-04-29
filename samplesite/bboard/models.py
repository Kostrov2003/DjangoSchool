from django.db import models
from django.contrib.auth.models import User

class CarBrand(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Марка машины')

    def __str__(self):
        return self.name

class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='models', verbose_name='Марка машины')
    name = models.CharField(max_length=30, verbose_name='Модель машины')

    class Meta:
        unique_together = ('brand', 'name')

    def __str__(self):
        return f'{self.brand.name} {self.name}'

class Car(models.Model):  # Конкретная машина
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, verbose_name='Марка машины')
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name='Модель машины')
    year = models.IntegerField(verbose_name='Год выпуска')
    mileage = models.IntegerField(verbose_name='Пробег')
    content = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='cars/', verbose_name='Фото машины', blank=True, null=True)

    def __str__(self):
        return f'{self.model}'

