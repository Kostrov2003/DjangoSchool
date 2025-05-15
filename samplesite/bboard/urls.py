from django.urls import path
from django.contrib.auth import views as auth_views



from .views import index
from .views import page_bmw, car_info
from .views import add_car_poster,get_models, manage_car_poster, delete_car_poster, add_car_model


urlpatterns = [
    path('', index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='bboard/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='bboard/logout.html', next_page='logout'), name='logout'),
    path('add_car_poster/', add_car_poster, name='add_car'),
    path('get_models/', get_models, name='get_models'),  # для AJAX
    path('add_car_model/', add_car_model, name='add_model'),
    path('delete_car_poster/', manage_car_poster, name='manage_car'),
    path('delete_car_poster/<int:car_id>/', delete_car_poster, name='delete_car'),
path('car-info/<int:car_id>/', car_info, name='car_info'),
    path('BMW/', page_bmw, name='page_bmw'),

]