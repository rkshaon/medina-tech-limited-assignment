from django.urls import path

from user_api import views


urlpatterns = [
    path('registration', views.user_registration),
    path('login', views.user_login),
]
