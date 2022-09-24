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