from django.urls import path
from django.views.decorators.cache import cache_page
from app_weather.views import WeatherApiView, LogInView

urlpatterns = [
    path('weather/', cache_page(60)(WeatherApiView.as_view()), name='weather'),
    path('login/', LogInView.as_view(), name='login')

]