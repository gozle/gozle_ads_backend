from django.utils.translation import gettext as _

from rest_framework import serializers


def age_validator(data):
    if ("age_from" not in data
            or "age_to" not in data):
        raise serializers.ValidationError(
            _("Age from and age to are required."))

    ages = (data["age_from"], data["age_to"])
    if None not in ages:
        if ages[0] > ages[1]:
            # If there is no None in ages and from age less than to age it raises Validation Error
            raise serializers.ValidationError(
                _("Age from must be less than age to."))
        if ages[0] == ages[1]:
            # If there is no None in ages and from age less than to age it raises Validation Error
            raise serializers.ValidationError(
                _("Ages mustn't be equal to each other."))
    return data
