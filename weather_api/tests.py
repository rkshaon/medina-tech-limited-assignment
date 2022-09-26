from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from weather_api.views import get_all_weather_type
from weather_api.views import add_weather_type
from weather_api.views import handle_weather_type_get_or_update_or_delete


class TestUrls(SimpleTestCase):
    def test_all_weather_types_url_resolves(self):
        url = reverse('all_weather_types')
        self.assertEquals(resolve(url).func, get_all_weather_type)
    
    def test_add_weather_url_resolves(self):
        url = reverse('add_weather')
        self.assertEquals(resolve(url).func, add_weather_type)
    
    def test_get_or_update_or_delete_weather_url_resolves(self):
        url = reverse('get_or_update_or_delete_weather', args=['some-id'])
        self.assertEquals(resolve(url).func, handle_weather_type_get_or_update_or_delete)