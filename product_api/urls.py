from django.urls import path

from product_api import views


urlpatterns = [
    path('', views.get_all_product, name='all_products'),
    path('add', views.add_product, name='add_product'),
    path('weather-recommended', views.recommended_product, name='receommended_product'),
    path('<pk>', views.handle_product_get_or_update_or_delete, name='get_or_update_or_delete_product'),
]