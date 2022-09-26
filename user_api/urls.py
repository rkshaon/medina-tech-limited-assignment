from django.urls import path

from user_api import views


urlpatterns = [
    path('registration', views.user_registration, name='registration'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('profile', views.user_profile, name='profile'),
]
