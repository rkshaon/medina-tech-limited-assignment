from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from product_api.views import get_all_product
from product_api.views import add_product
from product_api.views import recommended_product
from product_api.views import handle_product_get_or_update_or_delete


class TestUrls(SimpleTestCase):
    def test_all_product_url_resolves(self):
        url = reverse('all_products')
        self.assertEquals(resolve(url).func, get_all_product)
    
    def test_add_product_url_resolves(self):
        url = reverse('add_product')
        self.assertEquals(resolve(url).func, add_product)
    
    def test_recommended_product_url_resolves(self):
        url = reverse('receommended_product')
        self.assertEquals(resolve(url).func, recommended_product)
    
    def test_get_or_update_or_delete_product_url_resolves(self):
        url = reverse('get_or_update_or_delete_product', args=['some-id'])
        self.assertEquals(resolve(url).func, handle_product_get_or_update_or_delete)