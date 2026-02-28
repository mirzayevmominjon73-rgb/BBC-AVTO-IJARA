from django.views.generic import ListView, TemplateView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter

from .models import Car, InterestSetting, About, Contact, Employee
from .serializers import CarSerializer


# ======================
# FRONTEND PAGES
# ======================
class HomeView(ListView):
    model = Car
    template_name = 'cars/list.html'
    context_object_name = 'cars'

class PromoCarListView(ListView):
    model = Car
    template_name = 'cars/list.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Car.objects.filter(is_promo=True)

class ElectricCarListView(ListView):
    model = Car
    template_name = 'cars/list.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Car.objects.filter(is_electric=True)

class AboutView(TemplateView):
    template_name = 'company/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['employees'] = Employee.objects.all()
        return context


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        return context

class ContactView(TemplateView):
    template_name = 'company/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.first()
        return context


# ======================
# API
# ======================

class CarViewSet(ReadOnlyModelViewSet):
    queryset = Car.objects.all().order_by('-created_at')
    serializer_class = CarSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']

    # 🔥 MUHIM: rasm URL uchun
    def get_serializer_context(self):
        return {'request': self.request}


@api_view(['GET'])
def car_list(request):
    car_type = request.GET.get('type')
    search = request.GET.get('search', '')

    qs = Car.objects.all().order_by('-created_at')

    if car_type == 'promo':
        qs = qs.filter(is_promo=True)
    elif car_type == 'electric':
        qs = qs.filter(is_electric=True)
    elif car_type == 'auto':
        qs = qs.filter(category='auto')

    if search:
        qs = qs.filter(title__icontains=search)

    serializer = CarSerializer(
        qs,
        many=True,
        context={'request': request}  # 🔥 RASM UCHUN SHART
    )
    return Response({'results': serializer.data})


@api_view(['POST'])
def calculate_finance(request):
    car_id = request.data.get('car_id')
    down_payment = float(request.data.get('down_payment', 0))
    years = int(request.data.get('years', 1))

    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return Response({'error': 'Car not found'}, status=404)

    interest = InterestSetting.objects.first()
    rate = interest.yearly_interest if interest else 25

    remaining = float(car.price) - down_payment
    total_interest = remaining * rate / 100 * years
    total_payment = remaining + total_interest
    monthly_payment = total_payment / (years * 12)

    return Response({
        'remaining': round(remaining, 2),
        'total_payment': round(total_payment, 2),
        'monthly_payment': round(monthly_payment, 2)
    })
