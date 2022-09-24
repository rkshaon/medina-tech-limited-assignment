from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import os
import requests

from medina_assignment.utility import auth_user

from product_api.models import Product
from weather_api.models import WeatherType

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
    # user = auth_user(request)

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


def update_product(request, pk):
    user = auth_user(request)

    try:
        product = Product.objects.get(id=pk, is_deleted=False)
    except Exception as e:
        return Response({
            'status': False,
            'message': 'Product does not found!'
        }, status=status.HTTP_404_NOT_FOUND)
        
    if product.added_by.id != user.id and user.role !=1:
        return Response({
            'status': False,
            'message': 'You are not authorized to update this product!'
        }, status=status.HTTP_401_UNAUTHORIZED)
    
    data = request.data.copy()

    if product.added_by.id == user.id:
        if 'name' in data:
            product.name = data['name']
        if 'quantity' in data:
            product.quantity = data['quantity']
    
    if user.role == 1:
        if 'product_type' in data:
            if data['product_type'] == 'NULL':
                product.product_type = None
            else:
                weather_type = WeatherType.objects.get(id=data['product_type'])
                product.product_type = weather_type
        
        product.edited_by = user
    
    product.save()
    
    return Response({
        'status': True,
    })


def delete_product(request, pk):
    user = auth_user(request)

    try:
        product = Product.objects.get(id=pk, is_deleted=False)
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


@api_view(['GET'])
def recommended_product(request):
    user = auth_user(request)
    WEATHER_API_URL = os.environ['OPEN_WEATHER_API_URL']
    WEATHER_API_KEY = os.environ['OPEN_WEATHER_API_KEY']
    LOCATION = 'dhaka'

    URL = WEATHER_API_URL + 'weather?q=' + str(LOCATION) + '&units=metric&APPID=' + WEATHER_API_KEY

    req = requests.get(URL)

    WEATHER_DATA = req.json()

    if user.role != 3:
        return Response({
            'status': False,
            'message': 'Only customers can view products!'
        }, status=status.HTTP_403_FORBIDDEN)

    data = []
    data = {
        'url': WEATHER_API_URL,
        'key': WEATHER_API_KEY,
        'location': LOCATION,
        'weather-url': URL,
        'weather-data': WEATHER_DATA,
    }

    return Response({
        'status': True,
        'data': data,
    })


PRODUCT_GET_OR_UPDATE_OR_DELETE = {
    'GET': get_product,
    'PUT': update_product,
    'DELETE': delete_product,
}


@api_view(['GET', 'PUT', 'DELETE'])
def handle_product_get_or_update_or_delete(request, pk):
    return PRODUCT_GET_OR_UPDATE_OR_DELETE[request.method](request, pk)