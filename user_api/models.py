from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ADMIN = 1
    VENDOR = 2
    CUSTOMER =3
      
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (VENDOR, 'Vendor'),
        (CUSTOMER, 'Customer'),
    )
    
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=255)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

    