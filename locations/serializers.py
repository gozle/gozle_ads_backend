from rest_framework import serializers

from .models import City, Province


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = "__all__"


class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        fields = "__all__"
