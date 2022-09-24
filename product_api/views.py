from itertools import product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from medina_assignment.utility import auth_user

from product_api.models import Product

from product_api.serializers import ProductSerializer


@api_view(['GET'])
def get_all_product(request):
    products = Product.objects.filter(is_deleted=False)
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


def get_product(request, pk):
    user = auth_user(request)

    try:
        product = Product.objects.get(id=pk, is_deleted=False)
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


def delete_product(request, pk):
    user = auth_user(request)

    try:
        product = Product.objects.get(id=pk)
    except Exception as e:
        return Response({
            'status': False,
            'message': 'Product does not found!'
        }, status=status.HTTP_404_NOT_FOUND)
    
    if product.added_by.id != user.id:
        return Response({
            'status': False,
            'message': 'You are not authorized to delete this product!'
        }, status=status.HTTP_401_UNAUTHORIZED)
    
    product.is_deleted = True
    product.save()

    return Response({
        'status': True,
    })


PRODUCT_GET_OR_UPDATE_OR_DELETE = {
    'GET': get_product,
    'DELETE': delete_product,
}


@api_view(['GET', 'DELETE'])
def handle_product_get_or_update_or_delete(request, pk):
    return PRODUCT_GET_OR_UPDATE_OR_DELETE[request.method](request, pk)