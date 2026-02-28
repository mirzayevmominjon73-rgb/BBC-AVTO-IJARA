from django.urls import path
from .views import car_list, calculate_finance

app_name = 'cars_api'

urlpatterns = [
    path('list/', car_list, name='car-list'),
    path('calculate/', calculate_finance, name='calculate-finance'),
]
