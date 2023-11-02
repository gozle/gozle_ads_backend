import random

from django.core.cache import cache

from rest_framework.response import Response


def ads_data(model, serializer_class):
    # gets model's verbose name
    model_name = model._meta.verbose_name.lower()
    # gets model's active object's count
    queryset_count = model.objects.active_advertisements().count()
    
    if queryset_count != 0:
        if model_name not in cache:
            queryset = (
                model.objects
                .active_advertisements()
                .order_by("view_count")
                .first()
            )
        else:
            ads_list = cache.get(model_name)
            obj = random.choice(ads_list)
            queryset = model.objects.get(id=obj.id)

        serializer = serializer_class(queryset)
        queryset.view_count_increase()
        return Response(serializer.data)

    return Response({"message": "No ads found."}, status=204)
