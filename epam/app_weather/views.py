from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from app_weather.business_logic.weather_get import Weather


class WeatherApiView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        city = request.GET.get('city')
        fahrenheit = request.GET.get('f')
        if city:
            weather = Weather(city, fahrenheit=True) if fahrenheit else Weather(city)
        else:
            return JsonResponse({'code': 404, 'message': 'no city chosen'})
        return JsonResponse(weather.to_dict())

