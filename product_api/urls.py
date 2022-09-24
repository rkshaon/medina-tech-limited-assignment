from django.urls import path

from product_api import views


urlpatterns = [
    path('', views.get_all_product),
    path('add', views.add_product),
    path('weather-recommended', views.recommended_product),
    path('<pk>', views.handle_product_get_or_update_or_delete),    
]