from drf_extra_fields.fields import Base64ImageField
from rest_framework import fields, serializers

from helpers.validators import age_validator

from .models import Banner, Device, Imput, Video


class DeviceSerializer(serializers.ModelSerializer):
    platforms = fields.MultipleChoiceField(choices=Device.Platforms.choices)

    class Meta:
        model = Device
        fields = ["id", "name", "platforms"]


class AdvertisementCommonFieldsSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    view_count = serializers.IntegerField(read_only=True)

    def validate(self, data):
        return age_validator(data)


class BannerSerializer(AdvertisementCommonFieldsSerializer):

    class Meta:
        model = Banner
        fields = [
            "id",
            "text",
            "description",
            "link",
            "age_from",
            "age_to",
            "status",
            "duration",
            "view_count",
            "image",
            "devices",
            "uuid",
            "cycle_duration"
        ]


class ImputSerializer(AdvertisementCommonFieldsSerializer):

    class Meta:
        model = Imput
        fields = [
            "id",
            "link",
            "age_from",
            "age_to",
            "status",
            "duration",
            "view_count",
            "image",
            "devices",
            "uuid"
        ]


class VideoSerializer(AdvertisementCommonFieldsSerializer):

    class Meta:
        model = Video
        fields = [
            "id",
            "text",
            "description",
            "link",
            "video",
            "age_from",
            "age_to",
            "status",
            "duration",
            "view_count",
            "image",
            "devices",
            "uuid",
            "skip_duration"
        ]
