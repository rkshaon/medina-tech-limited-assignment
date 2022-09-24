from itertools import product
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
    
    product_data = request.data.copy()
    product_data['added_by'] = user.id

    product_serializer = ProductSerializer(data=product_data)

    if product_serializer.is_valid():
        product_serializer.save()

        return Response({
            'status': True,
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            'status': False
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


@api_view(['GET'])
def get_product(request, pk):
    user = auth_user(request)

    try:
        product = Product.objects.get(id=pk)
    except Exception as e:
        return Response({
            'status': False,
            'message': 'Product does not found!'
        }, status=status.HTTP_404_NOT_FOUND)
        
    product_serializer = ProductSerializer(product, many=False)
    data = product_serializer.data

    return Response({
        'status': True,
        'data': data,
    })