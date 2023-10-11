from drf_extra_fields.fields import Base64ImageField
from rest_framework import fields, serializers

from .models import Banner, Device, Imput, Video
from helpers.validators import age_validator

class NameField(serializers.RelatedField):

    def to_representation(self, value):
        return f"{value.name}"


class DeviceSerializer(serializers.ModelSerializer):
    platforms = fields.MultipleChoiceField(choices=Device.Platforms.choices)

    class Meta:
        model = Device
        fields = ["id", "name", "platforms"]


class BannerSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    def validate(self, data):
        return age_validator(data)

    class Meta:
        model = Banner
        fields = ["id", "image", "link",
                  "age_from", "age_to",
                  "view_count", "devices"]


class ImputSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    def validate(self, data):
        return age_validator(data)

    class Meta:
        model = Imput
        fields = ["id", "image", "link",
                  "age_from", "age_to",
                  "view_count", "devices"]


class VideoSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    def validate(self, data):
        return age_validator(data)

    class Meta:
        model = Video
        fields = ["id", "image", "link",
                  "video", "age_from", "age_to",
                  "view_count", "devices"]
