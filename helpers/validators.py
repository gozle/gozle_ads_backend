from datetime import datetime
from pytz import timezone

from django.utils.translation import gettext as _
from rest_framework import serializers

from gozle_ads.settings import TIME_ZONE


def age_validator(data):
    if ("age_from" not in data
            or "age_to" not in data):
        return data

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


def dates_are_valid(start_data: datetime, end_data: datetime):
    current_time = datetime.now(timezone(TIME_ZONE))

    if (start_data >= end_data
            or end_data < current_time
            or not start_data
            or not end_data):
        return False

    return True
