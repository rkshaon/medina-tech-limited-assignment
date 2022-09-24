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


WEATHER_TYPE_GET_OR_UPDATE_OR_DELETE = {
    'GET': get_weather_type,
    # 'DELETE': delete_product,
    # 'PUT': update_product,
}


@api_view(['GET', 'PUT', 'DELETE'])
def handle_weather_type_get_or_update_or_delete(request, pk):
    return WEATHER_TYPE_GET_OR_UPDATE_OR_DELETE[request.method](request, pk)