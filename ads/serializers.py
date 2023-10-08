from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from .models import Banner, Imput, Video
from devices.models import Device
from helpers.validators import age_validator


class PlatformNameField(serializers.RelatedField):

    def to_representation(self, value):
        return f"{Device.Platforms(value.platform).label} {value.name}" # returns device platform and device names. NOT just id


class BannerSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    devices = PlatformNameField(read_only=True, many=True)

    def validate(self, data):
        return age_validator(data)

    class Meta:
        model = Banner
        fields = ["id", "image", "link",
                  "age_from", "age_to", "view_count", "devices"]


class ImputSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    devices = PlatformNameField(read_only=True, many=True)

    def validate(self, data):
        return age_validator(data)

    class Meta:
        model = Imput
        fields = ["id", "image", "link",
                  "age_from", "age_to", "view_count", "devices"]


class VideoSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    devices = PlatformNameField(read_only=True, many=True)

    def validate(self, data):
        return age_validator(data)

    class Meta:
        model = Video
        fields = ["id", "image", "link",
                  "age_from", "age_to", "view_count", "devices"]
