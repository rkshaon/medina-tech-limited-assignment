from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from user_api.views import user_registration
from user_api.views import user_login
from user_api.views import user_logout
from user_api.views import user_profile


class TestUrls(SimpleTestCase):
    def test_registration_url_resolves(self):
        url = reverse('registration')
        self.assertEquals(resolve(url).func, user_registration)
    
    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, user_login)
    
    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, user_logout)

    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, user_profile)