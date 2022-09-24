from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from product_api.models import Product

from product_api.serializers import ProductSerializer


@api_view(['GET'])
def get_all_product(request):
    products = Product.objects.all()
    print(products)
    product_serializer = ProductSerializer(products, many=True)
    print(product_serializer)
    print(product_serializer.data)
    data = product_serializer.data
    # data = []

    return Response({
        'status': True,
        'data': data
    })


@api_view(['POST'])
def add_product(request):
    return Response({
        'status': True,
    })