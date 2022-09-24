from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from medina_assignment.utility import auth_user

from weather_api.models import WeatherType

from weather_api.serializers import WeatherTypeSerializer


@api_view(['GET'])
def get_all_weather_type(request):
    user = auth_user(request)

    weather_types = WeatherType.objects.filter(is_deleted=False)
    weather_types_serializer = WeatherTypeSerializer(weather_types, many=True)
    data = weather_types_serializer.data

    return Response({
        'status': True,
        'data': data,
    })


@api_view(['POST'])
def add_weather_type(request):
    user = auth_user(request)

    if user.role != 1:
        return Response({
            'status': False,
            'message': 'You are not allowed to add weather type!'
        }, status=status.HTTP_403_FORBIDDEN)
    
    weather_type_data = request.data.copy()
    weather_type_data['added_by'] = user.id

    weather_type_serializer = WeatherTypeSerializer(data=weather_type_data)

    if weather_type_serializer.is_valid():
        weather_type_serializer.save()

        return Response({
            'status': True,
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            'status': False,
            'message': str(weather_type_serializer.errors())
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


def get_weather_type(request, pk):
    user = auth_user(request)

    try:
        weather_type = WeatherType.objects.get(id=pk, is_deleted=False)
    except Exception as e:
        return Response({
            'status': False,
            'message': 'Weather type does not found!'
        }, status=status.HTTP_404_NOT_FOUND)

    weather_type_serializer = WeatherTypeSerializer(weather_type, many=False)
    data = weather_type_serializer.data
    
    return Response({
        'status': True,
        'data': data,
    })


def update_weather_type(request, pk):
    user = auth_user(request)

    try:
        weather_type = WeatherType.objects.get(id=pk, is_deleted=False)
    except Exception as e:
        return Response({
            'status': False,
            'message': 'Weather type does not found!'
        }, status=status.HTTP_404_NOT_FOUND)
    
    if weather_type.added_by.id != user.id:
        return Response({
            'status': False,
            'message': 'You are not authorized to update this weather type!'
        }, status=status.HTTP_401_UNAUTHORIZED)
    
    data = request.data.copy()

    if 'name' in data:
        weather_type.name = data['name']
    if 'lowest_temp' in data:
        weather_type.lowest_temp = data['lowest_temp']
    if 'hightest_temp' in data:
        weather_type.hightest_temp = data['hightest_temp']
    
    weather_type.save()
    
    return Response({
        'status': True,
    })


def delete_weather_type(request, pk):
    user = auth_user(request)

    try:
        weather_type = WeatherType.objects.get(id=pk, is_deleted=False)
    except Exception as e:
        return Response({
            'status': False,
            'message': 'Weather type does not found!'
        }, status=status.HTTP_404_NOT_FOUND)
    
    if weather_type.added_by.id != user.id:
        return Response({
            'status': False,
            'message': 'You are not authorized to delete this weather type!'
        }, status=status.HTTP_401_UNAUTHORIZED)
    
    weather_type.is_deleted = True
    weather_type.save()

    return Response({
        'status': True,
    })


WEATHER_TYPE_GET_OR_UPDATE_OR_DELETE = {
    'GET': get_weather_type,
    'PUT': update_weather_type,
    'DELETE': delete_weather_type,    
}


@api_view(['GET', 'PUT', 'DELETE'])
def handle_weather_type_get_or_update_or_delete(request, pk):
    return WEATHER_TYPE_GET_OR_UPDATE_OR_DELETE[request.method](request, pk)