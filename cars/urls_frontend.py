from django.urls import path
from .views import HomeView, PromoCarListView, ElectricCarListView

app_name = 'cars'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('promo/', PromoCarListView.as_view(), name='promo-list'),
    path('electric/', ElectricCarListView.as_view(), name='electric-list'),
]
