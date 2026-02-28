from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from cars.views import HomeView
from company.views import AboutView, ContactView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Frontend
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),

    # Cars
    path('cars/', include(('cars.urls', 'cars'), namespace='cars')),
    path('api/cars/', include(('cars.urls_api', 'cars_api'), namespace='cars_api')),

    # Other apps
    path('news/', include(('news.urls', 'news'), namespace='news')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
