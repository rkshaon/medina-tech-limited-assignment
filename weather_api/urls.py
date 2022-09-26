from django.urls import path

from weather_api import views


urlpatterns = [
    path('', views.get_all_weather_type, name='all_weather_types'),
    path('add', views.add_weather_type, name='add_weather'),
    path('<pk>', views.handle_weather_type_get_or_update_or_delete, name='get_or_update_or_delete_weather'),
]