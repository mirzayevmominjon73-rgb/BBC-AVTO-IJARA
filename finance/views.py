from rest_framework.decorators import api_view
from rest_framework.response import Response
from cars.models import Car
from .models import InterestSetting
from .services import calculate_installment

@api_view(['POST'])
def calculate_view(request):
    price = float(request.data.get('price'))
    down = float(request.data.get('down_payment'))
    years = int(request.data.get('years'))

    interest = InterestSetting.objects.last().yearly_interest

    result = calculate_installment(price, down, years, interest)
    return Response(result)


@api_view(['POST'])
def calculate_view(request):
    car_id = request.data.get('car_id')
    down = float(request.data['down_payment'])
    years = int(request.data['years'])

    car = Car.objects.get(id=car_id)

    if car.is_promo and car.promo_interest:
        interest = car.promo_interest
    else:
        interest = InterestSetting.objects.last().yearly_interest

    return Response(
        calculate_installment(car.price, down, years, interest)
    )
