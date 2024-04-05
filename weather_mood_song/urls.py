from django.urls import path
from .views import InputMood, MatchWeatherWithMood

urlpatterns = [
    path('input-mood/', InputMood.as_view(), name='input_mood'),
    path('match-weather-with-mood/', MatchWeatherWithMood.as_view(), name='match_weather_with_mood'),
]
