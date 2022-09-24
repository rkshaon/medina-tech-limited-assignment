from rest_framework import serializers

from weather_api.models import WeatherType


class WeatherTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherType
        fields = '__all__'