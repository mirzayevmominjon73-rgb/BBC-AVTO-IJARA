from django.urls import path
from company.views import AboutView, ContactView

app_name = 'company'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
