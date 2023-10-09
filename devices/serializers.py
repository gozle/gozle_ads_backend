from rest_framework import serializers, fields

from .models import Device


class PlatformNameField(serializers.RelatedField):

    def to_representation(self, value):
        return f"{value.name}" # 


class DeviceSerializer(serializers.ModelSerializer):
    platforms = fields.MultipleChoiceField(choices=Device.Platforms.choices)

    class Meta:
        model = Device
        fields = ["id", "name", "platforms"]
