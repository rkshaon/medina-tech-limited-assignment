from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ipware import get_client_ip
from ip2geotools.databases.noncommercial import DbIpCity

import os
import requests

from medina_assignment.utility import auth_user

from product_api.models import Product
from weather_api.models import WeatherType

from product_api.filters import ProductFilter

from product_api.serializers import ProductSerializer


@api_view(['GET'])
def get_all_product(request):
    user = auth_user(request)
    products = []
    data = []
    print(request.GET)

    if 'weather' in request.GET or 'name' in request.GET:
        print('query-param-exist')        
        # products = ProductFilter('stylish', queryset=Product.objects.all())
        # print(products)
        # filterset = ProductFilter(request.GET, queryset=Product.objects.all())
        # filterset = ProductFilter(request.GET, queryset=Product.objects.all())
        # if filterset.is_valid():
        #     # queryset = filterset.qs
        #     products = filterset.qs
    else:
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
    
    if user.role != 3:
        return Response({
            'status': False,
            'message': 'Only customers can view products!'
        }, status=status.HTTP_403_FORBIDDEN)
    
    WEATHER_API_URL = os.environ['OPEN_WEATHER_API_URL']
    WEATHER_API_KEY = os.environ['OPEN_WEATHER_API_KEY']
    
    client_ip, is_routable = get_client_ip(request)
    
    if client_ip is None:
        client_ip = '0.0.0.0'
    
    try:
        response = DbIpCity.get(client_ip, api_key='free')
        city = response.city
    except Exception as e:
        city = 'Unknown'
    
    if city is None:
        city = 'Unknown'
        
    LOCATION = 'dhaka'
    LOCATION = city

    URL = WEATHER_API_URL + 'weather?q=' + str(LOCATION) + '&units=metric&APPID=' + WEATHER_API_KEY

    req = requests.get(URL)

    WEATHER_DATA = req.json()
    
    TYPE = WEATHER_DATA['weather'][0]['main']
    TEMP = WEATHER_DATA['main']['temp']

    weathers = WeatherType.objects.filter(lowest_temp__lte = TEMP, hightest_temp__gt = TEMP)
    weather = WeatherType.objects.filter(name=TYPE)

    weather_list = set(weathers)

    for w in weather:
        weather_list.add(w)
        
    product_list = []

    for weather in weather_list:
        product = Product.objects.filter(product_type=weather)
        product_list.extend(product)
    
    product_serializer = ProductSerializer(product_list, many=True)
    data = product_serializer.data

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