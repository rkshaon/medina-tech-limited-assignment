from django.urls import path

from weather_api import views


urlpatterns = [
    path('', views.get_all_weather_type),
    path('add', views.add_weather_type),
    path('<pk>', views.handle_weather_type_get_or_update_or_delete),
]