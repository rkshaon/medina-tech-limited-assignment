from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from user_api.views import user_registration


class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        # assert 1 == 2
        url = reverse('registration')
        self.assertEquals(resolve(url).func, user_registration)
        # print(resolve(url))
        url = reverse('login')
        # print(resolve(url))
        url = reverse('logout')
        # print(resolve(url))
        url = reverse('profile')
        # print(resolve(url))