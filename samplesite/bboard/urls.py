from django.urls import path

from .views import index
from .views import page_bmw

urlpatterns = [
    path('', index, name='index'),
    path('BMW/', page_bmw, name='page_bmw'),

]