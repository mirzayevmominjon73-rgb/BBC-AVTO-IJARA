from django.urls import path
from .views import (
    HomeView,
    AboutView,
    ContactView,
    PromoCarListView,
    ElectricCarListView,
)

app_name = 'cars'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('promo/', PromoCarListView.as_view(), name='promo-list'),
    path('electric/', ElectricCarListView.as_view(), name='electric-list'),
]
