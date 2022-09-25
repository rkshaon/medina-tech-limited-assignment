import django_filters

from product_api.models import Product


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['name', 'product_type__name']