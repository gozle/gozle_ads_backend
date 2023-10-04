from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from .models import Banner, Imput, Video
from helpers.validators import age_validator


class BannerSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    def validate(self, data):
        return age_validator(data)

    class Meta:
        model = Banner
        fields = ["id", "text", "description",
                  "image", "link", "age_from", "age_to"]


class BannerAdsSerializer(serializers.ModelSerializer):
    age_limit = serializers.SerializerMethodField()

    def get_age_limit(self, obj):
        return {
            "from": obj.age_from,
            "to": obj.age_to,
        }

    class Meta:
        model = Banner
        fields = ["id", "text", "description", "image", "link", "age_limit"]


class ImputSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    def validate(self, data):
        return age_validator(data)

    class Meta:
        model = Imput
        fields = ["id", "image", "link", "age_from", "age_to"]


class ImputAdsSerializer(serializers.ModelSerializer):
    age_limit = serializers.SerializerMethodField()

    def get_age_limit(self, obj):
        return {
            "from": obj.age_from,
            "to": obj.age_to,
        }

    class Meta:
        model = Imput
        fields = ["id", "image", "link", "age_limit"]


class VideoSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    def validate(self, data):
        return age_validator(data)

    class Meta:
        model = Video
        fields = ["id", "image", "link", "age_from", "age_to"]


class VideoAdsSerializer(serializers.ModelSerializer):
    age_limit = serializers.SerializerMethodField()

    def get_age_limit(self, obj):
        return {
            "from": obj.age_from,
            "to": obj.age_to,
        }

    class Meta:
        model = Video
        fields = ["id", "image", "link", "age_limit"]
