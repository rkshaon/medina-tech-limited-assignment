from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from medina_assignment.utility import auth_user

from product_api.models import Product

from product_api.serializers import ProductSerializer


@api_view(['GET'])
def get_all_product(request):
    products = Product.objects.all()
    product_serializer = ProductSerializer(products, many=True)
    data = product_serializer.data

    return Response({
        'status': True,
        'data': data
    })


@api_view(['POST'])
def add_product(request):
    user = auth_user(request)

    if user.role != 2:
        return Response({
            'status': False,
            'message': 'You are not allowed to add product!'
        }, status=status.HTTP_403_FORBIDDEN)

    return Response({
        'status': True,
    })