from django.urls import path

from weather_api import views


urlpatterns = [
    path('', views.get_all_weather_type),
]