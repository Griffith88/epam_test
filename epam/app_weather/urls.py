from django.urls import path
from django.views.decorators.cache import cache_page
from app_weather.views import WeatherApiView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('weather/', cache_page(60)(WeatherApiView.as_view()), name='weather'),
    path('token/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),

]
