from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views import View

from app_weather.business_logic.weather_get import Weather


class WeatherApiView(LoginRequiredMixin, View):

    def get(self, request):
        city = request.GET.get('city')
        fahrenheit = request.GET.get('f')
        if city:
            weather = Weather(city, fahrenheit=True) if fahrenheit else Weather(city)
        else:
            return JsonResponse({'code': 404, 'message': 'no city chosen'})
        return JsonResponse(weather.to_dict())


class LogInView(View):

    def post(self, request):
        name = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=name).first()

        if user is None:
            return JsonResponse({'message': 'login not exists'})

        if not user.check_password(password):
            return JsonResponse({'password': 'bad password'})

        user = login(request, user)
        authenticate(user)
        return JsonResponse({'login': 'success'})
